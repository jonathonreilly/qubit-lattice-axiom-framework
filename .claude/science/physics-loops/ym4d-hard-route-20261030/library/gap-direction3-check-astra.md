## Repo search

Writer: OpenAI Codex, gpt-6-astra, xhigh (this run's requested configuration).
Pinned source: `2f317758f3e7ec465e8ddf19897601ae8f4997b1`.
Checked text: row 1051, written by Claude Fable 5.2 at max effort.
Research check of row 1051, not an audit; grants no status. No mass gap claimed.
Not covered: a new attack, row 1056, the start-values proof row, a global
literature survey, numerical or computer-assisted proof, or Lean execution.

The task-specific prior digest is absent. The November 8 repository digest
concerns earlier UV admissions, covariance and history work. Its hits are
related background, not a check of the present ring-response identities.
Row 1051 identifies the closest prior results: Identity AV (row 1016),
Lemma TAN and GR+ (row 1046), WN/JEN (row 1013), and TREE (row 1038).
These were read as sources, not counted as new results here. The digest's
finite-clock and noncompact-Maxwell hits on main, and its one-step loop
witness on PR 10114, were opened: they concern different measures or
consumers, not the present identities. Exact paths and ranges are below.
The registry search found no owner for this check or these exact new claims.
The separately commissioned row 1056 is not read.

The outline and CA-I were each downloaded once, at `31a47c543775`, into the
new directory `/tmp/sa-gap-direction3-check-astra.7wvRq1`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text; Balaban for the underlying construction; OpenAI for the 2D
commutator method; and the authors of the earlier lane notes named below.

## Checkpoint

Plan: (1) source and index readings; (2) hand tests (a)-(e); (3) RM and TREE;
(4) PIN, SF-D and the shell count; (5) K4, blind statements and controls;
(6) exact verdicts and ranking. Only this output file is edited.
Completed: prescribed hand tests, exact-identity checks, control models,
taxonomy, stop verdicts and ranking. No further proof attack is authorized.
Open estimates remain open; the final RESULT records the precise scope.

## Hand tests required by 7.1, before the verdicts

All computations here are symbolic arguments, not program output.
Write unit quaternions as `t+s`, with `[u,v]=2u×v`.

**(a) One link.** For `Phi=-beta t`, `S_epsilon U=exp(epsilon a)U`,
`|a|=1`, the derivatives are `Phi'=beta a·s`, `Phi''=beta t`.
Conjugation invariance gives `E(a·s)^2=E(1-t^2)/3`. Thus RM reads
`E t=(beta/3)E(1-t^2)` for beta positive; at beta zero both sides
vanish. The sign and factor three pass.

**(b) One plaquette and TREE.** Condition on all tree links. In tree
coordinates they are 1, and each remaining link is independently conjugated
by `exp(-epsilon lambda_head a)`. This preserves conditional product Haar.
For a plaquette whose tree meets just one edge, put two adjacent chord
links equal to `i,j`, the other two equal to 1, and take `a=k`.
Its trace derivative is `2(lambda_1-lambda_2)`. It is nonzero when the
heads have different lambda. Every other plaquette containing at most one
of these two links has a conjugation-invariant trace. This verifies the
unit-cell witness. Such a partial tree on the square means a spanning tree
of a larger graph, with the other connections outside the square.
In contrast, a standalone square's spanning tree has three edges. Its sole
chord is conjugated, its trace is unchanged, and the response mean is zero.
Strict positivity is therefore not part of the TREE identity alone.

**(c) P2 and TAN.** On one plaquette take links `(1,1,1,-k)` in the
convention `U_p=U_1 U_2 U_3^{-1} U_4^{-1}`, so `U_p=k`. Take gauge
parameters `F_x=i,F_{x+e_1}=j`, zero at the other two vertices.
After the exact gauge return the trace is
`Re(exp(-epsilon i) exp(epsilon(i-j)) exp(epsilon j) k)`.
The product before k is `1+epsilon^2 k+O(epsilon^3)`.
For `f=exp(beta Re U_p)` this gives `D²f[dF,dF]/f=-2 beta`,
while `Df[B_2]/f=-beta`. Thus P2 and TAN agree, including the force sign:
`H=2 beta`. This is a finite-plaquette test of the gauge identity.

**(d) SF-D at L=2,T=1.** Keep the positively oriented periodic bonds,
including the two bonds joining each neighbouring pair on the size-two
circle. The time links are independent Haar variables `V_x` at beta zero.
The nonconstant action is `beta sum_e Re(V_x V_y^{-1})`.
Each unordered pair occurs twice. Haar moments are
`E_0 t_e²=1/4`, `E_0(u·s_e)²=|u|²/4`.
Different unordered pairs have zero covariance, by integrating a vertex
occurring only once. Hence `xbar_1=beta/2+O(beta²)` and
`E X(dF)²=(beta²/2) sum_directed |F_x-F_y|²+O(beta³)`.
This is precisely `beta xbar_1 sum |dF|²` to its first nonzero order.
The test is outside SF-D's printed L>=3 domain; the multigraph convention
explains the factor two. For L>=3 the corresponding leading coefficient
is beta²/4. No numerical test was used.

**(e) The shell count.** At boundary dimension b, a directional shell
has `M~r^b` modes, signal `M epsilon² r/L`, and individual Dirichlet
energy `g epsilon² r² L^(b-2)`, where `g=beta xbar_1`.
For unit signal `1/L`, its sum-of-squared-energies cost is
`C_r~K g² r^(2-b) L^(2b-4)`.
For g>0 and independent dyadic shells with signal fractions `a_j` summing to 1,
Cauchy-Schwarz gives `sum C_j a_j² >= 1/(sum C_j^{-1})`, attained at
`a_j` proportional to `C_j^{-1}`. Thus b=2 gives `K g²/log L`;
b=3 gives `K g² L`. These are costs in the postulated bound, not lower
bounds on the response. For g=0 the postulated cost is zero. Use directional half-shells (and transverse
reflections), since a symmetric full shell cancels its sine signal.
This reproduces the logarithmic power recorded for OpenAI's Lemma 3.2
in row 1007, lines 129-133; it does not verify that paper's family estimate.

## Verdicts on 5.1

Line numbers below refer to `gap-direction3-max.md` at the pin.

**Lemma RM, lines 320-333: HOLDS.** An alternative derivation is the
normalization identity
`E_rho exp[-(Phi(S_epsilon omega)-Phi(omega))+log J_epsilon]=1`.
Its first two derivatives give exactly (i) and (ii). Compactness and smoothness
supply one integrable bound for both derivatives. For J=1 the result is a
square. The density is strictly positive everywhere, so zero expectation
of the continuous square implies `Phi'=0` everywhere. No stationarity of
rho under S is assumed. Haar preservation is the relevant hypothesis.

**(RM-fr), lines 338-349: HOLDS.** Given the outer pin, the ring density
is `exp(-sum_c F_c)/Z`. The weights add to the union action. Freeze the
same n at the base configuration for every cell. Gauge-transform the changed
pin by `g_x=exp(epsilon lambda_x n_x)`. On link x->y its product becomes
`exp(epsilon(lambda_x-lambda_y)n_x) omega_l`.
Thus the finite identity with the original boundary twist holds before
any derivative. This independently verifies GR+'s identification here.
All outer links stay fixed because lambda vanishes at their heads.
The smooth family is locally a diffeomorphism: its derivative is uniformly
close to the identity on the compact manifold; a local diffeomorphism
homotopic to the identity is a one-sheeted covering. RM then applies.

**RM-TREE and its one-cell form, lines 351-363: HOLDS for the stated fixed
root colour.** Condition on the tree links and use the chord coordinates
`H_l=W_x^{-1} omega_l W_y`. Haar measure is still product Haar in the
chords. The transformation is
`H_l -> exp(-epsilon lambda_y a) H_l exp(epsilon lambda_y a)`.
Tree links do not move, so each conditional transformation preserves Haar.
The same argument applies to the free-boundary density `Z_c/Z_free`.
There is no extra variance over the frame to insert in either formula.

There is a scope correction in identifying this with **all of row 1038's
TREE frames** (first at line 367). That row, lines 155-165, allows a
pin-dependent root vector `a(omega)`, covariant at the root. Fixing the tree
links alone does not fix that vector. A fixed external colour is admissible
for the algebra; it is not an intrinsic covariant selector at the root.
Row 1038, line 248, makes the additional specific choice: the axis of one
chord `H_l0`. For that choice condition on the tree and on `H_l0`.
That chord is fixed and every other chord is a fixed conjugation. This proves
Haar preservation there too. Choose a free chord: its undefined central-axis
set has Haar measure zero. If the outer pin fixes that chord, its prescribed
holonomy must instead be noncentral. Differentiate in epsilon by dominated
convergence: the frame has unit norm and the first two derivatives of F are uniformly bounded, even
near that null set. Do not assert the smooth-global RM hypotheses for
this axis selector, or Haar preservation for an arbitrary root selector.

**The four numbered readings: HOLDS AFTER CORRECTION**, with this text:

1. For a fixed-root TREE move, or the conditioned single-chord-axis move just
   specified, the summed gradient response has mean `E(Phi')²`. It is
   strictly positive exactly when `Phi'` is not identically zero (almost
   everywhere for the axis version). For positive beta the unit-cell,
   identity-outer-pin witness in hand test (b) proves this for the fixed
   root colour a=k when the two
   non-tree links are free ring links, share a plaquette, and have distinct
   head values of lambda. The source's generic-quaternion step is valid
   for that fixed root colour. It does not automatically apply to a
   root-axis selector: if the root axis is chosen from either of the two
   nontrivial chords in that witness, that chord stays fixed and the other
   is conjugated about its axis, preserving their product trace. A strict
   witness for the specified intrinsic selector needs its own check.
   It is not a claim for every tree, every lambda or every cell size.
   A zero gradient, the standalone one-chord square, and beta zero have
   equality. The larger-cell claim outside a discrete set remains conditional
   on a nonzero first Taylor coefficient at a specified pin and geometry;
   the row labels that supply ARGUED, correctly. Analyticity alone does not
   supply the coefficient or identify a named beta in the band.
2. For J=1 and nonzero score on a set of positive measure, a nonpositive
   mean sign is impossible. Negative responses on special pins are compatible
   with this result. The literal unconditional sentence at line 379 needs
   that nonzero-score premise. It gives no estimate of rare bad cells or
   their possible compensation in a different consumer.
3. For a smooth general frame, nonpositive mean is **equivalent** to
   `E l'' <= -E(Phi'-l')²`. Since `E(Phi'-l')=0`, the square is a variance.
   This is an averaged logarithmic-Jacobian condition, not pointwise volume
   contraction. It is a necessary and sufficient test for this mean sign,
   not an equivalence with the full typical-pin, all-field obligation (N1).
4. The identity covers every Haar-preserving move, not TREE exclusively.
   It supplies no strict lower constant, no co-closed estimate and no
   conclusion against a non-Haar-preserving frame without its Jacobian.
   For general families stationarity means `Phi'=0`; finite invariance
   follows for the TREE group action but need not for an arbitrary family.

**Decision requested in 7.1.** The conditional claim “TREE fails in the
mean wherever its ring action is nonstationary” is proved, including the
specified unit-cell witness. The unqualified “TREE fails (N1) in the band”
is **not** proved. Nor does the check prove failure for “TREE and no other
frame”: the identity is broader, and the fixed lab frame already has the
separate AV/BH obstruction. No new obstruction to a general covariant
selector, including COUL, is obtained here.

## Verdicts on 5.2

**Proposition PIN, lines 399-408: HOLDS.** Multiplying `E_F omega` at its
endpoints by `exp(F_x),exp(-F_y)` leaves exactly
`exp(F_x-Ad(omega_l)F_y) omega_l`. Gauge covariance of Z proves the
finite identity, with no smallness assumption on F.

**P2 and P4, lines 410-420: HOLDS.** In the local logarithm,
`B(epsilon)=epsilon² B_2+epsilon³ B_3+epsilon⁴ B_4+O(epsilon⁵)`.
The order-two term of `exp(-epsilon X) exp(epsilon(X-Y)) exp(epsilon Y)`
is `[X,Y]/2`. Expanding f at zero gives, through order four,
`f(0)+epsilon² Df[B_2]+epsilon³ Df[B_3]`
`+epsilon⁴(Df[B_4]+D²f[B_2,B_2]/2)`.
Thus no B_3 cross term or factorial is missing in P4. This verifies the
coefficients without importing a convergence claim about the full BCH series.
TAN's force has the correct sign, as test (c) shows. For transverse F at
an abelian pin, the quaternion cross product is along the remaining axis;
its complex coefficient is the stated imaginary part, up to the declared
orientation convention. P4 is an identity, not a fourth-order inequality.

**SF-D (a), (b), (c), lines 422-438: HOLDS** for nonnegative homogeneous
Wilson coupling and the stated L>=3 slab. Global conjugation of all
integrated variables fixes the identity pins and rotates each N_l, giving
`E N_l=0`. For a top field B the exact differentiated integral is

`-D²f[B,B]/f = beta xbar_1 sum_l |B_l|²`
`+ beta sum_top_p w_p |dB|_p² - E X(B)²`.

Each top link belongs to one temporal plaquette with exactly one moved link.
For spatial plaquettes all four pin links are 1, so their second-order
term is the ordinary curl square and their force vanishes. These observations
account for every affected plaquette. At B=dF, P2 and `Df=0` make the left
side zero, proving (b). For B=h sigma_3 with dh=0, dropping the nonnegative
score square proves (c). This also explains the size-two test above.

For `h=1/L` on one spatial direction, `sum h²=L`, so the **direct trial
cost** is exactly `beta xbar_1 L`. The response is that number **minus**
`E X²`. Any occurrence of “exactly” in lines 440, 496 or the summary must
refer to the trial cost, not the response or its infimum over extensions.
A classical interpolation `h_j=j/(LT)` through the slab has quadratic
cost `beta L/T` (apart from a fixed Hessian convention), hence order beta
when T=L. This is a comparison of trial costs, not a lower bound on H.

**The count, lines 444-468: HOLDS AFTER CORRECTION as a conditional scaling
argument only.** Replace its conclusion by:

> For the postulated sum-of-squared-Dirichlet-energies estimate, the specified
> directional Fourier shells give cost of order `K (beta xbar_1)² L` in
> boundary dimension three, at fixed geometry T=L. In dimension two they
> give the logarithmic improvement. The bound obtained this way does not
> establish an L-uniform response estimate. No response lower bound,
> impossibility theorem for other families, or exclusion of C1/C2 follows.

Test (e) supplies the optimization. Keep xbar_1 if it depends on L; treating
it as a fixed positive number requires separate uniform estimates. Replacing
it by 1 is a valid coarse upper estimate, not a lower estimate on the best
cost. The actual OpenAI Proposition 2.2, as recorded in row 1007 line 132,
also contains a nonnegative remainder with sup norms. The simplified
postulate is an optimistic model of that estimate. Its full gauge version,
including force terms in P4, has not been proved here. WN's quadratic
corner form does not fill that gap (row 1013 check, items 12-17).
The sentence at lines 459-463 is a comparison of these constructions,
not a classification of all field-independent actions or costs.

## Verdicts on 5.3 and K4

**K4's change of variables, lines 529-546: HOLDS.** At the double seam,
substitute `U_1=U~_1 Omega_1` and `U_2=U~_2 Omega_2` in the four factors.
The uncancelled word between the second and third link is
`Omega_2 Omega_1 Omega_2^{-1} Omega_1^{-1}`. At a single seam all constant
factors cancel. Right multiplication preserves each link's Haar measure.
There are L² double-seam plaquettes, one for each x_3,x_4. For i,j the
word is -1. This verifies the 't Hooft centre-twist identity directly.
It remains valid for class plaquette weights, with the weight evaluated
on the displayed corner product rather than literally replacing it by a
real trace for every choice of weight.

**K4's interpretations: HOLDS AFTER CORRECTION.** For arbitrary Omega_1,
Omega_2 the finite seam-action identity is valid. Calling it consistent
constant transition boundary conditions on the covering lattice requires
`Ad(Omega_1)` and `Ad(Omega_2)` to commute, equivalently K central.
This condition holds for i,j. For a noncentral K retain only the
explicit finite seam action and its sheet-insertion family.
At line 548 restrict “largest weight” to Wilson weights with beta>=0
(or other weights maximized at 1). Class functions alone do not imply it:
`w(U)=exp(-beta Re U)` is a positive class weight maximized at -1.
For the Wilson case U=1 has every seam plaquette equal to 1, so both
sectors attain the same maximum classical action. The precise conclusion
is **zero difference of classical minimum energies**. It does not assert
that the finite-beta free-energy difference has no energetic contribution,
or verify the recalled log-beta fluctuation asymptotics.

**Attempt 7, lines 514-527: HOLDS** for its specified site-conjugation
maps and Wilson beta>=0; it is a bound on their Jensen exponent only.
Here is a separate metric check of its coefficient. Write `q_x=c(x)`.
A plaquette trace after the change of variables has three fixed insertions
`q_x^{-1}q_{x+mu}`, `q_{x+mu}^{-1}q_{x+nu}`,
`q_{x+nu}^{-1}q_x`. Gauge averaging at those distinct vertices multiplies
its mean by their three real parts. If d_x is the distance of the first
insertion's class angle from `{0,pi}`, then
`1-product >= 1-|Re(q_x^{-1}q_{x+1})|`
`=1-cos d_x >= 2 d_x²/pi²`.
In the quotient of the unit-quaternion sphere by sign, the endpoint
condition along a direction-1 line has distance pi/2. The triangle
inequality and Cauchy-Schwarz give `sum_line d_x² >= pi²/(4L)`.
There are L³ such lines and three plaquette orientations containing
that directed edge. Summing yields the claimed exponent lower bound
`(3/2) beta xbar L²`. Homogeneous periodic Wilson symmetry and convexity
of log Z give xbar>=0: its derivative is zero at beta=0 and is
nondecreasing. None of this lower-bounds the actual vortex free energy.
It only shows why this Jensen estimate does not prove (BL-c).

**The four SU(2) open entries: HOLDS AFTER CORRECTION to a bounded record
statement.** No proof of their stated uniform estimates is supplied by
row 1051 or its prescribed source list. No contrary complete theorem was
located in the indexed passages read here. This is not a theorem that the
literature contains no proof, or that no pin class admits an upper bound.
The distinctions are material:

- `(BDD-Delta)` is the size-uniform Casimir bound on the trajectory.
  The exact Corollary NUC in row 1032, lines 311-324, bounds **all four**
  nonnegative G_i, including partially infinite-volume terms. It is not
  equivalent merely to bounded counts below inverse side in one cube.
  `G_0=log(1+S)` is one summand, and even G_0 is a thermal sum, not a
  single-threshold count. The next paragraph in that source labels the
  weak-end state-count reading GUIDE. Correct row 1051 lines 478 and 256-257
  to the four-G_i formulation.
- `(BL)` is one scalar response along a special slab-pin family, uniformly
  in L and t. SF-D gives only its O(L) direct bound at t=0.
- `(BL-c)` is a lower bound for one chosen centre-twist ratio.
  K4 and attempt 7 do not establish its size-uniform positive constant.
- `(L1)` in row 1018, lines 111-136, concerns the ring-law mean of a sum
  of squared cross-face Neumann covariance entries. It is not the scalar
  slab Hessian in (BL). No implication `(BL)=>(L1)` is supplied. The
  claimed consumer in row 1051 section 7.3 needs that separate bridge.

**Taxonomy, lines 472-476: FAILS as written**, first at line 473,
“Each holds for compact U(1).” The exact supplied proofs establish (BL)
and (BL-c) for the Wilson abelian model; they do not prove (BDD-Delta),
which `gap-dichotomy.md:367-369` explicitly leaves GUIDE for this control,
or (L1), whose actual covariance definition has no supplied comparison.
This is a failure of the claimed proof/record, not a counterexample to
those two abelian statements.

The further identification at lines 474-475 with all constants log m also
fails. A centre twist measures its own charged sectors. A neutral
m-fold degeneracy can cancel from `Z_tw/Z` and still contribute log m
to D. By the product identity, twisting factor 1 gives
`Z_tw,total/Z_total=Z_tw,1/Z_1`, whereas `D_total=D_1+D_2`.
Thus a constant degeneracy in the untouched factor is invisible to (BL-c).
Equivalently, in an abstract limiting transfer spectrum with m zero-energy
states on which the twist is +1, the ratio is 1 and D=log m. These are
scope tests, not counterexamples within Wilson SU(2). Even with charged
states present, a strictly positive twist ratio need not force multiplicity
one. No sector theorem identifying all of Proposition CONST's m states
with evenly balanced flux sectors is supplied.

Replace the taxonomy by this text:

> (BDD-Delta) bounds the full Casimir quantity and permits constant log m
> limits. (BL-c) excludes regimes where the specified twist ratio tends to
> zero; it does not imply (NO-CONST) without an additional sector theorem.
> The continuous definitions of (BL) and (L1) use Lie derivatives, so those
> definitions do not directly apply to a finite group. This does not rule
> out discrete analogues. Only the abelian (BL) and (BL-c) controls have
> elementary proofs here. No equivalence between the four statements,
> identification with “infrared freedom only”, or common consumer follows.

The frozen-Z_2 comparison remains a cited control for (BL-c), in its stated
low-temperature regime. Its Peierls theorem is not rebuilt in this check.
It does not repair the inference about every constant critical element.

## Controls and kill tests

**Compact U(1): HOLDS for the three identities and the two twist controls.**
RM is a measure identity. In PIN all factors commute, so E_F=1 and B_F=0.
SF-D holds, with inversion `U->U^{-1}` replacing the nonabelian
conjugation proof of the zero force. It yields no bracket gain.
For (BL), translate the direction-1 links on slice j by `t j/(LT)`.
The only action derivatives are on the temporal plaquettes, with
coefficient `1/(LT)`. At every t, differentiating under the finite integral
and dropping `E[(A')²]>=0` gives `-Z''/Z <= beta L/T=beta` when T=L.
This proves the printed supremum over t, not just its value at zero.

For abelian (BL-c), the sheet 2-cochain and the uniform 2-cochain
`alpha/L²` on direction-(1,2) plaquettes differ by an exact periodic
cochain. To construct it, first solve a cyclic difference with right side
`delta_{x_1,L-1}-1/L` and then one with right side
`delta_{x_2,L-1}-1/L`; both have zero sum, so partial sums are periodic.
These two shifts spread the sheet in directions 1 and 2. Inversion symmetry
kills the sine mean. Jensen and `1-cos u<=u²/2` give
`Z_tw/Z >= exp[-beta L⁴(1-cos(alpha/L²))] >= exp(-beta alpha²/2)`.
This argument is for Wilson U(1); it supplies neither compact-U(1)
(BDD-Delta) nor the covariance-norm comparison (L1).

**Frozen groups: HOLDS as a domain check.** There is no nontrivial
one-parameter subgroup of a finite group, so the Lie derivatives in RM/PIN
supply no selective mechanism there. This is not a necessity theorem that
every successful argument must use a Lie algebra. The frozen-Z_2 twist
control and the Q_8/2T seed obstructions keep their original domains.

**D2 and SHEET: they do not bind these identities.** D2 assumes a
supremum over prescribed pinning/tilt laws. SHEET takes special
inhomogeneous strengths B to infinity. RM is in one given ring law;
PIN is a finite gauge identity; SF-D uses one homogeneous pinned slab.
None claims a small uniform covariance over the D2/SHEET families.
A future deduction through such a supremum would have to pass those tests.
In particular a single slab calculation is neither a refutation of a
cube-only typical-ring claim nor its proof.

**PT: it binds a seed inference, not these identities.** Moves and twists
in one factor leave their normalized response unchanged under tensoring
with an untouched factor. The gap of the product is the smaller gap.
Thus these observations cannot imply a whole-state seed without a consumer
that checks the other factor. Correct the brief's “every statement of
Section 5 reads one factor”: full-model D is additive and the T-pin
covariance matrix is block diagonal, with squared norms adding; those
objects can read both factors. A chosen centre twist can still miss one.

**Four-test specification check on the ranking.** S0: BDD-Delta is one
named half of the existing criterion, not a solution; BL and BL-c are
separate questions until bridges are supplied. S1: the two elementary
abelian controls show that their boundedness is not a nonabelian selective
gain. S2: no strict decay rate or scale-transport law has been proved.
S3: a single twist does not control the whole state space; the product test
above remains. S4: homogeneous coupling and a prescribed pin family avoid
the forbidden all-fields supremum, but give no typical-ring distribution
estimate. These are tests of a proposed sufficient tool, not a rule that
every preliminary lemma must itself imply the gap.
In five dimensions the abelian spread-twist cost is proportional to
`beta L^(d-4)=beta L`, and the slab interpolation has the same dimension
factor. The scaling check is consistent. The alleged five-dimensional
phase remains a GUIDE comparison here, not a proof premise.

## Stop verdicts and ranking in 4.2

| Item | Verdict | Replacement text / first failing inference |
|---|---|---|
| Stop A, line 280 | **HOLDS AFTER CORRECTION** as a research choice; **FAILS** as a general obstruction | “Set aside the Haar-preserving TREE mean-sign proposal where its nonzero score is established. General (N1), compensating rare-cell forms and other frame selectors remain open.” The first overreach is from that restricted identity to stopping (N1) at bare coupling in general. |
| Stop G, line 286 | **HOLDS AFTER CORRECTION** as a research choice; **FAILS** as an exclusion of C1/C2 | “The specified Dirichlet-cost Fourier-shell estimate has not supplied an L-uniform bound. C1 in corner form, other fourth-order inequalities and C2 retain their prior open standing.” The count is about one postulated inequality only. |
| Ranking, lines 289-297 | **HOLDS AFTER CORRECTION** as an argued priority, not a theorem | “Several proposed stiffness engines lack a proved uniform bound. The separate four-G_i, slab, twist-ratio and covariance questions deserve distinct consumers. This check does not rank their mathematical difficulty or prove that all routes stop together.” |
| Necessity/reopen equivalence, lines 506-510 and 688-691 | **FAILS** as a deduction, first at line 506 | “A sufficiently parallel colour frame is one proposed construction. No necessity of such a frame, of 1/L accuracy, or of blocked fields is proved for all admissible flows.” Delete “equivalently” at line 689. EXT allows general smooth interior vector fields; no reduction of all those fields to a site colour has been supplied. |
| Seven stopped mechanisms as counterexamples, lines 563-564 | **HOLDS AFTER CORRECTION** | “Attempts 1 and 7 evaluate restricted trial bounds; attempt 3 is a conditional cost count; attempts 2, 5 and 6 remain heuristic or uncomputed; attempt 4 describes particular positivity tools. No successful mechanism was found by that row.” |

The first two corrections preserve the valid narrower obstructions rather
than discard RM, PIN or SF-D. Nothing here upgrades an ARGUED stop into a
proof that the associated research line cannot work. Line F cannot be
called tried in equivalent BL/BL-c forms: no such equivalence is on file.
The phrase “first statement of any kind” at line 559 likewise lacks the
required scope and search evidence. No new attack is proposed by this check.

## Source record and limits

The November 8 prior digest was read in full. Its nearest outside-lane
matches were checked on current fetched main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`:
`docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:1-12,79-94`
is a different finite-clock measure; and
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120-145`
is a noncompact Dirichlet Maxwell score-covariance implication, related in
method only. Fetched PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106-149`
gives a one-step loop witness, not a stiffness or size-uniform twist bound.
No proof from these different models was imported. The lead's supplied
all-PR search is not independently repeated or upgraded to an absence theorem.

The outline index was searched for the named ring, pinned-cell, twist,
vortex, response and mass-gap objects, including neighbouring rows and
obligations. Its finite-Haar/gauge entries point to SA 240-293; the
scope entries point to 588-599 and 31871-31882. The relevant source
reads were SA 225-237,278-293,565-600. They provide finite-dimensional
invariance and explicitly distinguish clustering from a gap. No matching
ring-TREE or SF-D theorem was located under the searched names.
The CA 4.12-4.19 index has no named match for these targets. CA-full's
neighbouring entries point to `1.1:lem-invariance`, `4.2:lem-first-passage`
and `4.3:thm-small-field-step`. CA-I 550-585,2703-2712,3628-3665,4136-4155
were read: the last is a **cited** small-field theorem with explicit smallness
hypotheses, not a bound through the band. The account says “Not asserted”
and lists “a mass gap” at 2706-2710. This is the credited source scope,
not a new audit of the account or of Balaban's papers.

The requested lane sources were read at the ranges used above: row 1046
TAN and GR+; row 1016 AV and BH with their proofs; row 1013 WN and JEN
and its Astra check items 12-17; row 1011 conventions and Proposition A;
row 1038 TREE and its specified root-axis rule; row 1007's account of the
2D family estimate. Additional exact definitions were read in row 1018
(T-pin/L1), row 1032 (CHAIN-4/NUC/CAS-0), the dichotomy, and the original
PT/D2/SHEET statements. Their wider theorems, numerical values and recalled
literature assertions were not re-proved. OpenAI's original 2D paper and
Balaban's original PDFs were not needed for these finite identities and
were not read. In particular this report verifies the b=2 scaling against
the required row-1007 account, not the original Lemma 3.2 proof.

No numerical or computer-assisted proof step, simulation, Lean run, audit,
ledger update or source repair was performed. Row 1056 was not opened.
Only the requested output file was written. It remains local on
`research/gap-direction3-check-astra-20261116`; no commit or push was made.

RESULT: HOLDS for RM, RM-fr, fixed-root RM-TREE and its one-cell form, PIN/P2/P4, SF-D and K4's seam identity; HOLDS AFTER CORRECTION for the TREE readings, conditional shell count, Wilson K4 interpretation, two stop recommendations and ranking; FAILS as supplied deductions for the all-four U(1) control, BL-c exclusion of all log-m degeneracies, single-cube state-count identification and necessary-frame equivalence. TREE's strict mean-sign obstruction is proved only with Haar preservation and nonzero score, explicitly for the stated unit-cell witness; no general (N1) refutation or route exclusion follows. The count concerns one form of inequality only. The four SU(2) uniform estimates remain open in the inspected record. Research check only; no mass gap claimed.
