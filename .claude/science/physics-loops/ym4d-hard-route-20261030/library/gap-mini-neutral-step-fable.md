lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T17:12Z

# gap-mini-neutral-step-fable (queue row 1353)

Worker file for queue row 1353 of `FINISH.md`, branch `claude/ym4d-hard-route`, pinned at commit `33f734aed`.
Started 2026-11-21T05:12Z (from `date -u`). Written section by section; each section says what is PROVED, ARGUED, GUIDE or OPEN.

## 0. Status log

- 2026-11-21T05:12Z: file created; reading the row, `GOAL.md`, the rule sections of `FINISH.md`, `parts/gap.md`, rows 1342, 1349, 1351, 1352.
- 05:13Z: read the row (L1434 of `FINISH.md`), `GOAL.md`, the rule sections of `FINISH.md` (L52-73, L320-350), and the RESULT lines of rows 1332, 1335, 1340, 1342, 1349, 1351. Next: `library/gap-blockstep4-astra62.md` in full, then Proposition CH.
- 05:13Z: read `library/gap-blockstep4-astra62.md` (row 1351) in full, L1-355. Its own last section states the open step: carry the short factors (the remaining Wilson plaquettes and the window quotients g_(i,H)) into the end class (23)-(24); its (16) and (25) are lower bounds on interactions that a scalar approximation loses. Next: Proposition CH (row 1332, check 1335), the statement (N-phys) (row 1161), Lemma TP (row 1342), the cores of row 1348.
- 05:35Z: registry grep run (Section 1); Sections 1 and 2 written.
- 06:00Z: further matches found while working (row 1145: anisotropic seed, near-Haar straight transports (3), unprojected transfer (17); rows 1060-1061: frozen two-skeleton arrays) and added to Section 1; Sections 3 and 4 written.
- 06:02Z: Section 5 written (a second end class, with no centre coherence; proof by the deletion induction).
- 06:05Z: Section 6 written (the rank-one form of the target, the state of each route, what stays open).
- 06:08Z: every PROVED item re-read; three wordings corrected (3.3: the face modes beyond the one of (16) are a reading, not a bound; the cell statements are not written and their sufficiency is not proved; 4.2: the pairs with two shared eliminated columns are now covered). RESULT line written. No numeric run was made, so the numeric lock was not taken. Run window 05:12Z to 06:10Z, both from `date -u`.

## 1. Repo search and inputs

Searched before deriving (rule 0a and "Repo first"): `library/open-core.md`, every `library/gap-*.md`,
`library/prior/gap-*.md`, `parts/gap.md` and the `FINISH.md` rows, with `grep -c -i -F`, for the terms of each
candidate statement of this file. `library/open-core.md` has no line on (N-phys), on an end class or on a neutral
block step (0 hits for "N-phys", "end class", "chi-square", "gauged"; its 17 hits for "admission" are about the
hard-core part, not about this lane). Cross-branch search (main, PR 10114, 10133, 10134, 10141): not repeated here;
row 1351 ran it for the same statement on the same day (`gap-blockstep4-astra62.md` L3) and found no proof of the
block induction. I rely on that record and did not fetch the other branches.

Matches for the statements I considered, so that none of them is called new below:

| Candidate (my words) | On file | Verdict |
|---|---|---|
| The bond test of a product-reference class at a time cut is the seed itself (Hilbert-Schmidt distance to rank one = thermal sum) | Identity I1, `gap-compress-opus.md` L36-46 ("the thermal sum is a chi-square mutual information"); its 2.4 ("the partition tensor of one box is close to rank one"); Lemma MC, `gap-glue-max.md` (maximal correlation of slices) | on file; cited in Section 3, not re-proved |
| The centre sums may be taken at one fixed block side on the whole cutoff tail | row 1345, `gap-blockstep2-astra62.md` L61 and L103 ("One may even fix B = L^j once and for all") | on file |
| The neutral mass is a positive angular integral with the cube constraints opened | row 1351 (18)-(20), `gap-blockstep4-astra62.md` L232-265; row 1345 (9) | on file |
| The ordinary box blocking fails the bond test at every block side | row 1351 (16), L175-194 | on file |
| Freezing a sparse net of straight lines changes each mass by a factor near 1 (evaluate the joint density of the straight transports at the identity) | row 1145, `gap-solve2-astra62.md` (1)-(3) L17-38 (joint density between (1 - eta)^M and (1 + eta)^M; check row 1146) and (17) L213 (the unprojected transfer; the density is evaluated at the identity there) | on file for the time lines and, as a density bound, for coarse grids; not re-proved |
| A neutral gap for anisotropic couplings (temporal coupling free, spatial coupling small) | row 1145 RESULT (temporal beta at least 1, spatial coupling at most c/(1 + beta)) | on file |
| A model with rigid frames on a frozen skeleton | rows 1060-1061, `gap-wall-vectors-max.md` L140-142 (frozen two-skeleton arrays, a changed regularisation, not an identity for the Wilson masses) | on file as a proposal |
| A finite-size mixing condition gives a cluster expansion at that scale (Olivieri, Olivieri and Picco) | 35 lane files name Olivieri; the uniform-in-boundary form fails above about 1.01 (Proposition CA-FAIL, row 1072) | on file |

Inputs read for this row. In full: `library/gap-blockstep4-astra62.md` (row 1351, author gpt-6.2-astra; its check,
row 1352, was running when this row started, so every statement of row 1351 used below is "unchecked at this pin").
In part: `library/gap-shrink-box-fable.md` 5.3 and Section 6 (Proposition CH, row 1332; check row 1335);
`library/gap-seed-audit-fable.md` L77-207 (statements (N-phys), (G_ev-phys), Lemma TP, Theorem O; row 1342, check
row 1349); `parts/gap.md` L8-104; the RESULT lines of rows 1332, 1335, 1340-1351.

Credits. Tadeusz Balaban (the block renormalization method). Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text (the account, the trajectory, first-passage data). G. Mack and V. Petkova (the centre
split). G. 't Hooft (twists and flux sectors). K. Osterwalder and E. Seiler, M. Luscher (transfer operator,
reflection positivity). E. Olivieri and P. Picco (cluster expansion from a finite-size mixing condition). In this
lane: gpt-6.2-astra (rows 1341, 1345, 1348, 1351: the centre-sign block map, the cores, the strip elimination, the
neutral end class and bound (24)); Claude Fable 5.2 (rows 1332, 1340, 1342: Proposition CH, Theorem TL, the neutral
target); Claude Opus 5.5 (checks 1344, 1347, 1350; Identity I1 of `gap-compress-opus.md`).

## 2. The target, and how best to attack it

### 2.1 The statement (from row 1342, L93-94, and row 1351, L11-20)

(N-phys): there is an admissible physical side L such that for all late j: 4 divides n_j, n_j >= 2^70, and there is
an integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j; n_j^3) <= 1/2. Here s(u) = sum over a >= 1 of x_a^u is the
excited trace of the neutral sector (electric flux zero, magnetic twist zero) of the Wilson transfer operator on the
box n^3, in units of its vacuum eigenvalue. With Z_+(T) the mean of the partition function over the eight temporal
twists, 1 + s(u) <= Z_+(u)^2/Z_+(2u) (Lemma TP). So (N-phys) follows from D_+(u) := 2 log Z_+(u) - log Z_+(2u)
< log(3/2) at one such u, for all late j.

The row asks for a chain as in Proposition CH: sets C_0, ..., C_N of models that carry the two numbers Z_+(u),
Z_+(2u); maps that keep both numbers; (BASE): every late Wilson datum has a representative in C_0; (END): every
model of C_N has D_+ < log(3/2) with a margin. Row 1351 supplies one (END): a class of models with independent
link variables, small plaquette marks and coherent centre weights, with D_+ <= 8 v e^(-theta j_0), its (23)-(24).

### 2.2 What the chain formalism contains and what it does not (PROVED, by inspection of Proposition CH)

A map that keeps the two masses is not restricted in any other way by Proposition CH. So, for one datum d:

    there is a model in the end class of row 1351 with the two masses of d
    if and only if D_+(d) lies in the set of values of D_+ on that class.

The class contains the pure coherent centre models with weight ratio e^(-2J), J >= 3, and a free scalar per
plaquette. So a representative with the right two masses exists as soon as D_+(d) is a value that those models
take; the chain is then the one map "d goes to that model". Hence the formalism alone is never the proof: all
content is in maps that are LOCAL and EXPLICIT, so that membership of the image can be verified from bounds on the
input. This is known to rows 1332 ("the proof is one line") and 1351; I state it because it fixes what a block step
has to be: a local construction R together with a proof that R(C_k) lies in C_(k+1), where both classes are given
by bounds.

### 2.3 The three legs, with their state on file

- (E) END. On file: row 1345 (11)-(12), row 1351 (10)-(11), (15), (23)-(24). All of them are classes with a
  PRODUCT reference measure (independent variables on links, or on boxes and bonds) and small marks.
- (M) The middle leg. From first-passage data (effective inverse coupling above 5 by check 1331, with no upper
  value) through the band to couplings of order one, and from there into (E). On file: exact maps at every coupling
  (the 2^4 cube map of row 1341, the centre-sign map of row 1345, the strip elimination of row 1351), and
  obstructions to the simplest landings (rows 1345 (14), 1351 (13), (16), (25)). No class is carried by any of
  these maps. This is the open step.
- (U) Entry. The account's last-scale densities on the two neutral tori. Row 1345 avoids it for the centre part by
  working at the bare scale with a large block side. The angular part is not avoided by any row.

### 2.4 Choice of attack

The lane's lesson from rows 1188-1259 is that blind candidate lists return items already on file. So I start
from the open step that row 1351 names (L338, L351): carry the short factors into an end class with a product
reference. I ask first what any landing in such a class needs (Section 3), then try the two landings that the
exact maps on file suggest: more colours of the strip elimination (Section 4) and the opened angular integral
(20) (Section 5). Each section ends with its first failing step.

## 3. What a landing in a product-reference class is

All end classes on file have a product reference measure and small marks. This section reads the smallest mark
test, the bond test of row 1351 (15), on the Wilson law. The result is on file as an identity (Identity I1 of
`gap-compress-opus.md` L36-46, Claude Opus 5.5). I add the direction for an arbitrary reference law and constant,
because that is the form in which a class states its test.

### 3.1 Lemma BT (the bond test at a time cut is the seed; PROVED, elementary)

Let rho be a probability measure on a space X. Let b be a real symmetric kernel in L^2(rho x rho) whose integral
operator B on L^2(rho) is positive semi-definite. Let mu_0 >= mu_1 >= ... >= 0 be the eigenvalues of B.

- (a) For every integer t >= 2, the integral of b(A_1, A_2) b(A_2, A_3) ... b(A_t, A_1) against rho in each
  variable is Tr B^t = sum_i mu_i^t.
- (b) For every c > 0: norm(b/c - 1)^2 >= sum over i >= 1 of (mu_i/c)^2, and abs(mu_0/c - 1) <= norm(b/c - 1).
  The norm is that of L^2(rho x rho).
- (c) If eps := norm(b/c - 1) < 1, then sum over i >= 1 of (mu_i/mu_0)^2 <= eps^2/(1 - eps)^2. Hence
  Tr B^t / mu_0^t - 1 <= eps^2/(1 - eps)^2 for every t >= 2.
- (d) If mu_0 > mu_1 and the top eigenfunction psi_0 is positive almost everywhere, put rho' = psi_0^2 rho and
  b' = b/(mu_0 psi_0 x psi_0). Then the cyclic integrals of b' against rho' are Tr B^t / mu_0^t, and
  norm(b' - 1)^2 in L^2(rho' x rho') equals sum over i >= 1 of (mu_i/mu_0)^2 exactly.

Proof. (a) B is Hilbert-Schmidt. The trace of a product of t >= 2 Hilbert-Schmidt operators is the cyclic
integral of their kernels. (b) The kernel 1 is the kernel of the projection P_1 on the constants, which has rank
one, so norm(b/c - 1) is the Hilbert-Schmidt norm of X - P_1 with X = B/c. Write sigma_0 >= sigma_1 >= ... for
singular values; sigma_i(Y) is the least norm of Y on a closed subspace of codimension i. For Q of rank one,
sigma_(i+1)(X) <= sigma_i(X - Q): take a subspace S of codimension i on which X - Q has norm sigma_i(X - Q);
on the intersection of S with the kernel of Q, of codimension at most i + 1, X equals X - Q. Summing squares
over i >= 0 gives sum over i >= 1 of sigma_i(X)^2 <= the squared Hilbert-Schmidt norm of X - Q. Here
sigma_i(X) = mu_i/c because B >= 0. The second bound is abs(sigma_0(X) - sigma_0(P_1)) <= the operator norm of
X - P_1. (c) By (b), mu_0/c >= 1 - eps, so (mu_i/mu_0)^2 <= (mu_i/c)^2/(1 - eps)^2; and x^t <= x^2 for x in
[0, 1]. (d) The map g -> psi_0 g is unitary from L^2(rho') to L^2(rho), and it carries the operator with kernel
b' on L^2(rho') to B/mu_0. Its top eigenfunction is the constant 1 with eigenvalue 1, so the operator with
kernel b' - 1 has the eigenvalues mu_i/mu_0, i >= 1. QED

### 3.2 Corollary BT1 (PROVED GIVEN the transfer-operator facts of rows 667, 671 and 731, as quoted in row 1342 L159-168)

Fix the spatial box n^3 and an integer w >= 1. Let T be the Wilson transfer operator on L^2 of the slice
configurations (Haar measure), P_0 the mean of the eight centre translations, K_w the kernel of P_0 T^w. P_0
commutes with T, K_w is bounded, and P_0 T^w is positive semi-definite with the eigenvalues lambda_0^w x_a^w on the
neutral sector and 0 elsewhere. So Tr (P_0 T^w)^t = lambda_0^(wt) (1 + s(wt)), which is the neutral mass
Z_+(wt) of row 1342 in the normalization of the kernel.

Take any probability density r > 0 on the slices, the reference law rho = r x Haar, and the bond factor
b = K_w/(r x r)^(1/2). Then the cyclic integrals of b against rho are the neutral masses at the times wt, and the
operator with kernel b on L^2(rho) is unitarily equivalent to P_0 T^w (by g -> r^(1/2) g). Lemma BT gives:

- for every constant c and every p >= 2: if norm(b/c - 1) in L^p(rho x rho) is eps < 1, then
  s(2w) <= eps^2/(1 - eps)^2;
- the reference r = Omega^2 (Omega the vacuum vector, positive almost everywhere) with c = lambda_0^w has
  norm(b/c - 1)^2 = s(2w) in L^2, and no reference and constant do better than s(2w)^(1/2) (1 + s(2w)^(1/2))^(-1).

So, for a cut along time, the bond test of a product-reference class with tolerance eps holds if and only if,
up to the factor (1 - eps)^(-2), the neutral thermal sum at twice the bond length is at most eps^2. The bond test
is the neutral seed at the time 2w for the cross-section n^3. It is not a weaker statement.

### 3.3 Reading for presentations with boxes (ARGUED; one step is a GUIDE estimate)

- Row 1351 (16) shows that the bond between two adjacent boxes fails the test at every box side. In the terms of
  Lemma BT the reason is that the bond is a one-step kernel across the common face (w = 1). The test bounds the
  squared singular values after the first one, relative to it. For one step, the face mode that (16) uses has a
  relative coefficient (I_2/I_1)^4, above 0.025 in the band, against the tolerance 2^(-14). (16) is proved for
  that one mode; that the other face modes add to it is my reading, not a proved bound.
- To have a bond of length w between two parts, the parts must be separated by a corridor of width w. The
  corridor is a four-dimensional region. Its other faces touch other corridors. Its partition function, as a
  function of what surrounds it, is then the mark, and the marks of a tiling come in sixteen kinds (cells that
  are thin in a subset of the four directions). The smallness of each mark in L^p of a product reference is a
  statement of the kind of Corollary BT1 for an open cell: a seed for that cell, in the law of independent
  neighbours. Such statements are finite and in-law, and they are not suprema over boundary values. I did not
  write them, and I did not prove that a finite list of them suffices: the dependence of a corridor on one
  neighbour alone is of order one and has to go into that neighbour's reference law, and I did not carry that
  bookkeeping through the sixteen kinds.
- GUIDE (sizing; uses the measured masses recorded in `gap-trajtest-opus.md` L157, Teper hep-th/9812187: a m =
  1.216(23) at beta 2.3 and 0.51(3) at beta 2.6). The tolerance of row 1351 (15) is eps = 2^(-14). With
  s(2w) at least e^(-2 a m w), the test needs w >= (14 log 2)/(a m): about 8 lattice units at beta 2.3 and 19 at
  beta 2.6. A cell with corridors of that width and parts at least as wide holds more than 16^4 sites, that is
  more than 2.6 x 10^5 link variables at beta 2.3. Row 1341's exact enclosure covers an eight-link integral.
  So no finite statement of a product-reference landing at the window is within the budget of 10^15 exact
  operations by any method on file. This agrees with rows 1326, 1331 and 1340 (their sizings are for other
  statements).

Conclusion of this section (ARGUED from 3.1 to 3.3). An end class with a product reference does not lower the bar of the last step. The
map into it must prove, for every late datum, the seeds of the cells at the block scale. The chain of Proposition
CH then has the same content as the engine of the lane (Theorem S and its neutral forms, rows 697, 731, 1161): a
seed at one scale, carried by maps that are the identity on the model. The block maps on file add exact
bookkeeping. They do not add a contraction outside the engine's own domain.

## 4. More colours of the strip elimination

Row 1351 eliminates one colour: the links of one spatial direction whose tails have an even sum of the two
transverse spatial coordinates, in every time slice ((17), (21)-(23) there). I asked whether the same step can be
repeated on the remaining links, so that the short factors are removed colour by colour.

### 4.1 Lemma (count; PROVED, elementary)

After the first colour, of the six plaquettes per site exactly 5/2 contain an eliminated link and 7/2 do not.

Proof. Let the eliminated links have direction 1. A plaquette in the plane (0, 1) holds two links of direction 1,
at successive times of one column; both are eliminated or neither is; half of the columns are eliminated. A
plaquette in the plane (1, 2) or (1, 3) holds two links of direction 1 at transverse neighbours, which have
opposite parity, so exactly one is eliminated. The planes (0, 2), (0, 3), (2, 3) hold no link of direction 1.
The count is 1/2 + 1 + 1 = 5/2 per site. QED

So 58 percent of the plaquette factors remain as raw Wilson factors at the same coupling. The other 42 percent
are replaced by the window quotients g_(i,H), which row 1351 (25) shows are of order one.

### 4.2 Lemma (the first colour couples the columns of the second; PROVED)

Notation as in row 1351 L222-226. Unit quaternions; x . y is the dot product in R^4, so (1/2) tr(x y^(-1)) = x . y.
Take one eliminated column with the links x_i, i mod T. Freeze the temporal links at its two end sites and the
eight spatial connector links of its four spatial plaquettes to the identity, at every time. Let y^1_i, ..., y^4_i
be its four parallel neighbours at time i. Up to a factor that does not depend on the column, its integral is

    F(y) = integral of prod_i exp( beta x_i . x_(i+1) + beta x_i . Y_i ) prod_i dx_i,     Y_i = y^1_i + y^2_i + y^3_i + y^4_i.

Write 1, I, J, K for the quaternion units. Take the configuration y^1_i = 1, y^2_i = -1, y^3_i = I, y^4_i = -I for all times i, so Y = 0. Move
y^1 at the time i along a curve with velocity a (a vector orthogonal to y^1_i) and y^2 at the time j along a
curve with velocity b (orthogonal to y^2_j). Then, at this configuration,

    (d/d theta)(d/d phi) log F = beta^2 kappa_d (a . b),     d = j - i mod T,     kappa_d > 0,     kappa_0 = 1/4.

Here kappa_d is defined by E[x^mu_i x^nu_j] = kappa_d delta^(mu nu) for the periodic chain with the electric
kernels only.

Proof. log F is a function of the vectors Y_i. Its second derivative in (Y^mu_i, Y^nu_j) is beta^2 times the
covariance of x^mu_i and x^nu_j under the chain with weights exp(beta x_i . x_(i+1) + beta x_i . Y_i). At Y = 0
the chain is invariant under x_i -> g x_i h for all i, with g, h in SU(2). These maps are the rotations of R^4.
So the means vanish and the covariance is kappa_d delta^(mu nu). The two moved variables belong to different
neighbours, so no second derivative of Y enters, and the mixed derivative is beta^2 kappa_d (a . b). For d = 0,
the sum over mu of (x^mu_i)^2 is 1, so kappa_0 = 1/4. For general d, kappa_d = Tr(X C^d X C^(T-d))/Tr C^T, with X
the multiplication by x^1 and C the electric convolution operator. This is the squared Hilbert-Schmidt norm of
C^(d/2) X C^((T-d)/2) divided by Tr C^T. It is not zero, because C is injective with dense range (all its
multipliers I_(2j+1)(beta)/I_1(beta) are positive; outline (GL3) of Sussman and Alpoge, with Claude and Codex)
and X is not zero. The two terms of the trace in which one factor acts on the constants give kappa_d >= ((I_2/I_1)^d + (I_2/I_1)^(T-d))/(4 Tr C^T), with C normalized so that its top multiplier is 1. Take a = b = J, which is orthogonal to 1 and to -1; then a . b = 1. QED

Consequences (PROVED from the lemma by continuity, on an open set of the frozen links).

- The factor that one eliminated column leaves behind is not a product of functions of single neighbour columns.
  Two columns of the other parity that share an eliminated neighbour are coupled. The formula of the lemma holds
  at every configuration with Y = 0, for any two of the four neighbours, and two tangent spaces of the
  three-sphere always contain vectors a, b with a . b not zero. A pair at transverse distance 2 shares one
  eliminated column. A pair at distance sqrt(2) shares two; with the pair at 1 and I and the other two
  neighbours of each shared column at -1 and -I, both columns have Y = 0 and their two terms are equal and add.
  Every column of the other parity shares eliminated neighbours with eight others. So, given all links
  that are not of direction 1, the second colour of the same direction is one connected system in two transverse
  dimensions and time. It is not a family of independent chains, and (17) with the ratio R does not apply to it.
- The size at this configuration is beta^2/4 at equal times: 1.32 at beta = 2.3, against the bare coupling 2.3
  (arithmetic only). In the time distance d it is at least beta^2 (I_2/I_1)^d/(4 Tr C^T), so it has no fixed range.
- Row 1351 L214 and L228 say in words that the next colour is not covered. The lemma gives the first failing
  step with its size: it is the very next elimination, and the obstruction is of the order of the coupling.

### 4.3 What the strip route can and cannot remove (ARGUED)

A set of columns can be eliminated with a uniform ratio only if, given the rest, its columns are independent
chains, or form groups of k chains (ratio R^k, row 1351 L218). After the first colour this holds only for sparse
sets (no two columns sharing an eliminated neighbour), with a ratio that is already exp of order beta R, because
the window quotients have temporal range of order R. Each round is sparser and its ratio is an exponential of the
last. No finite number of rounds removes the connected three-dimensional net of separators that row 1351 L228
names. First failing step of this route: the second colour (Lemma 4.2).

## 5. A second end class, with no centre coherence (Theorem END-D)

Why. Every end class on file for general effective densities assumes coherent centre weights: the weight of a
plaquette with centre curvature 1 is small against the weight with curvature 0 (row 1345 (11); row 1351 (10),
(15), (23)). That fits presentations in which a centre bit is split off at fixed fine field. It does not fit a
chain whose coarse variables are SU(2)-valued block links with a nearly Haar law: there the two centre values of a
coarse plaquette have nearly equal weight. For such a chain the end class is the one below. On file for it are
only the Wilson plaquette weight at small coupling (Theorem 1 of `gap-seed-sc.md`, radius 1/12800) and the
Dobrushin-type ends (Theorem DOB of row 785; Lemma END-RAY of row 1340). The method here is the standard polymer
expansion in the form of the deletion induction (Dobrushin; Kotecky and Preiss), with the two-period bookkeeping
of row 1351 (11) and (24). Nothing in it is hard. It is PROVED here, by hand, unchecked.

### 5.1 The class

- Torus. Gamma_T = (Z/T) x (Z/m)^3 with T, m >= 4; v = T m^3 sites; pi: Gamma_2T -> Gamma_T reduces the time.
- Windows. A box is the image of x + prod_mu [0, r_mu] with 0 <= r_mu <= min(T, m) - 2 and not all r_mu = 0. The
  same bound, with the numbers T and m of the short torus, is used on Gamma_2T. So a box is embedded, a box of
  Gamma_2T projects injectively, and the boxes of Gamma_2T are exactly the lifts of the boxes of Gamma_T. Its window W is the set of
  links with both ends in the box; its size, written size(W), is the number of sites of the box. A window has at
  most 4 size(W) links.
- Variables. One variable V_l in SU(2) for each link, with Haar measure. (Any probability space with a
  measure-preserving involution in place of V -> -V serves as well.)
- Interaction. For each window W of Gamma_T a bounded measurable real function f_W of the variables of W, with
  the invariance (G): f_W does not change when, for a function sigma from the sites of the box to {1, -1}, each
  V_l of W is multiplied by sigma at its two ends. On Gamma_2T the interaction is the lift: f of a window is f of
  its projection.
- Twists. For i = 1, 2, 3 the stack S_i is the set of the plaquettes of the plane (0, i) at one fixed pair of
  coordinates (x_0, x_i). Every three-cube contains 0 or 2 plaquettes of S_i. For e in F_2^3, S_e is the sum mod 2
  of the S_i with e_i = 1. In a box there is a function tau from the links of its window to {1, -1} whose product
  around each plaquette of the box is -1 exactly on the plaquettes of S_e. (For one stack: tau = -1 on the links
  of direction i at the stack's coordinate x_i and at box times later than the stack's time, in the linear order
  of the box; tau = 1 everywhere if the box holds no plaquette of the stack. For several stacks take the product.) Two such functions differ by end signs sigma as in (G), because a closed lattice path in a box is
  a sum of plaquette boundaries. Put f^e_W(V) = f_W(tau V). By (G) it is well defined.
- Masses. Z^e = integral of prod_W (1 + f^e_W) against Haar, and Z_+ = (1/8) sum_e Z^e, on each of the two tori.
  For the Wilson plaquette weight, 1 + f_p = e^(beta q)/A(beta), Z^e is the partition function with the temporal
  twist e divided by A(beta)^(6v), and Z_+ is the neutral mass of rows 1342 and 1351 up to that factor, which
  cancels in D_+.
- Norm. For kappa in (0, 1]: N_kappa(f) = sup over links l of the sum over windows W containing l of
  e^(kappa size(W)) sup abs(f_W).

### 5.2 Theorem END-D (PROVED)

If N_kappa(f) <= kappa/32, then on both tori every Z^e is positive, and with j_0 = min(T, m) - 1,

    abs( 2 log Z_+(Gamma_T) - log Z_+(Gamma_2T) ) <= 4 v e^(-kappa j_0 / 4).

Proof. Fix a torus and a twist e, and write u(W) = sup abs(f_W).

Step 1 (polymers). Call two windows adjacent if they share a link. A polymer is a set gamma of windows that is
connected under adjacency; supp(gamma) is its set of links; size(gamma) is the sum of the sizes of its windows.
Its activity is zeta(gamma) = integral of prod over W in gamma of f^e_W. Expand prod_W (1 + f^e_W) into a sum over
sets of windows and split each set into its connected components. Components have disjoint link sets, so the
integral factors. Hence Z^e is the sum, over families of polymers with pairwise disjoint supports, of the product
of their activities. For a set D of links let Xi_D(s) be the same sum over families supported in D, with each
activity multiplied by s^size(gamma), s complex. It is a polynomial in s and Xi_D(0) = 1.

Step 2 (rooted sums). Put Phi(l) = sum over polymers gamma with l in supp(gamma) of
e^(kappa size(gamma)/2) prod over W in gamma of u(W). Then Phi(l) <= N_kappa(f) <= kappa/32. To see this, fix an
order of the windows. Root gamma at its first window containing l, and build a spanning tree by breadth-first
search, the parent of a window being the first window of the earlier layer adjacent to it. The tree determines
gamma. Let Phi_h(l) be the sum, over rooted trees of height at most h whose root contains l and in which the
children of a window are distinct windows adjacent to it, of the product of u(W) e^(kappa size(W)/2) over the
nodes. The children of W contribute at most the product over the windows W' adjacent to W of (1 + the sum of the
trees rooted at W'), which is at most exp of the sum over the links l' of W of Phi_h(l'). So

    Phi_(h+1)(l) <= sum over W containing l of u(W) e^(kappa size(W)/2) exp(4 size(W) sup Phi_h).

If sup Phi_h <= kappa/32, the exponent is at most kappa size(W)/2 + kappa size(W)/8, so Phi_(h+1)(l) <=
N_kappa(f) <= kappa/32. The same bound holds for Phi_0. Induction on h gives the claim.

Step 3 (deletion induction). Claim: for abs(s) <= e^(kappa/4), every D and every l in D, Xi_(D - l)(s) is not
zero and abs(Xi_D/Xi_(D - l) - 1) <= kappa/32. Induction on the number of links of D. A family in D either has no
polymer through l, or exactly one, gamma, and then the rest is supported in D - supp(gamma):

    Xi_D = Xi_(D - l) + sum over gamma through l in D of s^size(gamma) zeta(gamma) Xi_(D - supp(gamma)).

Remove the other links of supp(gamma) from D - l one at a time. There are fewer than 4 size(gamma) of them. By
the induction hypothesis each removal changes Xi by a factor of modulus at least 1 - kappa/32, so
abs(Xi_(D - supp(gamma))/Xi_(D - l)) <= (1 - kappa/32)^(-4 size(gamma)) <= e^(kappa size(gamma)/4). With
abs(s)^size(gamma) <= e^(kappa size(gamma)/4) and abs(zeta(gamma)) <= prod u(W), the sum is at most Phi(l) <=
kappa/32. This closes the induction. Consequently Xi(s), for the set of all links, has no zero in the disc; the
branch of log Xi(s) that vanishes at 0 is the sum of the principal logarithms of at most 4v ratios, each of
modulus at most kappa/31; so abs(log Xi(s)) <= kappa v/7 on the disc. In particular Xi(1) = Z^e is positive: Xi is
real on [0, 1], has no zero there, and Xi(0) = 1.

Step 4 (coefficients). Write log Xi(s) = sum over k >= 1 of c_k s^k. Cauchy's estimate on the disc gives
abs(c_k) <= (kappa v/7) e^(-kappa k/4). Give each window its own variable s_W for a moment. Then log Xi is a formal
power series in the s_W. A monomial whose set of windows splits into two parts with no adjacency between them has
coefficient zero, because Xi restricted to those windows is the product of the two restricted sums. So every
monomial has a connected set of windows, and after the substitution s_W = s^size(W) it has degree at least the
total size of that set. Its coefficient depends only on the adjacency pattern of its windows and on the
activities of the polymers inside it.

Step 5 (small supports do not see the twist or the period). Let a connected set of windows have total size at
most k <= min(T, m) - 2. The union of its boxes is a connected set of at most k sites, so its projection to each
coordinate is an arc with at most k points, and the union lies in one embedded box. Take the function tau of that
box for the twist e. Its restriction to each window of the set is a valid tau for that window. So, for every
polymer gamma inside the set, zeta(gamma) = integral of prod f_W(tau V) = integral of prod f_W(V), by the
invariance of Haar measure under V_l -> -V_l. The activity does not depend on e. On Gamma_2T the set projects
injectively to a set of the same kind on Gamma_T with the same adjacency pattern and the same activities, and
each such set of Gamma_T has exactly two lifts. Hence, for k < j_0: c_k is the same for all eight twists, and
c_k(Gamma_2T) = 2 c_k(Gamma_T).

Step 6 (tails). Put L = sum over k < j_0 of c_k(Gamma_T). By Steps 4 and 5, for every twist,
abs(log Z^e(Gamma_T) - L) <= (kappa v/7) e^(-kappa j_0/4)/(1 - e^(-kappa/4)) <= v e^(-kappa j_0/4), using
1 - e^(-x) >= 7x/8 for 0 <= x <= 1/4. In the same way abs(log Z^e(Gamma_2T) - 2L) <= 2 v e^(-kappa j_0/4). Z_+ is
a mean of eight positive numbers, so its logarithm obeys the same two bounds. Then
abs(2 log Z_+(Gamma_T) - log Z_+(Gamma_2T)) <= 2 v e^(-kappa j_0/4) + 2 v e^(-kappa j_0/4). QED

### 5.3 Remarks

- Margin (PROVED from 5.2). With T = floor(m/512) the bound is at most (m^4/128) e^(-kappa (m/512 - 2)/4). It is
  below any fixed positive number for m large. So every model of the class has D_+ < log(3/2) - eta on large
  coarse tori, uniformly in the class. This is an (END) in the sense of Proposition CH.
- Size of the class (arithmetic). For the Wilson plaquette weight a window has size 4 and a link lies in 6
  plaquettes, so N_kappa = 6 e^(4 kappa) max(e^beta/A(beta) - 1, 1 - e^(-beta)/A(beta)). With kappa = 1/4 the
  condition holds for beta up to about 4.7 x 10^(-4). The constants are not tuned. The point is the class, not
  the range: the interaction may have any range and any form, with the decay that N_kappa demands.
- The long windows of row 1351 (22) fit this class as they stand, if the short factors do (they read projective
  links and the twisted curvature in a tube, which is the invariance (G)).
- What the class does not contain: the Wilson weight at any coupling of order one. There sup abs(f_p) is 4.5 at
  beta = 2.3 (e^2.3/A(2.3) - 1 with A = 2 I_1(2.3)/2.3 = 1.824, my arithmetic). An end class is where a chain
  stops, not how it gets there.

## 6. The target in its largest end class, and where the row stops

### 6.1 Corollary BT2 (the neutral seed as a rank-one test with tolerance 2/5; PROVED from Lemma BT)

Norms are Hilbert-Schmidt norms on L^2 of the slice configurations of the box n^3. P_0 and T as in 3.2.

- (i) Let w >= 2 be an integer, phi a unit vector and c > 0 with norm(P_0 T^w/c - |phi><phi|) <= 2/5. Then
  s(2w) <= 4/9. So if, for an admissible L and all late j, such w_j <= n_j/1024, phi_j, c_j exist (with 4 | n_j
  and n_j >= 2^70), then (N-phys) holds with u_j = 2 w_j.
- (ii) Conversely, if s(u) <= 1/2, then w = 2u, phi = Omega and c = lambda_0^w give
  norm(P_0 T^w/c - |Omega><Omega|) = s(4u)^(1/2) <= 1/4.

Proof. (i) is Lemma BT (b), (c) with Q = |phi><phi| in place of P_1 (the proof uses only that Q has rank one and
largest singular value 1): the eigenvalues mu_i = lambda_0^w x_i^w of P_0 T^w obey sum over i >= 1 of
(mu_i/mu_0)^2 <= (2/5)^2/(3/5)^2 = 4/9, and that sum is s(2w). (ii) The operator P_0 T^w/lambda_0^w - |Omega><Omega|
has the eigenvalues x_i^w, i >= 1, so its squared norm is s(2w) = s(4u) <= s(u)^4 <= 1/16, because a sum of
positive terms obeys sum x_i^(4u) <= (sum x_i^u)^4. QED

Reading. Up to a factor 4 in the time, (N-phys) is the statement that the neutral transfer kernel over a time
w is within 2/5 of a rank-one kernel in Hilbert-Schmidt norm. This is an end class in the sense of Proposition
CH: the models are triples (space, reference law, positive symmetric bond kernel), the two masses are Tr B^t and
Tr B^(2t), and the class is "bond test with tolerance 2/5". By Lemma BT (c) every model of it has
D_+ = 2 log(1 + s_B(t)) - log(1 + s_B(2t)) <= 2 s_B(2) <= 8/9 for t >= 2, and D_+ <= 2 s_B(2)^2 <= 0.4 <
log(3/2) for t >= 4 (s_B(4) <= s_B(2)^2 <= 16/81; arithmetic). The Wilson datum is in the class, with the
identity as the map, exactly when the seed holds. Three consequences (ARGUED):

- The small tolerances of the classes on file (2^(-14), 2^(-30)) and their product structure in space serve the
  method of proof (a convergent expansion). The consumer needs neither. The consumer needs one in-law number
  below 2/5.
- The number is the distance of an operator on the slice space of the whole box n^3 from rank one. It is not
  local. A local proof must produce it from cells, and Section 3 says what each cell then has to satisfy.
- A proposed block step should be judged by one question: does it bound this distance for the late data. Exact
  maps alone leave the distance unchanged.

### 6.2 State of each route tried in this row

| Route | What was done here | First failing step |
|---|---|---|
| Land the short factors of row 1351 in its class (23)-(24) | Section 4: count (58 percent of the plaquette factors stay raw); Lemma 4.2 (the first colour couples the columns of the second at order beta^2/4) | the second colour; after it, a connected net in three dimensions |
| Any landing in a product-reference class at the window | Section 3: the bond test at a time cut is the seed (Lemma BT, Corollary BT1; on file as Identity I1); box tests are seeds of open cells (ARGUED); cells exceed 16^4 sites at beta 2.3 (GUIDE) | the seeds of the cells; no finite statement within the budget by a method on file |
| The opened angular integral, row 1351 (20) | read only: by (18)-(19) it equals the neutral mass up to a factor near 1, with the centre sums done; the angular measure is the Wilson measure itself | the same inequality as (N-phys) |
| A second end class for block-link chains | Theorem END-D (PROVED here, unchecked) | none (it is an end, not a step) |
| Ideas considered and found on file before any work (Section 1 table) | frozen line nets (row 1145), anisotropic seed (row 1145), frozen two-skeleton (rows 1060-1061), fixed block side on the tail (row 1345) | each is an exact or near-exact reformulation; none supplies a contraction |

### 6.3 What stays open, in one statement

(M-neutral), OPEN. For the Wilson trajectory there are an admissible L and, for all late j, an integer
w_j <= n_j/1024, a unit vector phi_j and c_j > 0 with norm(P_0 T_j^(w_j)/c_j - |phi_j><phi_j|) <= 2/5.

By 6.1 this is (N-phys) up to the factor 4 in the time. I found no proof and no reduction of it to a finite
statement within the computation budget. I prove no impossibility. Nothing in the chain is disproved.

What a proof must contain, from the record and this row (ARGUED; the tests are the lane's, lead rule W2):

- It must read first-passage data, or the cutoff tail directly. A statement at one coupling in the window does
  not reach the late data without a carry (row 1332, Theorem T).
- Its step must fail for compact U(1) at large coupling and for a product with a factor that has no seed. All
  exact maps on file (the 2^4 cube map, the centre-sign map, the strip elimination, the line freezing of row
  1145) hold for every compact group, so none of them can be the selective step.
- If it lands in a class with a product reference, it proves the seeds of the cells on the way (Section 3). So
  the landing is not a smaller statement than the seed. If it lands in the rank-one class of 6.1, the landing is
  the seed.

### 6.4 For the lead

- Row 1351's stability bound (24) and Theorem END-D are two ends for a chain. Neither is reached by a map on
  file from any datum of the trajectory, or from the Wilson weight at any coupling above the hand zone.
- I would not queue more colours of the strip elimination, or a landing of the ordinary box blocking: Lemma 4.2
  and row 1351 (16) are their first failing steps, and both are of the order of the coupling.
- A row that proposes a block step can be asked to state its claim as a bound on the rank-one distance of 6.1
  for late data. That is the weakest end test, it has an order-one tolerance, and it makes the selective input
  visible: an exact map does not change the distance.
- The check of this file can be short: Lemma BT, Corollaries BT1 and BT2 (one page of linear algebra plus the
  quoted transfer facts), Lemmas 4.1 and 4.2 (a count and one covariance), Theorem END-D (a standard expansion,
  six steps). The ARGUED and GUIDE items are marked and carry no weight in the chain.

RESULT: Row 1353 (Claude Fable 5.2 max, Mac mini Claude worker 1; author only, checked by no one; no numeric run; 05:12Z to 06:10Z by date -u). NOT solved: no block step carries the Wilson trajectory, or the Wilson weight at any coupling of order one, into a neutral end class; no impossibility is proved; nothing in the chain is disproved. PROVED here (by hand, unchecked): Lemma BT with Corollaries BT1 and BT2 (for a cut along time, the bond test of a product-reference class with tolerance eps holds if and only if, up to the factor (1 - eps)^(-2), the neutral thermal sum at twice the bond length is at most eps^2; so (N-phys) is, up to a factor 4 in the time, the statement that the neutral transfer kernel is within 2/5 of a rank-one kernel in Hilbert-Schmidt norm; this is Identity I1 of gap-compress-opus.md with an arbitrary reference law and constant); Lemma 4.1 (after the first colour of row 1351's strip elimination 7/2 of the 6 plaquettes per site stay raw Wilson factors) and Lemma 4.2 (the eliminated colour couples the columns of the second colour, at order beta^2/4 at equal times and with no fixed range in time), so the strip route stops at the second colour; Theorem END-D (a second end class, with no centre coherence: every interaction of SU(2) link variables with norm N_kappa at most kappa/32 has abs(2 log Z_+(T) - log Z_+(2T)) at most 4 v e^(-kappa j_0/4), j_0 = min(T, m) - 1). ARGUED: a landing in any product-reference class proves the seeds of its cells on the way, so it is not a smaller statement than the seed; exact maps leave the rank-one distance unchanged. GUIDE: such cells exceed 16^4 sites at beta 2.3. Found on file before work and not re-proved: frozen line nets and the anisotropic seed (row 1145), the fixed block side on the tail (row 1345), frozen two-skeleton arrays (rows 1060-1061). OPEN: (M-neutral) of 6.3, which is (N-phys) up to the choice of times; a selective step that reads first-passage data and fails for compact U(1); the mass gap. Output library/gap-mini-neutral-step-fable.md.
