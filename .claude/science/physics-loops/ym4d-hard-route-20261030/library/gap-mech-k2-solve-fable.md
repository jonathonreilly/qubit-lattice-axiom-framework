lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-26T09:12Z

# Row 1542, gap-mech-k2-solve-fable: solve brief on the (K-II) step

Pinned commit 1813043e8, branch claude/ym4d-hard-route. Started 2026-11-25T21:12Z (date -u). Worker: Claude Fable 5.2,
reasoning effort high, Mac mini worker 1. No subagents. Status of everything below: unchecked by a second
party unless a check is named.
Resumed 2026-11-25T21:38Z (date -u) as a laptop Claude Fable 5.2 high subagent, after the Mac mini account
reached its usage limit. Sections 0 to 2 are the first run's text. Sections 3 to 6 are the resumed run's.

## 0. Plan (written first, per the save protocol)

1. Read the rule sections of FINISH.md and GOAL.md, the seed statement (gap-k2-tool-design-fable.md 3.1),
   and the results of rows 1528 to 1541 and 1468 to 1500 (RESULT parts first, bodies where needed).
2. State precisely what a (K-II) step must deliver, and what is on file about why each tried step fails.
3. Choose one attack, write it as lemmas with proofs or with the exact failing line.
4. Registry greps (open-core.md, FINISH rows) before any statement is called new.
5. End with the exact stopping statement, its non-equivalence to the seed, its selectivity, and a RESULT line.

## Status log

- 2026-11-25T21:12Z: file created, plan written. Nothing read yet beyond the queue row.
- 21:12Z: read FINISH rule sections (L1-84, L299-360), GOAL.md, queue row 1542, RESULT parts of rows 1528-1541.
- 21:12Z: read RESULT parts of rows 1468-1500 (the earlier K-II tool attempt, checkpoint 1496, check 1497).
- 21:19Z: read gap-k2-tool-design-fable.md 3.1, 4.3-4.5 (seed, (K2-STEP), GA, filter). First candidate under test: the 2+2 split (4D gauge theory as a 2D gauged sigma model on B with target the 2D connections on A), compared with 2D O(4) by a Durhuus-Froehlich type inequality. Registry grep next.
- 21:19Z: the 2+2 candidate is ON FILE: sheets / transverse lattice (rows 1103-1114, GH2, P4, BR-2; prior/gap-gauged-sigma-read-luna.md Section 4), worst-case layer comparison refuted (rows 1139-1140). Not pursued as new. Reading Theorem T (row 1332) for the rate budget.
- 21:26Z: read the digest of the two 2D O(N) proofs (prior/gap-2don-proofs-read-opus.md Step 6, B(1)-B(6)). Blind candidates on file: relative form bound along beta = route B1 / (LEV_K) (rows 669, 708, 1517); MK sandwich = row 1025. Reading Theorem T 4.4 in full for the rate budget (A2)-(A3).
- 21:30Z: read Theorem T 4.4 (row 1332). Note: in the K-II form the seed needs no rate (l is free); a rate is needed only in Theorem T because of (A1). Next: keyword counts for the remaining blind candidates, then Lemma CEN / CEN+ statements.
- 21:33Z: frame decoupling (Proposition LOC 1, gap-invent-selective-max.md L197), twist eaters and the beta^(-3/2) toron count are ON FILE. Found a possible unrecorded combination: row 1108's (MON-L) / BR-2 with the anchor rate pi against Theorem T's budget (A3) (row 1332 is later than row 1108). Reading row 1108's definitions.
- 21:35Z: Sections 1-2 written (reading record; table of eight blind candidates, all on file). Run stopped at 21:37Z: the Mac mini Claude account reached its usage limit.
- 2026-11-25T21:38Z (date -u): row RESUMED as a laptop Claude Fable 5.2 high subagent (no further subagents), from the relayed Sections 0-2, which are kept unchanged. Next: row 1108's (MON-L) / BR-2 definitions and Theorem T's budget (A3), to test the combination named at 21:33Z.
- 21:41Z: Section 3 written. The combination is not on file and is consistent at one loop, but it is no mechanism (needs (A1) geometric, a proved sheet rate, a face rate, and (MON-L)). Next: one attack of my own, on the step itself.
- 21:52Z: Section 3 corrected in two places after reading the two-dimensional digest (the O(4) rate pi is posted two-sided; the five-dimensional failure sits at the face, not at the anchor). 3.3 added.
- 21:58Z: Section 4 written (window of a useful infrared rate, table, architecture point, (IR-LOSS)). Memory free 48 percent at 21:53Z: no numeric run. Next: screen of further candidates, then the stopping statement.
- 21:58Z: Sections 5 and 6 written (nine more blind candidates, all on file or dead; the stopping statement (IR-LOSS); two next rows).
- 21:59Z: counts in Section 5 corrected against a second grep; reading record 6.6 added.
- 22:01Z: read the two-dimensional digest L186-212 and row 1011 Section 7 in full. 4.3 was wrong (the two-dimensional infrared bound is a stiffness flow whose step holds at order-one stiffness). 4.3, 6.2 item 3, 6.3 and 6.4 corrected.
- 22:02Z: 6.4 rewritten (no row recommended, by the worth-doing rule); RESULT line written. Row ends.

## 1. Repo search and reading record

Read in this session (at commit 1813043e8): FINISH.md L1-84 and L299-360 (rules); GOAL.md; queue row 1542;
the RESULT text of rows 1468-1500 and 1528-1541 (rows 1531, 1534, 1538, 1539, 1541 had no RESULT yet);
`library/gap-k2-tool-design-fable.md` 3.1 and 4.3-4.5; `library/gap-shrink-box-fable.md` 4.4 (Theorem T);
`library/prior/gap-2don-proofs-read-opus.md` Step 6, B(1)-B(6); the RESULT text of rows 1105-1114, 1139,
1140, 1332; `library/gap-br2-direction-fable.md` headings and L188-191.

Search method: one shell loop of `grep -l -i -F` file counts over `library/gap-*.md`,
`library/prior/gap-*.md` and `parts/gap.md` for about 50 key words, then the hits opened. No cross-branch
fetch was run in this session (the brief limits reading to this checkout); the cross-branch state is as
recorded by rows 1468 (Section 9) and 1529.

Numeric jobs: none. `memory_pressure` showed 34 percent free at 21:34Z, below the 50 percent rule. All work
below is by hand.

## 2. Blind candidates and where each one is on file

I derived each candidate before searching. Every one is on file. None is claimed as new.

| # | Blind candidate | On file at | State there |
|---|---|---|---|
| 1 | Split Z^4 = A x B (two planes). The links along A at a site b of B are a "spin" in the space of plane connections; the links along B are a gauge field with group G^A. So the theory is a two-dimensional gauged model on B, and with the B-links frozen and the A-plaquettes off it is one free 2D O(4) model per A-link. Compare the 4D theory with these sheets. | Model W(beta_L, beta_M, beta_T) on Z^2 x Z^2, route BR-2: `gap-bridge-exercise-opus.md` L380 (row 1072); `gap-br2-direction-fable.md` S7 L35, D1 L48 (row 1108); first cases GH2, P4 (rows 1109-1114); literature `prior/gap-gauged-sigma-read-luna.md` Section 4 (transverse lattice) | (MON-L) and (FACE-SG) open, no mechanism; first cases stopped (rows 1109, 1110; checks 1113, 1114) |
| 2 | "Gauging disorders": a Durhuus-Froehlich layer comparison, used twice | rows 1139-1140 (`gap-frameless-2d-astra.md`) | worst-case form refuted (a background orders the frameless layer above b_* >= 4.0e3); typical-background form open |
| 3 | A relative form bound: the level velocity along beta is at most K times the level gap | route B1 `gap-skeleton-max.md` L104 (row 669); (LEV_K) `gap-mid-max.md` L138 (row 708); row 1517 | the wall in the coupling variable; equivalent kind |
| 4 | Two-sided Migdal-Kadanoff bounds for the sixteen masses | (TB)_n `gap-cr-tomboulis-max.md` L38 (row 1025; check 1029) | errors are extensive; one open inequality (TB)_n |
| 5 | Port the one-annulus engine of the posted 2D O(n) proof (vanishing twist cost from a commutator identity) | `prior/gap-2don-proofs-read-opus.md` B(5) L153; row 1011 (`gap-pinned-cell-gauge-max.md` 4.3 Lemma CEN L263); row 1529 | no continuous twist on gauge-invariant data; fails |
| 6 | Use Haar translations of links by fixed Lie-algebra fields as the change of variables of that engine. After the gauge average the colour frames at different sites are independent, so two-site brackets average to zero | Proposition LOC 1, `gap-invent-selective-max.md` L197 (row 1013); second-order Schwinger-Dyson with bracket, row 1011 Proposition W | gain zero |
| 7 | The twist ratio as a running coupling: a single-plane centre twist has a zero-action flat connection (anticommuting holonomies), so Z^z/Z^0 is a power of beta at one loop, not an exponential | "twist eater" in 24 files, "toron" in 68 files of the lane; Proposition TW of row 1533; Proposition J of row 1179 | the flux half only; proved bounds favour U(1) (row 1533) |
| 8 | No continuous non-abelian symmetry acts on gauge-invariant data (higher-form symmetries are abelian; the centre is Z_2), so no twist engine of the 2D kind exists | `gap-crux-fp.md` L88 (per my notes of row 1011; "1-form" occurs in 36 files) | reading, on file |

Reading of the table (mine): candidates 1, 2 are one route (sheets). Candidates 5, 6, 8 are one fact (no
frame). Candidates 3, 4 are the wall in two variables. Candidate 7 is the flux half.

## 3. The combination named at 21:33Z: sheet rate against the rate budget of Theorem T

Written 2026-11-25T21:41Z (date -u) by the resumed run (laptop Claude Fable 5.2 high subagent). Author only, checked by
no one. No numeric run.

Read for this section: `library/gap-br2-direction-fable.md` Steps 1, 2 and 5 (row 1108); `library/gap-shrink-box-fable.md`
1.1-1.4 and 4.1-4.6 (row 1332, Theorem T; check 1335); `library/gap-univk-rate-fable.md` Step 5 (row 1391;
check 1392, RESULT text); `library/gap-sing-direction-fable.md` L236-250 (row 1115); `parts/gap.md` L173-177.

### 3.1 The combination

Row 1108 Step 5, Way B, closed the route "BR-2 at every large beta" for this reason: the anchor rate is
about e^(-pi beta), the physical rate is about e^(-(3 pi^2/11) beta), and pi > 3 pi^2/11. So a lower bound by a
sheet rate is zero in physical units. Row 1108 named the missing statement (FACE-SCALE) and row 1115 judged it
false at guide grade.

Theorem T (row 1332, three days later) does not ask for a rate in physical units. Its hypothesis (A2) asks
for a seed size N(beta) <= C_1 e^(c (beta - beta_w)), and (A3) asks c < (log L)/kappa + log(1/q)/(4 kappa).
With the one-loop step kappa = (11/(3 pi^2)) log L and q = L^(-2) the budget is c < (3/2)(3 pi^2/11) = 4.04
(row 1332, 4.4, last GUIDE remark). And pi = 3.14 < 4.04.

**Statement COMB (ARGUED; arithmetic on recalled one-loop values; GUIDE for the constants).** Let the
ultraviolet carry (A1) hold with rate q. With kappa = (11/(3 pi^2)) log L, a seed function of size
N(beta) <= C e^(c beta) meets (A3) exactly when

    c (11/(3 pi^2)) < 1 + log(1/q) / (4 log L).

For the anchor rate c = pi the left side is 11/(3 pi) = 1.167. So the sheet rate fits the budget exactly when
q < L^(-0.669). The rate q = L^(-2) (cutoff effects of order a^2) has room: the budget is then 4.04, and
the sheet rate uses 78 percent of it.

So (FACE-SCALE) is stronger than what a consumer needs. The weaker statement is:

**(FACE-RATE_c)**: there are C and c such that the face model (infinity, beta, beta) has a seed (in the form of
(A2): a thermal sum on a torus pair, flux sectors included) at a size at most C e^(c beta), for all
beta >= beta_w; and c is inside (A3).

Registry: grep of `library/`, `parts/` and FINISH.md for "FACE-SCALE" gives rows 1108 and 1115 and `parts/gap.md`
L173 only. No file has (A3) of row 1332 next to (MON-L), BR-2 or the anchor rate (checked by grep on the sixteen
files that hold both strings; in each, "(A3)" is a different label or the two strings are far apart). So COMB
is not on file. It is a remark, and I do not count it as progress, for the reasons of 3.2.

### 3.2 Why COMB is not a mechanism (four points, each from the record)

1. **It needs (A1) at full strength, and (A1) is open.** Row 1391, 5.3-5.5: when the loss is unbounded
   (c kappa > log L, which is the case for c = pi), Theorem T needs a geometric rate with a constant at most
   polynomial in ell. The account's own sketch has the rate rho^K + Pi_K with Pi_K a negative power of K and a
   constant e^(c ell^4). Row 1391 names the two statements between them, (LOG) and (GEO); both are open
   (check 1392: HOLDS AFTER CORRECTION; the table 5.4 fails as a necessity claim only). With a polynomial
   rate the loss that can be absorbed is a power of log, and the sheet rate does not fit.
2. **The anchor rate pi is a posted theorem, not a checked one.** The lane's digest of the posted
   two-dimensional programme (`library/prior/gap-2don-proofs-read-opus.md` L207, L218; row 1007; row 1108 F6) reads,
   for O(4): c sqrt(beta) e^(-pi beta) <= m_lat(beta) <= C sqrt(beta) e^(-pi beta) for beta >= beta_0, for the full
   transfer gap. Its Theorem 3.1 and Corollary 1.2 (digest L208-209) give, for every beta, a preliminary
   length exp(pi beta + C sqrt((1 + beta) log(2 + beta))). So c = pi, up to a sub-exponential factor, is the posted
   rate of the anchor. For O(3) the same digest (L200) reads a
   preliminary mixing length C e^((4 pi - eta) b), twice the rate 2 pi; a rate of that doubled kind (2 pi - eta
   = 6.28 for O(4)) would be outside 4.04. The digest marks those proofs as unread and unchecked in the lane.
   I did not open them in this run. (This item was first written from row 1332's remark alone and was
   corrected at 21:52Z after reading the digest.)
3. **The face is not the anchor.** (FACE-RATE_c) is a statement about a four-dimensional gauge model with one
   plane flat. Row 1115 (L244-247) reads the face as "at least as deep as the anchor" or deeper. No file gives
   it a rate. The reduction of the face to sheets covers only the strip beta_T up to about 10^(-3) (`parts/gap.md`
   L173).
4. **(MON-L) carries the four-dimensional difficulty.** Row 1108 D6 and check 1075: the descent
   m(beta_L, beta, beta) >= m(infinity, beta, beta) is "C_beta with a number in it". It has no mechanism; its
   covariance form is false; box-uniform proofs are refuted at guide grade above beta 3.4 (row 1090). COMB
   changes none of this. It changes only the number that the face must supply.

Selectivity and equivalence of the pair ((MON-L) at all large beta in seed form, (FACE-RATE_c)): not
equivalent to the seed (it allows a seed size up to the power 1.5 of the physical length, and the seed gives
nothing about the face model). Selectivity (ARGUED). Group: for compact U(1) the
left side of (MON-L) is zero at weak coupling (Guth; Froehlich-Spencer), and the abelian sheet (the XY model)
is also massless there (Froehlich-Spencer, recalled), so the inequality reads 0 >= 0 and gives nothing; the
group is read through the sheet's mass. Dimension: in five dimensions with A a plane and B = Z^3 the anchor is
unchanged (two-dimensional O(4) sheets, gapped). So the dimension is not read at the anchor. It is read at the
face leg: row 1053's reading (quoted in row 1108 F4) is that the tie between sheets is marginal for two
transverse dimensions; for three it is relevant, and the face is expected to order. (Corrected at 21:52Z: my
first draft of this paragraph put the five-dimensional failure at the anchor. That was wrong.) So the
selective content sits in the anchor for the group and in the face for the dimension. A selective statement
with no method is the state of row 1108.

### 3.3 A remark on the number 11/(3 pi) (GUIDE; recalled one-loop coefficients, not rebuilt)

For SU(N) with the Wilson coupling beta = 2N/g^2 the four-dimensional one-loop rate is 12 pi^2/(11 N^2) per
unit of beta. A sheet is a principal chiral model with the weight (beta/N) Re tr(U U'^(-1)) per bond, and its
one-loop rate is 4 pi/N^2 per unit of beta (for N = 2 this is the O(4) value pi). The ratio is 11/(3 pi) = 1.167
for every N. So at one loop the sheet's length is the power 1.167 of the four-dimensional length at the same
beta, for every SU(N), and the condition q < L^(-0.669) of COMB does not depend on N. I use this nowhere.

**Verdict of Section 3.** The unrecorded combination exists and is consistent at one loop: Way B of row 1108
needs (FACE-RATE_c) with c < 4.04, not (FACE-SCALE). It does not supply a step. It moves no open input. What
is left of it: one line for the route registry (BR-2 line): "with Theorem T the face may lose up to the power
3/2 of the physical length; needs (A1) geometric".

## 4. What the rate budget means for the missing step

Written 2026-11-25T21:56Z (date -u). Arithmetic and reading. Nothing here is a
proof of an open input.

### 4.1 Proposition B (the window of a useful infrared rate). PROVED as an implication; it restates row 1332 (A3) and row 1391 5.3 in one variable, so it is not counted as progress

Assume (A0) with the step kappa and (A1) with q = L^(-p), p > 0. Let (A2) hold with the exponent c. Put
r = c kappa / log L. Then the seed size at a datum of cutoff K is at most a constant times (L^K)^r, and:

- if r <= 1, the loss is bounded and (A2) is already the seed (row 1391, Corollary S3);
- if 1 < r < 1 + p/4, Theorem T gives (SEED-FP) (row 1332, (A3));
- if r >= 1 + p/4, Theorem T does not apply.

Proof. (A3) is c < (log L)/kappa + log(1/q)/(4 kappa). Multiply by kappa / log L. The first item is Corollary
S3. QED

So the useful window is 1 < r < 1 + p/4. The number r is the power of the physical length that the seed
size may reach. For p = 2 the window is (1, 3/2).

### 4.2 Table: where the crude infrared inputs on file sit (GUIDE: one-loop kappa = (11/(3 pi^2)) log L, recalled values)

| Infrared input | Exponent c per unit of beta | r | Inside the window for p = 2? | Smallest p that admits it |
|---|---|---|---|---|
| Sheet rate through BR-2 at all large beta (COMB, Section 3) | pi = 3.142 (posted for O(4), unchecked here) | 11/(3 pi) = 1.167 | yes | 0.669 |
| (LEV_K) with the largest published logarithmic rate near the window (row 708's quote, through row 1332 4.4) | about 3.3 | about 1.23 | yes | about 0.90 |
| A sheet rate of the doubled kind (as the O(3) preliminary length, digest L200); hypothetical for O(4), where the digest reads the rate pi | 2 pi - eta | 2.33 - 0.37 eta | no, unless eta > 2.24 | 5.3 at eta = 0 |
| An infrared flow that keeps only the fraction f of the one-loop drift at every scale | 2.69 / f | 1/f | iff f > 2/3 | 4 (1/f - 1) |

The last row is the plain reading of the window: with q = L^(-2), an infrared argument may lose up to one
third of the one-loop drift, at every scale, and no more.

A remark on the last row (GUESSED; recalled physics; no proof step). The one-loop coefficient 11/3 is
4 - 1/3: a spin (paramagnetic) part 4 that lowers the stiffness and an orbital (diamagnetic) part 1/3 that
raises it. An upper bound on the stiffness must pay the orbital part in full. If it keeps the fraction s of
the spin part, then f = (4 s - 1/3)/(11/3), and f > 2/3 exactly when s > 25/36 = 0.694. Row 1530 (check 1535)
bounds the spin response on typical Wilson fields, on scales up to beta^(1/16) only. So the budget says how
much of that response a carry to all scales must keep: more than 69 percent.

### 4.3 The architecture point (reading). Corrected at 22:01Z: the first draft of this subsection was wrong

Theorem T asks for a bound at the bare coupling beta, at one size e^(c beta), for every beta, with r in the
window. I name it:

**(IR-LOSS)**: there are beta_w, an integer n_w >= 3, q_0 in (0, 1), C_1 and c with r = c kappa/log L below
1 + p/4, such that every beta >= beta_w has an integer N(beta) <= C_1 e^(c (beta - beta_w)) with
5041 S(N(beta); (2 N(beta))^3; beta) <= q_0.

This is (A2) with (A3) of row 1332, with the base seed moved into the statement. It is on file.

My first draft said: in the posted two-dimensional proofs the band of order-one effective coupling is
crossed by the loss, not by a controlled step, so (IR-LOSS) is of another kind than (K-II). I then read the
digest in full at `library/prior/gap-2don-proofs-read-opus.md` L186-212 and row 1011's Section 7
(`library/gap-pinned-cell-gauge-max.md` L438-512). The draft was wrong. What the digest reads:

- In the O(4) paper [28] the preliminary length is Xi(beta) = exp(pi beta + C sqrt((1 + beta) log(2 + beta))), for
  every beta. The loss is sub-exponential: r tends to 1.
- It is proved by a flow of one number. The number is an upper bound on the twist stiffness of a pinned
  square, uniform over signed, twisted and pinned couplings. Each step from side R to side L R lowers it by
  at least (log L)/pi - C log B, the one-loop amount up to the correction. The flow runs from the bare bound b
  down to B^(-D). So it passes through stiffness of order one, with a step that holds at every stiffness.
- The step holds at every stiffness because the twist is an exact symmetry, defined on every configuration
  (row 1011, 7.4, last line). It needs no effective action: the measure is always the bare one, and the
  scales come from conditioning on rings.
- For O(3) ([15]) the same flow gives X(b) = C e^((4 pi - eta) b): r = 2 - eta/(2 pi), inside the
  two-dimensional window (1, 2) by the margin eta.

So (IR-LOSS) is not of another kind. In two dimensions it was reached by a step at order-one effective
coupling. The brief's reading stands: on both routes the missing input for the gauge theory is a step that
holds at order-one effective coupling. The routes differ in two points only:

| | Route through (PUR-io) with exact carries (Theorem K2, row 1468) | Route through Theorem T (row 1332) |
|---|---|---|
| What the step carries | a tube of local rules, with the sixteen masses exact | one bound on a response of pinned cells (the two-dimensional form), or anything that ends in a seed at the bare coupling |
| Loss allowed | none: the drift must follow the true flow, and the band takes a bounded number of steps | a fixed fraction of the drift at every scale: r < 1 + p/4, that is up to one third for p = 2 |
| Extra open input | none beside (BASE-K2), (END-K2) | (A1) at full strength |

What the window adds for a four-dimensional port of the two-dimensional flow (rows 1009 to 1021): a number
for (N3) of row 1011 (keep more than 25/36 of the spin part, 4.2; row 1011 7.4 already records the split
4 - 1/3). It adds nothing for (N1): the colour frame exists only above the band (row 1011 7.4), and a loss in
the rate does not make a frame.

### 4.4 Why (IR-LOSS) is not the seed (ARGUED; the example uses the posted O(4) bounds, unchecked here)

(IR-LOSS) names no trajectory. With r > 1 it allows a lattice gap of order e^(-c beta) with c above the
asymptotic-freedom rate. Along the trajectory such a gap is of order L^(K (1 - r)) in the units L^(-K), which
tends to zero. So (IR-LOSS) alone gives no seed at a fixed physical size. The two-cutoff input (A1) is what
turns it into one.

An example of the pattern, outside the Wilson class: the anchor W(infinity, beta, 0), one free two-dimensional
O(4) model for each bond of B. By the posted two-sided bound c sqrt(beta) e^(-pi beta) <= m_lat(beta)
<= C sqrt(beta) e^(-pi beta) and the posted periodic bound (row 1007: Theorem 3.1 of [28] with the lane's
Theorem D (b) gives the two-dimensional seed), each sheet has seeds at sizes of order e^(pi beta) up to powers
of beta. The thermal sum of the product over the bonds is the product of the factors (1 + S_sheet) minus one,
with of order N^2 bonds, so the size grows by one more logarithm. That is c = pi, r = 1.167. Its gap in the
units L^(-K) of the four-dimensional trajectory is of order sqrt(beta_K) L^(-0.167 K). Limits of this
example: the anchor is not hypercubic, so it is outside the class in which Lemma Z3 and the engine are
proved (they use the exchange of all four axes); I did not write its thermal sums on the tori of (A2). It
shows the pattern only.

The other direction (reading): the seed with a pinched flow gives a statement of the form (A2) with r = 1
from a large beta_w (row 1332, consistency remark). So inside the Wilson theory the seed implies (IR-LOSS),
and (IR-LOSS) with (A1) implies the seed. By the rule of 2026-11-22 I therefore claim only this: (IR-LOSS)
is weaker than the seed by (A1), and (A1) is an ultraviolet statement that is not selective.

## 5. Further blind candidates of the resumed run

I derived each line below before searching. For each I ran one keyword count over `library/gap-*.md`,
`library/prior/gap-*.md` and `parts/gap.md`. A count shows that the idea is on file. It is not a reading: I
opened none of the files named in this table. None is claimed as new. None is pursued.

| # | Blind candidate | Why I dropped it (my reason, ARGUED) | Keyword count; file with most hits |
|---|---|---|---|
| 9 | The Wilson flow as a smoothing map: it commutes with the centre translations, so it carries each of the sixteen masses; the flowed energy t^2 E(t) is a selective running quantity (constant for a Gaussian abelian field in four dimensions) | No consumer: the flow changes no mass, and no inequality on file turns a large flowed coupling into purity. The sign of d(t^2 E)/dt is a virial inequality on typical flowed fields, not an identity | "Wilson flow" or "gradient flow": 25 files; `prior/gap-outside-read-opus.md` |
| 10 | A trivializing map (Luscher): an exact transport between two couplings | Transport along beta; row 1438's class (an invertible slice-by-slice factor leaves the neutral spectrum unchanged) | "trivializing": 9 files; `prior/gap-lit-transport.md` |
| 11 | Entropy inequalities: the purity is a Renyi-2 quantity of the thermal state; strong subadditivity gives signed carries at every coupling (the entropic c- and a-theorems) | Group-blind; needs Lorentz boosts; a monotone a-function does not give a gap | "c-theorem", "a-theorem" or "strong subadditivity": 15 files; `prior/gap-kflow-read-opus.md` (13 hits) |
| 12 | Step scaling of z(L) = L m(L): the engine is a step-scaling inequality at large z; the missing part is the step at small and middle z | It is (Z-UNB) and (NOCRIT) in another variable | "step scaling": 43 files; `prior/gap-carry-lit-luna.md` |
| 13 | The Hamiltonian virial identity: the logarithmic rate of a level is its magnetic deficit over its energy; bound the deficit | It is (DEF_K) of row 708, failed there in three ways | read at the lines a grep showed (partial lines): `library/gap-mid-max.md` L160-176, L333 |
| 14 | Mack-Petkova split SU(2) = Z_2 x SO(3) with Griffiths inequalities for the Z_2 part | Compares with a Z_2 theory that deconfines; the frozen-group tests of the lane | "Mack" or "Petkova": 119 files (a loose pattern); `gap-short-step-max.md` (13 hits) |
| 15 | Diamagnetic bound: a gauged sheet has a smaller partition function than the ungauged one | Bounds masses one by one with extensive loss; gives no ratio | "diamagnetic": 39 files; `gap-mech-attack-neon.md`, `gap-global-reform-max.md` (9 hits each) |
| 16 | Self-duality (the Bogomolny bound) as the four-dimensional exact structure | No lattice form with a sign; no link to the thermal sum | "Bogomolny" or "self-dual": 41 files; `gap-mini-solve-j-fable.md` (9 hits) |
| 17 | Centre-vortex spreading by a rotation of each loop about its own axis (no global frame needed, because -1 is the rotation by 2 pi about every axis) | Link rotations about varying axes do not add; this is the frame problem (N1)-(N3) of row 1011 again, and Proposition TW (ii) of row 1533 | read: rows 1011, 1529, 1533 RESULT text |

Reading of Sections 2 and 5 together (mine): seventeen blind candidates, all on file or dead by an on-file
argument. This agrees with rows 1496 (finite list, no survivor) and 1529.

## 6. Where this row stops

### 6.1 What I did not do

I did not construct a renormalization or blocking step at an effective coupling of order one. I did not
prove (PUR-io) another way. I did not prove that a stated class of steps cannot exist. I did not disprove
anything. No statement of the chain is changed.

### 6.2 What this file adds

1. **COMB (Section 3; ARGUED, GUIDE constants; not on file by grep).** Row 1108 closed Way B of BR-2 because
   a sheet rate is zero in physical units. With Theorem T of row 1332 that closure is too strong: the face
   may lose up to the power 1 + p/4 of the physical length when the ultraviolet carry has the rate L^(-p).
   The anchor's posted rate pi gives the power 11/(3 pi) = 1.167 (for every SU(N), at one loop), inside the
   window when p > 0.669. So Way B needs (FACE-RATE_c), not (FACE-SCALE). This moves no open input: (MON-L)
   has no mechanism, the face has no rate, and (A1) is open.
2. **The window and the table (Section 4; Proposition B is an implication that restates rows 1332 and 1391).**
   With p = 2 an infrared argument may lose up to one third of the one-loop drift at every scale. In the
   recalled split 11/3 = 4 - 1/3 this means: keep more than 25/36 of the spin response (GUESSED reading).
3. **The architecture point (4.3; reading; corrected during the run).** The infrared input of Theorem T,
   (IR-LOSS), is not of another kind than (K-II): in the posted two-dimensional proofs it is reached by a
   stiffness flow whose step holds at order-one stiffness. The two routes differ in what is carried and in
   the loss allowed (none against up to one third of the drift), and Theorem T needs (A1) in addition.

### 6.3 The exact statement where I stopped

**(IR-LOSS)** of 4.3: there are beta_w, n_w >= 3, q_0 in (0, 1), C_1 and c, with c kappa / log L < 1 + p/4, such
that every beta >= beta_w has an integer N(beta) <= C_1 e^(c (beta - beta_w)) with
5041 S(N(beta); (2 N(beta))^3; beta) <= q_0. Here kappa is the flow bound of (A0) and L^(-p) the rate of (A1).
By Theorem T (row 1332; check 1335: HOLDS AFTER CORRECTION), (IR-LOSS) with (A0) and (A1) gives (SEED-FP).

- **Is it new?** No. It is (A2) with (A3) of row 1332. I stop at a statement that is on file, and I say so.
- **Not equivalent to the seed (4.4, ARGUED).** It names no trajectory and allows a lattice gap that is zero in
  physical units. It gives the seed only with (A1). Inside the Wilson theory the seed implies it. So it is
  weaker than the seed by (A1). I cannot show more than that, and by the rule of 2026-11-22 I do not count
  it as progress.
- **Selective (ARGUED; recalled theorems).** Compact U(1) in four dimensions: at weak coupling there is no seed
  at any size, since a seed gives a gap on all larger cubes by the engine, and the model is massless (Guth;
  Froehlich-Spencer). So (IR-LOSS) fails there. SU(2) in five dimensions: it fails if the weak-coupling
  phase has no gap (belief, as in the brief). The ultraviolet half (A1) is not selective.
- **First failing step of each way to it.** Through sheets (COMB): (MON-L) at all large beta in seed form;
  no mechanism (row 1108 D6; check 1075). Through levels: (LEV_K) or (VIR-log) of row 708; three failed
  ways on file. Through a stiffness flow as in two dimensions: no continuous twist on
  gauge-invariant data; the pin-uniform form fails (Proposition B' of row 1011); the typical-pin form needs
  the frame (N1)-(N3), which exists only above the band (row 1011 7.4); the spin response on typical fields
  reaches scales up to beta^(1/16) only (rows 1530, 1535).

### 6.4 Next rows

I recommend no row. Reasons, by the worth-doing rule (FINISH.md, How we work, item 0):

- A check of Sections 3 and 4 would move no item on the critical path. Its only product would be one line
  in the BR-2 entry of the route registry. If the lead reopens the BR-2 line for another reason, the points
  to check first are: the arithmetic of COMB and of table 4.2; whether (FACE-RATE_c) is the right weakening
  of (FACE-SCALE) given check 1392's corrections to row 1391 5.4; the selectivity paragraph of 3.2.
- My first draft proposed a reading row on how the posted two-dimensional preliminary length is proved.
  The lane's digest already answers it (4.3). The posted proofs are still unread and unchecked in the lane
  (row 1007); reading them does not move the four-dimensional wall.
- I name no proof row, because I have no first lemma for one.

### 6.5 Labels

| Statement | Label |
|---|---|
| Sections 0-2 (first run): eight blind candidates on file | reading, by the first run |
| COMB, (FACE-RATE_c) as the consumer's need in Way B | ARGUED; constants GUIDE; unchecked |
| Ratio 11/(3 pi) for every SU(N) | GUIDE; recalled one-loop coefficients |
| Proposition B | PROVED as an implication from Theorem T and Corollary S3; a restatement |
| Table 4.2; the 25/36 reading | GUIDE; GUESSED for the last remark |
| (IR-LOSS) not equivalent to the seed; selective | ARGUED |
| 4.3: (IR-LOSS) is of the same kind as (K-II); the two routes differ in carry and loss | reading of the digest and of row 1011; the posted proofs are unread |
| (IR-LOSS), (A1), (MON-L), (FACE-RATE_c), (LEV_K), (K2-STEP), (PUR-io), the mass gap | OPEN |

### 6.6 Reading record of the resumed run

Lane checkout at commit 8d76c945d (the first run pinned 1813043e8). Read: FINISH.md L1-84 and L299-360; GOAL.md;
queue row 1542; the RESULT text of rows 1108, 1332, 1335, 1378, 1386, 1391, 1392, 1442, 1443, 1468, 1496 to
1500, 1528 to 1530, 1533, 1535 to 1537, 1540 (rows 1108, 1386, 1442, 1443, 1468 and 1496 in part: the queue
view cut them); `library/gap-k2-tool-design-fable.md` 3.1 to 4.5 and its RESULT; `library/gap-shrink-box-fable.md`
Sections 0, 1 and 4; `library/gap-br2-direction-fable.md` Steps 1, 2, 3, 4.2 and 5; `library/gap-univk-rate-fable.md`
Step 5; `library/gap-sing-direction-fable.md` L236-250; grep lines of `library/gap-mid-max.md` (partial lines, cut at about 260 characters);
`library/prior/gap-2don-proofs-read-opus.md` L186-212 in full and grep lines elsewhere; `library/gap-pinned-cell-gauge-max.md`
L438-512 (Section 7). Not read: the files
of rows 1544 and 1547 (by the brief); any file of Section 5's last column; the posted two-dimensional proofs;
the account. Registry greps: `library/open-core.md` has no hit for MON-L, BR-2, (A2), (A3) or "sheet";
"FACE-SCALE" occurs in rows 1108 and 1115 and `parts/gap.md` L173 only; no FINISH row after 1332 names MON-L
or BR-2. No numeric run (free memory 48 percent at 21:53Z, below the 50 percent rule). No subagent. No edit
in the lane checkout, no commit, no post.

RESULT: Row 1542 (Claude Fable 5.2 high; started on Mac mini worker 1, resumed 21:38Z and finished 2026-11-25T22:02Z (date -u) as a laptop subagent; author only, checked by no one; no numeric run, no Lean, no subagent). NOT solved: no step at order-one effective coupling is constructed, (PUR-io) is not proved another way, no class of steps is excluded, nothing is disproved. Seventeen blind candidates were derived before searching; all are on file or dead by an on-file argument (eight read in the first run; of the nine in the resumed run, seven by keyword count only). One remark is not on file by grep (ARGUED, constants GUIDE): COMB. Row 1108 closed Way B of BR-2 because the sheet rate pi exceeds the asymptotic-freedom rate 3 pi^2/11; but Theorem T of row 1332 admits a seed size up to the power 1 + p/4 of the physical length when the ultraviolet carry (A1) has the rate L^(-p), and the sheet's power is 11/(3 pi) = 1.167 at one loop (for every SU(N)), inside the window for p > 0.669; so Way B needs (FACE-RATE_c), not (FACE-SCALE). COMB moves no open input: (MON-L) has no mechanism, the face has no rate, and (A1) is open. Restated, not counted: Proposition B (the useful infrared window is 1 < r < 1 + p/4; with p = 2 an infrared flow may lose up to one third of the one-loop drift, that is keep more than 25/36 of the spin part, GUESSED). Corrected during the run: the infrared input of Theorem T, (IR-LOSS) = (A2) with (A3), is not of another kind than (K-II); by the lane's digest the posted two-dimensional proofs reach it through a pin-uniform stiffness flow whose step holds at order-one stiffness; the two routes differ only in what is carried and in the loss allowed, and Theorem T needs (A1) in addition. Stopped at (IR-LOSS), which is on file: weaker than the seed by (A1) (ARGUED), selective (it fails for four-dimensional compact U(1) at weak coupling, and in five dimensions by belief), with no method; first failing steps: (MON-L) through sheets, (LEV_K) through levels, the colour frame (N1)-(N3) through a stiffness flow. Open: (IR-LOSS), (A1), (MON-L), (FACE-RATE_c), (K2-STEP), (PUR-io), the mass gap. No row is recommended.
