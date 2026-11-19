# Check of gap-solve16-astra62.md (FINISH row 1176)

Status: in progress. Checker: Opus 5.5 (Claude Code subagent). This file is
appended to as the check proceeds.

Task: FINISH row 1176. Check line by line, by hand, `library/gap-solve16-astra62.md`
(row 1175). Positive claims first.

## Plan (at most eight steps)

1. Read the file under check in full, the council brief, and the cited parts
   of rows 1161-1173 and their checks. Record the statement list with lines.
2. Check the equivalence: (W), given the one-cube neutral bound, iff the twist
   cost is o(N^2/log N).
3. Check the competing-seed upper bounds (3)-(4).
4. Check the competing-seed upper bounds (7)-(8).
5. Check the competing-seed upper bound (20).
6. Check everything else, statement by statement.
7. Numeric guide run where useful (a guide only, under 2 GB).
8. Verdict table, counts, and the RESULT line.

## Step 1 result: what was read, and the statement list

File under check: `library/gap-solve16-astra62.md`, 340 lines plus a final
newline, read in full. Pin named in its L3: `f216fbb66` (exists in this clone:
"record row 1173, start check 1174 and row 1175").

Read for the check (the parts cited):
- `library/gap-council-brief.md` (whole).
- `library/gap-crux-restate.md` L22-66 (setting, (TM), (TM-c), Lemma A),
  L170-296 (Lemmas K, X, E, E', Theorem S, S3', Theorem F, Remark F3).
- `library/gap-flux-exercise.md` L107-170 (C1-C7, (S1)-(S3)), L485-515
  (Proposition CL (b), Lemma W, Theorem S-w).
- `library/gap-solve9-astra62.md` (row 1161) L20-100 ((1)-(9), the two
  alternatives), L171-184 ((13)-(14)), L213-306 (explicit K = 512 test,
  (17)-(20)); its check `library/gap-solve9-check-opus.md` S11-S15, S24-S25.
- `library/gap-phys-seed.md` L305-340 (Theorem ZD-c); `library/gap-zd-astra.md`
  L195-225 (strict-margin completion) and item 18 (L403-417).
- `library/gap-solve15-astra62.md` (row 1173) L13-80 ((1)-(5)), L330-354
  ((23)), L474-500 ((31)-(32)); RESULT of its check `gap-solve15-check-opus.md`.
- `library/gap-solve7-astra62.md` (row 1155) (9) and its proof.
- `library/gap-solve14-astra62.md` (row 1171) (2) and proof; RESULT of check.
- `library/gap-solve12-astra62.md` (row 1167) (1) and proof; RESULT of check.
- `library/gap-solve10-astra62.md` (10); `library/gap-skeleton-max.md` N3;
  `library/gap-wall-max.md` B1; `library/gap-cr-tomboulis-max.md` 6.1
  (Lemma PAR-T); spot greps of `gap-solve8`, `gap-solve11`, `gap-solve13`,
  `gap-sc-check-astra`, `gap-council-synthesis`, `gap-glue-tree-astra`.

Statement list (S-number, line, mark in the file):

| S | Line | Mark | Content |
|---|---|---|---|
| S1 | L3 | GUIDE | repo search |
| S2 | L5 | GUIDE | credits |
| S3 | L9 | GUIDE | plan |
| S4 | L11 | OPEN | strict seed at 1/1650 and the repaired (W) |
| S5 | L13 | GUIDE | starting point |
| S6 | L15 | GUIDE | summary of the note |
| S7 | L19 | PROVED | the two pairs (V,Q) and their sector traces |
| S8 | L21-26 | PROVED | (1) |
| S9 | L28-30 | PROVED | proof of (1) |
| S10 | L32-36 | PROVED | (2) |
| S11 | L40-49 | PROVED | (3), (4) |
| S12 | L51-55 | PROVED | (5); enlargement at t < b |
| S13 | L57 | PROVED | tile choice; proof of (3) |
| S14 | L59-64 | PROVED | (6): sufficiency and necessity |
| S15 | L68-73 | PROVED | (7), statement |
| S16 | L75 | PROVED | box kernel between e^{-M} and e^{M} |
| S17 | L77 | PROVED | oscillation 4M, contraction 1 - e^{-4M} |
| S18 | L79 | PROVED | domination by e^{eta} of the product channel |
| S19 | L81 | PROVED | the channel depends on B_i only |
| S20 | L83 | PROVED | squared loss gives (7) |
| S21 | L85-89 | PROVED | (8) |
| S22 | L91 | PROVED | competing bound 128 exp[...]; b ~ (log N)^{1/3} |
| S23 | L95-100 | PROVED | (9), statement |
| S24 | L102-108 | PROVED | (10) and E|m| <= TV |
| S25 | L110 | PROVED | odd-projection amplification; X(2g) <= 2; (9) |
| S26 | L112 | OPEN | missing lower bound |
| S27 | L116-120 | PROVED | (11) |
| S28 | L122 | PROVED | tile size forced by (11) |
| S29 | L124-128 | PROVED | (12) |
| S30 | L130-135 | PROVED | (13) |
| S31 | L139-144 | PROVED | (14) |
| S32 | L146-150 | PROVED | (15) |
| S33 | L152-157 | PROVED | (16) |
| S34 | L159 | PROVED | first crossing width; thin-width selector |
| S35 | L161 | PROVED | scope of (14) |
| S36 | L165-171 | PROVED | (17) |
| S37 | L173-181 | PROVED | (18); Mack-Petkova credit |
| S38 | L183-188 | PROVED | (19); fairness of strict subsets |
| S39 | L192-202 | PROVED | (20), statement |
| S40 | L204-206 | PROVED | fixed axial gauge bound C b^3 (S_1+S_2) |
| S41 | L208 | PROVED | ordering chain on each arm |
| S42 | L210 | PROVED | bond bound; L_i bounds; (1 +- u)(1 +- v) |
| S43 | L212-223 | PROVED | (21); the moment bound e^{xi_p} |
| S44 | L225 | PROVED | assembly of (20) |
| S45 | L227-231 | PROVED | (22) |
| S46 | L235-240 | PROVED | heavy/light table |
| S47 | L242 | PROVED | heavy entries |
| S48 | L244-248 | PROVED | (23) |
| S49 | L250 | PROVED | light magnetic entry, periodic seed |
| S50 | L252 | PROVED | light electric entry, competing seed |
| S51 | L254 | PROVED | one-sector selector |
| S52 | L258-266 | PROVED | (24), statement |
| S53 | L268 | PROVED | proof of (24) |
| S54 | L270-274 | PROVED | gamma >= c_q/n_0; (25) |
| S55 | L276-281 | PROVED | (26) |
| S56 | L283 | PROVED | example with O_N <= 2 c_s^{-floor(M/2)} |
| S57 | L287-291 | PROVED | (27) |
| S58 | L293 | PROVED | optimal order N min{2(t+1), N/2} |
| S59 | L295-300 | PROVED | (28); two-point sharpness; obstruction |
| S60 | L304 | PROVED | the cooling comparison, claims |
| S61 | L306 | PROVED | spectator partition function and transfer |
| S62 | L308-313 | PROVED | (29) |
| S63 | L315 | PROVED | bounded excess and vanishing gap |
| S64 | L319-324 | PROVED | (30) |
| S65 | L326 | PROVED | barrier in both branches |
| S66 | L330-336 | PROVED | table of stopped routes (5 rows) |
| S67 | L338 | OPEN | what is missing |
| S68 | L340 | RESULT | summary |

Positive claims checked first (Steps 2-5): S7-S14 (the equivalence and
(1)-(6)), S11 again for (3)-(4), S15-S22 ((7)-(8)), S39-S45 ((20)-(22)).

## Step 2 result: (1), (2) and the equivalence (6)

**S7 (L19), the two pairs (V,Q). HOLDS.** Electric pair: in the a frame
Q = (Z_0 - Z_ab)/2 = Tr(T^a P_{b,-}), in the b frame Tr(T^b P_{a,-})
(Theorem F (a), row 697); the vacuum is even, so Q's states are V's states
minus at least the vacuum. Magnetic pair: in the a frame the planes ab, ac, ad
are electric and bc, bd, cd magnetic, so summing the eight electric bits gives
Q = sum over m in M_a with m_cd = 1 of Tr(T_{B,m}^a P_0), four magnetic
sectors with the neutral projection; the plane cd is magnetic in the b frame
too, so the same holds there. V = W_full = sum over all m of Tr(T_{B,m}^a P_0)
(Lemma W (b), row 731). The m = 0 sector, which holds the vacuum, is not in Q.
V is invariant under axis permutations (Lemma W (a)). Note: this uses
(TM-tw) for all 64 twists, as row 731 does.

**S8-S9 (L21-30), inequality (1). HOLDS.** Re-derived:
- f_cd = inf over a,b >= 3 of log V(a,b,c,d)/(ab) is finite: V >= Z_0/8 and
  Z_0 >= exp(-12 beta abcd). W(a,b) := V(a,b,c,d) is in the setting of the
  lemmas (row 697 L174), with lambda(b) the periodic top eigenvalue (Lemma W
  (c) for W_full).
- Lemma K (b), (d): kappa >= 0 and nonincreasing. Lemma X with a = t:
  t kappa(b) + g_V(t;b,c,d) = b kappa(t) + g_V(b;t,c,d), and for t < b,
  (b - t) kappa(b) <= g_V(t;b,c,d) = log(1+s). Needs t >= 3: given.
- In the a frame on the box (b,c,d) let x_i = mu_i/lambda in [0,1] be Q's
  eigenvalue ratios. They are a sub-multiset of V's ratios with one copy of
  the vacuum removed, so sum x_i^t <= s, and
  Q(b,b,c,d)/lambda^b = sum (x_i^t)^{b/t} <= s^{b/t} since b/t > 1.
- Lemma A (a) in the a frame, then in the b frame (box (R,c,d)):
  Q(R,b,c,d) <= Q(b,b,c,d)^{R/b}, Q(R,H,c,d) <= Q(R,b,c,d)^{H/b}. Valid for
  every integer R, H >= b (monotone l^p norms; no multiple needed).
- V(R,H,c,d) >= exp(f_cd RH). Then
  Q/V <= [ (Q(b,b,c,d)/lambda^b) exp(b kappa(b)) ]^{RH/b^2}
      <= [ s^{b/t} (1+s)^{b/(b-t)} ]^{RH/b^2}.
This is (1). The bound holds even if the bracket exceeds one.

**S10 (L32-36), inequality (2). HOLDS.** (S2) of row 731 gives Z_B <= Z_0 for
all 64 twists, so V = (1/8) sum Z_B <= 8 Z_0. Positivity of the other terms
gives Z_cd <= 8Q, and the same for any Z_B with B_cd = 1. Hence
Z_B/Z_0 <= 64 Q/V.

**S14 (L59-64), the equivalence (6). HOLDS.** Inputs: (3) and (4), checked in
Step 3; row 1161's explicit K = 512 test (L215-227 there; checked HOLDS in row
1162, S12); Theorem ZD-c (row 720) with the repaired domain and the strict
margin (row 730, item 18 and L195-225).
- Sufficiency. At every sufficiently fine cutoff (4 | n_0, n_0 >= 2^70 is
  covered by "sufficiently fine"), s_+(floor(n_0/512)) <= 1/2 gives either
  S_per(n_0/2;n_0^3) < 2^{-19} or S_full(n_0/2;n_0^3) < 2^{-18}. Both give
  5041 S_V <= q := 5041 * 2^{-18} < 0.0193, one absolute q. In the competing
  case (4) gives
  -log zeta(N) >= c_q (N/n_0)^2/log(2+N/n_0) - log 64
  for N/n_0 >= R_q. Since log(2+N) >= log(2+N/n_0), the quantity in (6) has
  liminf >= c_q/n_0^2 > 0. So (6) at every j >= j_0 excludes the competing
  alternative at every j >= j_0; the periodic alternative then gives
  limsup_j S_per <= 2^{-19} < 1/1650, the strict seed, hence (W).
- Necessity. (W) gives (PHYS-SEED) with threshold 1/5041 and a uniform
  q' < 1 at an enlarged size l of P (Theorem ZD-c proof, first line); l/a_j
  is a multiple of 4 and at least 12, so (3) applies with n_0' = l/a_j. At
  each such fixed j, (3) gives 1 - zeta(N) <= 2 exp[-c_{q'} ...] -> 0, so
  -log zeta -> 0 and the liminf in (6) is 0 (in fact the limit). Since
  zeta <= 1 by (S2), the quantity in (6) is nonnegative.
- Comparison with row 1161 (13): (13) implies (6) along the same subsequence,
  so (6) is the weaker sufficient condition. A cost N^{3/2} violates (13) and
  satisfies (6). Both statements in L64 hold.
- Quantifier note (reading only): the sufficiency needs (6) at all
  j >= j_0; "at each sufficiently fine fixed bare coupling" says exactly
  this. A subsequence of cutoffs would not suffice. The note does not claim
  otherwise.

## Step 3 result: the bounds (3)-(4) and their proof via (5)

**S12 (L51-55), estimate (5). HOLDS.** Theorem S (row 697), or Theorem S-w
(row 731 8.4) for W_full, with n = n_0/2 >= 3 and s <= q/5041 < 1/5041 gives
S_V(2^k n_0/2; (2^k n_0)^3) <= q^{2^k}/5041; with b = 2^k n_0 this is
e^{-delta b/n_0}/5041. Lemma E' (row 699) with a = b/2, h = N >= b costs the
factor N/(b - b/2) = 2N/b on g_V, once with the other two sides (b,b) fixed
and once with (b,N) fixed; Lemma E' allows any fixed pair. With
g_V(b/2;b^3) <= S_V(b/2;b^3) this is (5). The "for completeness" lines are the
proof of Lemma E' and are correct.

**S13 (L57), choice of tile and proof of (3). HOLDS.** With r = N/n_0,
delta = -log q, K = max(1, 8/delta), b/n_0 = 2^k the least power of two
>= K log(2+r):
- 2^k < 2K log(2+r) once K log(2+r) > 1, and 2K log(2+r) <= r for large r, so
  n_0 <= b <= N.
- delta b/(4 n_0) >= delta K log(2+r)/4 >= 2 log(2+r) >= 2 log r.
- (N/b)^2 <= r^2 <= e^{delta b/(4 n_0)}, so g_V <= 4 e^{-3 delta b/(4 n_0)}/5041
  < 1 and s <= 2 g_V <= e^{-delta b/(2 n_0)} (e^x - 1 <= 2x on [0,1]).
- At t = b/2 the bracket is (1+s)^2 s^2 <= 4 e^{-delta b/n_0}
  <= e^{-delta b/(2 n_0)}, because delta b/(2 n_0) >= 4 log(2+r) > log 4.
  (So the "further fixed increase in R_q" at L57 is not even needed.)
- (1) with R = H = c = d = N gives
  Q/V <= exp[-delta N^2/(2 n_0 b)] <= exp[-(delta/(4K)) r^2/log(2+r)].
So c_q = delta/(4K), and R_q depends only on q. All side conditions of (1)
hold: R = H = N >= b >= n_0 >= 6, c = d = N >= 3. N need not be a multiple of
anything.

**S11 (L40-49), (3) and (4). HOLDS.** (3) is the bound just proved. For the
periodic pair Q/V = (1 - Z_ab/Z_0)/2; for the magnetic pair
Q/V = sum over B_cd = 1 of Z_B / sum over all B of Z_B, the stated
probability. (4): a nonzero B has some entry B_{mu nu} = 1; on the symmetric
torus V is axis-permutation invariant, so (3) holds for the magnetic pair of
the plane mu nu, and the argument of (2) gives Z_B/Z_0 <= 64 Q_{mu nu}/V.
Both bounds are in seed units r = N/n_0 with constants depending on q only,
and they concern the unmodified Wilson integrals.

## Step 4 result: the comparison (7) and the deck bound (8)

**S16 (L75), box kernel. HOLDS.** Given the skeleton E_i and the two full
end slices, the free variables of a box are its off-boundary spatial links and
the temporal links at interior vertices. In a box with all sides >= 4 an edge
with both ends on the boundary is a boundary edge. So a temporal plaquette
either has all four edges in the skeleton (a fixed factor) or has a temporal
link at an interior vertex of a unique box. There are at most
3(2b+1)^3 <= C_0 b^3 per layer. After removing e^{-beta} per plaquette, each
factor exp(beta w_p) lies in [e^{-beta}, e^{beta}], and the normalized Haar
integral lies in [e^{-M}, e^{M}], M = C_0 beta b^3, also into a prescribed
terminal slice.

**S17 (L77), oscillation and contraction. HOLDS.** First push: the kernel
ratio K(x,y)/K(x,y') is in [e^{-2M}, e^{2M}], so for any two nonzero positive
inputs the output log ratio has oscillation <= 4M. Later pushes: with
phi = log(d mu_1/d mu_2) bounded, the u-derivative of the output log density
at y is the mean of phi under nu_{u,y}(dx) ~ mu_u(dx) K(x,y); the laws
nu_{u,y}, nu_{u,y'} dominate each other with factor e^{-4M} (kernel ratio
e^{+-2M}, normalization e^{+-2M}); writing nu_y = eps nu_{y'} + (1-eps) rho
gives a mean difference <= (1 - e^{-4M}) osc(phi); integrate in u. Common
slice factors cancel. From an end slice to the middle there are r pushes, so
one arm gives 4M (1-e^{-4M})^{r-1} <= 4M exp[-(r-1) e^{-4M}], two arms
8M exp[...]. Two normalized densities whose log ratio has oscillation w have
log ratio in [-w, w]. (The factor 1 - e^{-4M} is weaker than the Birkhoff
factor tanh M, so it is valid.)

**S18 (L79), product channels. HOLDS.** The middle law factors over boxes, so
log ratios add: at most (N/b)^3 boxes per collar and two collars give
eta = 16 (N/b)^3 M exp[-(r-1) e^{-4M}]. Given both skeletons and the whole
exterior (end slices included), the two collar interiors are independent by
locality. A mixture over end data of laws within e^{+-w} of each other is
within e^{+-w} of each of them. So the true conditional law of the two middles
given (E_0, E_t) and K_0(E_0) x K_t(E_t), with K_i = L(middle_i | E_i), are
within e^{+-eta}; projection to (Y_0, Y_t, Z) keeps this.

**S19 (L81), the channel depends on B_i only. HOLDS.** Two skeleton lifts
with the same adjoints differ by a sign cochain sigma; equal nonzero trace
signs (almost surely nonzero) force d sigma = 1 on every skeleton plaquette of
skeleton x interval. The box boundaries form the 2-skeleton of a product CW
structure of T^3, subdivided; the product with an interval does not change
H^1; so H^1(.; Z/2) = (Z/2)^3, dual to the three windings. After removing the
flat-flip part, sigma = dg on the vertices of skeleton x interval. Extending g
by any values, and using flat flips at all times on the whole torus, gives
symmetries of the periodic Wilson law that map one lift to the other and fix
Y_i. Hence L(Y_i | E_i) is a function of B_i. Z = s_0 s_t is a function of
(E_0, E_t) and is kept.

**S20 (L83), squared loss. HOLDS.** E[(Z - E(Z|D))^2] = 1 - E m^2 = 2 p(D).
Let phi = E_true(Z | Y_0, Y_t). In the channel law (B, Z) has the true law and
the middles are drawn from B alone, so phi(channel middles) is a randomized
predictor based on B: its error is >= 2 p(B). By domination and loss >= 0 it is
<= e^{eta} * 2 p(Y_0, Y_t). This is (7).

**S15 (L68-73), statement of (7). HOLDS**, by S16-S20.

**S21 (L85-89), the deck bound (8). HOLDS.** On the symmetric torus both
half periods are N/2 and the transfer is symmetric, so given the two quotients
the relative label z (signs of three winding traces, almost surely nonzero)
has probability w_z ~ k_z^2, k_z = K_{N/2}(x, z y) >= 0. The twisted trace
gives zeta_h = E sum_z sqrt(w_z w_{z+h}). Two conditionally independent paths
have label difference h with probability E sum_z w_z w_{z+h}. For h != 0,
sqrt(w_z w_{z+h}) <= (w_z + w_{z+h})/2 <= 1/2, so this is <= zeta_h/2. Z
differs exactly when h_1 = 1: four shifts. This is the upper half of row 1171
(2), checked HOLDS in row 1172; here Y_i is the whole middle modulo vertex
gauges and flat flips, a finer but still flip-invariant observation, and the
proof applies unchanged (the note re-derives it).

**S22 (L91), the competing sparse bound. HOLDS.** (8) with (4) for the four
nonzero h with h_1 = 1: p(Y) <= (1/2) * 4 * 64 exp[...] = 128 exp[...]; (7)
adds eta. With b = c_beta (log N)^{1/3} and c_beta^3 <= 1/(8 C_0 beta):
4M <= (1/2) log N, e^{-4M} >= N^{-1/2}, (r-1) e^{-4M} >= (N/16 - 2) N^{-1/2},
so eta <= C N^3 log N exp(-c N^{1/2}) -> 0. b >= 4 and N >= 2b hold for large
N. The skeleton has O(N^3/b) links per layer. The replacement in (6) then
gives liminf >= c_q/n_0^2 > 0 in the competing branch; necessity is (9),
checked in Step 6. The scope sentence (fixed bare coupling per cutoff, no
uniform mixing of a finite physical collar) is accurate.

## Step 5 result: the comparison (20), its inputs (21), and the test (22)

**S40 (L204-206), fixed axial gauge bound. HOLDS.** Re-derived in a
temporary axial gauge at every vertex (top and sides included): axial edges
are 1; a column step has squared chord 2(1 - w_p); Cauchy-Schwarz gives a
total discrepancy from the bottom edges <= 2(l+1)^2 S_alpha and at the top
<= 2l S_alpha (as row 1173 (3)). Side gauges are transports inside side faces
with common links, so they agree in both copies and undoing them changes no
distance. H_z = p_2(z) p_1(z)^{-1} is 1 on the rim of the top face. From
H_z U1bar(e) H_{z'}^{-1} = U2bar(e):
|H_z - B_e H_{z'} B_e^{-1}| <= |U1bar(e) - B_e| + |U2bar(e) - B_e|, squared sum
<= Cb(S_1+S_2). Conjugation is an isometry fixing 1, so h_z = |H_z - 1| has
increments bounded by these terms; a row Poincaré sum gives
sum h_z^2 <= (2b)^2 Cb(S_1+S_2). In the final representative, interior
transverse edges differ by at most the two bottom discrepancies (sum
<= Cb^2(S_1+S_2)), side, top and bottom edges are common, and only the last
axial bonds differ, by |H_z - 1|. Total <= C b^3 (S_1+S_2), with no smallness
assumption.

**S41 (L208), ordering on each arm. HOLDS.** The three-path law
L(U) L(V_0|E_0(U)) L(V_t|E_t(U)) has Wilson marginals, and its density with
respect to Haar x (Haar given the shared skeletons) is
w(U) w(V_0) w(V_t)/(rho_0(E_0) rho_t(E_t)). The exchange is a finite
permutation group in forest coordinates, preserves the reference measure and
the skeletons; the end slices (different in the two copies) carry label 0 and
are not exchanged. Spatial action sums are unchanged; at an interface the
exponent is beta(a_1.v_1 + a_2.v_2) or the swapped sum, giving the zero-field
Ising chain with J_s = (beta/2) sum_e (a_1 - a_2).(v_1 - v_2). The two collars
factor.

**S42 (L210), bond bounds. HOLDS.** sum|v_1 - v_2|^2 <= Cb^3(S_1+S_2) by S40
at the top slice; sum|a_alpha - v_alpha|^2 = 2 T_alpha; Cauchy-Schwarz and
b^3 >= 1 give |J_s| <= C b^3 beta D_s. An exchange at one end of a bond flips
its sign, so |J_s|, |u| and L_i = 2 artanh|u| are orbit invariant.
L_i <= 2|J_{s*}| <= C b^3 A_i (minimum <= mean). If A_i <= K_0 b^3, Markov
gives at least (r-1)/2 retained bonds with |J_s| <= 2CK_0 b^6, so
|u| <= exp[-((r-1)/2) e^{-4CK_0 b^6}] <= v_b for r >= 4, and
L_i <= 4|u| <= 4 v_b when |u| <= 1/2. With both end labels plus, the middle
label has probabilities proportional to (1+u)(1+v) and (1-u)(1-v), so the log
ratio is at most L_i + L_{i'}. The middle labels of different boxes are
independent on the orbit, so reversing all of them changes the law of the
label vector by a density at most exp(sum_i L_i).

**S43 (L212-223), (21) and the moment bound. HOLDS.**
r A_i <= (r/(r-1)) sum over retained s of beta D_s. Each face of a copy is used
by a bounded number of (box, interface) pairs (a boundary face lies in at
most two boxes; an interface lies in one arm); there are at most C r b^3 |I|
faces per copy; the copies are U, V_0, V_t, each with the Wilson marginal.
Hölder with exponent three and row 1155 (9) (absolute c = 1/8 and C, any
beta > 0, any periodic rectangle; `gap-solve7-astra62.md`) give (21) after
reducing theta. On {A_i > K_0 b^3}, p C b^3 A_i <= (theta r/2) A_i
<= theta r A_i - (theta K_0/2) r b^3, so with theta K_0/2 > C_2 + 1 the
truncated product has mean <= e^{-r b^3 |I|}. Then
e^{p L_i} <= e^{p C v_b} (1 + X_i), X_i = e^{pCb^3 A_i} 1{A_i > K_0 b^3},
and expanding over deterministic subsets,
E e^{p sum L_i} <= e^{p C v_b m_b} (1 + e^{-r b^3})^{m_b}. Taking the 1/p power
gives e^{xi_p} with xi_p = C m_b v_b + (m_b/p) e^{-r b^3}. Condition
p C b^3 <= theta r/2 is p <= c r/b^3. Correct.

**S44 (L225), assembly. HOLDS.** On an orbit, the comparison's middle in a
label vector equals the original's middle in the reversed vector; the
comparison middles have the product-channel law of (7) (V_i drawn from
L(.|E_i(U)), independently); exterior, skeletons and both winding signs (on
skeleton lines) are fixed. For f >= 0 of the projected middles and Z only the
marginal law of the middle labels enters, so
E_channel f <= E[e^{sum L_i} f] <= e^{xi_p} 4^{1/p} (E f)^{1-1/p}
(Hölder; f <= 4). With f = (Z - phi(Y))^2: 2p(B) <= e^{xi_p} 4^{1/p}
(2p(Y))^{1-1/p}, i.e. (20). Reading precision: the reversal acts on the
marginal of the middle labels; flipping only the middle label in a full label
configuration would have an unbounded density ratio. "The conditional law of
the vector of middle labels" (L210) is that marginal, so the text is right.

**S39 (L192-202), statement of (20). HOLDS**, by S40-S44, with absolute
constants under v_b <= 1/2, 2 <= p <= c r/b^3, beta >= 1, r >= 4.

**S45 (L227-231), the test (22). HOLDS.** With b ~ (log N_j)^{1/8},
b^6 = o(log N_j), so r e^{-Cb^6} = N_j^{1-o(1)}, v_b is smaller than any power,
m_b <= N_j^3, and p = floor(c r/b^3) -> infinity with xi_p -> 0. In a competing
cutoff with the absolute q, (4), (8), (20) give
-log p(B_j) >= (1-1/p)(c_q A_{R_j} - log 128) - xi_p - (log 2)/p, so the
quantity in (22) has liminf >= c_q along any competing subsequence (beta_j >= 1
on the trajectory). Hence (22) forces the periodic alternative at all large j,
the strict seed, and (W). Conversely, under (W), a periodic seed with margin
at n_j' = L'/a_j and (9) with alpha = 1/4 (each gap is N/2 - 2r >= 3N/8) give
1/2 - p(B_j) -> 0, so (22) holds; changing n_j to n_j' rescales R_j by the
fixed factor L/L'. No constant used depends on beta_j, so beta_j of order
log N_j is allowed.

## Step 6 result: all other statements

### 6a. Periodic complement, tile size, short collars, thin tori, stacks

**S23-S25 (L95-110), (9) and (10). HOLDS.** With P the vacuum Markov
transfer (reversible, positive), two stationary collar segments and two gaps
of length g each, the periodic law has density
p_g(x_+,y_-) p_g(y_+,x_-)/X(N) against the product of the segment laws
(telescoping the vacuum factors; true also with the inner temporal links).
The flip h at every layer of segment 2 preserves its stationary law, fixes B,
reverses Z. In each connector the two arguments are independent with law pi,
so ||p_g||^2 = X(2g), and ||p_g - p_g(., h.)||^2 = ||P^g(1-h)||_HS^2
= 4 Tr(P_{h,-} P^{2g}). Subtracting one factor at a time and Cauchy-Schwarz
gives ||f - f^h||_1 <= (4/X(N)) sqrt(X(2g) Tr(P_{h,-}P^{2g})), i.e. (10) for
TV. Testing against Z sgn m(B): 2E|m| <= 2 TV. Then
1/2 - p(B) = E m^2/2 <= E|m|/2. Tr(P_{h,-}P^{2g})/X(2g) = Q/V for the electric
pair with R = 2g, H = c = d = N; (1) with the tile of (5) gives the exponent
of (3) times 2g/N (b <= 2g for large N/n_0). X(2g) <= 2: a dyadic b' in
[c_alpha N, 2c_alpha N], Lemma E' three times with factors 2N/b' <= 2/c_alpha,
and time monotonicity (b'/2 <= 2g). X(N) >= 1. So
1/2 - p(B) <= 2 exp[-alpha c_q (N/n_0)^2/log(2+N/n_0)]: (9) with
C_{q,alpha} = 2, c_{q,alpha} = alpha c_q. The sparse B_i are invariant under
the flip at every layer of a collar (adjoints are centre blind; skeleton
plaquettes inside the collar interval contain 0 or 2 flipped links).

**S26 (L112), OPEN.** Correctly marked.

**S27 (L116-120), (11). HOLDS.** For b >= 16, a stride-4 grid with seam
strips omitted gives at least c b N^2 separated plaquettes; for 6 <= b < 16,
one layer in the N,N plane gives c N^2 >= c' b N^2. The Chebyshev observables
g_p = cos(d arccos w_p), d = ceil(A sqrt beta), are centre blind, so the
columns f_p psi are neutral and orthogonal to the vacuum; the one-link
variance bound c_0 = 1/4 and conditional independence give Gram >= I/4; row
1161 (20) with four links bounds each inverse form by C_A^4 (its proof uses no
side length). Then Tr(W* U^{-1} W) <= 4 C M on the span, at least M/2
eigenvalues of the compression are <= 8C, and Cauchy-Schwarz
(|x|^2 <= <x,U^{-1}x>^{1/2} <x,Ux>^{1/2}) with min-max gives M/2 neutral
excited levels with ratio >= 1/(8C). So S_+(u) >= (M/2)(8C)^{-u}.

**S28 (L122). HOLDS.** S_V >= S_+ >= c b N^2 e^{-Ct}; S_V < 1 needs
t > C^{-1} log(cbN^2), and t < b. For b = o(log N), s > 1 and the bracket of
(1) exceeds one. The scope sentence (this specific full-trace input) is
accurate.

**S29 (L124-128), (12). HOLDS.** Gamma (transverse points with a coordinate
on a grid plane) has |Gamma| <= 2N^2/b and |boundary| <= 4|Gamma|. On the
second skeleton every direction-1 link crossing the cut sits over Gamma, so
the move equals a flat flip there at every collar time; it fixes both B_i and
reverses only s_t. Changed faces: |boundary| per slice over 2r+1 slices and
|Gamma| at each of the two collar ends; or 2N^2 for the whole transverse
torus. The Haar-preserving involution changes the density by e^{+-K},
K = 2 beta x (smaller count), and fixes {B = B}. Applied to one copy it maps
agreement to disagreement: 1 - p(B) <= e^K p(B), so
-log p(B) <= log 2 + K <= log 2 + C beta N^2 min{1, (r+1)/b}. Collars are
disjoint for r < N/8.

**S30 (L130-135), (13). HOLDS.** For any channel with domination e^D the
squared-loss argument gives p(B) <= e^D p(Y); (12) gives
p(B) >= exp(-C beta N^2 (r+1)/b)/2; (4), (8) give p(Y) <= 128 exp[-c_q A];
hence D >= c_q A - C beta N^2 (r+1)/b - log 256. For r ~ N/16 the minimum in
(12) is 1 and the cost is of order beta N^2, as stated.

**S31 (L139-144), (14). HOLDS.** The N^2 stacks S_x (one per position x in
the 12 plane, w^2 plaquettes each) partition the 12-plaquettes; moving a twist
from x to x + e_1 is the coboundary of -1 on the direction-2 links at
x_1 + 1, which flips exactly S_x and S_{x+e_1}. With stack weight
e^{-beta A} e^{eps_x J_x}, the parity sums are 2^{N^2-1} Z_0 and
2^{N^2-1} Z_12, and (1-z)/(1+z) = E_nu prod tanh J_x with nu ~ prod cosh J_x
times the rest. |tanh J_x| <= tanh(beta w^2). z <= 1 by (S2). The scale
matches N3 of `gap-skeleton-max.md` and (10) of row 1163.

**S32 (L146-150), (15). HOLDS.** For w/n_0 >= R_q, the electric pair on
(N,N,w,w) with spectators w,w, tile b/n_0 in [K log(2+w/n_0),
2K log(2+w/n_0)), Lemma E' from b to w, and R = H = N >= w >= b give
1 - z = 2Q/V <= 2 exp[-c_q (N/n_0)^2/log(2+w/n_0)]
<= 2 exp[-c_j N^2/log(2+N)], c_j = c_q/n_0^2. For the finitely many smaller w,
(14) at the largest of them gives 1 - z <= 2(1-z)/(1+z) <= 2 e^{-c' N^2}.

**S33 (L152-157), (16). HOLDS.** Magnetic pair with c d = 12 (lengths N,N),
active lengths w,w >= b, s = S_V(b/2; b,N,N) as in (5): Q/V <= exp[-delta
w^2/(2 n_0 b)] <= exp[-c_q (w/n_0)^2/log(2+N/n_0)]; (2) adds the factor 64.

**S34 (L159). HOLDS.** (tanh x)^{N^2} <= exp(-N^2 e^{-2x}) <= exp(-N^{2 eps})
for beta w^2 <= (1-eps) log N. In the competing branch z(N,N) <= 1/2 for large
N by (16), so a first crossing exists; it exceeds sqrt((1-eps) log N/beta)
and is at most w_N = ceil(2K n_0 log(2+N/n_0)), where (16) gives z -> 0. In
the periodic branch (15) keeps z > 1/2 for all w. At w_N, (16) gives
-log z >= 4K^2 c_q log(2+N/n_0) - log 64, so liminf[-log z]/log N = 0
excludes the competing branch, and (15) makes it necessary.

**S35 (L161). HOLDS.** At the identity field J_x = beta w^2; and
1 - (tanh x)^{N^2} <= N^2 (1 - tanh x) <= 2 N^2 e^{-2x} -> 0 for x ~ (log N)^2.

**S36 (L165-171), (17). HOLDS.** nu has total mass
2^{N^2-1}(Z_0+Z_12) times its normalizer; cancelling cosh on D and expanding
the others leaves 2^{N^2-|D|} twisted integrals with D deleted, all equal to
Z_del(D) because any residual twist moves onto a deleted stack (D nonempty);
the constants give 2 e^{-beta A|D|} Z_del(D)/(Z_0+Z_12). Row 1167 (1) (all
deleted faces contain direction 1; sides >= 4, hence w >= 4) gives
Z_del(D) <= z_beta^{-A|D|} Z_0. With Z_0/(Z_0+Z_12) <= 1 this is (17). Cap
estimate: z_beta >= c(1+beta)^{-3/2}. Note: "taking one normal direction as
time" means a direction of the 12 plane (the plane of the positions x), as in
L144; with direction 1 as time the 12-plaquettes are electric, as row 1167
needs.

**S37 (L173-181), (18). HOLDS.** Fixing all but one link of one plaquette of
S_x makes J_x a nonconstant affine function of that quaternion, so J_x = 0 is
null. 1 - |tanh u| = e^{-|u|} sech u <= sech u;
1 - prod|tanh J_x| <= sum sech J_x; (17) with |D| = 1. Second line:
E_nu P_J - E_nu prod tanh = E_nu P_J (1 - prod|tanh|) and
E_nu P_J = 1 - 2 nu(P_J = -1). h_beta^{-1} = int e^{beta tr g/2} dg > 1 by
strict Jensen. Credit: Lemma PAR-T of `gap-cr-tomboulis-max.md` 6.1 states
that every proper sub-product has mean 0 (Mack-Petkova parity algebra).

**S38 (L183-188), (19) and fairness. HOLDS.** Joint law of (U, eps):
P(prod eps = -1) = z/(1+z). A misread at x needs
sum over S_x of (1 - eps_x w_p) >= k; Markov with exp(beta(. - k)) deletes
those k faces; moving the twist (deleted faces are sign blind) leaves no
twist or one full stack, a temporal insertion with direction 1 as time;
trace Hölder with a norm-one unitary bounds the integral by z_beta^{-k} Z_0;
divide by the uniform sign average (Z_0+Z_12)/2 >= Z_0/2; sum over N^2
positions. Fairness: an even number of whole-stack changes, using a spare
position, is a link-sign change of variables that preserves the joint law and
the label parity and flips the read signs on the chosen subset.

### 6b. Energies, one-slice test, cooling comparison, barrier, tables

**S47 (L242), heavy entries. HOLDS.** (1) with R = T >= b, H = c = d = N and
the tile of (5) gives Q/V <= exp[-delta T N/(2 n_0 b)]
<= exp[-c T N/(n_0^2 log(2+R))]. Electric pair, a = time: Q contains the
C_b-odd sector, so (||F_0|_q||/lambda_0)^T <= Q/V for q_b = 1 (already at finite
T). Magnetic pair: Q^{1/T} -> max over m_cd = 1 of ||F_m|_0||, V^{1/T} ->
lambda_0 (Lemma W (c)); the magnetic top vector is even by (S3). So
E >= c R/(n_0 log(2+R)).

**S48 (L244-248), (23). HOLDS.** A dyadic b' in [N/4, N/2], Lemma E' three
times (factors <= 8), gives S_V(u;N^3) <= C e^{-cN/n_0} at u = b'/2 in
[N/8, N/4]. Sum of x^k <= (sum of x)^k for x in [0,1] and time monotonicity
give S_V(T/2) <= S_V(u)^{floor(T/(2u))}, and (N/n_0) floor(T/(2u)) >= T/n_0.

**S49 (L250), light magnetic entry (periodic seed). HOLDS.** Electric pair
for the plane of the spatial twist, spectators of lengths N and T; Lemma E'
from b to N and to T gives the factor 4NT/b^2; with b/n_0 the first power of
two above K log(2+T/n_0) and log(2+T/n_0) <= 2 log(2+R), b <= N and
1 - Z_m/Z_0 <= C e^{-c A_R}. Tr M^T = (Z_m/Z_0)(Z_0/lambda_0^T)
>= 1 - C e^{-cA_R}; Tr M^{T/2} <= Z_0(T/2)/lambda_0^{T/2} <= 1 + C e^{-cT/n_0}
by (S2) and (23); Lemma A (b) gives ||M||^{T/2} >= Tr M^T/Tr M^{T/2}; with
T ~ n_0 R^2 this gives E_{m,0} <= C e^{-cA_R}/(n_0 R^2) (the top of F_m is in
q = 0 by (S3)).

**S50 (L252), light electric entry (competing seed). HOLDS.** A nonzero
temporal seam e has an entry in a plane (0,i); the magnetic pair of that plane
has active spatial directions j,k, in whose frames (0,i) is magnetic; the tile
on (b,T,N) as in S49; Z_e <= 8Q and V(T)/lambda_0^T <= 1 + C e^{-cT/n_0}.
Fourier inversion: X_{0,0}(T) - X_{0,q}(T) = (1/4) sum over chi_q(e) = -1 of
Z_e/lambda_0^T in [0, C e^{-cA_R}]; X_{0,0}(T) >= 1; X_{0,q}(T/2) <= X_{0,0}(T/2)
<= 1 + C e^{-cT/n_0}; the two-period quotient finishes.

**S46 (L235-240), the table. HOLDS**, by S47-S50 (the periodic light row is
stated for elementary spatial twists only, which is what S49 proves).

**S51 (L254), one-sector selector. HOLDS.** Competing row:
E_{m,0} >= cN/(n_0^2 log(2+N/n_0)), not o(N/log N); E_{0,q}
<= C e^{-cA_R}/(n_0 R^2), so -log E_{0,q} >= c N^2/(n_0^2 log(2+N/n_0)) - O(log N),
not o(N^2/log N). Periodic row: E_{m,0} -> 0 and E_{0,q} -> infinity, so both
conditions hold there in the stated one-sided sense.

**S52-S53 (L258-268), (24). HOLDS.** P = psi^{-1}(F/lambda_0)psi is
reversible and positive (F = DCD >= 0), so the Poincaré inequality with
gamma = 1 - ||P_{+,exc}|| holds for neutral functions. A unit top h in q has
Dirichlet form d; |h| is neutral with form <= d; ||h - f||^2 = 2(1 - E|h|)
<= 2 Var|h| <= 2d/gamma; eps = Pr(f(X) != f(Y)) = E(f(X)-f(Y))^2/4
<= (3/4)(4d/gamma + 2d) <= C d/gamma. A single link flip u changes D (four
faces, half weight) by e^{+-4 beta} and the one electric face by e^{+-2 beta}:
F(ux,y)/F(x,y) in [e^{-6 beta}, e^{6 beta}], the same for psi, e^{12 beta} for
the joint density; so pi{f(x) != f(ux)} <= (1 + e^{12 beta}) eps. f(g_M x) =
-f(x) since q is odd on the cut. Summing over the first sign change and
changing variables by g_l gives O_N(pi) <= N^2 (1 + e^{12 beta}) C d/gamma.

**S54 (L270-274), gamma and (25). HOLDS.** x_1^u <= S_V(u;N^3) <= C e^{-cN/n_0}
at u ~ N gives gamma >= c_q/n_0. (24) with the light bound gives the first
estimate. For (25): pi_T = sum_k w_k phi_k^2 with w_k ~ mu_k^T; each
X_{0,q}(T) is within C e^{-cA_R} of its leading term x_q^T >= 1 - C e^{-cA_R};
int |h^2 - 1| dpi <= ||(|h|-1)||_2 ||(|h|+1)||_2 <= 2 sqrt(2d/gamma)
<= C e^{-cA_R} after lowering c; hence ||pi_T - pi||_TV <= C e^{-cA_R}; and
|min_l a_l - min_l b_l| <= sum_l |a_l - b_l| with Haar invariance gives the
factor 2(M+1).

**S55 (L276-281), (26). HOLDS.** A prefix (k full rows and part of the next)
has transverse boundary at most 2N + 2 <= 4N + 4 edges; only those spatial
faces change sign; D(g_l x)/D(x) >= e^{-beta(4N+4)}; with psi = D G this gives
(26). lambda_0 G = C(D psi) follows from psi = lambda_0^{-1} D C D psi.

**S56 (L283), the auxiliary density. HOLDS.** The M straight
direction-1 holonomies use disjoint links and are independent Haar, so
c_s^{-M} cosh(s sum W_y) is a probability density; it is gauge and flat-flip
invariant (cosh is even), analytic and positive; one link flip changes at most
one W_y, a factor in [e^{-2s}, e^{2s}]. At the half prefix l = floor(M/2) the
four component affinities are c_s^{-l} or c_s^{-(M-l)}, so
O_N <= affinity <= c_s^{-l} + c_s^{-(M-l)} <= 2 c_s^{-floor(M/2)}. The three
orientation factors live on disjoint link sets and do not change under the
direction-1 cut.

**S57 (L287-291), (27). HOLDS.** Extending the prefix flip through all
layers leaves every temporal face unchanged and changes at most 4N + 4 spatial
faces per layer (half weight at the two ends): cost <= C beta N (t+1).
Flipping the bottom only changes at most N^2 temporal faces plus the bottom
perimeter: cost <= C beta N^2. Both are Haar translations of the integrated
links, so v_t(g_l x)/v_t(x) is bounded pointwise, and int v_t^2 = 1.

**S58 (L293), optimal order. HOLDS.** For each z, h_s(., z) is a sign on the
y circle; a change in y or s forces an odd number of changed faces in the
corresponding longitudinal ribbon, and distinct ribbons are face disjoint. The
bottom row is half negative; if every layer has both signs there are at least
2(t+1) changes, otherwise some layer is constant and at least N/2 temporal
changes lie between it and the bottom. Summing over z gives
N min{2(t+1), N/2}; at the identity field each changed face costs at least
beta. This matches C beta N min(t+1, N) in order.

**S59 (L295-300), (28) and the two-point example. HOLDS.** 1 = eta_N psi + r,
r neutral, r orthogonal to psi, ||r|| <= 1; (F/lambda_0)^t 1 = eta_N psi + e,
||e|| <= (1-gamma)^t; ||u/||u|| - psi|| <= ||e||/eta_N, so the factor 2 is
generous. ||v_t^2 - psi^2||_1 <= 2||v_t - psi||_2 and the min-difference bound
give the second inequality. Two-point example: with u = c(psi_2, -psi_1),
F_12 = gamma psi_1 psi_2 > 0 and F_ii > 0; <1,u> != 0 because psi is
nonconstant; the error is of order (1-gamma)^t. The obstruction sentence is
right: the error term is at least of order N^2 e^{-2 gamma t} while (27) gives
only exp(-C beta N t), and gamma <= 1 < C beta N. The final clause is OPEN, as
marked.

**S60-S62 (L304-313), the spectator and (29). HOLDS.** Fair signs on
three-cells, factors 1 + rho prod over the boundary on four-cells: expanding,
an unpaired sign integrates to zero, so on a connected torus only the empty
set and the whole torus survive (each three-cell lies in exactly two
four-cells, so the full product is 1): Z_spec = 1 + rho^{V_4}. In a one-step
slab the same argument on the connected spatial torus gives
K(x,y) = 1 + rho^s v(x) v(y) = |1><1| + rho^s |v><v|. The spectator is
independent of the links, so all Wilson-path quantities and ratios are
unchanged and every partition function gets the factor 1 + rho^{V_4} in
(1,2]. The state psi_0 x v is centre invariant with normalized eigenvalue
rho^{n^3}; at u = floor(n_j/512), rho^{n_j^3 u} >= exp(-a_j L^4/512) -> 1, and
at n_j/2 the excess is >= exp(-a_j L^4/2) -> 1. Physical energy
a_j^5 n_j^3/a_j = a_j L^3 -> 0.

**S63 (L315). HOLDS.** f_prod >= f_W since the added term is >= 0;
enlarging all sides by an integer k does not increase F_W/|n| (Lemma A) and
log 2/|kn| -> 0, so f_prod = f_W. The excess correction is
log(1 + e^{-a_j L^4}) -> log 2, and n_j m_prod <= a_j^5 n_j^4 = a_j L^4 -> 0.

**S64 (L319-324), (30). HOLDS.** On {|J_x| <= t}, sech J_x >= e^{-t}, so
(17) with |D| = 1 gives nu(|J_x| <= t) <= 2 h_beta^A e^t; t = d_beta A/2 and
a union bound give (30). A change of at most d_beta A/(8 beta) face traces
moves J_x by at most d_beta A/4, so a sign change of J_x needs the event in
(30). Union bound over k stationary steps.

**S65 (L326). HOLDS.** Periodic branch: z -> 1 by (15), so
nu(P_J = -1) -> 1/2 by (18) (w ~ log N makes N^2 h^{w^2} -> 0). Started from
nu given P_J = +1, the chance of parity -1 after k <= e^{d_beta A/4} steps is
<= 2kN^2 e^{-d_beta A/2}/nu(P_J=+1) -> 0, so TV >= 1/2 - o(1). Competing
branch: z -> 0 at the logarithmic width by (16), so nu(P_J = -1) -> 0.

**S66 (L330-336), table of stopped routes. HOLDS.** Each row restates
S27-S28, S29-S30 with S15 and S39, S37-S38 with S64, S56-S59, S60-S63.
Reading precision: row 3's "fair ... by (19)" refers to the fairness paragraph
after (19), not to inequality (19) itself.

**S4 (L11), OPEN restatement of (W). HOLDS as a restatement.** It matches
Theorem ZD-c (row 720, L311 here and on main at `8b11ae2bb9`), with the
domain repair L >= 4L_0 (row 730 item 18) and the strict-margin completion
(row 730 L195-225).

**S1-S3, S5, S6 (L3, L5, L9, L13, L15), GUIDE.** Local claims checked: the
pin `f216fbb66` exists; `prior/repo-search-2026-11-08.md`,
`prior/gap-crux-prior-ym.md` and `../parts/gap.md` exist; Theorem ZD-c is at
L311 of `research/mass-gap/library/gap-phys-seed.md` at `8b11ae2bb9`; Theorem F
(b) is the two-direction amplification at fixed other sides; Remark F3 treats
the static twist on a fixed section. "Row 1173, unchecked at this pin" (L13)
was true at the pin; row 1174 has since checked it (HOLDS,
`gap-solve15-check-opus.md`), and this note re-derives the parts of row 1173
it uses. External PR heads and outline line ranges in L3, L5 were not
re-opened (reading only).

**S67 (L338), OPEN. HOLDS as marked.** **S68 (L340), RESULT. HOLDS as a
summary**; for (20) the exponent carries the factor 1 - 1/p, which the form
C_j exp[-c_j N^2/log N] absorbs.

### 6c. Completion of 6b (second session)

Resumed by Claude Opus 5.5 (laptop Claude Code subagent) after the first
session lost its connection. It is the same model as the first session, so
this pass is not an independent check of the first one.

What was on disk. Section 6b above already has entries for S46-S66, S4,
S1-S3, S5, S6, S67 and S68. The first session stopped after these entries,
before Steps 7 and 8. I read the file under check in full again, and Steps 1-6b
of this file in full. For each 6b entry I re-derived the statement by hand from
the note and the cited lines: row 697 (`gap-crux-restate.md` L37 Lemma A,
L178-184 Lemmas K and X, L213-215 Lemma E'), row 731 (`gap-flux-exercise.md`
L129-133, C2 (S1)-(S3)), row 720 (`gap-phys-seed.md` L55 notation, L311-320
Theorem ZD-c). The 6b verdicts stand. Below: one error in the first session's
text (N1), one reading point in the note (N2), one precision (N3), and the
places where my derivation adds to a 6b entry. No earlier text is changed.

**N1 (S47, the 6b parenthesis "already at finite T"). The parenthesis is
false as written; the verdict is unchanged.** At finite T one has
Q >= ||F_0|_q||^T and V >= lambda_0^T. This gives only
(||F_0|_q||/lambda_0)^T <= (Q/V)(V/lambda_0^T), and V/lambda_0^T > 1. Example:
Q = mu^T and V = lambda_0^T + mu^T give Q/V < (mu/lambda_0)^T. The note (L242)
takes T-th roots and lets T grow. Then V^{1/T} -> lambda_0, because the vacuum
is simple, and in the magnetic case ||F_m|_0|| <= lambda_0 by (S2), (S3). So
S47 HOLDS as the note states it. A finite-T form also holds: for T >= N/4 and
large R, V/lambda_0^T = 1 + S_V(T;N^3) <= 1 + S_V(u;N^3) <= 2 with u <= N/4
from the propagation in S48, so (||F_0|_q||/lambda_0)^T <= 2Q/V.

**N2 (S58, L293, reading point in the note). HOLDS unchanged.** L258 orders
the M = N^2 cut links "row by row" but does not say which transverse
coordinate is constant on a row. L293 needs, for each z, a line along y on
which the half prefix has exactly N/2 negative signs. This is true when the
rows of L258 are the lines of constant y. Then the "row" of L293 (a line of
constant z) is a column of the L258 ordering. With the other orientation,
exchange y and z in L293 and use ribbons in the (1,3) planes. The bound
N min{2(t+1), N/2} is the same. The 6b entry reads it the same way.

**N3 (S59, the 6b phrase "the error term is at least of order
N^2 e^{-2 gamma t}"). Precision only.** (1-gamma)^t >= e^{-2 gamma t} needs
gamma <= 1/2. This holds for the gap c_q/n_0 that the seed furnishes, which is
the case L300 treats. For any fixed gamma in (0,1) the error bound
4(N^2+1) eta_N^{-1} (1-gamma)^t still exceeds exp[-C beta N (t+1)] at large N,
since -log(1-gamma) is fixed and C beta N grows. The obstruction sentence
holds.

Additions to the 6b entries (re-derived by hand):

- S47-S50. The two-period quotient is Lemma A (b) of row 697 L37,
  lambda_0^k >= Tr S^{2k}/Tr S^k for S >= 0, S != 0, with k = T/2. (S3) of row
  731 L133 (lambda_m(B) <= lambda_0(B), with an even top eigenvector) gives
  ||F_m|| = ||F_m|_0||, so E_{m,0} is the energy of the magnetic vacuum. In S49
  the tile margin is 4NT/b^2 <= 4(T/n_0)^2 <= 4 e^{delta b/(4 n_0)}, since
  N <= T, b >= n_0, delta K >= 8; this is the margin of S13 with
  log(2+T/n_0) <= 2 log(2+R). In S48, with u = b'/2 <= N/4 and
  k = floor(T/(2u)) >= 2T/N - 1, one gets (N/n_0) k >= (2T - N)/n_0 >= T/n_0
  because T is about N^2/n_0 >= N. In S50, X_{0,0} - X_{0,q} equals
  (1/4) times the sum of Z_e/lambda_0^T over the four e with chi_q(e) = -1, at
  both times T and T/2, and every Z_e >= 0.
- S51. At a fixed cutoff the competing row gives E_{m,0} log N/N >= c/n_0^2 > 0
  along every sequence, and
  -log E_{0,q} >= c A_R + log(n_0 R^2/C) >= c N^2/(n_0^2 log(2+N/n_0)). The
  periodic row gives E_{m,0} -> 0 and E_{0,q} -> infinity, so
  [-log E_{0,q}]_+ = 0 for large N. Under (W) the periodic row holds with the
  enlarged seed side n_0' = l/a_j of Theorem ZD-c, as in S14.
- S52-S53. Re-derived without change: the Dirichlet form of h is d; |h| is
  neutral with form at most d; the Poincaré inequality on neutral functions
  holds since 0 <= P <= 1 - gamma on the neutral complement of 1;
  1 - E|h| <= Var|h|; E(f(X)-f(Y))^2 <= 3(4d/gamma + 2d); one link flip moves
  F by at most e^{6 beta} (four spatial faces at half weight, at most beta
  each; one temporal face, at most 2 beta, pointwise in the integrated
  temporal links); the joint density by at most e^{12 beta}; the sum runs over
  the M sign-change positions after the substitution x -> g_l x.
- S54. In (25) the normalizer of pi_T in vacuum units is the sum over the eight
  characters of X_{0,q}(T), which is within C e^{-c A_R} of 8. If one character
  had two eigenvalues near lambda_0, then X_{0,q}(T) would be near 2, against
  X_{0,q}(T) <= 1 + C e^{-cT/n_0}. So each leading charged state is simple for
  large R, and the step for "a leading charged state" applies.
- S56. A different derivation of the same conclusion. Let S_l be the tilt
  argument after the prefix flip of length l. Then S_M = -S_0 and
  |S_{l+1} - S_l| <= 2, so min_l |S_l| <= 1 at every configuration. Hence
  O_N <= c_s^{-M} cosh s, which is at most 2 e^{-c N^2} for large N. The note's
  affinity bound 2 c_s^{-floor(M/2)} is weaker but sufficient.
- S60-S63. Row 720 L55 defines Delta(n) = F(n) - f|n| with
  f = inf F(n)/|n|. Its L135 and L370 give D(n) = Delta(n^4) through the same
  doubling series, consistent with the identity at its L361. So the spectator changes D_j by log(1 + rho_j^{n^4}), a
  number in (0, log 2], and leaves f unchanged by the enlargement argument of
  L315. D^+ changes by at most log 2, while n_j m_prod <= a_j L^4 -> 0, so the
  gap half of (W) fails for the product.
- S64-S65. Re-derived without change. In S65, k <= e^{d_beta A/4} gives
  2kN^2 e^{-d_beta A/2} <= 2N^2 e^{-d_beta w^2/4} -> 0 at w of order log N.

GUIDE statements S1, S2: external sources. The first session did not open
them. I read the cited lines read-only in this clone (git show at the PR head
commits) and in a local copy of the Sussman-Alpoge repository outside the
repository.
- PR 10114 at `f76f6c649cff`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` L4-14, L106-123:
  a positive one-step plaquette witness at every beta > 0, and a fixed-spacing
  threshold at 0 < beta <= 1/32. Matches L3.
- PR 10133 at `89faef229ff6`, ym4d-proof `APPROACH_REGISTRY.md` L226-229: the
  crossover hybrid is "Reduction only" and closes no MG row. Matches "leaves
  the crossover open".
- PR 10134 at `1e70c7211a2c`, `mass-gap-interface.md` I1-I5: I3 says NT1 gives
  no gap. Matches.
- PR 10141 at `a2f6a430e251`, `research/ym4d/library/fp1.md` L299-315: a
  constrained single-scale H^1 estimate. Matches.
- PR 10149 at `7fc6b1a3e644`, `PROOF_TREE.md` L47-51: third transition, depth
  and cutoff control, and the physical gap are OPEN. Matches.
- Sussman-Alpoge: `YM4_sketch_500.tex` L2313-2336 is (GL8),
  Z_s(0) = Tr L^s with L = P C^{1/2} e^{-V} C^{1/2} P; L588-599 is the
  (1+t)^{-2} spectral example; L2195-2243 contains (GL3), (GL4). CA-I
  L2704-2712 lists "a mass gap" among the statements not asserted; CA-I
  L47244-47251 is a remark that bounds depend on d and L only. Matches. The
  byte sizes of the local copy agree with its tree listing, but its commit is
  not recorded, so the pin `31a47c543775` was not confirmed.

## Step 7 result: numeric guide (a guide only)

One scratch script outside the repository, not kept: Python with numpy, peak
memory about 1.0 GB, run time about 1 s.
- S56. Monte Carlo, 2 x 10^5 Haar samples of the M straight windings, N = 4, 6,
  s = 0.5, 1, 2. In all six cases the estimate of O_N was below the note's bound
  2 c_s^{-floor(M/2)} and below c_s^{-M} cosh s. Example N = 6, s = 2: O_N about
  6.0 x 10^{-8}, c_s^{-M} cosh s about 2.1 x 10^{-7}, note bound
  4.7 x 10^{-4}. The largest sampled min_l |S_l| was 0.99.
- S59. Two-point example with uniform weights, psi = (0.6, 1.281) and
  (1.2, 0.748), gamma = 0.1 and 0.5. All kernel entries were positive, and
  ||v_t - psi||/(1-gamma)^t settled at a positive constant (about 0.36 and
  0.23), below 2/eta_N, for t up to 12.
No verdict depends on these runs.

## Step 8 result: verdict table, counts and RESULT

Status: complete. This section replaces the "in progress" status line at the
top. Checked by hand by Claude Opus 5.5 (row 1176), in two sessions of the
same model: Steps 1-6b in the first session, 6c-8 in the second.

Positive claims, in the order of the row:
- The equivalence (6): given the one-cube neutral bound
  s_+(floor(n_0/512)) <= 1/2 at the sufficiently fine cutoffs, (W) holds if
  and only if the elementary twist cost is o(N^2/log N) along a sequence at
  each sufficiently fine fixed cutoff. HOLDS (S7-S14; Step 2 and Step 3).
- The competing-seed upper bounds (3)-(4): HOLD (S11-S13; Step 3).
- The sparse-endpoint bounds (7)-(8) at fixed bare coupling: HOLD (S15-S22;
  Step 4).
- The coupling-free comparison (20) and the varying-cutoff test (22): HOLD
  (S39-S45; Step 5).

| S | Line | Mark | Statement | Verdict | Checked in |
|---|---|---|---|---|---|
| S1 | L3 | GUIDE | repo search, pins, PR citations | HOLDS | 6b; 6c (PR heads read) |
| S2 | L5 | GUIDE | credits, outline and CA-I citations | HOLDS (pin `31a47c543775` not confirmed) | 6c |
| S3 | L9 | GUIDE | plan | HOLDS | 6b |
| S4 | L11 | OPEN | strict seed 1/1650; repaired domain of (W) | HOLDS as a restatement | 6b |
| S5 | L13 | GUIDE | starting point: rows 697, 1161, 1173 | HOLDS | 6b |
| S6 | L15 | GUIDE | summary and scope of the note | HOLDS | 6b |
| S7 | L19 | PROVED | the two pairs (V,Q), sector traces | HOLDS | Step 2 |
| S8 | L21-26 | PROVED | (1) | HOLDS | Step 2 |
| S9 | L28-30 | PROVED | proof of (1) | HOLDS | Step 2 |
| S10 | L32-36 | PROVED | (2) | HOLDS | Step 2 |
| S11 | L40-49 | PROVED | (3), (4) | HOLDS | Step 3 |
| S12 | L51-55 | PROVED | (5); enlargement at t < b | HOLDS | Step 3 |
| S13 | L57 | PROVED | tile choice; proof of (3) | HOLDS (the extra increase of R_q is not needed) | Step 3 |
| S14 | L59-64 | PROVED | (6): sufficiency and necessity | HOLDS | Step 2 |
| S15 | L68-73 | PROVED | (7) | HOLDS | Step 4 |
| S16 | L75 | PROVED | box kernel in [e^{-M}, e^{M}] | HOLDS | Step 4 |
| S17 | L77 | PROVED | oscillation 4M; contraction 1 - e^{-4M} | HOLDS | Step 4 |
| S18 | L79 | PROVED | domination by e^{eta} of the product channel | HOLDS | Step 4 |
| S19 | L81 | PROVED | the channel depends on B_i only | HOLDS | Step 4 |
| S20 | L83 | PROVED | squared loss gives (7) | HOLDS | Step 4 |
| S21 | L85-89 | PROVED | (8) | HOLDS | Step 4 |
| S22 | L91 | PROVED | competing sparse bound; b of order (log N)^{1/3} | HOLDS | Step 4 |
| S23 | L95-100 | PROVED | (9) | HOLDS | 6a |
| S24 | L102-108 | PROVED | (10); E abs(m) <= TV | HOLDS | 6a |
| S25 | L110 | PROVED | odd-projection amplification; X(2g) <= 2 | HOLDS | 6a |
| S26 | L112 | OPEN | missing sparse lower bound | HOLDS as marked | 6a |
| S27 | L116-120 | PROVED | (11) | HOLDS | 6a |
| S28 | L122 | PROVED | tile size forced by (11) | HOLDS | 6a |
| S29 | L124-128 | PROVED | (12) | HOLDS | 6a |
| S30 | L130-135 | PROVED | (13) | HOLDS | 6a |
| S31 | L139-144 | PROVED | (14) | HOLDS | 6a |
| S32 | L146-150 | PROVED | (15) | HOLDS | 6a |
| S33 | L152-157 | PROVED | (16) | HOLDS | 6a |
| S34 | L159 | PROVED | first crossing width; thin-width selector | HOLDS | 6a |
| S35 | L161 | PROVED | scope of (14) | HOLDS | 6a |
| S36 | L165-171 | PROVED | (17) | HOLDS (time is a direction of the 12 plane) | 6a |
| S37 | L173-181 | PROVED | (18); Mack-Petkova credit | HOLDS | 6a |
| S38 | L183-188 | PROVED | (19); fairness of strict subsets | HOLDS | 6a |
| S39 | L192-202 | PROVED | (20) | HOLDS | Step 5 |
| S40 | L204-206 | PROVED | fixed axial gauge bound C b^3 (S_1+S_2) | HOLDS | Step 5 |
| S41 | L208 | PROVED | ordering chain on each arm | HOLDS | Step 5 |
| S42 | L210 | PROVED | bond and L_i bounds | HOLDS | Step 5 |
| S43 | L212-223 | PROVED | (21); moment bound e^{xi_p} | HOLDS | Step 5 |
| S44 | L225 | PROVED | assembly of (20) | HOLDS (reversal acts on the label marginal) | Step 5 |
| S45 | L227-231 | PROVED | (22) | HOLDS | Step 5 |
| S46 | L235-240 | PROVED | heavy and light table | HOLDS | 6b, 6c |
| S47 | L242 | PROVED | heavy entries | HOLDS (6b parenthesis wrong; 6c N1) | 6b, 6c |
| S48 | L244-248 | PROVED | (23) | HOLDS | 6b, 6c |
| S49 | L250 | PROVED | light magnetic entry, periodic seed | HOLDS | 6b, 6c |
| S50 | L252 | PROVED | light electric entry, competing seed | HOLDS | 6b, 6c |
| S51 | L254 | PROVED | one-sector selector | HOLDS | 6b, 6c |
| S52 | L258-266 | PROVED | (24), statement | HOLDS | 6b, 6c |
| S53 | L268 | PROVED | proof of (24) | HOLDS | 6b, 6c |
| S54 | L270-274 | PROVED | gamma >= c_q/n_0; (25) | HOLDS | 6b, 6c |
| S55 | L276-281 | PROVED | (26) | HOLDS | 6b |
| S56 | L283 | PROVED | auxiliary density with O_N <= 2 e^{-cN^2} | HOLDS | 6b, 6c, Step 7 |
| S57 | L287-291 | PROVED | (27) | HOLDS | 6b |
| S58 | L293 | PROVED | optimal order N min{2(t+1), N/2} | HOLDS (row orientation; 6c N2) | 6b, 6c |
| S59 | L295-300 | PROVED | (28); two-point sharpness; obstruction | HOLDS | 6b, 6c (N3), Step 7 |
| S60 | L304 | PROVED | cooling comparison, claims | HOLDS | 6b |
| S61 | L306 | PROVED | spectator partition function and transfer | HOLDS | 6b |
| S62 | L308-313 | PROVED | (29) | HOLDS | 6b |
| S63 | L315 | PROVED | bounded excess; vanishing product gap | HOLDS | 6b, 6c |
| S64 | L319-324 | PROVED | (30) | HOLDS | 6b |
| S65 | L326 | PROVED | barrier in both branches | HOLDS | 6b, 6c |
| S66 | L330-336 | PROVED | table of stopped routes | HOLDS (row 3 cites the paragraph of (19)) | 6b |
| S67 | L338 | OPEN | what is missing | HOLDS as marked | 6b |
| S68 | L340 | RESULT | summary | HOLDS as a summary (factor 1 - 1/p of (20) absorbed) | 6b |

Counts: 68 statements (59 PROVED, 3 OPEN, 5 GUIDE, 1 RESULT). 68 HOLDS,
0 HOLDS AFTER CORRECTION, 0 FAILS. Corrections: none needed in the note. One
error in the first session's text (S47, 6b) is recorded in 6c N1, with no
verdict change. Not done: the commit pin of the external outline (S2), and any
check by a second provider (row 1177 runs in parallel).

RESULT: Row 1176 (check of row 1175, `library/gap-solve16-astra62.md`), by hand by Claude Opus 5.5 in two sessions: 68 statements, 68 HOLDS, 0 HOLDS AFTER CORRECTION, 0 FAILS. Given the one-cube neutral bound, (W) is equivalent to an elementary twist cost o(N^2/log N) along a sequence at each sufficiently fine fixed cutoff, and the competing-seed upper bounds (3)-(4), (7)-(8) and (20) hold; one error in this file's own 6b text (S47) is noted in 6c with no verdict change; the note's OPEN items (branch selection, physical neutral bound, (W), mass gap) stay OPEN.
