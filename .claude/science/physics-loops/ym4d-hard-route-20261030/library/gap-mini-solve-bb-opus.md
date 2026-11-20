lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:30Z

# gap-mini-solve-bb-opus: the SU(2) mass gap, attack by the Mac mini worker 3

Queue row 1314 of `FINISH.md`, pinned at commit 44ea76b9f on branch `claude/ym4d-hard-route`. Started 2026-11-20T17:30Z.

Labels used: PROVED (a complete written argument, checkable by hand), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## Status log

- 17:30Z: file created (save protocol). Reading FINISH.md, the earlier RESULT lines, `parts/gap.md`, and `library/prior/gap-onebound-read-sol.md`.

## Step 0. Record read (statements about the record, not evidence; 17:40Z by date -u)

Read: GOAL.md (all), FINISH.md L1-85 and L299-352 (rules, joining, efficiency), the RESULT lines of rows 1290-1313,
`parts/gap.md` L1-104 (state of attack) and L223-268 (route registry), `library/prior/gap-onebound-read-sol.md` (all;
row 1218's reading of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A), the four-author
Hexagon text (B), and Zeng (C)), and the plan of the concurrent row 1309 (`gap-mini-solve-ay-opus.md` Step 1).

Where the lane stands, as the record says it (not re-proved here):
- Given the account's premises (Sussman and Alpoge, with Claude and Codex as authors of their text, after Balaban),
  the Jaffe-Witten gap on the account's tr F^2 sector follows from (N-phys) alone (row 1225 Theorem E-N, built on row
  916 Theorem E, check 917, and row 1179 Theorem BP, check 1183). (N-phys) is a neutral-sector thermal trace bound on
  one physical spatial cube, uniform in the cutoff (row 1218 reading, display (N)).
- (A-B*) of paper A implies (N-phys) (row 1218 reason 1; row 1295 Corollary AU2).
- The carry from one coupling to finer cutoffs has its own open inputs (rows 1256-1309); concurrent rows 1309, 1310,
  1313 work there. Row 1309 attacks the account's `9.1:prop-blind-site-expansions`.
- The seed itself is the infrared problem: every route on file stops at an order-one-coupling estimate (row 998 6b;
  rows 1225, 1229, 1291, 1300). Row 998 9.5 lists what not to repeat.

## Step 1. How best to attack it (judgement, ARGUED; 18:05Z by date -u)

**The seed.** The Jaffe-Witten gap needs, beside the account's existence chain, one infrared statement: (N-phys), or
(A-B*), at one physical size. Along the trajectory this is the lattice gap of Wilson SU(2) on a box a few tens of
correlation lengths wide, at a coupling where the running coupling is of order one. I see no reduction of it. Every
selective fact I can name (asymptotic freedom, the so(3) bracket, the Z_2 centre, pi_3, the O'Neill curvature of the
orbit space) either is perturbative or acts through the running coupling, and the 2D mechanisms (OpenAI's annulus
twist bound, Ding-Huang-Yang's third loop-soup copy, row 1007) use a continuous global symmetry on the integration
variables, which 4D gauge theory lacks: a colour rotation of pinned data is a bulk gauge transformation and costs
nothing (row 1013 Lemma TWIST; row 1016 Lemma CEN+). Grep of FINISH.md and `library/` (18:00Z) finds each angle I
considered on file: O'Neill/orbit space (20 files), Tomboulis-Yaffe (50), Mack-Petkova (63), electric flux (77),
Luscher/van Baal (80), Bakry-Emery (95), (BDD-Delta)/(Z-UNB) (rows 720, 1031-1056, 1135). Row 998 9.5 calls another
screen by this model family a waste. So I do not screen the seed again. Nothing in this file is progress on the seed.

**The item.** `9.10:thm-last-lattice-comparison` of Sussman and Alpoge's complete account (CA-III L63225; "Stated;
proof incomplete at the step marked (*)"; open registry L38, owner none; chain-ca D10). Why:
- It is on the gap carry: the carry reads `9.1:cor-sourced-integrals` at zero source (row 1233 R-i, Lemma 3.5;
  rows 1255-1296), whose hypotheses are those of `9.1:thm-last-lattice-comparison`, and row 1233 3c-3d names
  `9.10:thm-last-lattice-comparison` as the supply of its hypothesis (iv).
- Rule 0a: open-core.md has no entry; the open registry lists it with owner none; no FINISH row attacks it (the
  label occurs in FINISH only inside row 1233's material). Row 1309 (concurrent) attacks the other open input,
  hypothesis (e), `9.1:prop-blind-site-expansions`; this row does not touch that.
- Success: the account's last-lattice comparison becomes an implication from its PROVED statements (or the exact
  failing clause is named), so the carry's hypothesis (iv) loses its outstanding status. Failure: the exact clause of
  the marked step (*) that does not follow, with why.

**Plan (one step per response, appended before the next).**
- Step 2: fetch CA-III at 31a47c543775 into a scratch folder; read the statement, the marked step (*), its proof
  around it, and what the step needs.
- Step 3: prove the marked step from statements the account proves, or isolate the precise missing lemma.
- Step 4: consumers (9.1 hypothesis (iv)) and labels; RESULT.

## Step 2. Correction to Step 1: the 9.10 statement is not on the gap carry (READ; 18:20Z by date -u)

Source: CA-III = `theorem_0_complete_account_raw_III.tex` of Sussman and Alpoge's complete account at 31a47c543775
(Claude and Codex as authors of its text; after Balaban), fetched by URL into a scratch folder outside the repository
(111,583 lines). L-numbers are TeX lines of that file.

- `9.10:thm-last-lattice-comparison` (L63225-63351) is the "geometric" form: rate rho^(n-w) "with no floor". Its
  step (*) is that eleven listed statements also hold "read on the hatted array" (L63230-63255). Its proof applies
  `9.10:lem-objective-test-rest` and `9.10:lem-load-envelope` (itself incomplete at one step) on the hatted array.
- It is cited only inside 9.10: its two corollaries (L63353-63418) and `9.10:thm-exponential-rate` (L63536-63700),
  the exponential rate for the renormalised-coupling family (grep of CA-III for the label: L63354, 63378, 63384,
  63417, 63578, 63582, 63589, 63655, 63691; nothing outside L63225-63700).
- The gap carry reads `9.1:cor-sourced-integrals` (L18136-18215; row 1233 R-i, Lemma 3.5), whose hypotheses are those
  of `9.1:thm-last-lattice-comparison` (L17912-17990): (a) standing hypotheses, (b) the four chapter-9.1 lemmas,
  (c) g at most gamma_U and n at least n_1, (d) theta_chi at most rho, (e) the blind-site expansion. Its rate is
  e_w = rho^(n-w) + Pi_n (L17981-17984) with the power-law floor Pi_n, which the carry already sums (row 1233 3d
  item 3: Pi_n at most C n^(-(kappa_0-4)/2) (log n)^(c_3) with kappa_0 at least 10). No 9.10 statement enters.

So (READ): `9.10:thm-last-lattice-comparison` and its incomplete inputs (`9.10:lem-load-envelope`, clause (a) of
`9.10:thm-refiled-lipschitz`) are off the gap carry; they serve the account's geometric rate. Row 1233's phrase
"hypothesis (iv) ... supplied by 9.10" (its 3b-3c) should be read with this in mind; its 3d already uses 9.1. Step 1's
item is withdrawn. The carry's only chapter-9 outstanding input stays (e), which row 1309 works on.

## Step 3. New item: premise (P4) and (E0) of row 1299 (plan; 18:30Z by date -u)

After Step 2 the carry's open inputs are (row 1299 5.1, 4.7-4.8): the blind-site expansion (row 1309, concurrent),
(V9)/(DET)'s normalisation (row 1296), (M) (a supplier choice, row 1299 5.1), and the premises (P1)-(P5) of row 1299
4.8, among them **(P4): the constant conditions (UM14), (UM19), (UM23), (UM26') of Sussman and Alpoge's outline in one
order of choice, together with q > p_0**, on which row 1299's (E0) (4.7, ARGUED) rests. Rule 0a: neither (P4) nor
(E0) is attacked by any FINISH row (row 1299 lists them OPEN, not attacked); open-core.md has no entry.

Moves: the carry's cut half of (FC-1) (row 1268 Theorem FCT', row 1299 4.8). Success: (E0) becomes READ/PROVED and
(P4) becomes PROVED from stated constants, so the cut half rests on (P1)-(P3), (P5) only. Failure: the exact pair of
conditions that cannot hold together, which would break row 1299's Lemma TL-SA as used.

Sources to read: the outline `YM4_sketch_500.tex` at 31a47c543775, L14276-14811 (the regular-gas chapter) and
L13893-14272 (the Gaussian comparison theorem, FG1-FG12); CA-I L4150-4190 (cut radius and fluctuation domain).

## Step 4. The exponents p_0, p_1, q in the account, against row 1299's (E0) (READ; 18:50Z by date -u)

Sources: CA-I (`theorem_0_complete_account_raw_I.tex` at 31a47c543775, 166,711 lines), fetched by URL into a scratch
folder; Balaban, CMP 119 (1988), the owner's copy (outside git), pp. 268 and 276 read as page images in a scratch
folder. Credit: Sussman and Alpoge (Claude and Codex as authors of their text); Balaban.

**4.1 READ.**
- CA-I Stage 0 (L1349-1366): "p_0 in N, free upward, with p_0 >= 5r [CMP119] and the floor p_0 >= (d+5)r_0+8r+3";
  "p_1, a window, under three kinds of condition: 2p_1-(d+5)r_0 > p_0 [CMP122b]; **p_1 < p_0 [CMP122a]**; finitely
  many lower bounds on p_0-p_1 by numbers at most 4r+1"; "With p_1 := p_0-4r-1 ... p_0-p_1 = 4r+1"; "q := q_0 = q_1,
  free upward, with floors such as q >= p_0+7r+1 and q >= 3p_0+3r+1". The same window is repeated at L1866-1874 and
  L2017-2019.
- CA-I L29104-29117 (4.7): p_0(g') = A_0 (log g'^(-2))^(p_0); eps_m := g_m p_0(g_m); delta_m := (A_1/A_0) eps_m =
  A_1 (log g_m^(-2))^(p_0) g_m, "the threshold of [CMP119 (3.16)]"; "The complex box of [CMP119 (3.43)] is printed
  there as |A| < C_1 p_1(g_k), with A the fluctuation variable ... a smaller power of the logarithm in p_1(.) than in
  p_0(.) only improves the bound C_1^fl delta_m." CA-I L29124-29126: "q - p_0 >= 3r+2 > 0".
- CA-I 4.3 (L4166-4180): the two extra conditions of the small-field step are C_1 g' p_1(g') <= eps^I_1 and "the
  cutoff radius (A_1/A_0) p_0(g) ... exceeds the constant of [CMP116 (2.31)]"; "When g = g_k, this radius is the
  quantity delta_k/g_k of [CMP119]". No condition compares the cutoff radius with the box radius C_1 p_1(g).
- CMP 119 p. 268, (3.16): the decomposition of unity on Omega_(k+1) minus one layer uses chi({sup_b |A_k(b)| <
  delta_k}) and its complement, cubewise: a cut of the fluctuation field at delta_k.
- CMP 119 p. 276, (3.43): the terms of the expansion whose localization domains are not inside Lambda_(k+1) are analytic
  on U~^c_(k+1)(Y, (1+beta) alpha~_0, (1+beta) alpha~_1) x {A : supp A in Y cap Lambda^((k)*)_(k+1), |A| < C_1 p_1(g_k)}.

**4.2 Consequence for row 1299 4.7 (PROVED from 4.1, elementary).** In the account's choice, p_1 < p_0 < q. Row
1299 4.7 needs the cut threshold b (of order A_1 (log)^(p_0) in chart units) to lie inside the box where the step's
potentials are holomorphic, and writes "provided q > p_0 (equivalently p_1 > p_0; not checked)". The two conditions
are not equivalent in the account: q > p_0 holds (q >= 3p_0+3r+1), while p_1 > p_0 is false (p_1 = p_0-4r-1). Which
one (E0) needs depends on which box the carry's cut lives in:
- if the box is the lane's ci-form radius R = l^q (row 1299 4.7), (E0)'s containment b_hi < R holds above a floor,
  READ from the account's q >= 3p_0+3r+1;
- if the box is CMP 119's (3.43), |A| < C_1 p_1(g_k) (row 1268's own wording of (E0): "inside the fluctuation domain
  [B-CMP119 (3.43)]"), then for small g the cut radius A_1 (log g^(-2))^(p_0) exceeds C_1 (log g^(-2))^(p_1)
  (their ratio is (A_1/C_1)(log g^(-2))^(4r+1) -> infinity), and (E0) **as row 1268 words it FAILS** for the account's
  parameters.
So (E0) is not settled by row 1299 4.7: its "equivalently" is wrong, and the reading must say which box holds the
step's potentials on the whole cut region. Next (Step 5): read how Balaban and the account treat fluctuations with
C_1 p_1(g_k) <= |A| < delta_k/g_k inside the cut, and what box SA's (UM1) "declared complex fluctuation boxes" are
in the carry's presentation.

## Step 5. Which box holds the cut: the two p_1's (READ; 19:10Z by date -u)

**5.1 READ (Balaban; owner's copies, page images and text extractions in a scratch folder).**
- CMP 119 p. 250, (1.18): the first cut is chi({sup_b |A(b)| < g_0^(-1) delta_0}) on the scaled fluctuation A
  (U = exp(i g_0 A) U_1), so in chart units the cut is at g^(-1) delta = A_1 (log g^(-2))^(p_0). p. 247 (text): "We
  assume that the constant A_0 is much larger than A_1."
- CMP 119 p. 259, (2.28): the analyticity radii of the effective-action terms are alpha_(0,j) = g_j C_0 (log
  g_j^(-2))^(q_0), alpha_(1,j) = g_j C_1 (log g_j^(-2))^(q_1), "where q_0, q_1 are integers greater than 1, C_0, C_1
  are sufficiently large positive numbers".
- CMP 119 p. 265, (3.3) (text extraction): the decomposition "restricting the approximate fluctuation fields" uses
  delta_k = g_k (A_1/A_0) p_0(g_k): CMP 119's chi'_k cut is at the p_0 scale.
- CMP 119 p. 268, (3.16): the cut of the fluctuation field A_k at delta_k (p_0 scale), on Omega_(k+1) minus one layer.
- CMP 119 p. 276, (3.43): the remaining terms are analytic on U~^c_(k+1)(Y, (1+beta) alpha~_0, (1+beta) alpha~_1) x
  {A : supp A in Y cap Lambda^((k)*)_(k+1), |A| < C_1 p_1(g_k)}. No definition of p_1(.) was found in CMP 119's text
  extraction (searched for p1, its OCR variants, and the pages of (1.18), (2.28), (3.3), (3.16), (3.43)).
- CMP 122a p. 183, (1.27): "delta'_j = g_j A_1 p_1(g_j), p_1(g_j) = (log g_j^(-2))^(p_1) and p_1 < p_0; other
  conditions on p_1 will be formulated later", for its cut chi'_j of the approximate fluctuation field at 2 delta'_j.
  CMP 122b (text): "2p_1 - (d+5) r_0 > p_0" and a bond with |B(b)| >= g_j^(-1) ... A_1 p_1(g_j).
- The account (CA-I L9788): "A second function of the coupling, the function p_1(.) of [B-CMP119], distinct from the
  degree function p_0(.)"; Stage 0 (L1353-1363) gives one exponent p_1 with p_1 < p_0 citing CMP 122a; 4.4 (L9965-9972)
  takes the fluctuation polydisc D = {|A|, |A_k| < C_1^fl p_1(g_k)}; 4.29 (L149146-149149) bounds the "second region"
  by C_II C_1^(3.43) delta_k, i.e. uses g_k p_1(g_k) <= delta_k (A_1 = 1 normalisation aside), which needs p_1 <= p_0.

**5.2 What follows (PROVED from 5.1, elementary; the reading of CMP 119's p_1 is OPEN).** In chart units the regular
step integrates the fluctuation over the cut region {|A| < A_1 (log g^(-2))^(p_0)} (CMP 119 (1.18), (3.3), (3.16)).
Its potentials are claimed analytic on {|A| < C_1 p_1(g_k)} ((3.43)). Exactly one of two readings holds.
- (R+) CMP 119's p_1(.) is a function with exponent above p_0 (for instance one tied to q_1 of (2.28)). Then the cut
  region lies inside the box above a floor in log g^(-2), and row 1268's (E0) ("inside the fluctuation domain
  [CMP119 (3.43)]") holds for every threshold of the form c delta_k with c bounded, above a floor.
- (R-) CMP 119's p_1 is the account's p_1 = p_0 - 4r - 1 (CMP 122a's). Then for small g the cut region is NOT inside
  the box: at |A| = (C_1 (log g^(-2))^(p_1), A_1 (log g^(-2))^(p_0)) the step's remaining terms are not known to be
  analytic, the ratio of radii being (A_1/C_1)(log g^(-2))^(4r+1). Row 1268's (E0) fails as worded, and so does the
  account's own second part of 4.3:thm-small-field-step, which takes both "the fluctuation domain of [CMP119 (3.43)]"
  and "the cutoff radius (A_1/A_0) p_0(g)" together (L4176-4178), unless a further cut at the p_1 scale is in force.
Under (R-) a further cut is in fact in force in Balaban's large-field papers: CMP 122a's chi'_j cuts the approximate
fluctuation at 2 delta'_j = 2 g_j A_1 p_1(g_j), inside a C_1 p_1 box when C_1 > 2 A_1; and the account's (I4)
(CA-I L148994-148997) records "|A_k| <= p_1(g_k) on supp chi'_k". So under (R-) the active cut of the regular gas is
the p_1-scale cut, and the carry's two-frame thresholds must be read at delta'_k, not at delta_k as row 1268 2.1 reads
them.

Either way row 1299 4.7's sentence "provided q > p_0 (equivalently p_1 > p_0)" is wrong as an equivalence: in the
account q > p_0 holds and p_1 > p_0 fails. Which reading is right needs CMP 116 (paper II, where Balaban's p_1(.) for
the fluctuation box is presumably introduced), which is not on this machine (row 1264: Project Euclid bot check).
