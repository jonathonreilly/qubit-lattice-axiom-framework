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
  squared singular values after the first one, relative to it. For one step these are of order one in every face
  mode ((16) uses one mode).
- To have a bond of length w between two parts, the parts must be separated by a corridor of width w. The
  corridor is a four-dimensional region. Its other faces touch other corridors. Its partition function, as a
  function of what surrounds it, is then the mark, and the marks of a tiling come in sixteen kinds (cells that
  are thin in a subset of the four directions). The smallness of each mark in L^p of a product reference is a
  statement of the kind of Corollary BT1 for an open cell: a seed for that cell, in the law of independent
  neighbours. I did not write these sixteen statements. They are finite and in-law, and they are not suprema
  over boundary values.
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
  Two columns of the other parity that share an eliminated neighbour are coupled. Every column of the other
  parity shares eliminated neighbours with eight others (transverse distance 2 or sqrt(2)). So, given all links
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
