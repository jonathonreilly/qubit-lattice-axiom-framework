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
   and found every one on the lane's map (about 65 route families in all, tables in rows 1189, 1190, 1194).
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

A finite multigraph with sites V and oriented bonds b = (x -> y). Spins n_x are unit quaternions, with the
uniform probability measure on S^3. <p, q> = Re(conj(p) q) is the inner product of R^4. A one-sided twist is a
unit quaternion g_b on each bond, acting on the left. For couplings J_b >= 0:

  Z_g(J) = integral of exp( sum_b J_b <n_x, g_b n_y> ),   <n_x, g_b n_y> = <n_x conj(n_y), g_b>.

E_g is the normalized expectation. The right rigid group n -> n k is exact for every g. A change of variables
n_x -> lambda_x n_x maps g_b to conj(lambda_x) g_b lambda_y, so only the holonomies of g matter. Q_g(x, y) :=
E_g[n_x conj(n_y)] is a quaternion; its norm is gauge invariant. The same setting with a general orthogonal
4 x 4 matrix R_b in place of left multiplication is the two-sided case.

### 3.2 Lemma U (the unnormalized comparison; PROVED; the method is Brydges, Frohlich and Seiler's, RECALLED as
the source of the method, rebuilt here)

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

For the neutral half the analogue of (M) is false in the smallest example. Two sites, two bonds, J_1 = J_2 = 2.
With psi(s) = log Phi(sqrt(s)) = s/8 - s^2/384 + ..., log Z_h = psi(J_1^2 + J_2^2 + 2 J_1 J_2 Re h), and the
covariance of the two bond energies is its mixed derivative. For h = -1 it is -2 psi'(0) = -1/4 exactly. For
h = 1 it is phi''(4) with phi = log Phi and phi'' = 1 - A^2 - 3A/R, A = I_2/I_1. From the series, I_2(4) >=
6.4215 and I_1(4) <= 9.76, so A(4) >= 0.65 and phi''(4) <= 0.09. So the twisted covariance is larger in
absolute value, and has the other sign. A frustrated loop shares its frustration among its bonds, and this
couples their energies. So (N-tw) of row 1194 cannot be reached by a domination principle. The neutral
response of a twisted sheet is carried by the frustration itself. This agrees with row 1194 5.3, way 2.
