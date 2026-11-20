lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:52Z

# gap-mini-solve-az-opus: the SU(2) four-dimensional mass gap (FINISH row 1310)

Started 2026-11-20T17:52Z (date -u) at commit 6d4a6f177 on branch claude/ym4d-hard-route, Mac mini Claude worker 2.
Research-stage working state; nothing here is a public claim. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Record read (statements about the record, not evidence; written 17:56Z by date -u)

Read at pin 6d4a6f177: `GOAL.md` in full; `FINISH.md` L1-100, L299-352 and the rows 1299-1315 (L1380-1396, with their
RESULT lines); `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; Steps 0-2 and 5-6 of
the sibling row 1313 (`gap-mini-solve-ba-opus.md`) and Step 0 of row 1314 (`gap-mini-solve-bb-opus.md`) as they stand at
this pin; Steps 0-1 and 6-7 of row 1309 (`gap-mini-solve-ay-opus.md`); Step 5 of row 1299 (`gap-mini-solve-aw-opus.md`).

What the record fixes (pointers, not evidence):
1. Modulo the ultraviolet carry and the continuum datum, the gap clause reads one lattice input at one physical size,
   uniformly in the cutoff: (N-phys) of row 1161 (row 1218 digest, display (N)); its fixed-coupling forms are the seed.
   Rows 1296, 1299, 1300, 1302, 1309, 1313 find no route to the seed off the record; rows 1301-1308 worked the owner's
   tiling and positivity directions on it and closed them as routes (checks 1305, 1306, 1308, 1312).
2. Published work (row 1218, rows 1295/1311): paper A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha
   Roy) proves a conditional ascent from a one-scale thermal window (A-B*) to a full transfer gap; (A-B*) implies
   (N-phys) (row 1295 Corollary AU2, held by check 1311). Paper B's Corollary 166 is a weak-coupling bound for coarse
   straight-path variables; row 1220 found it carries no gap information. Neither supplies the seed at weak coupling.
3. The one-cutoff carry (rows 1256-1309) is reduced to named inputs. Open after rows 1299, 1309, 1313: the outline's
   premises (row 1313 reduces (P3)-(P4); (P1), (P2), (P5) stay), the margin reading (M), (V9), and in the account's
   OUTSTANDING `9.1:prop-blind-site-expansions` (CA-III L16559, T0 node F56): the reading (H-par'), the (P) part for
   stores younger than the shell, and clause (c)'s second alternative (row 1309 Step 6.2).

## Step 1. How best to attack it (judgement, ARGUED; written 17:56Z by date -u)

**The seed.** A rough count (GUIDE, physical glueball numbers, not a proof step) shows what (N-phys) asks at a window
coupling: with m a about 1 and K = 512, the neutral excited trace on an n^3 cube at time n/K is about
n^3 (m a K / (2 pi n))^(3/2) e^(-m a n/K), which is below 1/2 only for n of order 10^4. So the seed is a statement about
a lattice of side about 10^4 at order-one coupling: the lattice mass gap itself, with its count. The record holds about
45 route families to it, each at its first failing step, and row 998 9.5 calls another screen by this model family a
waste. I name no route off the record, so I do not attack it, and nothing below is progress on it.

**The item.** The two open clauses that row 1309 left in `9.1:prop-blind-site-expansions` (Sussman and Alpoge, CA-III
L16559, Proof outstanding in their account; hypothesis (e) of `9.1:thm-last-lattice-comparison`, CA-III L17912, which
the one-cutoff carry reads; T0 node F56 of `library/chain-ca.md` L208):
- (Y) the (P) part for blind stores younger than the shell. The account's (d3) sends this case to "the class
  assignment of stored terms in the relative expansion at the preparatory integrations" (CA-III L15576-15579), which
  row 1309 could not locate by name. This could hide a real gap in the account, so it goes first.
- (H) the reading (H-par'): a fourth-class unit may keep its island slots in its read set while its localisation
  domain is its active domain.
Rule 0a: `grep -n -i "younger than the shell\|(H-par')\|class assignment\|blind-site\|island-blind"
library/open-core.md` gives nothing; in `FINISH.md` the first three strings occur only in row 1309 (L1390), which is
finished and lists them as OPEN. Row 1313 owns (P3)-(P4); row 1314 had no item at this pin.

Moves: T0 node F56 and hypothesis (e) of Theorem 9.1 on the carry. Success: the (P) part for young stores PROVED or
located as proved text, and (H-par') PROVED from the account's definitions, so that F56 becomes an implication from the
account's own plain site statements. Failure: the exact clause of the account that a young store or an island slot
breaks, which would be a real gap in their outstanding proposition. Neither outcome changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 2: fetch CA-II and CA-III at 31a47c543775 into a new scratch folder; read (d3) and its surroundings
  (CA-III L15540-15600), the preparatory integrations and the relative expansion where stored terms get their class,
  and the (P) site statement the account cites.
- Step 3: the young-store (P) case: proof from the located text, or the failing clause.
- Step 4: (H-par') from the account's T-site definitions (localisation datum versus read set).
- Step 5: labels, what a checker should redo, RESULT.

## Step 2. The site (P) and young stores, as the account states them (READ; written 18:01Z by date -u)

Sources: Sussman and Alpoge's complete account CA-II and CA-III at 31a47c543775, fetched by URL into a scratch folder
outside the repository (line numbers are TeX lines of those files).

**2.1 What the site (P) integrates (READ).** The site (P) is "The N(g) preparatory integrals [CMP122a (1.60)-(1.63)]
... Both slots of the bracket in [CMP122a (1.60)] are included: the response Phi(B'_j), and also the integration
variable A_j" (5.2:def-sites-units, CA-II L5273-5276). The rim field A_j "is an integration variable on
Z_(j+1) cap Omega_(j+1)", and B_j comes from "the group variables V_j on Omega^c_(j+1) minus Z''_(j+1)"
(5.2:prop-two-slot-preparation, CA-II L12980-12983, L13017-13019). The bracket evaluates
(E_k + R_k + B_k + B_k^(n)) at the shifted configuration (CA-II L12991-12996). So every stored boundary term of
level up to k that reads the shell is an input, whatever its age.

**2.2 Young stores read the integrated variables (READ).** "A boundary term B^(l)(X) with l - j >~ N_0(g) depends on
A_j on a number of collar cubes of order R_(j+1)^d. Each of these cubes is charged a factor e^(c_F) by [CMP116
(2.26)]" (CA-II L13063-13068). The account pays this by the two-slot expansion: Moebius inversion over the response
cubes and over "the weak A_j-cubes q meeting S", with parameters u_q of radius r_A, so that each element depends on the
rim only on its rim set b(e) (CA-II L13072-13090). So at (P) the decay over integrated rim cubes comes from the
u-expansion, not from the inputs' own decay.

**2.3 The separation (d3) is for stores no younger than the shell (READ).** 9.1:lem-island-geometry (d3) (CA-III
L15559-15579, proof L15774-15805) shows: at the preparatory integration of scale j+1 inside a component C' of Z(m),
an island of I_(j+1) (j+1 < m) or of I_m^- (j+1 = m) is off the shell. The proof uses condition (ii) of CMP 122a (no
new large-field region inside C' in the last N_pr steps), so every birth of an island inside C' is at a level
i' <= m - N_pr - 1 <= j - 1, and then (b) at level j+1: dist_(j+1)(cl_(j+1)(s')^(4), Lambda_(j+1)) >= 3 R_(j+1) - 5 >= 2.
It ends: "The treatment by the preparatory integrations of a stored term younger than the shell at which it is
evaluated (of level l > j+1) is not part of this statement; it is governed by the class assignment of stored terms in
the relative expansion at the preparatory integrations."

**2.4 The sizes the account allows (READ).** N(g) is the number of preparatory stages; "N(g_k) <= C_N T_k^(r_pr), since
R(x) < L max{1, (log x)^(r_pr)} and Balaban's N is bounded by R at the scale of the chain [CMP122b] (it is assumed
there that N <= R_k)" (CA-II L114-120). The island geometry lemma says of itself: "None of the statements (a)-(f)
depends on ... N_pr ... The scaffold radius enters only through distances of the form 3 R - O(1)" (CA-III
L15860-15863).

**2.5 Where "class assignment" points (READ).** The only definition in CA-III that assigns classes to stored terms at
the R-step is 9.1:def-resolved-members (CA-III L12933-13140): a class is a pair z = (n, k') (zone, reading level);
the marks of a read term are split into a stored class-n member, a reading part and (for R-born terms) an own member,
"Each of them is assigned exactly one class" (L12996); for an R-born term the classes split into Z_surv and Z_own, and
Z_own contains "(b1) Every class all of whose slots lie inside the healed components ... The preparatory integrations
of these components, as in [CMP122a], are included" (L13033-13041). This governs the two-run differences (the
S°-part of the island-blind format), not the one-run size bound (the N°-part) that the site's expansion statement
needs. I take it as the place (d3) points to; the account does not say so by label.

## Step 3. The (P) part for stores younger than the shell (written 18:04Z by date -u)

Notation as in 9.1:lem-island-geometry: level-k cubes are M-cubes of the level-k lattice, nested, a level-(k+r) cube
being L^r level-k cubes wide; cl_k is closure in level-k cubes; X^(4) adds four layers. Fix R_m, a component C' of
Z(m), a preparatory scale j+1 with m - N_pr + 1 <= j+1 <= m, the shell Sh := (Z_(j+1) minus Z''_(j+1)) cap C' (one layer
of level-(j+1) cubes at the boundary of Z_(j+1)), and an island-blind stored term v of level l = j+1+r, r >= 1, that is
an input at this integration. Its blind set B is a union of islands of I_l (of I_m^- if l = m), and each such island is
a union of sets [cl_l(s'')]^(4), s'' over its strips (lem-island-geometry (e), proof, CA-III L15816-15821).

**Lemma Y1 (PROVED, given lem-island-geometry (b), (c1), (e) and the birth bound of its proof of (d3)).** If
5 L^r + 2 <= 3 R_(j+1), then B does not meet Sh.

*Proof.* Let s'' be a strip of an island in B, born at (C_1, i''). The term exists at R_m, so the births of its islands
are live at m (lem-island-geometry (e), first sentence). Case 1: at level m the island lies in a component of Z_m other
than C'. Then cl_m([cl_l(s'')]^(4)) lies in [cl_m(S_m^-)]^(1), inside an island of I_m^- in that component (the second
inclusion of (e), with births at levels <= l <= m-1, or l = m and I_m^- directly), which is at least (R_m+1)/2 >= 5
level-m cubes from C'^sharp if the component is not in Z(m) ((c1)), and at least R_m cubes from C' otherwise (separation
of components, as in the proof of (d3), CA-III L15776-15781). Since Sh is inside C', the set misses Sh. Case 2: the
island lies inside C'. Then C_1 is inside C', and condition (ii) of CMP 122a excludes births inside C' at the levels
m - N_pr, ..., m-1 (proof of (d3), CA-III L15786-15794), so i'' <= m - N_pr - 1 <= j - 1. By (b) at level j+1 >= i''+1,
dist_(j+1)(cl_(j+1)(s'')^(4), Lambda_(j+1)) >= 3 R_(j+1) - 5, so every level-(j+1) cube of s'' is at least
3 R_(j+1) - 1 level-(j+1) cubes from Lambda_(j+1). Every cube of cl_l(s'') lies within one level-l cube of s'', that is
within L^r - 1 level-(j+1) cubes, and the four added layers are 4 L^r level-(j+1) cubes wide. So every cube of
[cl_l(s'')]^(4) is at least 3 R_(j+1) - 1 - (5 L^r - 1) = 3 R_(j+1) - 5 L^r >= 2 level-(j+1) cubes from Lambda_(j+1),
hence off the one-layer shell at the boundary of Z_(j+1) = Lambda_(j+1)^c, exactly as (d3) concludes from ">= 2". QED.

**Corollary Y1' (PROVED GIVEN the hypotheses of Theorem RL-P of row 1309).** Theorem RL-P (row 1309 Step 5.3) holds for
blind stores of every level l <= j+1+r_*(j), where r_*(j) := max{r >= 0 : 5 L^r + 2 <= 3 R_(j+1)}: by Lemma Y1 the
parameter set Y minus A(Y), which lies in B, contains no integrated variable of scale j+1, and the proof of RL-P applies
unchanged. Since R_(j+1) >= 9 only, r_*(j) may be 0 (it is 0 when R_(j+1) = 9 and L = 5: 5 L + 2 = 27 = 3 R).

**3.2 Why Lemma Y1 does not reach every young store (ARGUED).** (i) The account's own regime contains stores much
younger than the shell that read the shell's variables: "A boundary term B^(l)(X) with l - j >~ N_0(g) depends on A_j
on a number of collar cubes of order R_(j+1)^d" (CA-II L13063-13064), with N_0(g) the number of zones, and the number of
stages N(g) may be as large as Balaban's R (CA-II L114-120). (ii) The account's geometry gives only lower bounds of
order 3R on the distance from a strip to the boundary of Z_(j+1) (lem-island-geometry (a), (b)); nothing in it bounds
that distance above. In the history that condition (ii) of CMP 122a describes (no new large field inside C' for N_pr
steps), the large-field region grows by Balaban's construction (1)-(3) of CA-III L15399-15410, a few layers of
LM R_(k+1)-cubes per step, so the strip-to-shell distance at scale j+1 is of order R_(j+1) level-(j+1) cubes, while the
level-l fattening is 4 L^r of them. Once L^r is several times R_(j+1), the young island covers shell cubes of scale j+1.
I have not exhibited such a history in full (it needs the account's large-field selection rules), so this is ARGUED.
(iii) If a young island covers a shell cube, the re-indexing of row 1309 fails there: an integrated variable A_j lies in
the store's parameter set, so the parameter principle (the account's 4.24:prf-exterior-independence, CA-I L109371) does
not apply.

**3.3 The repair through the read set, and where it stops (ARGUED).** The natural repair is the reading (H-par') at (P):
keep the young store's island part in its read set S_v and its localisation domain at A(Y). Then the two-slot
expansion covers the island rim cubes, since its weak cubes are "the weak A_j-cubes q meeting S" (CA-II L13079-13081),
and each element depends on the rim only on its rim set (CA-II L13087-13090). The output's island cubes are excused
again at level m, since cl_m(B) lies in W_m (lem-island-geometry (e)). What this does not pay: the Moebius sum over
subsets F_w of the weak cubes Q of the read set costs up to (1 + 1/r_A)^|Q| times the input's sup norm (the derivative
in each u_q at radius r_A gives at most 1/r_A by Cauchy). For a plain term |Q| is at most a constant times d(X) + 1 and
is paid by its decay. For the island part of a young store, |Q cap B| is not bounded by d°(Y): the account claims no
bound on an island's size or on its number of strips (CA-III L15444-15446). So the young case at (P) needs one of:
- (Y-a) a bound |Sh cap B| <= c (d°(Y) + 1) for every young blind input at the preparatory scale (for instance, that
  only a bounded number of island cubes of a young store lie on old shells), or
- (Y-b) an expansion of the young store in the island rim variables whose Moebius cost is charged to the island
  itself (a per-island factor, as the large-field step charges a healed box through Balaban's Hamiltonian-path bound
  exp(2 kappa (100 R_k)^d), CA-III L15845-15852), or
- (Y-c) a proof that at the preparatory integrations the account's class assignment (Step 2.5) removes young blind
  inputs over islands inside C' from the one-run integrand.
None of (Y-a)-(Y-c) is in the text I read. So the (P) part for stores younger than the shell by more than r_*(j)
levels stays OPEN. If (Y-a)-(Y-c) all fail, the outstanding proposition is false as stated at (P) for such stores; I
have not shown that.

**3.4 The account excludes young stores at (P) in a second place too (READ, 18:04Z by date -u).** 9.1:lem-blind-domination
(CA-III L16801-16850), whose clause (b) gives the activity sums of island-blind members at the three sites, names the
site cells as: "at (T), a cell Delta inside Y_0 ...; at (L), an exterior anchor ...; at (P), a collar cell of scale at
least the level of the store" (L16823-16827). So at a preparatory cell of scale j+1 the account's activity sums cover
only stores of level at most j+1, the same restriction as (d3). The lemma pays island-blind values per island through
the large-field cell count (its (a): sum over X containing I of |delta(X)| at most (1 + 3^d C_fib N_l(I)) S°, at most
3^(d+1) C_fib sum_j |Gamma^0_j cap I| S°, L16846-16850), which is the per-cell budget that route (Y-b) of 3.3 would
use at (P). That budget is the account's mechanism for values; it is not asserted for young stores' activities at
older preparatory cells. So the young case is a gap in the outstanding proposition's stated scope, consistently
marked by the account, and not an error of its text.

## Step 4. The reading (H-par') at (T), and a correction to row 1309 (written 18:08Z by date -u)

**4.1 What the account's site (T) does with a unit's read set (READ).** (1) A response map R_p(t, sigma) is attached to
Balaban's localisation datum p = (square, Y_0); "the amplitude t multiplies the shift piece, which is the product of
chi-hat_square with the response"; and "eta_p <= 1 denotes the decay factor between the block square and the set S_v"
(5.2:def-sites-units, CA-II L5300-5333). (2) Type-four units (older B^(j), B'^(j), chain terms on live arrested
pieces) are read through their orbit datum, holomorphic over the chart G_eps(S_v) of gauge rotations on the read set,
whose radius at each live law site s is eps_k(s) = e(s) - sum_(k'<k) eta_(k')(s) >= (3/4) e(s) (CA-II L25200-25217); the
rotation u rides with t, and the riding-rotation lemma gives |d_t F(0)| <= N eta_p^(1/2) / w_L (CA-II L5869-5900,
L6684-6705). Inner-class law sites lie in Z_(k-N_k), deep inside the large-field region (CA-II L5340-5345), and the
allowances eta_(k')(s) are reserved there too. (3) The second stage is Balaban's cluster expansion [CMP116 (2.1)-(2.41)]
on potentials V(Y, ., B) of the form [CMP116 (1.42)-(1.43)]; an output with localisation domain X is bounded by a
constant times e^(-kappa d(X)) (5.2:lem-second-stage-activities, CA-II L6902-6960).

**4.2 Correction to row 1309 Step 7.2 (ARGUED; it weakens a claim of that row).** Row 1309 said that Theorem RL-T holds
under (H-par') "by the same proof: (T1)-(T6) use the localisation domain only". That is too quick. Under (H-par') the
read set of a re-indexed blind store is S_v = Y, so by 4.1 (1)-(2) its dependence on the amplitude t_square of a
response block decays only like eta_p(square, Y)^(1/2), that is, in dist(square, Y). A first-stage potential that
links the store to square is localised, in the plain machine, on A(Y) together with square and a connection, whose
plain length needs decay in dist(square, A(Y)). When a response block is nearer to an island part of Y than to A(Y)
(blocks are at least 3 R - 4 cubes from islands by the moat, lem-island-geometry (a), but nothing bounds their distance
to A(Y) by their distance to Y), the plain first-stage bound cannot be applied by statement. What the inputs do give is
e^(-kappa d°(Y)) eta_p(square, Y)^(1/2), and with W excused
d°(A(Y) union square union (Y cap W)) <= d°(Y) + dist(square, Y) + 1,
because every island part of the connected Y touches Y minus W, which lies in A(Y) (Lemma A1). So the output is
correct only in the island-blind format, filed with the island part. Hence:

**Proposition H (ARGUED, replaces row 1309's (H-par') claim).** The reduction of row 1309 (re-index at A(Y), take the
plain (T) statements by statement, re-file) is valid at (T) under
- (RS) the shifted configuration of the T-step, the rotation u included, is unchanged on the islands of the blind
  inputs: equivalently (H-par) with (U-loc) of row 1309;
and without (RS) it needs, in place of the plain first-stage bound, its island-blind form
- (FS°) for a blind store with read set Y and active domain A(Y), the first-stage elements that link it to response
  blocks square_1, ..., square_n obey the plain first-stage bound with each eta_p(square_i, A(Y)) replaced by
  eta_p(square_i, Y) and the output's tree length replaced by d°,
after which the second stage (Balaban's cluster expansion, CMP 116 Section 2) can still be taken by statement for
potentials indexed at their active domains, since islands carry no integration variable at (T) (lem-island-geometry
(d1)) and the parameter principle (4.24:prf-exterior-independence) covers non-integrated shared slots.

Evidence on (RS): the shift piece is supported on blocks (4.1 (1)), which supports (RS) for the shift; but the account
reserves rotation allowances at inner-class law sites deep inside large-field regions (4.1 (2)), so it does not assume
(RS) for the rotation. (FS°) is a statement about the proof of the account's first-stage lemma, not about Balaban's
cluster expansion, so it is a much smaller rerun than the account's route (which reruns CMP 116 Section 2).

**4.3 What Steps 3-4 change in row 1309's table.** Theorem RL-T and RL-L: PROVED GIVEN (H-fmt), (RS) (in place of
(H-par')), (TH), (F_RL); or GIVEN (H-fmt), (FS°), (TH), (F_RL). Theorem RL-P: extended to stores at most r_*(j) levels
younger than the shell (Corollary Y1'); the younger stores stay OPEN (Step 3). (H-par') alone is not enough (4.2).

