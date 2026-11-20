lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:35Z

# gap-mini-solve-ap-opus: queue row 1280

Started 2026-11-20T13:35Z (date -u). Pinned commit 220f8a48d, branch claude/ym4d-hard-route.
Task (row 1280): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the Jaffe-Witten sense; first consider how best to attack it, then do it.
Labels: PROVED, ARGUED, GUIDE, OPEN. Numerics guide only.

## Status

Step 0 (reading the folder rules and the earlier work): done 2026-11-20T13:48Z (date -u). Step 1 (choice of attack): done 2026-11-20T13:52Z. Step 2 (reading the account's test-cube rule): done 2026-11-20T14:01Z. Step 3 (statements and proofs): in progress.

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
