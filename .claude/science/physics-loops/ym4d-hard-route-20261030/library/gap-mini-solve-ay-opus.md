lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:09Z

# gap-mini-solve-ay-opus (FINISH row 1309): mass gap for 4D SU(2) Yang-Mills

Started 2026-11-20T17:09Z (date -u). Branch claude/ym4d-hard-route, pinned at 74a4c7244.
Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.


## Step 0. Record read (statements about the record, not evidence; written 17:12Z by date -u)

Read at pin 74a4c7244: `GOAL.md` in full; `FINISH.md` L1-84, L299-352 and this row (L1390); the RESULT text of rows
1296 and 1299; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` L1-126 (row 1218); Steps 0-1 and 5 of
`library/gap-mini-solve-aw-opus.md` (row 1299); `library/gap-mini-solve-ax-opus.md` (row 1300, Step 0 only at this pin).
Sources fetched by URL into a scratch folder outside the repository: Sussman and Alpoge's complete account CA-III and
outline `YM4_sketch_500.tex` at commit 31a47c543775.

What the record fixes (pointers, not evidence):
1. Modulo the ultraviolet carry, the gap clause reads one lattice input at order-one coupling: (N-phys) of row 1161, or a
   uniform cube gap plus the count (TR) of row 1259 at one coupling in the window. About 45 route families to it are on
   file with their first failing step (`parts/gap.md` route registry and methods 19-36; rows 1189, 1194, 1199, 1237,
   1241, 1273 tables). Rows 1296, 1299, 1300 find no route off the record; rows 1301-1308 work the owner's tiling and
   positivity directions on it now.
2. The one-cutoff carry (rows 1256-1299) is reduced to named inputs. Open after row 1299 (its Step 5.1 table): the
   outline's premises (UM1, UM4-UM6, UM14), p_1 > p_0 for (E0), (M), `9.1:prop-blind-site-expansions`, (V9), (DET),
   the seed. Row 1296 closed (DET)'s normalisation question (Lemma CONS, Proposition PN) and lists as OPEN "Theorem
   9.1's hypotheses, including the account's outstanding blind-site expansion".
3. `9.1:prop-blind-site-expansions` (CA-III L16559) is the one statement on that list that the complete account itself
   marks "Proof outstanding". It is hypothesis (e) of `9.1:thm-last-lattice-comparison` (CA-III L17912; rows 1233,
   1234, 1255), and `library/chain-ca.md` L208 lists it as F56, outstanding, on the T0 chain (core uniqueness, clause
   (v), CA-III L110798-110824 per chain-ca step 5).

## Step 1. How best to attack it (judgement, ARGUED; written 17:12Z by date -u)

**The seed.** I do not attack it. Every candidate I can name is on file at its first failing step (item 1 above), and
row 998 9.5 calls another screen by this model family a waste. Nothing below is progress on the seed.

**The item.** `9.1:prop-blind-site-expansions` (Sussman and Alpoge, CA-III L16559-16800). Why this one:
- It is OUTSTANDING in the account (index status OUTSTANDING; "Proof outstanding" at CA-III L16634). GOAL.md's method
  puts proof work on exactly such statements on the T0 chain.
- It is on the gap carry (hypothesis (e) of Theorem 9.1, which the carry of rows 1233, 1256-1299 reads).
- Rule 0a: `grep blind library/open-core.md` gives nothing; in FINISH.md the label occurs only in RESULT lines that
  list it as open (rows 1233, 1234, 1255, 1256, 1264, 1275, 1278, 1293, 1294, 1296, 1299); no row attacked it
  ("island-blind" occurs in rows 1234, 1264, 1278, 1284, 1299 only as a pointer). Row 1299 5.4 (2) names it as the
  precise next row on the carry and says its route can now start from the outline's regular-gas chapter.

Moves: T0 chain node F56 (`library/chain-ca.md` L208) and the carry's hypothesis (e) of Theorem 9.1. Success: the
account's last outstanding input of Theorem 9.1 becomes an implication from its PROVED geometry lemmas (9.1:lem-island-
geometry, 9.1:lem-blind-counts) and the site expansion statements as the account states them. Failure: the exact clause
of the site expansion whose proof reads the full tree length in a way the island-blind length cannot replace.

**Plan, one step per response, each appended before the next.**
- Step 2: read the island-blind format (CA-III L15889-16060), the two geometry lemmas (L15478, L15938), the
  proposition's route to its end (L16634-16800), and how its consumers read it (L16801-17060).
- Step 3: read the site (T) expansion statement as the account states it (cluster expansion lemma, marked sub-sum
  corollary, tolerance lemma, T-step expansion lemma (i)-(vii)) and the outline's printed regular gas (SA L13893-14811),
  and list every place where a tree length enters.
- Step 4: prove the (T) part: each place in the list, with d replaced by d°, from the geometry lemmas.
- Step 5: the (L) and (P) parts the same way, or the exact clause that fails.
- Step 6: labels, what a checker should redo, RESULT.

## Step 2. The proposition, its format and its geometry, as the account states them (READ; written 17:13Z by date -u)

All line numbers are CA-III at 31a47c543775 (Sussman and Alpoge, with Claude and Codex as authors of their text).

**2.1 Statement (L16559-16632).** At each of three sites of the correlation theorem, (T) (the expansion at a
T-step), (L) (the expansion that bounds bracket and volume terms) and (P) (the preliminary integrations giving the chain
terms C^(i)), the site's expansion statement "holds also when some of its input terms are island-blind stored terms".
Outputs: (a) an output that reads no island-blind input is unchanged; (b) an output that reads one is filed under
fil(X) in D^I of its level and obeys the site's bound with every tree length d_j replaced by d°_j: at (T) the factor
e^(-kappa_out d_(k+1)(X)) becomes e^(-kappa_out d°_(k+1)(X)) (cluster expansion lemma, marked sub-sum corollary, clauses
(ii), (vi) of the T-step expansion lemma); at (L) ||v^br||°_a <= eps_br; at (P) ||C^(n)||^(A,°) <= C_0^#; constants and
rates are the site's, floors the site's plus the per-cell domination (9.1:eq-blind-domination-a); (c) the E-, D-, R''-
families, the Gaussian part of the second expectation and the second-group R'-terms are never island-blind. Last
clause: for an island-blind potential the activity hypothesis at (T) is its anchored relative activity, at most
K°(4) times its sup-norm by 9.1:lem-blind-counts (ii).

**2.2 The format (L15889-15936).** D^I_l = domains Y in D_l with Y cap W_l a union of islands (W_l = closure of the
live strips with four layers, L15440-15445; islands = touch-components of W_l, pairwise non-touching, no size bound).
Relative length d°_l(Y) = d_(l,W_l)(Y), where (L15237-15252, also L3518-3524) d_W(Y) = least length of a tree graph
tau contained in Y that meets every cube of Y not contained in W; "The length of the tree is counted wherever the
tree runs, inside W included; only the requirement that the tree visit the cubes of W is removed." Filing
fil_l(X) = X together with the islands that X meets. Read at level m >= l through cl_m and
d°_m(Y) = d_(m,W_m)(fil_m(cl_m Y)). Norms: N°_l[F] = sup_Y e^(r_F d°_l(Y)) sup|F(Y)|, r_F = 9/8 kappa (R-born),
kappa_out (T-site), a_k or a_m (collar site); two-run seminorm S° with weight e^(kappa d°).

**2.3 Geometry, PROVED in the account (read, not re-checked here).** 9.1:lem-island-geometry (L15478): (a) moat:
dist_m(I, Omega_(m+1)) >= 3 R_m - 4 >= 23 for every island I of level m; no island meets Lambda_(m+1), the decoupling
region Y_0, or the support of the step-(m+1) fluctuation field; (d1) every decoupling cube, fluctuation cube and
random-walk origin at T_(m+1) lies in Omega_(m+1), hence at least 3 R_m - 4 cubes from W_m; (e) cl_m(Y cap W_l) is in
W_m. 9.1:lem-blind-counts (L15938): (i) sum over Y in D^I containing a cube Delta not in W of e^(-lambda_0 d°(Y)) <=
C_fib for lambda_0 >= k_d + 1; (ii) the same over blind Y whose closure at m contains a site cell at distance >= 1 from
W_m: <= K°(d) for lambda >= k_d + 2; (iii) an island's own cells; (iv) crossing: a blind store born at a T-step has
d° >= 3 R_l - 8; (v) levels: d°_m(Y) <= L^-(m-l) d°_l(Y), and a general tree form.

**2.4 The route (L16634-16781), five points the account says a proof must establish**, by repeating Balaban's
CMP 116 Section 2 expansion (and its analogues at (P), (L)) for one run with island-blind inputs:
(i) volume factors (CMP 116 (2.25)-(2.26), (2.31)-(2.34), (2.37)) count fluctuation volume only, which lies off W, and
the island-blind volume bound M^-d |Z minus W| <= c_d (d°(Z) + 1) replaces (2.30); 2 d_k >= L d_(k+1) holds for
relative lengths (lem-blind-counts (v));
(ii) domain sums ((2.29), the sums after (2.36), the weighted sums of the (L) lemma) anchored off W are bounded by
lem-blind-counts (i), (ii), replacing e^(c_d (n+1)) of CMP 116 (1.26); a polymer cube inside an island occurs only as a
walk cube that crossed the moat, counted from the walk's last off-island cube plus 3^d per walk step;
(iii) tree composition sum_D (d(Y) + 5) >= d(Y_0) + 5 (CMP 116 (2.27)) holds in relative form when Mayer and
decoupling links sit off W; a junction inside an island, reached by a walk, is re-routed to the nearest off-island
cube of the term's support, at most j_m = d (101 R_m + 8) + 1 cubes away, paid by the walk's moat factor
e^(-(kappa_1 - 1)(3 R_m - 4)) given L >= 18 (d + 1); a Mayer link between terms that overlap only inside an island is
declared a non-link (device of CMP 122b);
(iv) (P) and (L): the same points with the preparatory covariances; collar cells and (L)'s decoupling cubes lie off
the islands (lem-island-geometry (c1), (d));
(v) hull, fat core and collar: one layer each, inside the four spare layers; hull inequality in relative form.
The route also explains why outputs must be island-blind: an output that contains a young birth strip would need a
full-length tree through the strip, about (R_i/L)^d / c_d, against factors only linear in R in the exponent.

**2.5 Consumers.** 9.1:lem-blind-domination (L16801) assumes the (T) part; 9.1:thm-blind-fluctuation-bound (L16981)
reads the (T) part, clause (vi) of the T-step bound lemma for island-blind inputs (L17048-17060); Theorem 9.1
(L17912) lists the proposition as hypothesis (e).

**2.6 First observation (ARGUED, to be made precise in Step 4).** Read with the definition in 2.2, the relative length
charges a tree's run inside an island. So d° is not "d with W contracted"; it is d with the visiting requirement
dropped on W. Consequently the three combinatorial facts a cluster expansion reads (domain counts, volume bound, tree
composition) each need their own proof for d°, and the composition fact needs the links off W, as the route says.
Where a link or junction falls inside an island, the route's re-routing argument (iii) is the only device; I check it
in Step 4.

## Step 3. What the plain site (T) statement is, and a reduction that avoids rerunning CMP 116 (written 17:20Z by date -u)

**3.1 The plain site (T) statement is Balaban's, taken by statement (READ).** CA-II 5.2:prop-three-sites (L5336-5480):
"The expansion is that of [CMP109 (3.4), (3.7), (3.25)] and [CMP116 (1.9)-(1.22)] on the multiscale cover of
[CMP119 Section 3]". CA-II 5.2:lem-second-stage-activities (L6902-7040) names "the cluster-expansion lemma at site
(T), with its clauses (B1)-(B4)" and says at L7000-7001 that at site (T) the assertion is "that lemma's clauses
(B1)-(B4), taken by statement". The same lemma records three facts about how the second stage reads its potentials:
- F1 (L6977-6987): "In [CMP116 (2.1)] the potentials V(Y) enter only as Mayer factors of the polymers Y. ... After
  [CMP116 (2.20)] no potential occurs. ... The estimates [CMP116 (2.27)-(2.41)] depend on the potentials only through
  eps_2 = 2 eps'/alpha_4, and monotonically so."
- F2 (L6964, L6995-6997): "An output with domain X reads only the V(Y) with Y contained in X."
- F3 (L6919-6925): hypotheses on the potentials: analytic on Balaban's spaces and gauge invariant; of the form
  [CMP116 (1.42)] with [(1.43), (1.36)]; activity constant with 2 eps'/alpha_4 <= nu_0.
CA-II 5.2:lem-complex-fluctuation (L3521-3730) transcribes CMP 116 (2.1)-(2.20): Mayer expansion of
exp sum_Y V(Y,B), inclusion-exclusion of the cut, resummation into F(Z_0,B); conditioning; random-walk expansions,
decoupling in s(Delta), Cauchy representations; the term (2.14) with factor exp[sum over Y in D of tau(Y) V(Y,B)];
the radii 1/|tau(Y)| = E_0 eps_1 C_1 alpha_4^-1 M^q e^(C_2 kappa_1) e^(-(1-3 delta) kappa d_k(Y)) (L3712-3714). So the
format (1.42)/(1.36) is a bound per domain, |V(Y)| <= const e^(-kappa d_k(Y)), in the plain length.

**3.2 Idea (to be proved in Step 4): re-localisation.** For an island-blind input F(Y) choose an optimal relative
tree tau_Y of Y and put A(Y) := the union of the cubes of Y that meet tau_Y (the "active domain"). Then (Step 4):
A(Y) is a connected union of cubes inside Y, it contains every cube of Y off W, and d(A(Y)) <= |tau_Y| = d°(Y).
Since no integration variable of the T-step lies in W (lem-island-geometry (a), (d1)), F(Y) depends on the integrated
fields only through A(Y). Re-index: V'(A) := V(A) + sum of F(Y) over blind Y with A(Y) = A. This is an exact
regrouping of the exponent, sum_A V'(A) = sum_A V(A) + sum_Y F(Y), so the integrand is unchanged. The re-indexed
family is a family in the plain length: |V'(A)| <= |V(A)| + mult(A) N°[F] e^(-r d(A)), with mult(A) the number of
blind Y with A(Y) = A. Run the plain site statement on it, taken by statement as the account does. Its outputs
carry e^(-kappa_out d_(k+1)(X^a)) on plain output domains X^a. File each at X := X^a together with every island that
meets or touches X^a. Then X is in D^I, X minus W = X^a minus W, and a tree of X^a that meets all cubes of X^a meets
all cubes of X off W, so d°(X) <= d(X^a) and the plain bound gives the blind bound of clause (b).

Why this would matter: the account's route (Step 2.4) reruns CMP 116 Section 2 with relative lengths at five points,
which needs Balaban's text (not readable here) and is not session-sized. The re-localisation reads the plain site
statement only by its statement, as the account itself does for every plain input.

What must be checked (Step 4): (R1) the geometry of A(Y) and of the filing; (R2) mult(A) and the activity constant;
(R3) that the plain statement may be applied to inputs that depend on non-integrated fields outside their index
domain (island fields), i.e. which property of localisation the plain expansion reads; (R4) clause (a) and (c);
(R5) the levels (output read at k+1 with W_(k+1)); (R6) the corollary on the marked sub-sum and the tolerance lemma.

## Step 4. The (T) part by re-localisation (written 17:28Z by date -u)

Conventions are the account's (CA-I 4.21:not-cubes-cells-probes, L62735-62800; CA-III 9.1:not-cubes-strips,
L15209-15300; 9.1 format, L15889-15936). Level-m cubes are the closed M-cubes of pi_m, lengths in level-m units.
D_m = finite unions of level-m cubes that are wall-connected ("two consecutive cubes have a common wall"). d_m(X) =
least length of a tree graph contained in X that meets every cube of X. d_(m,W)(Y) = least length of a tree graph
contained in Y that meets every cube of Y not contained in W, and 0 if Y is in W. W = W_m is a union of level-m cubes;
islands are its touch-components and are pairwise non-touching. d°_m(Y) = d_(m,W_m)(Y) for Y in D^I_m. For a set S,
cl_m(S) is the union of the level-m cubes that meet S. k_d, c_d = 2 3^d, C_fib = 2 e^(2 k_d) as in
(9.1:eq-cubes-strips-2).

**Definition RL (active domain).** Let Y be a level-m union of cubes with Y not contained in W. Choose once and for all
a tree graph tau_Y contained in Y, meeting every cube of Y not contained in W, with |tau_Y| = d_(m,W)(Y) (a minimiser
exists: the relevant tree graphs are finite unions of segments in a compact set, and the account takes the minimum in
(9.1:eq-cubes-strips-1)). Put A(Y) := cl_m(tau_Y).

**Lemma A1 (active domain). PROVED.** For Y as above:
(i) tau_Y is contained in A(Y), and tau_Y meets every cube of A(Y);
(ii) A(Y) is in D_m, and d_m(A(Y)) <= d_(m,W)(Y);
(iii) every cube of Y not contained in W is a cube of A(Y);
(iv) every cube of A(Y) touches or equals a cube of Y.
Proof. (i) Each point of tau_Y lies in a closed cube, and that cube meets tau_Y, so it is in A(Y). The second claim
is the definition of cl_m. (ii) A(Y) is finite, since tau_Y is compact. Wall-connectedness: for a point p put S(p) :=
the set of cubes containing p. S(p) is the set of cubes prod_i [n_i, n_i + 1] with n_i in {floor(p_i) - 1, floor(p_i)}
if p_i is an integer and n_i = floor(p_i) otherwise; it is a box of 2^j cubes, j the number of integer coordinates, so
it is wall-connected. For p on tau_Y every cube of S(p) meets tau_Y, so S(p) is in A(Y). A cube not containing p has
positive distance from p, and there are finitely many cubes near p; hence p has a neighbourhood U_p such that S(q) is
contained in S(p) for every q in U_p. So the map p -> (the wall-component of A(Y) containing S(p)) is locally
constant on tau_Y. A tree graph is connected, so the map is constant. Every cube of A(Y) meets tau_Y in some p and so
lies in S(p). Hence A(Y) is one wall-component, and A(Y) is in D_m. By (i), tau_Y is a tree graph contained in A(Y)
meeting every cube of A(Y), so d_m(A(Y)) <= |tau_Y| = d_(m,W)(Y). (iii) tau_Y meets every such cube. (iv) A cube Q of
A(Y) contains a point p of tau_Y, which lies in Y, hence in some cube Q' of Y; Q and Q' share p. QED.

Remark. A(Y) need not be contained in Y; the cubes of A(Y) outside Y touch Y. Membership in D_m needs nothing else.

**Lemma A2 (filing of a re-localised output). PROVED.** Let X^a be in D_m and let P be a union of islands of W, each
meeting or touching X^a. Put X := X^a union P. Then fil_m(X) minus W = X^a minus W, and
d°_m(fil_m(X)) <= d_m(X^a).
Proof. fil_m adds islands, which lie in W, and P lies in W, so fil_m(X) minus W = X^a minus W. A tree graph tau of
length d_m(X^a) contained in X^a and meeting every cube of X^a is contained in fil_m(X) and meets every cube of
fil_m(X) not contained in W, since each such cube is a cube of X^a. QED.
Remark (applies equally to the account's own filing). Islands are touch-components, and two cubes of an island may
touch only at a corner, so X^a union P, and the account's fil_l(X) of L15905-15907, may fail to be wall-connected.
The account asserts fil_l(X) in D^I_l (L15907, and Lemma 9.1:lem-blind-counts (v)) without this check. Nothing below
uses wall-connectedness of a filed domain: the bound of Lemma A2 is a statement about d_(m,W), whose definition does
not need it. A repair, if a consumer needs D^I in the wall sense, is to define islands as wall-components; I did not
check the consumers for this.

**Lemma A3 (activity of the re-localised family). PROVED GIVEN 9.1:lem-blind-counts (i).** Let F = {F(Y)} be a blind
store of level m in format with N°_m[F] < infinity at rate r, and let kappa >= 0 with r >= kappa + k_d + 2. For A in
D_m put F'(A) := sum of F(Y) over the blind Y with Y not in W and A(Y) = A. Then
  (a) per domain: |F'(A)| <= c_d C_fib N°_m[F] e^(-kappa d_m(A));
  (b) anchored: for every cube Delta with dist_m(Delta, W) >= 1,
      sum over A containing Delta of e^(kappa d_m(A)) |F'(A)| <= 3^d C_fib N°_m[F].
Proof. (a) For each Y with A(Y) = A, Lemma A1 (ii) gives d°(Y) >= d(A), and Lemma A1 (iii) gives a cube of A not in W
contained in Y (Y minus W is non-empty because Y is blind and not in W). So
  |F'(A)| <= N° sum_(Y: A(Y)=A) e^(-r d°(Y)) <= N° e^(-kappa d(A)) e^(-d(A)) sum_(Y: A(Y)=A) e^(-(r-kappa-1) d°(Y))
          <= N° e^(-kappa d(A)) e^(-d(A)) sum_(Delta' in A, not in W) sum_(Y in D^I, Y contains Delta') e^(-(r-kappa-1) d°(Y))
          <= N° e^(-kappa d(A)) e^(-d(A)) N_m(A) C_fib,
by lem-blind-counts (i) with lambda_0 = r - kappa - 1 >= k_d + 1. By (g1) of 4.21:lem-tree-length-facts,
N_m(A) <= c_d (d(A) + 1), and (x + 1) e^(-x) <= 1 for x >= 0. (b) If A(Y) contains Delta then tau_Y meets Delta in a
point p, and p lies in a cube Delta' of Y. Delta' touches or equals Delta, so there are at most 3^d choices of Delta',
and Delta' is not contained in W, since otherwise p would lie in W and Delta would touch W. Then
  sum_(A contains Delta) e^(kappa d(A)) |F'(A)| <= N° sum_(Y: A(Y) contains Delta) e^(kappa d°(Y) - r d°(Y))
          <= N° sum_(Delta') sum_(Y contains Delta') e^(-(k_d+2) d°(Y)) <= 3^d C_fib N°. QED.
Both constants are at most the account's K°(d) = C_fib sup_(y>=1) y^d e^(-(y-3)) >= C_fib d^d e^(3-d) (= C_fib 256/e for
d = 4, which exceeds 3^4 = 81) for (b), and within a factor 2 of it for (a) (c_d = 162 at d = 4).

**The two readings the theorem uses (ARGUED; each is a statement about the plain site, not checked against Balaban's
text, which is not readable on this machine).**
- (H-fmt) Every condition that the plain site statement at (T) places on an input potential indexed by a plain domain
  A is either linear in the potential (a structural form, an analyticity domain given by conditions on the
  configuration cube by cube, gauge invariance, reality) or a bound on its modulus on that domain by a constant times
  e^(-kappa d(A)), where the constant enters the site's thresholds monotonically (the activity constant). Support:
  CA-II L6977-6987 (F1 of Step 3.1: the potentials enter only as Mayer factors and the estimates read them "only
  through eps_2 ... and monotonically so"); L3712-3714 (the radii fix |tau(Y)| by e^(-(1-3 delta) kappa d_k(Y)));
  L3721 ("These steps use only the form [CMP116 (1.42)] and the bounds [(1.43), (1.36)]").
- (H-par) The plain site statement at (T) holds verbatim when an input potential V(A) depends, besides the configuration
  on A, analytically and with the same bounds uniformly, on the configuration in a set P(A) that is a union of islands,
  provided the site integrates, decouples and shifts no variable in P(A) and the gauge invariance of V(A) is joint with
  the configuration on P(A); each output then depends in addition only on the configuration in the P(A) of the
  potentials it reads. Support: CA-II L3546-3548 (5.2:lem-complex-fluctuation: the outputs are analytic "in every
  parameter on which the V depend analytically with the bounds above"); CA-II L5285-5299 (5.2:def-sites-units (b):
  fourth-class units, which are the stored B, B' and chain terms, are invariant "jointly with its live exterior
  slots, ... and not ... as a function of its own configuration alone", after CMP119 (2.41)(iii)); CA-II L6995-6997
  (F2: an output reads only the potentials whose domains it contains); CA-III 9.1:lem-island-geometry (a), (d1)
  (L15489-15500, L15535-15540: no island meets Lambda_(m+1), the decoupling region Y_0 or the fluctuation support, and
  every decoupling cube, fluctuation cube and walk origin is at least 3 R_m - 4 cubes from W_m); the shift pieces are
  products with chi-hat_square, supported on blocks of the site (CA-II L5323-5326). The account's own route uses the
  same principle (CA-III L16752-16755: "a Mayer link between two terms that overlap only inside an island is declared a
  non-link, since the two terms share no integration variable there. This is the device of [CMP122b]").

**Theorem RL-T (the (T) part of 9.1:prop-blind-site-expansions). PROVED GIVEN (H-fmt), (H-par), the plain site
statements at (T) as the account takes them, and the floor (F_RL): kappa >= 8 (k_d + 2).** Consider the T-step from
level k to k+1. Let the inputs be the plain inputs of the site together with island-blind stores of levels l <= k, read
at level k (W = W_k), each blind store F of rate r_F in {9/8 kappa, kappa_out}. Then:
(T1) Re-index: for each blind store read at level k, take Y_k := fil_k(cl_k Y), tau := tau_(Y_k) and A := A(Y_k). Let
     V^m(A) be the sum of all blind stores with active domain A, and V^u the plain input family. Blind stores with
     Y_k in W contain no variable of the site and are carried unchanged (they are read by no output).
(T2) V = V^u + V^m is an input family of the plain site: V^m satisfies the plain per-domain bound at rate kappa with
     activity constant c_d C_fib N°[F] (Lemma A3 (a)), and its anchored activity at every cell of the site is at most
     3^d C_fib N°[F] <= K°(d) N°[F] (Lemma A3 (b)), which is the account's last clause of the proposition.
(T3) Outputs. Let t_lambda be the outputs of the plain site at the potential V^u + lambda V^m. The outputs that read no
     island-blind input are t_0, the outputs of the site without blind inputs: clause (a). The outputs that read an
     island-blind input are t_1 - t_0, the marked sub-sum of the corollary on the marked sub-sum with V^m as the marked
     potential; at plain output domain X^a they obey that corollary's bound, and t_1 obeys the cluster-expansion
     lemma's bound with the plain output factor e^(-rho d_(k+1)(X^a)), rho the site's rate (kappa_out at the T-site,
     9.1:lem-fresh-rate (ii), (vi)).
(T4) Filing. An output at X^a depends, besides the configuration on X^a, only on the configuration in the union P of
     the islands of the blind stores it reads (H-par). Each such island touches or meets A(Y_k), and A(Y_k) lies in X^a
     (F2), so cl_(k+1)(P) touches or meets X^a; by 9.1:lem-island-geometry (e), cl_(k+1)(P) lies in W_(k+1) (W^-_(k+1)
     at the T-step). File the output at X := fil_(k+1)(X^a union cl_(k+1)(P)). Lemma A2 at level k+1 gives
     d°_(k+1)(X) <= d_(k+1)(X^a), so e^(-rho d_(k+1)(X^a)) <= e^(-rho d°_(k+1)(X)): clause (b) at (T), with the
     site's constants and rates, in the cluster-expansion lemma, the marked sub-sum and clauses (ii), (vi) of
     9.1:lem-fresh-rate.
(T5) Clause (c). An output that reads a blind store has X^a containing A(Y_k), which contains a cube of Y_k off W
     touching an island (Y_k is connected, and islands do not touch each other); that cube is at least 3 R_k - 5 >= 22
     cubes from Omega_(k+1) by lem-island-geometry (a), so X^a is not contained in Lambda_(k+1). Hence no such output is
     a member of a family whose domains lie in Lambda_(k+1). (The other alternative of (c), domains "off
     (Z union Y_iota)^boxplus", is the account's definition of those families; I read it, not proved it.)
(T6) The tolerance lemma concerns the operators of the site, not its potentials, and is unchanged.
Proof. (T1)-(T2): Lemma A1 at level k applied to Y_k; Lemma A3 with kappa the plain input rate and r = r_F; the margin
r_F - kappa >= k_d + 2 holds for r_F = kappa_out >= 2 (c + 1) kappa (9.1:lem-fresh-rate (3)) once kappa >= k_d + 2,
and for r_F = 9/8 kappa by (F_RL). Reading at level k only improves the weight (9.1:lem-blind-counts (v):
d°_k(Y) <= d°_l(Y)). The integrand is unchanged, since sum_A V^m(A) = sum of the blind stores. The integration
variables of the site that lie in Y_k lie in cubes of Y_k off W (lem-island-geometry (a), (d1)), hence in A(Y_k)
(Lemma A1 (iii)); the rest of Y_k is island configuration, a parameter in the sense of (H-par). The conditions of
(H-fmt) that are linear pass to the sum V^m(A); the modulus bound is Lemma A3 (a). (T3): the marked sub-sum corollary
and the cluster-expansion lemma, taken by statement under (H-par). (T4): Lemma A2. (T5), (T6): as stated. QED.

Note on (F_RL). The account's own last clause of the proposition (anchored relative activity at most K°(d) times the
sup-norm) uses 9.1:lem-blind-counts (ii), which needs lambda >= k_d + 2 between the store's rate and the activity
weight, so the same margin is implicit there. The listed floors on kappa (CA-III L608-624) include (F_sigma)°:
sigma_* >= k_d + 4 with sigma_* in {beta kappa, kappa/(4 c#)}; if sigma_* = kappa/(4 c#) and c# >= 2, this implies
(F_RL). (F_RL) reads d only, so it can be imposed with the other floors on kappa.

**What this changes (ARGUED).** The account's route reruns CMP 116 Section 2 with relative lengths at five points.
Theorem RL-T does not rerun it: it applies the plain expansion by statement to a regrouped family, and moves the island
volume out of the length by choosing where each blind term is indexed. The route's points (i) volume factors, (ii)
domain sums, (iii) tree composition and the junction re-routing become unnecessary at (T): every polymer, walk and
junction of the plain expansion lives on plain domains and is paid in the plain length, which dominates the blind
length after filing (Lemma A2). The cost is the two readings (H-fmt), (H-par) and the floor (F_RL).
