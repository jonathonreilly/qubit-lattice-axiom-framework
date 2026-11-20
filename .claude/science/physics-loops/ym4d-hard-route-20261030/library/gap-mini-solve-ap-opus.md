lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:35Z

# gap-mini-solve-ap-opus: queue row 1280

Started 2026-11-20T13:35Z (date -u). Pinned commit 220f8a48d, branch claude/ym4d-hard-route.
Task (row 1280): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the Jaffe-Witten sense; first consider how best to attack it, then do it.
Labels: PROVED, ARGUED, GUIDE, OPEN. Numerics guide only.

## Status

Step 0 (reading the folder rules and the earlier work): done 2026-11-20T13:48Z (date -u). Step 1 (choice of attack): done 2026-11-20T13:52Z. Step 2 (reading the account's test-cube rule): done 2026-11-20T14:01Z. Step 3 (statements and proofs): done 14:06Z. Step 3b ((U-dom) from Balaban's decay estimate): done 2026-11-20T14:08Z, stays ARGUED. Step 4 ((H2)-(H3) of row 1267 from EM's definitions): in progress.

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T13:48Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84 and L299-360; the row of this item (L1361); the RESULT lines of rows
1007, 1009-1011, 1013, 1016, 1228, 1255-1260, 1264, 1267-1269, 1273-1276, 1279; `parts/gap.md` L1-104 (state of
attack); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; `library/gap-phys-seed.md` L311-401 (Theorem
ZD-c, Corollary Z4, Proposition MB, (MONO-Delta)); `library/gap-mini-solve-i-fable.md` L23-114 and
`library/gap-mini-solve-b-fable.md` L35-57 (the screening tables); `library/gap-mini-solve-al-opus.md` L34-59 and
L545-576; the opening of `library/gap-mini-solve-an-opus.md` (row 1277, in flight on worker 1: the slab hypothesis
(M) of Bhattacharjee et al. along the 4D tuning, so this row does not take it).

What the record fixes (each item cites where it is proved or checked; none is re-derived here):

1. The gap clause splits (Theorem BP, row 1179, check 1183): the continuum datum of the T0 chain plus one lattice
   input, (N-phys) of row 1161: at one physical side, uniformly in the cutoff, the periodic centre-neutral excited
   trace of the cube at a time u at most n/K is at most 1/2.
2. (N-phys) is equivalent in strength to a lower bound of asymptotic-scaling type on the deconfinement coupling at
   temporal extent n/K (rows 1180, 1184, check 1187). It implies confinement of static charges at every coupling,
   itself open for 4D SU(2).
3. The one-cutoff carry (row 1233 Proposition 3.7 and rows 1255-1275) reduces the all-cutoff input to one datum at
   one coupling, modulo inputs of the Sussman-Alpoge account and of Balaban's CMP 116 (not on this machine).
4. Row 1218's sources: A (Bhattacharjee et al.) gives a one-scale thermal criterion with a conditional ascent of the
   lane's own kind (stronger than (N-phys)); B's weak-coupling Corollary 166 is non-selective (it holds for the
   massless Villain U(1) as well; on file in the rows that cite it); Zeng's routes are conditional.
5. More than seventy candidate mechanisms for the seed have been screened by rows 998, 1128-1130, 1179-1199 and
   1255-1275; each stops at the same place: no selective inequality is known at order-one coupling, and the only
   all-coupling template (the posted 2D O(N) proofs) needs a rigid non-abelian symmetry on the integration variables,
   which lattice gauge theory lacks (Lemma CEN+, row 1016; row 1228).

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T13:52Z by date -u)

**The seed.** I re-derived, before reading the screening tables, about a dozen routes to the infrared input: center
vortex recursions, the 't Hooft electric-magnetic Fourier duality, abelian projection, the small-volume zero-mode
spectrum as a start for a flow, a strong-coupling expansion at the scale where the running coupling is of order one,
Durhuus-Frohlich layers with the posted 2D O(4) theorem, path coupling, Bakry-Emery, positivity of dual spin foams,
continuity in theta, and a scale-invariant infrared limit argued by compactness. Each has a match on file (Step 0, item
5, and the tables cited there), and each stops where the record says: no selective inequality at order-one coupling.
Two remarks of mine, GUIDE only: (i) in the small-volume regime the neutral gap in units of 1/L is smaller for SU(2)
(of order g(L)^(2/3), Simon's quartic valley, row 1273) than for compact U(1) (2 pi, the first photon), so the
deep ultraviolet gives no selective start for a flow in the plain gap variable; the crossing of 2 pi is inside the
band. (ii) The one-cutoff datum that the carry leaves is a statement at one coupling in the band; by the K7 constraint
(row 1189 table) a hand proof of it must be quantitative at order-one coupling. So the carry does not make the seed
easier; it makes the crux a single finite statement. I have no route to the seed that is not on file, and by
`parts/gap.md` (row 998 9.5) another blind screen is waste. I do not attack the seed.

**The item.** The open inputs of the one-cutoff carry on the pin route after row 1268 (8.2 there) are: (U) the
test-cube size; the readings (E0)-(E6) against Balaban's CMP 116 (not on this machine; Project Euclid bot check);
(H2)-(H3) of row 1267; the 9.1 hypothesis (e) `9.1:prop-blind-site-expansions` (outstanding in the account; it
reads CMP 116); (DET)'s inputs. Only (U) and (H2)-(H3) can be worked here without CMP 116. Rule 0a: (U) is named
only in row 1268 (author, this worker's thread); no queued row owns it (grep of FINISH.md for "(U)" at this pin).

**Item: (U) of row 1268 (7.7).** In the account the test-cube size is R_k = least power of L at least
(log g_k^(-2))^r (CA-I L45885-45912, from Balaban CMP 119 (2.5)); EM's age gate reads R at min_{i <= j} theta_i
(EM L364-370). The frozen-scaffold frame phi and the run's own frame psi have thresholds that differ by a relative
amount theta^(-1/2) polylog, so their R can differ near the jumps of R. Theorem FCT' of row 1268 assumes both frames
use one family of test cubes at every step.

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1256, 1260, 1267, 1268). Success: (U)
leaves the carry's input list, so (FC-1) along the pin runs rests only on the supplier's expansion (E0)-(E6), (TH),
(H2)-(H3). Failure: a use of R in the account's step that is two-sided at the precision theta^(-1/2), so that the
frames cannot share test cubes; then the comparison needs a cube-change estimate, which reads CMP 116.

**Plan.** Step 2: read the account's conditions on R (Definition 4.14:def-block-size-conditions, CA-I L45636-45915)
and the places where the one-step theorem and EM read R. Step 3: state a common test-cube sequence and prove that it
meets every condition in both frames. Step 4: what changes in Theorem FCT' and the carry. Step 5: labels, RESULT.

## Step 2. Where the test-cube size enters the unmarked total (READ; written 2026-11-20T14:01Z by date -u)

Sources: Sussman and Alpoge's complete account at 31a47c543775 (CA-I) and YM4_EM at c7fef8b21b58 (credit Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text; the construction is Balaban's), fetched by URL into
a scratch folder outside the repository; Balaban, CMP 119 (1988) 243-285, the owner's copy, read as page images of
pp. 246-247 and 265-267. I:n and EM:n are TeX lines.

**2.1 The account's cube size is a function of the run's running minimum.** `4.15:not-cube-sizes` (I:49745-49770):
x-check_j := min_(i<=j) x_i, R-check_j is the least power L^b with L^b >= (log x-check_j)^r, "Wherever Balaban's size
parameter R_j occurs, we read R_j := R-check_j", and the waiting depth is N_k := R-check_k. Stage 9 of the order of
choice (I:1702-1705) says the same for every level-indexed auxiliary quantity: it is "determined at each level from
x_0, ..., x_k, evaluated at x-check_k". The frozen scaffold sets every coupling-dependent choice at depth r to its value
at theta_r = X + c_0 r (III:70175-70230, read in row 1260 2.1). So on the pin run the own-threshold frame uses
R(x-check_k) and the frozen frame uses R(theta_(n-k)). Since theta_(n-i) decreases in i and |x_i - theta_(n-i)| is at
most of order theta_(n-i)^(1/2) (log theta_(n-i))^(p_0) (row 1260 2.1), |x-check_k - theta_(n-k)| is at most of the same
order at theta_(n-k).

**2.2 In EM the cube size enters the unmarked chain only through the cut.** The age gate M R-check_j <= L^(m+1-j)
(EM:364-372, EM:525-531) selects aged remainders for the full list only: "A family that fails this age test stays
outside the regular list. The unmarked list uses only its own regular outputs, from levels 1, ..., k" (EM:533-536).
The other uses of R-check in EM are one-sided floors (torus periods P_i >= 2 L^11 M R-check_i, EM:724-732; the size
condition EM:476-481), which each frame meets with its own R. The unmarked total is formed from "the fixed all-small-
field kernel ... It uses the given fibre density, gauge weight and fluctuation cut" (EM:544-547), the cut being "a fixed
Borel restriction in the real free variables" (EM:614-616). The account's cut is Balaban's (CA-I 4.35 (C)(b),
I:157457-157600, read in row 1267 4.1: "the decompositions of unity of [B-CMP119, Section 3]"). The waiting depth
N_k = R-check_k, the index k_1 and the localization domains S_i (I:56700-56735) belong to the R-operations on
large-field regions, which the all-small-field kernel does not contain.

**2.3 Balaban's all-small-field tests are cube tests with cube-dependent references.** CMP 119 (3.2), p. 265: the
test on each L^2 M_2 R_(k+1)-cube box' of the partition is sup over p in box'~ of |U_(k+1,box')(dp) - 1| <
eps_(k+1) (L^(-1) eta)^2, where U_(k+1,box') is a configuration built from the new block field on box'~4 (its form at
the first step is CMP 119 (1.2), p. 246: U_(1,box')(V) = U(B_1(box'~4), M(Q_1^(s*) V)), built on a minimal determining
set). CMP 119 (3.3), p. 265: the test on each such cube is sup over bonds b in (box'~2)^(k)* of
|V_k(b) (V^(k)_box'(b))^(-1) - 1| < 2 delta_k, with the cube reference V^(k)_box' = M^k(U_(k+1,box')) (3.4). With
P_(k+1) and Q_(k+1) empty, the all-small-field cut is the product of these two tests over all cubes of the
L^2 M_2 R_(k+1) partition (and of the soft axial truncation). So the cut depends on the cube size twice: through the
partition and through the references. Row 1268 7.7 found this; it is confirmed here.

**2.4 Balaban's own comparison of references across cubes (the model for what is needed).** CMP 119 (3.6)-(3.9),
pp. 266: to show that the previous step's tests chi_k(box) are implied on Omega~_(k+1), Balaban compares the old cube
reference U_(k,box) with the new cube reference U_(k+1,box') for box inside box', writes their ratio through a field
H_(k,box) and bounds it, by "the exponential decay property (190) [15]" (CMP 102), as
|H_(k,box)| <= B_3 (4 delta_k + exp(-delta 2 M_2 R_k) 30 d^2 L^2 B_3 (1 + beta_0) eps_k) < eps_k/10 on box~ (3.7).
So a test read on one cube's reference is controlled by the test read on a containing cube's reference, with a constant
that does not depend on the cube sizes, up to a boundary-layer term suppressed by exp(-c R). CMP 119 (3.13),
p. 267: every cube reference is within (4dL)^2 (1 + beta_0) B_3 eps_k of the global minimizer V^(k) on box'~.

**2.5 Consequence (READ, with the arithmetic of 3.1 below).** (U) of row 1268 is a real condition: in the windows where
R(x-check_k) differs from R(theta_(n-k)) the two frames' all-small-field cuts are products over different partitions,
with different reference configurations. Outside the windows the two frames use one partition and one family of
references, and (U) holds.

## Step 3. The windows, and a sandwich comparison that removes (U) (written 2026-11-20T14:05Z by date -u)

Notation as in rows 1260, 1267, 1268. Pin run of length n; level k; frozen entry phi_k := theta_(n-k) = X + c_0 (n - k);
own entry y_k := x-check_k. Drift hypothesis (DR), from row 1260 2.1 (III:69015-69017): |y_k - phi_k| <= D(phi_k) with
D(y) := C_D y^(1/2) (log y)^(p_0), for every level k up to first passage. R(y) := least L^b (b >= 0) with
L^b >= (log y)^r; jump points Y_b := exp(L^(b/r)), so R(y) = L^b exactly on (Y_(b-1), Y_b].

**3.1 Lemma W (the windows; PROVED, elementary).** Let X be so large that D(y) <= y/2 for y >= X/2, and
D(2 Y_b) < min(Y_b - Y_(b-1), Y_(b+1) - Y_b) for every b with Y_b >= X/2. (D is increasing on y > 1.) Let W be the set
of levels k with R(phi_k) != R(y_k). Then:
(a) at each k in W exactly one jump point Y_b lies in the closed interval between phi_k and y_k, and
R(phi_k)/R(y_k) is L or 1/L;
(b) for each b, the number of k in W whose jump point is Y_b is at most 2 D(2 Y_b)/c_0 + 1;
(c) outside W the two frames read the same cube size, so (U) of row 1268 holds there.
*Proof.* Both entries are at least X/2 (phi_k >= X and y_k >= phi_k - D(phi_k) >= phi_k/2). R(phi_k) != R(y_k) means
that some Y_b lies in [min(phi_k, y_k), max(phi_k, y_k)), so Y_b >= X/2. If phi_k >= Y_b then
phi_k - Y_b <= D(phi_k) <= phi_k/2, so phi_k <= 2 Y_b; if phi_k < Y_b this is clear. Hence the interval has length at
most D(phi_k) <= D(2 Y_b) < min(Y_b - Y_(b-1), Y_(b+1) - Y_b), so it contains no other jump point, and R changes by
one factor L across it: (a).
For (b), phi_k lies in [Y_b - D(2 Y_b), Y_b + D(2 Y_b)], and the values phi_k = X + c_0 (n - k) are distinct and spaced
by c_0. (c) is the definition of W with 2.2: the cube size is the only frame dependence of the unmarked total that
Theorem FCT' does not already treat. QED
The condition on X holds for X large because Y_(b+1) - Y_b >= Y_b (exp((L^(1/r) - 1) L^(b/r)) - 1) grows faster than
any power of Y_b, while D(2 Y_b) is of order Y_b^(1/2) polylog.

**3.2 Proposition W2 (the envelope route fails in the windows; PROVED, arithmetic).** At a window level the only
frame-by-frame bound on record is the envelope |f_(k+1)| <= C theta_k^(-1/2) (log theta_k)^(p_0) (EM:1365, row 1267 1.2),
which gives eta_k <= 2 C theta_k^(-1/2) (log theta_k)^(p_0). By Lemma W (b) the windows can hold up to about
2 D(2 Y_b)/c_0 levels each, so this bound sums to order sum_b (log Y_b)^(2 p_0) = sum_b L^(2 p_0 b / r) over the jump
points between X and theta_n, which grows like (log theta_n)^(2 p_0), that is like (log n)^(2 p_0): not bounded in n.
By contrast any window bound eta_k <= kappa(theta_k) with sum_b D(2 Y_b) kappa(Y_b/2) finite (for example
kappa(y) <= y^(-1/2 - delta) for some delta > 0) gives a window total that is bounded uniformly in n and tends to 0 as X
grows, since Y_b grows doubly exponentially in b. So the windows need a structural comparison of the two cube
families, not a size bound. *Proof.* Sum the two displayed bounds over b with Lemma W (b). QED

**3.3 The comparison hypothesis (U-dom) (ARGUED; a statement about Balaban's cube references, stated here).** Fix a
level k in W. Let the frame-psi family a be its cube tests (2.3) on the partition of side L^2 M_2 R(y_k) (units v,
Borel test values N_v >= 0, thresholds T_v), and the frame-phi family c be its cube tests on the partition of side
L^2 M_2 R(phi_k), composed with the dilation Psi_c of row 1268 7.3 and read in frame psi's presentation (units w, test
values N'_w, thresholds T'_w); both include the bond tests of the soft axial truncation (row 1268 6.1-6.3). The two
partitions are aligned (CA-I I:56744-56746; CMP 119 p. 265, "the partition is compatible with all the other
partitions"), so each cube of one is a union of L^4 cubes of the other. For a unit w of c let its shadow sigma(w) be the
set of units of a that meet w enlarged by four layers of L M R_max-cubes, R_max := max(R(phi_k), R(y_k)) (the
operation ~ of CMP 119 is formed with L M R-cubes; test regions are box'~ and box'~2, data regions box'~4). **(U-dom):** there is Delta_k >= 0 with
Delta_k <= T_v/4 and Delta_k <= T'_w/4 for all v, w, such that on the integration domain of frame psi's kernel
- (D1) N'_w >= T'_w implies N_v >= T_v - Delta_k for some v in sigma(w);
- (D2) N_v >= T_v + Delta_k implies N'_w >= T'_w for some w with v in sigma(w).
Why it should hold (ARGUED, not proved): at the same step the two cube references are built from the same block field
V_(k+1) on two nested data regions (CMP 119 (1.2), (3.4)); on the test region of the smaller cube both lie two layers of
cubes inside their data regions, so by the exponential decay property that Balaban uses for exactly this kind of
comparison (CMP 119 (3.7), citing CMP 102 (190); and (3.13)) they differ there by at most
C exp(-c L M R_min) eps_k, R_min = min(R(phi_k), R(y_k)) >= (log theta_k)^r / L, which is below any fixed fraction of
delta_k = (A_1/A_0) eps_k once theta_k exceeds a floor. The threshold change T'/T = 1 + O(theta_k^(-1/2) polylog) and
the dilation Psi_c (it moves the axial-gauge deviation by the factor c = 1 + O(theta_k^(-1/2) polylog), hence a test
value by O(theta_k^(-1/2) polylog) eps_k) add terms of the same small size. So Delta_k = o(T) as theta_k grows. What a
proof needs: the precise decay estimate for the minimal configurations of CMP 119 (1.2), (3.4) on two nested regions
with one block field, in the axial gauge of (3.10), on the all-small-field domain; Balaban's (3.6)-(3.9) is the
same argument for two consecutive scales. A point a checker should keep apart: Balaban's (3.13) compares a cube
reference with the global minimizer V^(k), which carries the constraints of all earlier scales on the domains Gamma_j
(CMP 119 (3.10)); that difference is O(eps_k) for an intrinsic reason and is much larger than delta_k when A_0 >> A_1.
(U-dom) compares two cube references built by one rule from one block field, which differ only through the size of
the data region; the derivative bound CMP 102 (190) (p. 308: the derivative of the background map in the datum at y'
decays like exp(-delta_0 d(y, y')/8)) is the tool for that boundary effect. (U-dom) with Delta of order eps_k, from
(3.13) alone, would NOT suffice: the shifted thresholds T - Delta would be negative.

**3.4 Lemma SW (sandwich comparison of two cuts; PROVED, given its hypotheses).** Setting of row 1268 3.1 and 7.4, with
one base expansion: frame psi's kernel in its own presentation, family a, base cut chi_+ := prod_v 1[N_v < T_v + Delta]
(Delta := Delta_k). Let chi^1, chi^2 be Borel functions with
    chi^i = chi_+ prod_(e in E_i) (1 + m^i_e)   on the integration domain   (i = 1, 2),                    (3.1)
where each m^i_e is Borel, depends only on the field in a region covered by a set sigma(e) of at most m_sig units of a,
each unit of a lies in at most m'_sig of the sets sigma(e), e in E_i, and
    |m^i_e| <= sum_(v in sigma(e)) 1[N_v >= T_v - Delta].                                                   (3.2)
Put T_- := min_v (T_v - Delta) and tau := m_sig e^(c_A) exp(-(1/2) gamma_2 T_-^2 / m'_sig). Hypothesis (E+): the
supplier's expansion of the base integral int K chi_+ e^Phi satisfies (E1)-(E4) of row 1268 (with (E2') on the base
domain and the one-term bound (E3) with Gaussian absorption at the units of a), and stays convergent with margin eps,
majorant Bbar and pointed norm Nbar when one more type of Mayer element is added, each element of activity at most tau,
supported on the units sigma(e) (the form of row 1268's (E6)). Then for every Y
    |Phi^1(Y) - Phi^2(Y)| <= (2 tau/eps) Bbar(Y),
and the pointed difference of the two localized logarithms has EM norm at most (2 tau/eps) Nbar.
*Proof.* Expand prod_e (1 + m^i_e) = sum over subsets E of E_i of prod_(e in E) m^i_e, and insert it in the base
expansion as new Mayer elements; a datum t of the base expansion with element set E has integrand G_t prod_(e in E)
m^i_e. By (3.2) and idempotence of indicators,
    |prod_(e in E) m^i_e| <= sum_s prod_(v in s(E)) 1[N_v >= T_v - Delta],
the sum over selections s with s(e) in sigma(e), at most m_sig^|E| of them, and |s(E)| >= |E|/m'_sig. For each
selection, prod_(v in s(E)) 1[N_v >= T_v - Delta] <= exp(-(1/2) gamma_2 T_-^2 |s(E)|) prod_(v in s(E))
e^((1/2) gamma_2 N_v^2). The one-term bound (E3) absorbs the Gaussian factors at cost e^(c_A |s(E)|) <= e^(c_A |E|).
So the datum is bounded by tau^|E| times the bound of the same datum without the elements. Hence
|F^i(X) - F^+(X)| <= tau Fbar(X) and |F^i(X)|, |F^+(X)| <= Fbar(X), where F^+ is the base activity and Fbar counts
data with element sets E with the weight tau^(max(|E| - 1, 0)). Lemma TL* of row 1268 (7.4) with lambda = tau gives
|Phi^i - Phi^+| <= (tau/eps) Bbar for i = 1, 2, and the triangle inequality gives the claim; the same for the pointed
norms. QED

**3.5 Corollary U (the two frames' cuts in sandwich form; PROVED GIVEN (U-dom)).** At a window level, with chi^2 :=
frame psi's cut prod_v 1[N_v < T_v] and chi^1 := frame phi's cut prod_w 1[N'_w < T'_w] (in frame psi's presentation),
(3.1)-(3.2) hold with E_2 = units of a, m^2_v := -1[T_v <= N_v < T_v + Delta], sigma(v) = {v}; and E_1 = units of c,
m^1_w := -1[N'_w >= T'_w], sigma(w) as in 3.3. m_sig and m'_sig are at most m_U := (L + 2 + 8 M/M_2)^4, a constant
fixed with d, L, M_1, M (Definition 4.14:def-block-size-conditions).
*Proof.* chi^2 = chi_+ prod_v (1 - 1[T_v <= N_v < T_v + Delta]) is an identity of indicators, and |m^2_v| <=
1[N_v >= T_v - Delta]. For chi^1: by (D2), if all N'_w < T'_w then all N_v < T_v + Delta, so chi^1 <= chi_+ and
chi^1 = chi_+ chi^1 = chi_+ prod_w (1 - 1[N'_w >= T'_w]); by (D1), 1[N'_w >= T'_w] <= sum_(v in sigma(w))
1[N_v >= T_v - Delta]. The counts: the region of a shadow has side at most L^2 M_2 R_max + 8 L M R_max, and the
units counted have side at least L^2 M_2 R_min with R_max = L R_min (Lemma W (a)); so it meets at most
((L^2 M_2 R_max + 8 L M R_max)/(L^2 M_2 R_min) + 2)^4 = m_U of them. Each unit lies in at most m_U shadows by the same
count. QED

**3.6 Theorem U (PROVED GIVEN (U-dom) at the window levels, (E+), and the hypotheses of row 1268's Theorem FCT' other
than (U)).** Along the pin runs, (FC-1) of row 1267 holds at every level, with
    nu_k <= K_1 exp(-(1/2) gamma_2 a'^2 (log theta_k)^(2 p_0)) + K_2 theta_k^(-3/2) (log theta_k)^(5 p_0)    (k not in W),
    nu_k <= K_3 exp(-(1/8) gamma_2 a^2 m_U^(-1) (log theta_k)^(2 p_0)) + K_2 theta_k^(-3/2) (log theta_k)^(5 p_0)   (k in W),
with K_3 := (2/eps) C_post Nbar_+ m_U e^(c_A); so
    sum_(k<n) nu_k <= K_1 S'(X) + K_3 S_U(X) + K_2 S''(X),
where S_U is the S of row 1268's Lemma S with alpha = gamma_2 a^2 / (8 m_U); all three sums are finite,
independent of n, and tend to 0 as X tends to infinity. Hence (U) is not needed for (FC), and with rows 1260 and 1267
the scaffold comparison at the pins holds with a bounded modulus, given the remaining inputs.
*Proof.* Outside W, Theorem FCT' applies as stated (Lemma W (c)). At k in W, write the difference of the two unmarked
totals as row 1268 7.5 does, cut part plus vertex part. The vertex part does not read the cube size (the soft gauge
weight lives on the L-blocks, CMP 119 (1.5), p. 247), so its bound K_2 theta^(-3/2) polylog stands. For the cut part
(E^(phi,rs) against E^(mix) in row 1268 7.5; the base expansion of Lemma SW is that of E^(mix), its vertex elements of
(E6) included), Corollary U puts the two cuts in the form of Lemma SW, with T_- >= (3/4) T_lo >= (3/4) a (log theta_k)^(p_0) by
Delta <= T/4 and (TH) of row 1268; so tau <= m_U e^(c_A) exp(-(9/32) gamma_2 a^2 (log theta_k)^(2 p_0)/m_U),
which is below the displayed exponential (9/32 > 1/8). The post-processing (E5) adds the factor C_post. Summation: the
window terms are a subfamily of the levels, and row 1268's Lemma S bounds the sum over all levels of
exp(-alpha (log theta_k)^(2 p_0)) for any alpha > 0 (with its floor y_* depending on alpha). QED

**3.7 What changed (PROVED from 3.1-3.6).** Row 1268's open input (U) ("fails in windows around the jumps of R_k") is
replaced by (U-dom) at the window levels and (E+), the same kind of supplier reading as (E0)-(E6). The windows are real
(Lemma W and 2.1-2.3: the account's own run reads its running minimum, the scaffold reads theta_r) and a size bound does
not close them (Proposition W2). The extra cost is only a smaller constant in the Gaussian exponent.

**3.8 Step 3b: can (U-dom) be proved here? (READ and ARGUED; written 2026-11-20T14:08Z by date -u).** CMP 102 (190), p. 308
(page image), is a pointwise derivative bound for Balaban's background map: the derivative of the background at x in
Delta(y) with respect to the datum B at y' is at most O(1) (L^j eta)^(-1-d) exp(-delta_0 d(y, y')/8), with the same
form for its covariant derivatives, for y in Lambda_j, y' in Lambda_(j'). A proof of (U-dom) would interpolate the
data region of the smaller cube's reference out to that of the larger one and integrate this derivative along the
interpolation; that needs the minimal configuration of CMP 119 (1.2), (3.4) to exist with uniform constants along the
interpolating family of determining sets, which is part of Balaban's variational theory (CMP 95, 96, 99, 102) and is
not rebuilt here. (U-dom) stays ARGUED. It is a statement of the same kind as Balaban's own (3.6)-(3.9) and as the
readings (E0)-(E6) of row 1268, and the account would have to state it.
