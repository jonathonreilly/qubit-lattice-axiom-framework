lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T13:36Z

# gap-mini-solve-i-fable (FINISH row 1199)

Research-stage working state. It grants no status. Nothing here is a public claim.

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 5e5082e7c.
No subagents. Checked by no one. File created 2026-11-20T01:36Z (`date -u`).

**The problem (row 1199).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the
sense of Jaffe and Witten. Labels used below: PROVED, ARGUED, GUIDE, OPEN.

## Plan (written before any reading of the lane files)

1. Step 0: read the lane's map (`parts/gap.md` method list and route registry, the RESULT lines of the
   mini-solve rows a to h, the two screening tables in `gap-mini-solve-b-fable.md` and
   `gap-mini-solve-e-fable.md` Step 2.1, `library/open-core.md`). Record where the lane stands.
2. Step 1: choose one named, unattempted item and say why it is not a repeat (rule 0a grep).
3. Steps 2+: attack that item, one stage per response, each stage appended here before the next.
4. End: one RESULT line.

## Step 0. Where the lane stands (statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L297-360, the row (L1280) and the RESULT lines of
rows 1179, 1180, 1184, 1187, 1188-1190, 1193-1195; `parts/gap.md` L1-104 and L213-322; the screening tables of
`gap-mini-solve-b-fable.md` (Step 2.1) and `gap-mini-solve-e-fable.md` (Step 2.1, Steps 5-6);
`gap-solve9-astra62.md` L120-175 (the form of (N-phys)).

1. **The target splits in two (Theorem BP, row 1179; check row 1183: main chain HOLDS AFTER CORRECTION).** The
   Jaffe-Witten gap clause follows from the continuum datum of the T0 chain (OPEN) and one lattice estimate,
   (N-phys) of row 1161 (OPEN): at one admissible physical side, uniformly in the cutoff, the periodic
   centre-neutral excited trace of the cube n^3 at a time u at most n/K is at most 1/2.
2. **(N-phys) in other words (rows 1180, 1184; check row 1187: main statements HOLD).** It is a neutral lattice
   gap at arbitrarily weak coupling with a bound of asymptotic-scaling type on the seed size. In thermal form:
   the cube at aspect K is on the confined side, with a dilute gas of neutral excitations.
3. **The wall (`parts/gap.md` L321-322).** One selective inequality at every scale between first passage and the
   seed size. Selective means false for a massless factor. Tests a tool must fail on: compact U(1) at weak
   coupling, the free photon, a product with a massless factor, Theorem D2, Lemma SHEET, Proposition V (the K7
   line in theorem form).
4. **Siblings.** Rows 1188-1190 and 1193-1195 (mini-solve a to f) each screened routes from first principles
   and found every one on the lane's map (about fifty candidates in all, by the counts in their RESULT lines).
   Each then worked one item to a first failing step. Rows 1197, 1198, 1200-1202 (g, h, j, k, l) have no
   result at this pin.
5. **Consequence for this row.** I do not screen route families again. Step 1 below records only the candidates
   that are not in those three tables, each with its grep. Then one item is attacked.

## Step 1. Literature probe, and what this session derived again (GUIDE; no statement here is a proof step)

### 1.1 Literature probe (arXiv API, two queries, sorted by date)

Queries: lattice gauge AND (mass gap OR confinement OR exponential decay) in math.PR and math-ph; and
(Yang-Mills OR gauge theory OR sigma model OR O(N)) AND (mass gap OR exponential decay OR confinement) in
math.PR, math-ph, hep-lat, hep-th. Newest entry seen: 2026-11-15. Result: no posted proof of a gap or of
confinement for a non-abelian lattice gauge theory beyond strong coupling. The entries that bear on the lane
are all on file already (file counts by `grep -l` over `library/gap-*.md`, `library/prior/*.md`, `FINISH.md`):
A. Mihajlovic, arXiv:2611.11534 (7 files); Yan Ru Pei, arXiv:2611.01532 (14); V. P. Nair, arXiv:2608.10133 (6);
S. Chatterjee, arXiv:2602.00436, confinement in three dimensions with a central U(1) (8). One sentence of Pei's
abstract states the lane's (SING) in two dimensions: "only odd observables transfer".

### 1.2 Candidates derived from the target in this session, each grepped before any work

Only candidates that are not in the tables of rows 1189, 1190 and 1194 are listed. Every one has a match.

| Candidate | Where it ends | Match on file |
|---|---|---|
| Fundamental Higgs with custodial SU(2), then hopping to zero (Fradkin and Shenker; Osterwalder and Seiler) | the rigid group acts trivially at zero hopping | Fradkin 18 files; row 1016 family 1 |
| Sharpness-type differential inequalities (Aizenman and Barsky; Duminil-Copin and Tassion) | need a monotone structure; none for SU(2) | sharpness 48 files, Aizenman 23 |
| Corner Hubbard-Stratonovich form: the links as an O(4) model in an annealed quaternion plaquette field, then loop soups | signs of the holonomy weights | Identity HS1, row 1016 3.3; `gap-mini-free-fable.md` 5.1 |
| Random surfaces from the multilinear action | crosscap signs (Frobenius-Schur indicator -1) | method 35; rows 737, 744, 878, 1127 |
| One-link noise acting on products of Wilson loops as a positive cone | the same sign: a reconnection inside one loop has coefficient -(1 - a_1)/2 | method 35 in other words; Mandelstam 3 files |
| Centre twist as a commutator of two removable colour twists; twist eaters | zero classical cost, so the twist cost is a logarithm of the coupling, not a stiffness | Fact T, `gap-crux-restate.md` Section 2; rows 731, 1181 |
| Spread vortex with a field-built colour axis | pays beta a^2 abs(D n)^2 with abs(D n)^2 at least c/beta on typical fields | row 1141 (2); row 1177 (14), (26), (33)-(35) |
| Thermal form: a lower bound of asymptotic-scaling type on the deconfinement coupling at temporal extent n/K | it is (N-phys) | rows 1180, 1184; "THERMAL", row 934 |
| Replica swap as a continuous family of field-dependent diagonal rotations (two replicas, sum and difference variables) | the collar cost is of mass form, proportional to sin^2 of the angle, so the sharp junction is optimal | Proposition J, checks 1121, 1123 (independent swaps); lead rule CL leaves coupled interpolations unbound |
| Durhuus-Frohlich layers with the posted two-dimensional O(4) theorem, for three dimensions first | two-sided backgrounds; worst case orders the layer | method 36, rows 1139, 1140 |
| Charged decay with a transitive rigid group gives neutral decay (a soft conversion) | false: van Enter and Shlosman weights; product examples | Proposition V; Example PROD; row 1115 2.3 |
| Stability of mixing of all observables under small perturbations (Dobrushin and Shlosman block criterion) | needs the unperturbed neutral mixing | `gap-face-stability.md` (FST-BD) |
| Mass inequalities from positivity of the measure (Weingarten; Vafa and Witten; West) | they bound the lightest mass from above only | Vafa 2 files; no consumer |

Three structural constraints that I derived again are on file: a proof at one coupling in the band reads a
number (K7, Proposition V); the gap is a property of the unique continuum object, so no model can refute a
(K-flow) tool (`parts/gap.md` test table, point 5); the neutral half is not implied by the charged half.

Verdict (GUIDE): a seventh plain-brief screening, about thirteen more candidates, no route off the lane's map.

## Step 2. Choice of attack

### 2.1 What is left to attack (ARGUED; the lane's reading, confirmed)

1. The only statement with a consumer on the path is (N-phys). Its engine (Theorem S, rows 697-699) carries a
   small neutral trace from one size to larger sizes. No engine creates the small trace: in a small box the
   neutral trace is large (a hot gluon gas), and it has to become small at about K correlation lengths.
2. The posted two-dimensional proofs create it in two halves. The charged half is the bracket gain. The neutral
   half is association of the untwisted linear-weight ferromagnet. The gauge theory has neither a rigid frame
   nor association. Rows 1011-1018, 1115-1123, 1188-1195 hold this with proofs of each obstruction.
3. So a row can do three things: a new mechanism for one half (none found here, Step 1.2), a bound with no
   association for a neutral response in a member of (SING) (the reopen condition of BR-2), or a decision on a
   side statement that an earlier row left open.

### 2.2 The item

I found no new mechanism. By rule 0a I do not attack the items of Step 1.2 again. I take the third kind, and
only one bounded item: the diamagnetic comparison for S^3 sheets with one-sided twists. Row 1194 5.1 records it
as "neither proved nor on file"; method 36 (rows 1139, 1140) settles the two-sided form by a counterexample.
What it can give: the answer to that recorded question, in three parts (unnormalized; normalized for charged
two-point functions; neutral covariances). What it cannot give: any step toward (N-phys). It is off the path,
and I say so before starting.

Pass and fail criteria of the guide run, written before the run: on four small graphs (triangle, square with
a diagonal, K_4, a five-site bridge graph), at four couplings, compare abs(E_g[n_x conj(n_y)]) under one-sided
twists g (a centre twist, two anticommuting twists, two Haar-random fields) with the untwisted E_1[<n_x, n_y>].
A violation is a difference above 6 standard errors and above 0.004. A run without a violation is no proof.

## Step 3. The item: diamagnetic comparison for S^3 sheets with one-sided twists

All statements are proved here by hand unless marked. Checked by no one. None is selective, and none is on
the path of (N-phys).

### 3.1 Setting

A finite multigraph with sites V and oriented bonds b = (x -> y), x not equal to y. Spins n_x are unit
quaternions, with the
uniform probability measure on S^3. <p, q> = Re(conj(p) q) is the inner product of R^4. A one-sided twist is a
unit quaternion g_b on each bond, acting on the left. For couplings J_b >= 0:

  Z_g(J) = integral of exp( sum_b J_b <n_x, g_b n_y> ),   <n_x, g_b n_y> = <n_x conj(n_y), g_b>.

E_g is the normalized expectation. The right rigid group n -> n k is exact for every g. A change of variables
n_x -> lambda_x n_x maps g_b to conj(lambda_x) g_b lambda_y, so only the holonomies of g matter. Q_g(x, y) :=
E_g[n_x conj(n_y)] is a quaternion; its norm is gauge invariant. The same setting with a general orthogonal
4 x 4 matrix R_b in place of left multiplication is the two-sided case.

### 3.2 Lemma U (the unnormalized comparison; PROVED; FOUND AGAIN, not new)

Match on file, found after writing the proof: Proposition LG of row 1016 (`gap-global-reform-max.md` L330-345),
the same loop series with its verdict "free energies only"; check row 1113 (`gap-descent-first-case-check-opus.md`
C3) holds a loop bound of the same kind. The method is
Brydges, Frohlich and Seiler's (RECALLED). I keep the short proof because Lemma E reads its notation.

For every finite multigraph, all J_b >= 0 and all orthogonal R_b: 0 < Z_R(J) <= Z_1(J). For all sites x, y and
indices i, k: abs( Z_R E_R[(n_x)_i (n_y)_k] ) <= Z_1 E_1[(n_x)_1 (n_y)_1] = (1/4) Z_1 E_1[<n_x, n_y>].

Proof. Expand each exponential in its power series. A term has m_b >= 0 copies of the factor <n_x, R_b n_y> =
sum over i, k of (n_x)_i (R_b)_(ik) (n_y)_k, with the coefficient prod_b J_b^(m_b)/m_b! > 0. At a site, the
integral of a monomial of even degree M in the components of n is c_M times the sum over all pairings of the
M index slots of the product of Kronecker deltas, with c_M = 1/E abs(G)^M > 0 for a standard Gaussian G in
R^4. (Write G = abs(G) n with abs(G) and n independent, and use Wick's rule for G.) Odd degrees give zero. A
choice of a pairing at every site joins the copies of the bonds into closed walks. The contraction of a
closed walk is the trace of the ordered product of the matrices R_b or their transposes along it. This trace
has absolute value at most 4, the value at R = 1. So every term at R is bounded in absolute value by the same
term at R = 1, and all terms at R = 1 are non-negative. Z_R > 0 is clear. With the two extra factors (n_x)_i
and (n_y)_k there is one open walk from x to y. Its contraction is one matrix entry of an orthogonal matrix,
of absolute value at most 1, the value of the (1,1) entry at R = 1. QED.

So D_g(J) := log Z_1(J) - log Z_g(J) >= 0. It vanishes when the bonds with J_b > 0 form a forest.

### 3.3 Lemma E (the normalized comparison is monotonicity of D; PROVED)

The following are equivalent, each quantified over all finite multigraphs, all J >= 0, all one-sided twists.
- (N1) abs(Q_g(x, y)) <= E_1[<n_x, n_y>] for all sites x, y.
- (M) D_g is non-decreasing in every coupling: E_g[<n_x, g_b n_y>] <= E_1[<n_x, n_y>] for every bond b = (x, y).

Proof. (N1) gives (M): E_g[<n_x, g_b n_y>] = <Q_g(x, y), g_b> <= abs(Q_g(x, y)). (M) gives (N1): if Q_g(x, y) is
not zero, add a bond from x to y with the twist Q_g/abs(Q_g) and coupling eps. Its bond energy has mean
abs(Q_g(x, y)) at eps = 0, and (M) at eps = 0 for the enlarged graph is (N1). QED.

Two cases are immediate. On two sites with two bonds, Z_h = Phi(abs(J_1 + J_2 h)) with Phi(r) = 2 I_1(r)/r, and
(M) holds because A = I_2/I_1 is increasing and abs(J_1 + J_2 h) <= J_1 + J_2. For twists that are pure gauge,
(N1) is an equality.

### 3.4 Lemma A (the abelian comparison; PROVED; the argument is Ginibre's, with shifted phases)

For the plane rotator on a finite multigraph, with weight exp( sum_b J_b cos(theta_x - theta_y - A_b) ), J_b >=
0 and any real A_b: abs( E_A[exp(i(theta_x - theta_y))] ) <= E_0[cos(theta_x - theta_y)].

Proof. Take an independent copy theta' with A = 0. Put Phi = (theta + theta')/2 and Psi = (theta' - theta)/2 at
each site, and X_b = X_x - X_y. For a real number a and a bond or pair o,
  cos(theta'_o) + cos(theta_o - a) = 2 cos(Phi_o - a/2) cos(-Psi_o - a/2),
  cos(theta'_o) - cos(theta_o - a) = 2 sin(Phi_o - a/2) sin(-Psi_o - a/2).
So the joint weight is exp( sum_b 2 J_b c_b(Phi) c_b(-Psi) ) with c_b(X) = cos(X_b - A_b/2), and the observable
cos(theta'_xy) + cos(theta_xy - alpha) or cos(theta'_xy) - cos(theta_xy - alpha) is 2 F(Phi) F(-Psi) with F a
cosine or a sine. Expand the exponential. Each term is a positive constant times G(Phi) G(-Psi), where G is a
product of such factors. Let kappa_x be the number of factors of G that contain site x. Then G(X + pi e_x) =
(-1)^(kappa_x) G(X), and G has period 2 pi in every X_x. The map (theta, theta') -> (Phi, Psi) has Jacobian
2^(-V) and a fundamental domain Phi_x in [0, 2 pi), Psi_x in [0, pi). If some kappa_x is odd, the integral over
Phi_x vanishes. If all kappa_x are even, G(-Psi) has period pi in every Psi_x, and the integral of the term is
(integral of G over [0, 2 pi)^V)^2 >= 0. So E_0 x E_A of both observables is non-negative, for every alpha. QED.

It does not give (N1) for S^3, even for twists in one maximal torus. In Hopf coordinates the two circles of a
spin have amplitudes r_1 and r_2 with r_1^2 + r_2^2 = 1. Lemma A compares the circles at fixed amplitudes. The
law of the amplitudes changes with the twist, and r_1 and r_2 are negatively dependent, which is the
obstruction of Lemma HF (row 1188) and Lemma D2 (row 1194).

### 3.5 Guide run for (N1) (GUIDE; a run cannot prove a bound)

Heat-bath sampling of the sheet, 4000 chains, 380 measured sweeps, under the numeric lock, free memory 57
percent (`memory_pressure`). Graphs: triangle, square with a diagonal, K_4, a five-site bridge graph. Couplings
0.6, 1.5, 3, 6 on every bond. Twists: a centre twist on one bond; two anticommuting twists; two Haar-random
fields. All site pairs: 400 comparisons of abs(Q_g(x, y)) with E_1[<n_x, n_y>]. Result by the criterion of Step
2.2: no violation. The largest difference was +0.0003 with a standard error of 0.003; every other difference
was negative. Sanity run of the same sampler on a two-sided twist (a hanging triangle whose holonomy is
n -> i n i^(-1), on a path of three sites, J = 3): the (1,1) entry 4 E[(n_x)_1 (n_y)_1] is 0.400 against 0.322
untwisted, so the sampler sees a failure of this size. The sum over the four entries is unchanged there.

So (N1) has no refutation on these graphs. It stays OPEN. First missing step of a proof: a comparison of two
normalized ratios. Lemma U bounds numerator and denominator separately; Ginibre's cone fails on S^3 (3.4).

### 3.6 Remark C (neutral covariances are not dominated; PROVED; elementary)

For the neutral half the analogue of (M), abs(Cov_g(E_b, E_b')) <= Cov_1(E_b, E_b') for bond energies, is false
in the smallest example. Two sites, two bonds, J_1 = J_2 = 2.
With psi(s) = log Phi(sqrt(s)) = s/8 - s^2/384 + ..., log Z_h = psi(J_1^2 + J_2^2 + 2 J_1 J_2 Re h), and the
covariance of the two bond energies is its mixed derivative. For h = -1 it is -2 psi'(0) = -1/4 exactly. For
h = 1 it is phi''(4) with phi = log Phi and phi'' = 1 - A^2 - 3A/R, A = I_2/I_1. From the series, I_2(4) >=
6.4215 and I_1(4) <= 9.76, so A(4) >= 0.65 and phi''(4) <= 0.09. So the twisted covariance is larger in
absolute value, and has the other sign. A frustrated loop shares its frustration among its bonds, and this
couples their energies. So (N-tw) of row 1194 cannot be reached by a domination principle. The neutral
response of a twisted sheet is carried by the frustration itself. This agrees with row 1194 5.3, way 2.

### 3.7 Exact quadrature on a cycle; the comparison reads the shape of the weight (GUIDE; one statement PROVED)

On a cycle the twist is one holonomy h, at angle theta from 1. Put w = n_x conj(n_y) for the chord (x, y). The
rest of the cycle gives w a zonal density P(<w, 1>), and the chord has the weight exp(J_c <w, h>). Then (M) for
the chord reads m(theta) <= m(0), with m(theta) the mean of <w, h>. A latitude sphere of S^3 has a uniform
height coordinate (Archimedes), so m(theta) is a two-dimensional integral. Criterion written first: a violation
is m(theta) - m(0) > 1e-9. Runs under the numeric lock, free memory 56 percent.

1. Linear weights, triangle (P is the convolution of two linear weights, P(c) = Phi(sqrt(J_1^2 + J_2^2 + 2 J_1 J_2
   c))): J_1, J_2 in {0.3, 1, 3, 10}, J_c in {0.1, 1, 3, 10, 30}, 40 angles. 3200 comparisons, no violation; the
   largest m(theta) - m(0) was -4.5e-8.
2. A hard cap, P = 1 on {c >= a} and 0 below: violations. For a = 0.5, theta = 0.8, J_c = 20: m(theta) = 0.9363
   against m(0) = 0.9261. Four more cases have the same sign.
3. A soft wall, log P(c) = K min(c - a, 0), continuous and non-decreasing: violations for K = 5, 20, 80, of size
   5e-3 to 1e-2 at the same parameters.
4. A linear part added, log P(c) = b c + 40 min(c - 0.5, 0), at theta = 0.8, J_c = 20: violation for b = 0 and
   b = 1; none for b = 3 and b = 10. Power weights ((1 + c)/2)^p, p = 50 and 200: no violation in four cases.

**Proposition S (the comparison fails for a hard cap; PROVED, as an asymptotic statement).** Two sites x, y and
two bonds. The first bond has the weight 1 on {<w, 1> >= a} and 0 elsewhere, with -1 < a < 1 and alpha = arccos a.
The second has the weight exp(J <w, h>), h at angle theta from 1, 0 < theta < alpha. Then there is J_0(a, theta)
such that m(theta) > m(0) for every J >= J_0. So the analogue of (M) fails for this pair of weights.

Proof. Put s = 1 - <w, h>, on [0, 2]. Under the uniform measure s has the density rho(s) = (2/pi) sqrt(s (2 - s)),
and given s the point w is uniform on a two-sphere of angular radius r = arccos(1 - s) about h. Let q_theta(s) be
the fraction of that sphere inside the cap, s_1 = 1 - cos(alpha - theta) and s_0 = 1 - a, so s_1 < s_0. Then
q_theta = 1 on [0, s_1], because the sphere stays inside the cap. For s a little above s_1 the sphere contains
points at angular distance theta + r from 1, with alpha < theta + r < pi, so q_theta(s) < 1 there; q_theta is
continuous, so 1 - q_theta >= eta > 0 on some closed interval [s', s''] inside (s_1, s_0). For theta = 0 the fraction is q_0 = 1 on [0, s_0] and 0 above. Let E be the
mean for the density rho e^(-J s)/Z on [0, 2], and mu = E[s]. For a weight q with values in [0, 1], the mean of
s under q rho e^(-J s) is E[s q]/E[q], and mu - E[s q]/E[q] = E[(s - mu)(1 - q)]/E[q]. Take J so large that
mu < s_1 and E[q_0] >= 1/2 (mu tends to 0 and E[q_0] to 1 as J grows). Then (s - mu)(1 - q_theta) >= 0 on [0, 2],
E[q_theta] <= 1, s - mu <= 2 and rho <= 2/pi, so
  mu - E_theta[s] >= (s' - s_1) eta (min of rho on [s', s'']) (s'' - s') e^(-J s'')/Z,
  mu - E_0[s] <= 2 . 2 . (2/pi) e^(-J s_0)/(J Z).
The quotient of the first bound by the second grows like J e^(J (s_0 - s'')). So E_theta[s] < E_0[s] for large J,
and m = 1 - E[s]. QED.

**Remark S (GUIDE for the soft walls; ARGUED).** The runs of items 3 and 4 show the same failure for continuous
non-decreasing weights that are flat near alignment, and no failure once the linear part is strong enough. The
mechanism is in the proof above: for 0 < theta < alpha the wall is nearer to h on one side, so it cuts more of
the low part of the Gaussian tail around h. A linear weight has no wall: it lowers the mean by focusing along
the geodesic from 1 to h. So a proof of (N1) in the linear class has to read the shape of the weight. This is
the kind of constraint that Proposition V puts on the neutral half; here it appears in the charged comparison.
The flat-topped weights of items 2 to 4 are not known to have non-negative character coefficients, so they do
not test the reflection-positive class.

Not on file under the words I searched (`grep` over `library/gap-*.md`, run after the work): "one-sided twist"
with "diamagnetic" (only row 1194 5.1, the open question itself); "flat-topped" (one hit on another subject,
`gap-brainstorm2-max.md` L280); "cap weight", "hard cap" (none); "monotonicity of D" (two hits on other
subjects). So Lemma E, the guide runs for the one-sided form, Proposition S and Remark S are new to the
record as far as these greps show. The two-sided normalized form is refuted on file (method 36, rows 1139,
1140), and the unnormalized form is on file (3.2).

## Step 4. State at the end (written 2026-11-20T02:41Z, last correction 02:42Z, both `date -u`)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session from 2026-11-20T01:36Z, no subagents.
Author only. Checked by no one. Four guide runs under the numeric lock (two heat-bath sampling runs, two
quadrature runs), free memory 56 to 57 percent; the scripts are in a scratch folder and are not committed. Literature:
two arXiv API queries, nothing fetched beyond titles and abstracts. I did not read the primary text of the
posted two-dimensional proofs or the Sussman-Alpoge repository in this session: their account lists the mass
gap as its own open requirement (`library/sa-index/chunk-01.md` L70, L86, as read in row 1194), so no step of
the gap can be ported from it. The search of `origin/main` and of the open PR branches is not possible from
this checkout.

| Statement | Label |
|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten) | OPEN. Not proved here, nothing disproved |
| (N-phys), the continuum datum, (BS), (W), (SING) | OPEN. Not attacked: no route off the lane's map was found |
| Step 1: literature probe to 2026-11-15; thirteen more candidates, each with its match | GUIDE |
| Step 2.1: the engine carries a small neutral trace upward and nothing on file creates it | ARGUED (the lane's reading) |
| Lemma U: Z_R <= Z_1 and the unnormalized two-point bound, one-sided and two-sided | PROVED; found again (Proposition LG, row 1016) |
| Lemma E: the normalized one-sided comparison (N1) holds iff D_g = log(Z_1/Z_g) is non-decreasing in every coupling | PROVED (elementary; not yet checked by the other model) |
| Lemma A: the normalized comparison for plane rotators with arbitrary phases | PROVED (Ginibre's argument with shifted phases; same standing) |
| (N1) for S^3 sheets with linear weights and one-sided twists | OPEN. GUIDE: no violation in 400 sampled comparisons on four graphs and 3200 quadrature comparisons on the triangle |
| Proposition S: the comparison fails for a hard cap weight at large chord coupling | PROVED as an asymptotic statement (same standing) |
| Remark S: it fails for soft flat-topped weights and holds once the linear part is strong | GUIDE; ARGUED |
| Remark C: bond-energy covariances of a twisted cell are not dominated by the untwisted ones (-1/4 against at most 0.09 at J_1 = J_2 = 2) | PROVED (elementary) |

What none of it does. It bounds no neutral covariance and no twist cost in four dimensions. It does not move
(N-phys), (SING), (BS) or (W). The item is off the path; Step 2.2 says so.

What it settles. Row 1194 5.1 left "a diamagnetic comparison for one-sided twists" undecided. In three parts:
the unnormalized form holds and was on file; the normalized form for charged two-point functions is equivalent
to monotonicity of D_g, has no counterexample in the linear class, and is false for flat-topped weights; the
neutral form is false.

For the lead (ARGUED, short).
1. This is the seventh plain-brief screening (rows 1188-1190, 1193-1195, this row). Together they hold more
   than sixty candidates with their matches (rows 1189, 1190, 1193, 1194, 1195 and Step 1.2 here). None found a
   route off the map. I expect no information from another screening row.
2. I recommend no row on (N1). It has no consumer. If one appears, the first lemma is the cycle case: for the
   convolution F of linear weights exp(J_i <., 1>), the ratio F(theta)/F(0) is non-increasing in every J_i.
3. No statement of this file is used by any other file. A check of Lemma E and Proposition S is short, and
   nothing waits for it.

RESULT: Row 1199 (Claude Fable 5.2 max, Mac mini worker 2, 2026-11-20 01:36Z-02:42Z; author only, checked by no one; four guide runs under the numeric lock): the mass gap is NOT proved and nothing is disproved; (N-phys), the continuum datum, (BS), (W), (SING) stay OPEN. A seventh plain-brief screening (a literature probe to 2026-11-15 and thirteen further candidates, each grepped) found no route off the lane's map (GUIDE). One bounded item was worked, off the path and said so: the diamagnetic comparison for S^3 sheets with one-sided twists that row 1194 5.1 left undecided. PROVED by hand, small, not selective: Lemma E (the normalized comparison (N1) for charged two-point functions holds iff D_g = log(Z_1/Z_g) is non-decreasing in every coupling); Lemma A (the comparison for plane rotators with arbitrary phases, by Ginibre's argument); Proposition S (the comparison fails for a hard cap weight at large chord coupling, so a proof in the linear class must read the shape of the weight); Remark C (neutral bond-energy covariances of a twisted cell are not dominated by the untwisted ones: -1/4 against at most 0.09). Found again, not new: Lemma U, the unnormalized comparison (Proposition LG of row 1016). GUIDE: (N1) for linear weights has no violation in 400 sampled comparisons on four graphs and 3200 quadrature comparisons on the triangle; soft flat-topped weights violate it. OPEN: (N1) in the linear class (no consumer), and everything on the path.
