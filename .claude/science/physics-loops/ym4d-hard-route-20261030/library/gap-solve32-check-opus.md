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

### Step 1 (done 14:35Z): inventory and cited rows

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

### Step 2 (done 14:58Z): the short-time slice information bounds (29)-(32)

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

### Step 3 (done 15:20Z): recovery (35) of flux sector ratios, with (33)-(34) and their inputs

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

### Step 4 (done 15:42Z): the endpoint removal (36)-(40)

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
