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
