lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:30Z

# gap-mini-solve-bb-opus: the SU(2) mass gap, attack by the Mac mini worker 3

Queue row 1314 of `FINISH.md`, pinned at commit 44ea76b9f on branch `claude/ym4d-hard-route`. Started 2026-11-20T17:30Z.

Labels used: PROVED (a complete written argument, checkable by hand), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## Status log

- 17:30Z: file created (save protocol). Reading FINISH.md, the earlier RESULT lines, `parts/gap.md`, and `library/prior/gap-onebound-read-sol.md`.
- 18:12Z: done (Steps 0-9); RESULT at the end of the file.

## Step 0. Record read (statements about the record, not evidence; written 17:30Z-18:10Z)

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

## Step 1. How best to attack it (judgement, ARGUED; written 17:30Z-18:10Z)

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

## Step 2. Correction to Step 1: the 9.10 statement is not on the gap carry (READ; written 17:30Z-18:10Z)

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

## Step 3. New item: premise (P4) and (E0) of row 1299 (plan; written 17:30Z-18:10Z)

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

## Step 4. The exponents p_0, p_1, q in the account, against row 1299's (E0) (READ; written 17:30Z-18:10Z)

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

## Step 5. Which box holds the cut: the two p_1's (READ; written 17:30Z-18:10Z)

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

## Step 6. What the two p_1's do to the carry's cut half (written 17:30Z-18:10Z)

Context (READ, row 1299 4.4): Lemma A and Lemma TL-SA apply to "admissible cuts", whose clause (C2) asks that every
potential of the step that reads a bond b obey (UM1) and be holomorphic on a declared complex box containing the real
box |B(b)| < b_hi. For row 1268's frame comparison (its 7.5) the two cuts are f^psi_b = 1{N_b < T^psi} and
f^phi_b = 1{N_b o Psi_c < T^phi}, with thresholds T a fixed multiple of the frame's delta (row 1268 2.1), so in chart
units b_hi = A_1 (log theta)^(p_0) (1 + O(theta^(-1/2) polylog)), theta = g^(-2).

**6.1 Lemma NC1 (non-containment under the account's p_1; PROVED, elementary).** Let C_1 > 0 and A_1 > 0 be fixed
before gamma, as in the account's order of choice (H3) (CA-I L1143-1165: A_1, A_0, C_0, C_1, ... are chosen before
gamma), and let p_1 = p_0 - 4r - 1 (CA-I L1359-1363). Then for every g in (0, gamma] with
    log g^(-2) > (C_1/A_1)^(1/(4r+1))                                                              (6.1)
the real box {|B| < A_1 (log g^(-2))^(p_0)} is not contained in {|B| < C_1 (log g^(-2))^(p_1)}.
*Proof.* The ratio of the radii is (A_1/C_1)(log g^(-2))^(p_0-p_1) = (A_1/C_1)(log g^(-2))^(4r+1), which exceeds 1
exactly when (6.1) holds. QED. Along the pin runs theta_k >= X + c_0 k (row 1268 Lemma S), so (6.1) holds at every
level once log X > (C_1/A_1)^(1/(4r+1)).

*Consequence (PROVED from NC1 and READ).* If some potential of the carry's step that reads a free bond carries only the
box {|A| < C_1 p_1(g_k)} of CMP 119 (3.43) (equivalently the account's polydisc D of 4.4, CA-I L9965-9972), then (C2)
fails for row 1268's delta-scale frame cuts at every level above the floor of NC1, and Lemma A and Lemma TL-SA (row
1299 4.4) do not apply to those cuts as stated. If instead every potential of the step reads the free bonds only
through configurations in Balaban's spaces U^c(Y, alpha_0, alpha_1) of CMP 119 (2.28) (radii g C_i (log
g^(-2))^(q_i), q_i = q >= 3p_0+3r+1 in the account), then in chart units their boxes have radius of order
(log g^(-2))^q and (C2) holds above a floor, which is row 1299 4.7's argument with its "equivalently p_1 > p_0"
deleted.

**6.2 Which case the carry is in (READ, partly OPEN).**
- CMP 119 p. 276 attaches the (3.43) box only to "the remaining terms", those of the expansion (I.6.41) whose
  localization domains are not contained in Lambda_(k+1); terms with Y in Lambda_(k+1) "satisfy exactly all the
  conditions of those lemmas" with the analyticity space (I.6.34) (the account's 4.17, CA-I L53400-53430 and
  L53526-53545, reads (I.6.34), (I.6.41) as CMP 116 (1.34), (1.41) in the continuous numbering of CMP 109 and 116).
- The carry runs the all-small-field step on the pin route (row 1293, READ of CMP 119 (3.15)-(3.16)). If in that
  step Lambda_(k+1) is the whole torus, no remaining term occurs, and the (3.43) box is not read.
- OPEN: whether CMP 116 (1.34), the analyticity space of the terms inside Lambda_(k+1), carries a fluctuation factor
  {|A| < C_1 p_1(g)} as (3.43) does, or only configuration radii. CMP 116 is not on this machine (row 1264: Project
  Euclid bot check, not bypassed). The account's polydisc D (4.4) carries the p_1 factor for both A and A_k.
- In the large-field papers the p_1 scale is a cut, not only a box: CMP 122a (1.27) cuts the approximate fluctuation
  at 2 delta'_j = 2 g_j A_1 p_1(g_j), and the account's 4.23 (CA-I L93565-93568) lets its real variables range over
  |B| < b'_k = A_1 p_1(g_k). CMP 119's own fluctuation cuts are at the p_0 scale: (3.3) at 2 delta_k (page image
  p. 265) and (3.16) at delta_k.

**6.3 Repair if the p_1 box is read (ARGUED, with one PROVED lemma).** If the step's potentials carry the p_1 box
with margin, i.e. are holomorphic and obey (UM1) on {|B(b)| < 2 A_1 p_1(g_k)} (a reading of (I.6.34)/(3.43) with
C_1 >= 2 A_1(1 + o(1)), OPEN), then insert in both frames the internal cut 1{N_b < A_1 p_1(g_k^frame)} by the
decomposition of unity prod_b [f_b + (1 - f_b)], and keep the delta-scale cut of CMP 119 (3.3), (3.16) as an extra
indicator. The internal cuts are admissible ((C1)-(C2) with b_lo, b_hi = A_1 (log theta)^(p_1) (1 + O(theta^(-1/2)
polylog))), so Lemma TL-SA applies to them with eta = exp(-gamma b_lo^2/2). The extra indicators differ between the
frames only where some bond has |B(b)| >= A_1 (log theta)^(p_0)(1 - o(1)), a failed bond of the internal cut; SA's
failed-test bound (FG12) ("Multiplication by additional indicators only improves the bound") then bounds that part by
the same scheme with exp(-gamma A_1^2 (log theta)^(2 p_0)/4), smaller still. What stays to be checked in this repair:
that a potential reading a failed bond is never selected (SA's convention L14321-14323, "If a potential is defined
only on a box, the corresponding sharp cutoff is kept wherever that potential occurs"), so that no potential is
evaluated between the two radii.

**Lemma S1 (summability at the p_1 scale; PROVED, elementary).** Let gamma, A_1 > 0, p_1 >= 1, c_0 > 0, and let
theta_k >= X + c_0 k for k >= 0 with X >= e. Put eta_k := exp(-(gamma/2) b_k^2) with b_k >= (A_1/2)(log
theta_k)^(p_1). If log X >= l_0 := (16/(gamma A_1^2))^(1/(2 p_1 - 1)), then
    sum_(k >= 0) eta_k <= X^(-2) + 1/(c_0 X),
which tends to 0 as X -> infinity.
*Proof.* (gamma/2) b_k^2 >= (gamma A_1^2/8)(log theta_k)^(2 p_1) = (gamma A_1^2/8)(log theta_k)^(2 p_1 - 1) log
theta_k >= 2 log theta_k, since log theta_k >= log X >= l_0 gives (log theta_k)^(2 p_1 - 1) >= 16/(gamma A_1^2).
So eta_k <= theta_k^(-2) <= (X + c_0 k)^(-2), and sum_(k>=0) (X + c_0 k)^(-2) <= X^(-2) + int_0^infinity
(X + c_0 t)^(-2) dt = X^(-2) + 1/(c_0 X). QED.
In the account p_1 > (p_0 + (d+5) r_0)/2 >= 5r/2 + 9r/2 > 1 (CA-I L1353-1363 with d = 4, r_0 >= r >= 2), so Lemma
S1 applies, and row 1268's sum of nu_k stays bounded and tends to 0 with the cut part read at the p_1 scale: the
summability of the cut half survives the repair.

**6.4 Status after this step.**
| Statement | Label |
|---|---|
| In the account p_1 = p_0-4r-1 < p_0 < q (q >= 3p_0+3r+1) | READ (CA-I L1353-1366, L29124-29126) |
| Row 1299 4.7's "q > p_0 (equivalently p_1 > p_0)" is false as an equivalence | PROVED (from READ) |
| CMP 119's fluctuation cuts (3.3), (3.16) are at the p_0 scale; its (3.43) box is at the p_1 scale | READ (page images pp. 265, 268, 276) |
| Lemma NC1: under the account's p_1 the delta-scale cut box is not inside the p_1 box above the floor (6.1) | PROVED |
| (E0) / (C2) for the delta-scale frame cuts: holds if the carry's potentials carry only configuration radii (2.28); fails if any carries only the p_1 box | PROVED as a dichotomy; which case: OPEN (needs CMP 116 (1.34)) |
| Repair at the p_1 scale (internal cut plus extra indicators) | ARGUED; its summability part, Lemma S1, PROVED |
| The account's own 4.3 second part takes the (3.43) box with the p_0-scale cutoff radius together (CA-I L4176-4178) | READ; whether this is consistent is the same OPEN question (a statement about their text, not a claimed error) |

## Step 7. Resolution: the carry's box is CMP 116 (1.34), so (E0) holds; the p_1 box is for straddling domains (written 17:30Z-18:10Z)

**7.1 READ (CA-I, 4.4, the remark after the post-step space).**
- Item (b), "Interior domains Y in Lambda_(k+1)" (L10031-10038): "Here the space of [B-CMP116 (1.34)] is
  U^c_(k+1)(Y, (1+beta) alpha_0, (1+beta) alpha_1, alpha_0) x {B : |B| < eps_1 g_k^(-1) on Y}, where B and eps_1 are
  the field variable and the constant so denoted in [B-CMP116 (1.34)]."
- Item (c), "Straddling domains, those Y that are not interior in the sense of item (b), treated in [B-CMP119]"
  (L10044-10050): this is where CMP 119's (3.43) applies (the "remaining terms", CMP 119 p. 276).
- B is in chart units: its physical size is g_k |B| < eps_1, a fixed small-field radius (a box |B| < eps_1/g_k in
  physical units would leave the small-field region, so the chart reading is the only consistent one; the same scaling
  as CMP 119 (1.18), where the cut on the scaled A is g_0^(-1) delta_0).

**7.2 Lemma C1 (containment; PROVED, elementary).** Let theta = g^(-2), A_1, eps_1 > 0, p_0 >= 1. If
    theta^(1/2) (log theta)^(-p_0) > 2 A_1 / eps_1,                                                    (7.1)
then the real box {|B| < 2 A_1 (log theta)^(p_0)} lies inside the polydisc {|B| < eps_1 g^(-1)} = {|B| < eps_1
theta^(1/2)}. *Proof.* 2 A_1 (log theta)^(p_0) < eps_1 theta^(1/2) is (7.1) rearranged. QED. Since theta^(1/2) (log
theta)^(-p_0) -> infinity, (7.1) holds for theta >= theta_1(A_1, eps_1, p_0); along the pin runs theta_k >= X, so it
holds at every level once X >= theta_1. In the account's order of choice A_1, p_0 and eps^I_1 are fixed before gamma
(CA-I L1143-1165), so the floor is a constraint on gamma (equivalently on X), which (H3) allows: no condition bounds a
coupling from below.

**7.3 Corollary E0 (PROVED GIVEN the READ items 7.1 and row 1268/1299's frame data).** On the pin route the carry runs
the all-small-field step (row 1293's reading of CMP 119 (3.15)-(3.16)), so every localization domain is interior and
no straddling domain, hence no (3.43) box, occurs. The step's potentials then carry:
- older terms: Balaban's configuration spaces of CMP 119 (2.28), radii g C_i (log g^(-2))^(q) in the configuration,
  with q >= 3p_0 + 3r + 1 > p_0 (CA-I L1365-1366), so in chart units their fluctuation radius exceeds A_1 (log
  theta)^(p_0) by a factor of order (log theta)^(q - p_0) above a floor;
- the step's own terms (the expansion (1.41) of CMP 116): the space (1.34) with the box {|B| < eps_1 g_k^(-1)}.
The two frame thresholds of row 1268 7.5 satisfy b_hi = A_1 (log theta)^(p_0) (1 + O(theta^(-1/2) polylog)) <= 2 A_1
(log theta)^(p_0) above a floor, so by Lemma C1 both lie inside every declared box above the floor max(theta_1, the
floor of the configuration radii). Hence (C2) of row 1299 4.4 holds for the frame cuts, (C1) holds with b_lo = A_1
(log theta)^(p_0)(1 - O(theta^(-1/2) polylog)), and (E0) holds: both thresholds lie "in the range where the
construction holds", above the CMP 116 (2.31) floor (the account's 4.3 condition, already assumed by row 1268) and
inside the declared boxes. What this uses beyond READ: that SA's (UM1) potential types in the carry's presentation are
exactly the older terms, the step's (1.41) terms and the inserted vertex of row 1299 Lemma V-SA, and that the inserted
vertex is holomorphic on the (1.34) box (ARGUED: it is a polynomial vertex in the fluctuation, row 1268 Lemma RS).

**7.4 What changes in the record.**
- Row 1299 4.7: its conclusion "(E0) above a floor" stands; its reason does not. The box is not the ci-form's R = l^q
  for the step's own terms, and "equivalently p_1 > p_0" is false in the account (Step 4). The right box for the
  step's own terms is CMP 116 (1.34) as transcribed at CA-I L10031-10038, and the right condition is Lemma C1's (7.1),
  which needs no relation between p_1 and p_0.
- Row 1268's wording of (E0), "inside the fluctuation domain [B-CMP119 (3.43)]", should read "inside the domain of
  [B-CMP116 (1.34)] (interior domains)". Read literally with the (3.43) box and the account's p_1 < p_0, (E0) would
  fail (Lemma NC1); that box belongs to straddling domains, which the carry does not meet.
- Caution for later rows: the account's fluctuation polydisc D of 4.4 (CA-I L9965-9972, radius C_1^fl p_1(g_k) for A
  and A_k) is a p_1-scale box. A carry step that took D as the box of its cut comparison would fail (C2) by Lemma NC1.
  Lemma S1 (Step 6) is the summability needed if a p_1-scale internal cut is ever required.
- (P4) of row 1299 4.8: its clause "q > p_0" is READ (q >= 3p_0+3r+1); the remaining clauses ((UM14), (UM19),
  (UM23), (UM26') in one order) are SA's constant conditions; (UM23) at b_lo holds above a floor because b_lo grows
  like (log theta)^(p_0) while n_b, Theta and SA's Gaussian rate are fixed first. Not checked here: (UM14), (UM19),
  (UM26') themselves.

## Step 8. (P4): one order of choice for SA's constant conditions (ARGUED, with READ inputs; written by 18:10Z)

Sources: SA = `YM4_sketch_500.tex` at 31a47c543775 (Sussman and Alpoge, Claude and Codex as authors of their text,
after Balaban), L14404-14720; CA-I Stages 3-6 (L1468-1550, L2070-2085).

**8.1 The conditions (READ).** Geometric constants fixed independently of L: C_h (UM7)-(UM8), kappa_f and S_xi (UM9),
c_f (UM10), c_b in n_b <= c_b (LM)^4 (UM11), c_l (UM17), C_v, C_D, kappa_D, c_adj (UM25)-(UM26); C_p "includes the
finite tags and their rooted sums, but no number of selected domains or global volume" (L14512-14514). Gaussian
package: K, rho_0(K), A_K, c_m, the matrix closeness eps (FG1), the coarse disc radius R_s (UM4)-(UM6). Choices:
- W_0 small, lambda_0 > kappa_f (L14482-14486); (UM14) C_p W_0 M^(-4) + gamma/2 <= rho_0(K);
- (UM15) C_0 = C_p W_0 L^4 + A_K c_m (LM)^4 (eps + C_p W_0 M^(-4) + gamma/2);
- (UM18) K_* = 2 + c_l Lambda, Theta = C_h (C_0 + K_*);
- (UM19) sigma_0 > kappa_f, lambda_V - lambda_0 >= Theta/L + sigma_0, log(R_s - 1) >= Theta;
- (UM23) a <= W_0/2, tau = e^Theta [2 c_f L^4 S_(sigma_0) a / W_0 + n_b e^(-gamma b^2/2)] <= 1;
- (UM26') g_* = Lambda - mu > kappa_D + C_v, e c_adj B_* <= 1, B_* = C_D e^(2 C_v) e^(-5 g_*) sum_m
  e^(-(g_* - kappa_D - C_v) m).
Here lambda_V is the decay rate of the actual potentials in fine-cube units (UM1), mu the output rate the consumer
reads, a the potentials' total norm, b the cut threshold (here b_lo of the frame cuts).

**8.2 An order (ARGUED; each step is an elementary inequality once the three readings (Q1)-(Q3) below hold).**
1. Geometric constants; then L >= max(L_0, 2 C_h c_l).
2. g_* := kappa_D + C_v + 1 + (1/5) log(e c_adj C_D e^(2 C_v) / (1 - e^(-1))). Then B_* <= C_D e^(2C_v) e^(-5 g_*)
   / (1 - e^(-1)) and e c_adj B_* <= 1: (UM26') holds, with geometric constants only.
3. lambda_0 := sigma_0 := kappa_f + 1.
4. Balaban's kappa (account Stage 3), with the extra floor kappa >= 2(lambda_0 + sigma_0) + 2 C_h (3 + c_l g_*)/L.
   With mu := kappa and Lambda := mu + g_*, and C_0 <= 1 (step 6), (UM19)(i) reads kappa >= lambda_0 + sigma_0 +
   C_h (3 + c_l (kappa + g_*))/L, which holds because C_h c_l / L <= 1/2. This uses (Q1): lambda_V >= kappa.
5. M (account Stage 6, free upward), with the extra floor log(R_s(M) - 1) >= C_h (3 + c_l (kappa + g_*)). This is a
   floor on M if (Q2): R_s(M) -> infinity as M -> infinity with the other letters fixed; it is of the same form as the
   account's own Stage-6 floors delta_0 M >= kappa, M >= M(kappa) (L2075-2084).
6. W_0 := min{1/(3 C_p L^4), rho_0(K) M^4/(2 C_p)}, SA's gamma := min{rho_0(K), 2/(3 A_K c_m (LM)^4)}. Then (UM14)
   holds, and C_0 <= 1/3 + 1/3 + A_K c_m (LM)^4 eps <= 1 once eps <= 1/(3 A_K c_m (LM)^4). Theta <= C_h (3 + c_l
   (kappa + g_*)) is now fixed.
7. Coupling floor (gamma of the account, equivalently X of the pin runs), using (Q3): eps -> 0 and a -> 0 as theta ->
   infinity, uniformly in the step: eps <= 1/(3 A_K c_m (LM)^4); a <= W_0 e^(-Theta) / (4 c_f L^4 S_(sigma_0)); and
   b_lo^2 >= (2/gamma)(Theta + log(4 n_b)), which holds above a floor since b_lo = A_1 (log theta)^(p_0)(1 - o(1));
   then tau <= 1/4 + 1/4 <= 1 and a <= W_0/2: (UM23) holds. Add Lemma C1's floor (7.1) for (E0).
No condition in 1-7 bounds a letter from above except the ceilings on W_0 and SA's gamma, which are SA's own free
choices made after L, M, kappa, and the coupling ceiling, which (H3) allows.

**8.3 The readings this rests on (OPEN; not checked here).**
- (Q1) In the carry's presentation the step's potentials decay at least like e^(-kappa d_f(Y)) with d_f in fine-cube
  units (Balaban's decay rate kappa per M-cube), so lambda_V >= kappa.
- (Q2) SA's matrix package (UM4)-(UM6) holds on coarse discs of a radius R_s that can be made as large as needed by
  raising M (for Balaban's decoupled covariances one expects log R_s of order (decay rate) x M; not read).
- (Q3) The step's matrix closeness eps (FG1) and the potentials' total norm a tend to 0 as the coupling does, at a
  rate uniform in the step (part of premises (P1)-(P2) of row 1299 4.8).
If (Q2) failed, so that R_s were bounded independently of M, then (UM19)(ii) would bound kappa from above, against the
account's statement (H3) that no condition bounds kappa from above (CA-I L1159-1161); that is the one place where SA's
chapter could conflict with the account's order of choice.

**Time note (18:12Z by date -u).** The per-step clock times first written in Steps 0-8 were estimates and were wrong
(they ran ahead of the clock). They are replaced above by the true window: Steps 0-8 were written between 17:30Z and
18:10Z by date -u.

## Step 9. Labels, what a checker should redo, credits, note for the lead (written 18:12Z by date -u)

**9.1 Mass gap.** NOT proved; nothing disproved. The infrared seed ((N-phys), equivalently a uniform cube gap with
the count at one coupling in the band, or the One-Bound paper's (B*)) was not attacked (Step 1: every angle I could
name is on file at its failing step; row 998 9.5).

**9.2 Labels.**
| Statement | Label | Where |
|---|---|---|
| `9.10:thm-last-lattice-comparison` and its incomplete inputs serve only `9.10:thm-exponential-rate`; the gap carry reads `9.1:cor-sourced-integrals`, whose floor Pi_n it already sums; Step 1's item withdrawn | READ (CA-III grep; agrees with `library/chain-ca.md` D10; CA-II not fetched, CA-I and the outline do not cite it) | Step 2 |
| The account takes p_1 = p_0-4r-1 < p_0 < q, q >= 3p_0+3r+1 | READ | Step 4 |
| Row 1299 4.7's "q > p_0 (equivalently p_1 > p_0)" is false as an equivalence | PROVED | Step 4 |
| CMP 119's fluctuation cuts (3.3), (3.16) are at the p_0 scale; its (3.43) box (p_1 scale) is for "remaining" (straddling) terms only | READ (page images pp. 250, 259, 265, 268, 276) | Steps 5, 7 |
| CMP 116 (1.34) for interior domains has the box {|B| < eps_1 g_k^(-1)} (the account's transcription) | READ (CA-I L10031-10038; CMP 116 itself not on this machine) | Step 7 |
| Lemma NC1 (the delta-scale cut box is not inside the p_1 box above the floor (6.1)) | PROVED | Step 6 |
| Lemma S1 (summability at the p_1 scale along pin runs) | PROVED | Step 6 |
| Lemma C1 (the delta-scale cut box lies inside {|B| < eps_1 g^(-1)} above the floor (7.1)) | PROVED | Step 7 |
| Corollary E0: (E0) and (C2) hold for row 1268's frame cuts on the pin route (all-small-field step, interior domains only) | PROVED GIVEN the READ items of 7.1 and the ARGUED identification of SA's potential types with the older terms, the (1.41) terms and the inserted vertex | Step 7 |
| Row 1268's wording of (E0) ("inside [B-CMP119 (3.43)]") must read "inside [B-CMP116 (1.34)]"; read literally with the account's p_1 it fails | PROVED (from NC1 and READ) | Step 7.4 |
| Repair at the p_1 scale if a p_1 box ever binds | ARGUED | Step 6.3 |
| (P4): one order of choice for (UM14), (UM19), (UM23), (UM26') | ARGUED, given readings (Q1)-(Q3) | Step 8 |
| (Q1) lambda_V >= kappa; (Q2) R_s can be raised with M; (Q3) eps, a -> 0 with the coupling | OPEN (readings) | Step 8.3 |

Every PROVED item is by Claude Opus 5.5 (this row) and is not checked by another model. The lemmas are elementary;
the weight sits on the READ items.

**9.3 What a checker should redo.** (1) Read CMP 119 pp. 250, 265, 268, 276 and confirm the scales of (1.18), (3.3),
(3.16), (3.43). (2) Read CA-I L10031-10050 and confirm that the carry's all-small-field step has interior domains only.
(3) If CMP 116 can be read, confirm (1.34) and the meaning of B and eps_1 there (chart units), which decides Corollary
E0 directly. (4) Redo Lemmas NC1, S1, C1. (5) Check the order of 8.2 against SA L14404-14720 and decide (Q1)-(Q3).

**9.4 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the complete account
CA-I, CA-III at 31a47c543775 (Stage 0-6, 4.3, 4.4, 4.17, 4.23, 4.29, chapter 9) and the outline `YM4_sketch_500.tex`
(the regular-gas chapter, (UM1)-(UM27)). Tadeusz Balaban: CMP 109, CMP 116 (through the account's transcription),
CMP 119, CMP 122a/b. Rows 1233, 1268, 1293, 1294, 1299 (Claude Opus 5.5) for the carry this note corrects and feeds;
`library/chain-ca.md` (Codex) for D10.

**9.5 Note for the lead (evidence only, no edit made).** (1) Row 1268's (E0) and row 1299's 4.7 should be re-read with
Step 7: the conclusion stands, the stated reason does not. (2) The open registry lists the 9.10/9.11 statements with
owner none; by Step 2 they are off the gap carry (they serve the account's geometric rate). (3) If a future carry row
uses the account's fluctuation polydisc D of 4.4 (radius C_1^fl p_1(g_k)) as the box of a cut comparison, Lemma NC1
says it fails above a floor; use CMP 116 (1.34)'s box for interior domains. (4) Concurrent row 1309 works on the
carry's other chapter-9 input, `9.1:prop-blind-site-expansions`; nothing here overlaps it.

RESULT: Row 1314 (Claude Opus 5.5 max, Mac mini worker 3, 17:30Z-18:12Z by date -u; author only, checked by no one; no numeric run, no subagent): the Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; the infrared seed was not attacked (no route off the record). Worked items, on the one-cutoff carry: READ in Sussman and Alpoge's complete account (CA-I, CA-III at 31a47c543775) and Balaban's CMP 119 (page images) that `9.10:thm-last-lattice-comparison` is off the gap carry (it serves only the geometric rate), and that the account takes p_1 = p_0-4r-1 < p_0 < q, so row 1299 4.7's "q > p_0 (equivalently p_1 > p_0)" is false as an equivalence; PROVED Lemma NC1 (under the account's p_1 the delta-scale cut is not inside CMP 119's p_1-scale box (3.43)), Lemma C1 and, given the account's transcription of CMP 116 (1.34) for interior domains (box |B| < eps_1/g_k), Corollary E0: (E0) of row 1268 holds on the pin route with the box of CMP 116 (1.34), the (3.43) box belonging to straddling domains only, so row 1268's wording of (E0) is corrected; Lemma S1 (summability if a p_1-scale cut is ever needed); ARGUED: one order of choice for the outline's constant conditions (UM14), (UM19), (UM23), (UM26') (premise (P4) of row 1299), given readings (Q1)-(Q3). OPEN: (Q1)-(Q3), CMP 116 (1.34) itself, premises (P1)-(P3), (P5), the blind-site expansion (row 1309), the account's premises, the infrared seed. Output library/gap-mini-solve-bb-opus.md.
