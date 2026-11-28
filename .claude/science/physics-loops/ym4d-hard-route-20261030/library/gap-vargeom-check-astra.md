# Repo search

Codex check for row 961, 2026-11-15, pinned to
`9e785dd8727ef1a84f9d874aabc2fc35949b04ba`. Requested runner:
gpt-6-astra, xhigh. Research text, not an audit; this grants no status.

The target-specific prior note does not exist at this revision. The general
`prior/repo-search-2026-11-08.md` concerns earlier RG targets. Its nearest hit,
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–174` on PRs 10114/10133, concerns a positive
one-step plaquette correlation, not comparison of different boxes. I fetched
PR 10114 and read that argument at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
The digest records the identical source on PR 10133. I also read the
finite temporal-gauge Wilson bridge on `origin/main` at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, sections 0–2 and the Gram
construction in section 3. It supplies nonnegative character coefficients
on a fixed slab, not varying-volume comparison or strict positivity for
every representation. These are credited prior results, not new work here.
The nearest exact predecessors are the local E2/B3/SH and transfer notes;
they are used below. No inspected hit already checks row 960. This is not
an exhaustive new search of all PR contents.
The registry search for varying geometry, seed, transfer and mass gap found
no other owner of this check. Row 960 is the text being checked; row 961
expressly owns this check. No new attack on LSI-J or the seed is opened.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for the pinned outline and complete account at `31a47c543775`.
Credit Claude Opus 5.5 for `gap-vargeom-opus.md`; Claude Fable 5.2 for SH
and the HC/BR-J notes; the earlier Codex/Astra authors for E' and the
PR 10114 transfer work; and the main-branch Wilson-bridge authors.
Downloads are confined to the
new directory `/tmp/sa-gap-vargeom-check-astra.Y0kQ7a`; the outline and CA-I
were fetched once each. CA-II was subsequently fetched once to verify the
actual chessboard statement. No numerical result discharges a statement.

**Finding.** The static threshold 1/550 and the conditional ratio-4 HC
consumer hold. The stated exclusion of projected averaging fails. The
support for the broad “varying geometry buys nothing” conclusion also
fails: the operator obstruction has a specified range, the overlap bound
has a specified time, and the scalar GUIDE tests a narrower state class.
No useful varying-geometry extrapolation is established by this check.
The author labels the global answer ARGUED. The failing verdict concerns
its supporting exclusions and stop-queuing recommendation; it does not
claim that a useful varying-geometry method has been found.

## Working checkpoint

- Source: `gap-vargeom-opus.md`, 253 lines, at the pinned revision.
- Plan: (1) inspect exact predecessors and indexed source ranges;
  (2) check maps, lenses and operator obstruction;
  (3) check extrapolation, overlap and static refinement;
  (4) check model arithmetic and saved GUIDE artifacts;
  (5) finish a verdict for every statement and one RESULT line.
- Completed: required GOAL/FINISH reads, revision and ownership checks;
  full reading of the author note, all 3 scripts and all 3 saved logs;
  mathematical checks, source comparisons and verdicts below.
- Open obligations: no unfinished part of this check. The seed and LSI-J
  remain open; actual averaging comparisons and general lens improvements
  are not ruled out. No repair lane is started.
- No source, registry, ledger, FINISH row or remote branch is edited.

## First findings saved: maps and scope

Line references below are to the pinned `gap-vargeom-opus.md`.

**J1, J2 and J4 HOLD (48–56).** Disjoint Haar coordinates give the stated
push-forward and conditional expectation. Intermediate gauge factors cancel
in the composite link. The retained-vertex projection of the fine gauge
group is Haar-surjective, which proves both intertwining identities. Only
translations along untouched directions commute with an insertion.
**J3 and J5 HOLD AFTER CORRECTION:** three commuting centre involutions give
eight sectors, not sixteen. Arbitrary compositions retain the isometry,
Markov and gauge properties; they retain translation symmetry only in
directions where the insertion schedule is translation invariant. They
cannot retain J4 literally after an insertion in direction 2 or 3.

**G3's exclusion of averaging FAILS (67).** For independent Haar unit
quaternions U,V, let A(U,V)=(U+V)/|U+V|, outside the null set U=-V.
Left multiplication by any h sends A to hA and preserves the input law.
Thus A is Haar distributed. Pullback by A is a positive unital isometry;
independent pairs give a product-Haar example as well. This does not assert
that the actual Balaban map pushes product Haar forward. It refutes the
stated reason for excluding projected averages. The account's actual R3
(outline 5631–5651, located through chunk-05:68–70) is a nearby logarithmic
contour mean with a separately required global measurable extension, not
the globally defined projected average described at line 67. No Haar law
for that actual map is supplied here. Open restriction leaves the periodic
family, and a weighted pullback is unital only when its weight is 1; those
two remaining claims HOLD.

**The mixed kernel and lens formulas HOLD (60–74).** Fubini gives the
polygon action, including five-edge faces at composite links. This is a
positive-preserving rectangular operator between different Hilbert spaces;
operator positivity is asserted only for its self-adjoint composites.
With A=T_L^(a/2)Y T_s^(k/2), the lens is Tr(A* A) and the cross-lens form
is the Hilbert–Schmidt inner product. This supplies the displayed reflection
form, not all-mirror positivity of an arbitrary non-product complex.

**NO-OP HOLDS (95–96)** for beta>0 and a path with at least one growth step,
ending in an insertion. Choose a transverse plaquette on the last inserted
plane and f=M_L^(-1) tr U_p. Its links are unused by rho; conditional Haar
integration therefore gives J* M_L f=0. Hence Y* f=0. On the invariant
space, M_L is invertible and C_L has strictly positive Fourier coefficients,
so <f,T_L^t f> is strictly positive for every t>=1. This contradicts the
proposed operator comparison at every finite C. The proof covers the
specified decimation path, not every map between boxes.

**DEN and OVL HOLD with their displayed hypotheses (82–86, 136–138).**
DEN concerns the denominator substitution in one application of E2. If U
is that old bound and delta its improvement, then for 3<=t<h,
delta<=t kappa(h)<=t g/(h-t) and g<=U-delta, so even
delta<=t U/h. On h=24a, t=a the absolute improvement is at most g/23.
OVL follows by splitting a normalized trial vector into vacuum and excited
parts. Under the additional hypothesis S(a;B_L)<=3/10, its right side is
at least ((1.3)^(-1/23)-0.3)/0.7>0.983.
These are not unconditional exclusions of denominator methods. In
particular, for any trial with vacuum weight p>0 and kappa(h)>0,
E_low(t)>=e(h)+log(p)/t exceeds ell h once t>log(1/p)/kappa(h).
The 0.983 requirement is specific to evaluating the trial at t=a on an
already-small seed. It does not hold at all trial times.

**Lemma Q and the new SH' threshold HOLD (142–150).** A direct check avoids
any integer-exponent interpolation: set z_i=r_i^a and s=sum z_i. The case
s=0 is immediate. For s>0 and q>=1,
sum z_i^q=s^q sum(z_i/s)^q<=s^q. Apply this at times pa, qa and ja.
The B3 recursion needs integer times, not integer p,q. Keep integer j>=2,
1<=p<=q, pa,qa integers, p<=j and qa<min b_i. The scaled times are integers.
For j=2,p=1,q=3/2 and even a>=4 the exponent is exactly
[8 log(1+x)+336 log(1+x^(3/2))]. At x<=1/550 it is at most 22.33x.
The author's bounds e^0.04061<1.04145, 22.33(1.04145)<23.26 and
23.26^2=541.0276<541.1 verify phi(x)<=541.1x^2.
Also 541.1/550<1 and e(64)<3(64)<541.1. Thus SH(ii) gives the claimed
positive rate on every integer cube side L>=2a. This improves a static
threshold; it is independent of the failed exclusion of averaging.

**The exploratory q=1.6 ordering FAILS (147).** At r=j=2, q=8/5 gives
beta_i=5, Pi=125 and j^3 C=620. Its recursion is
[(1+x)^8(1+x^(8/5))^620-1]^2. It is strictly *smaller* than the q=3/2
recursion for every 0<x<=1/550, wherever both sets of integer-time
conditions hold (for example a divisible by 10). Here is a hand check.
Since (0.54)^5>0.045, (0.54)^10>0.002025>1/550, so x^(1/10)<0.54.
Also x^(3/2)<0.001. Using z-z^2/2<=log(1+z)<=z gives

    620 log(1+x^(8/5)) < 334.8 x^(3/2),
    336 log(1+x^(3/2)) > 335.832 x^(3/2).

The common 8 log(1+x) term cancels. Thus “1.6 slightly worse than 3/2”
is not the ordering of the stated recursion. No numerical optimizer or
new best-threshold claim is used. The proved 1/550 line survives unchanged.

## Remaining mathematical checks

**L1–L4 HOLD (88–92).** Put R=Y T_s^k Y*. Its diagonal weights in the
large-box eigenbasis are nonnegative and sum to Tr R. The variational bound
T_L^a<=lambda_0(L)^a I gives L2 and L3. For L4, singular-value minimax gives
nu_i(R)=s_i(Y T_s^(k/2))^2<=||Y||^2 lambda_i(s)^k; the sum over any n
orthonormal vectors is at most the sum of the n largest eigenvalues of R.
The resulting count is a count above a fixed weight w_*>0. Take k>=1 for
the finite small-box trace used in these bounds.

**L5's implication HOLDS; its coverage reading needs correction (93).**
Subtract the j=0 term from the spectral sum to obtain the displayed
inequality under w_j>=c w_0. In infinite-dimensional Wilson theory no
positive uniform c can satisfy that hypothesis: sum_j w_j=Tr R<infinity
while w_0>0. Neither this nor NO-OP bounds the number of nonzero weights.
Even a rank-one positive operator |v><v| can have positive diagonal weight
in every vector of a fixed eigenbasis, when every coefficient of v is
nonzero. Replace “covers at most as many levels” by the thresholded count
actually proved in L4. An energy-dependent comparison or a bound on an
omitted trace is not excluded by these lemmas.

**Product-direction transfer HOLDS (100).** If growth is uniform in x_1,
the cell complex is S^1 times a finite complex M. Faces entirely in M
contribute a bounded gauge-invariant multiplication factor. Faces crossing
successive x_1 layers correspond to the edges of M and give the product
Wilson convolution. Gauge averaging therefore gives M_M C_M P_M M_M,
positive and trace class by exactly the fixed-box algebra. Lemma A compares
two such complexes with the same M. This is an extension of that algebra,
not a direct application of CA-II's rectangular-torus statement.

**Schatten Hölder HOLDS; the zigzag interpretation needs even n (101).**
The mixed kernels are smooth on compact spaces (indeed factor through the
trace-class C_B), so the indicated Schatten norms are finite. The norm
identity ||A||_n^n=Tr((A* A)^(n/2)) holds for every integer n>=2.
It is a partition function of n alternating steps only when n is even.
Odd products can instead use an even replication or different even Hölder
exponents. A fractional power is not a literal polygon complex.

**Shear identities HOLD AFTER CORRECTION (66, 106).** Let tau translate by
one site, not by k sites before taking tau^k. Unweighted averaging over k
projects onto p=0. To obtain Pi_p use
(1/b_1) sum_k exp(-ikp) tau^k. Positivity and uniqueness of the vacuum make
its translation eigenvalue 1. Thus S=sum_p S_p exactly. This decomposition
does not itself improve the full trace; an ordering of the sector minima
is neither supplied nor sufficient to count their multiplicities.

**The marginal LSI implication HOLDS (108–113).** The Dirichlet form and
test class must be those stated: a smooth simultaneously gauge-invariant
function of the transported pair, with the sum of the two tangential
gradient norms. Applying a uniform parent LSI to such cylinder functions
gives the same constant. The marginal is the raw, axial-gauge pair law
J(u,v)=lambda_0^(-1) Omega(u)T_0(u,v)Omega(v), not the independently
gauge-averaged pair kernel. In temporal gauge its finite-T density is
T_0(u,v)(T^(T-1)P)(v,u)/Z_T. The normalized second factor tends to
Omega(v)Omega(u); smooth bounded tests and their bounded gradient squares
permit passage to the LSI limit, including z log z at zero. The hypothesis
is a uniform LSI for these actual finite-T laws. No such estimate is proved
here. The cited ceiling for one vertex-block criterion does not exclude
every parent-law or averaged criterion.

**The E2 slack identity HOLDS (130–132).** Substituting
log W(t,y)=ell ty+t kappa(y)+g(t;y) gives
U-g_h=D_H+t kappa(h)+(h/b)t[g(t';b)/(b-t')-kappa(b)].
Each term is nonnegative by Lemma A, K or X, respectively. The ideal-gas
formulas are algebraically correct in that model. Their extrapolation to
the free field is the part the author properly withdrew after C1.

**Sharpness of (T) HOLDS in the abstract class (140), with a narrower
conclusion.** No recalled Ising claim is needed. Take
Z(n_1,n_2,n_3,n_4)=1+exp(-mu product_i n_i), mu>0, and T_B with eigenvalues
1 and exp(-mu |B|). This family is symmetric, has positive trace-class
transfers with simple tops and finite ell=0, and satisfies
S(qa;B)=S(a;B)^q exactly. It rules out a universally strict improvement
from one seed value and these abstract properties. It does not rule out
improvements using extra model or geometric information.

**The HC consumer implication HOLDS (154–168).** Keep its exact sufficient
constant, rather than a rounded decimal:

    K_a(r) = [log(72 beta r^3 / log(1+t(r))) + 3 log a]/(a-2).

Proposition HC then gives S(a;(ra)^3)<=t(r). For r=4 use t=1/25;
Corollary BR-J supplies HC at this rate if alpha_J>=2 beta K_a(4) and
K_a(4)<=1. This last condition holds for even a>=26 at both endpoint
couplings 2.3 and 2.6; the expression decreases with a and increases with
beta. The table's r=24 row deliberately uses the stricter old choice
log(22/17), not log(1.3). With that convention its rates are approximately
0.936 and 0.811 at beta=2.3, a=30. The new alpha_J requirement is about
3.731, so 3.73 must not replace the exact expression as a sufficient lower
bound. At a=40 the new rate is about 0.6204 (0.621 is a conservative rounding).
The r=4 row minimizes the listed constants, not all possible shapes.
For a hand comparison, 64/log(1.04)<64/0.0392<1633, whereas the r=6,
r=3 and refined r=2 ratios exceed 2160,2700 and 4400 respectively.
The remaining two ratios are larger still. Also C_beta(4)<13 throughout
beta<=2.6 and log 26<10/3, so K_26(4)<23/24<1; this avoids using rounded
table values to establish the admissible branch.

For composition, 22.2s_k<=(22.2s)^(2^k) with s<=1/25, hence s_k tends to
zero. With N=2a_k, (4a_k)^3=(2N)^3 and S(N;(2N)^3)<=s_k^2<1/5041 once
s_k<1/71. This supplies the claimed conditional SEED-FP implication.
The necessary condition concerns E_1 over every invariant sector. The
additional identification E_1=m_G and the assertion that flux states are
already heavy at side 120 (167) are not proved and must remain assumptions.

## Fact tests and GUIDE arithmetic

**The Gaussian/photon lower bounds HOLD (175–176).** The six distinct
momenta on a cube b=2a have epsilon=2 asinh(sin(pi/b))<=2pi/b. Expanding
the positive oscillator product gives S>=6 exp(-pi); two photon
polarizations give 12 exp(-pi). The displayed decimals 0.259 and 0.518
are conservative. Even the elementary bounds >1/4 and >1/2 suffice.
The compact Gaussian theta factors are at least one for every R>0.
This checks that exact Gaussian model, not compact Wilson U(1)'s Coulomb
spectrum; line 177 correctly leaves the latter recalled.

**Frozen-group count HOLDS for fixed B and a as beta tends to infinity
(179).** For the faithful Wilson representations of Q_8, 2T and Z_2,
c_beta tends to the indicator of the identity. Thus on the finite link
space T_beta tends in norm to |G|^(-|E|) times the projection onto
gauge-invariant functions supported on flat configurations. There are at
least eight distinct flat gauge orbits: the three central holonomies are
chosen independently from {1,-1}. All nonzero eigenvalues of the limiting
operator are equal. Consequently S(a;B) tends to the dimension of that
range minus one, at least seven. No uniform rate or joint limit in a,B,beta
follows. Strict Fourier positivity needed by NO-OP also holds here: the
faithful representation and its conjugate generate all functions on a
finite group by polynomial interpolation, and each tensor degree appears
with positive coefficient in the exponential. This is not an argument for
every compact-group action, beta=0, or the spin Ising model's different
configuration space.

**SMALL-BOX remains a conditional/recalled test (181).** The claimed
large-beta SU(2) spectrum was not derived in row 960. In particular, an
energy of order 1/b at fixed b does not itself tend to zero with beta.
The sound conclusion is that SH' keeps the original finite-box hypothesis;
it supplies no beta-uniform small-box seed. Do not count the word PASS as
a verification of the recalled SU(2) small-volume spectrum.

**The fixed-time countermodel HOLDS (183), with corrected wording.** In
the compact Gaussian model, choose nonzero integer momenta with
|n|<=L/(2pi a). Their energies obey a epsilon<=1, and their number grows
as (L/a)^3. Their thermal weights already diverge at fixed a. Thus no
finite F of fixed small-box data, independent of L, bounds S(a;L^3)
throughout this class. A valid bound may instead depend explicitly on L;
it need not change time unless it is meant to keep the seed uniformly
small. The extensive quantity is g=log(1+S), not S itself.

All three saved scripts and all three saved logs in `guide/lane960/` were
read. No new numerical job was run. The following checks cover the stated
model, formulas, log arithmetic and claimed interpretations; they do not
certify floating-point quadrature or use it as proof.

- **Model (189): HOLDS.** A one-mode kernel is exp[-A(x^2+y^2)/2+xy],
  A=1+K/2=cosh epsilon. Gaussian integration gives W=sqrt(A^2-1),
  lambda_0=sqrt(2pi) exp(-epsilon/2) and successive ratios exp(-epsilon).
  Tensoring gives exactly the scripts' e0 and thermal g. The independent
  finite determinant formula is log Z=(V_4/2)log(2pi)
  -(1/2)sum_q log(m^2+4 sum_mu sin^2(q_mu/2)), manifestly symmetric.
- **C0: HOLDS AFTER CORRECTION.** The code compares relative errors in
  log Z, not in Z. The saved worst value is 1.3815624e-15. All 48 printed
  E2 rows have U>=g; their displayed slack residual is at most 1.1e-16,
  not literally 1.0e-16. The Q check is only a saved no-violation report;
  the written inequality above is its proof. The C0 implementation does
  not assert the slack check or stop on every failure as its protocol said.
- **C1: HOLDS for its stated GUIDE comparison.** The code's N,D,X are the
  exact slack formulas with ell approximated by a 4096-point midpoint sum.
  There are 20,20,8 rows for masses 1,1/2,1/4. The ratio exceeds 0.1 in
  16 of the middle rows and all eight last rows, hence 24/48. At the quoted
  example, .00528+.00000252+.0506 is approximately .2326-.1767.
  D/X is below 5e-4 in the displayed rows; N/X reaches about 0.263.
  Tiny D values near cancellation precision are not certified. The test
  refutes the proposed *free-field* negligibility, not the ideal-gas algebra.
- **C2: HOLDS as logged.** The script uses log(1+expm1(g(a))^q)/g(qa),
  exactly the stated ratio. The logged extrema round to 4.4–30, 12–720
  and 51–3.0e5. In the dilute regime, writing the low levels as M copies
  of exp(-ma) gives the stated M^(q-1) factor. Neither log extrema nor
  that approximation proves monotonicity in the box size.
- **C3: HOLDS AFTER CORRECTION.** Let p_L(x) be the large vacuum's kept
  marginal and q_s(x)=|Omega_s(x)|^2. Conditional Cauchy–Schwarz gives
  max overlap^2=(integral sqrt(p_L q_s))^2. Gaussian integration gives
  sqrt(det W_s det W_M)/det((W_s+W_M)/2), with W_M the Schur complement.
  This is exactly the code. It optimizes states with *fixed kept marginal*
  q_s, not all mixed-transfer lens states: multiplication by M_L and C_s
  generally changes that marginal. Bare scalar pullback is not even an
  L2 isometry for Lebesgue measure on the dropped coordinates. Therefore
  the data do not establish an area law for the gauge J or for all Y phi.
  The recorded single-plane numbers fit the reported approximate area
  trend. The doubling range over the full log is 0.00333–0.00965 per kept
  site, not 0.0033–0.0048; the narrower range describes the b=6,c=4 rows.
  The recheck's eigenvalue determinants agree with three old values, but
  its slogdet path still raises warnings in two cases. This is a useful
  cross-check of those cases, not a root-cause diagnosis of every warning.
  The side-720 figure is an explicit extrapolation, not a measured overlap.
- **C4: raw crossings HOLD; claimed SH' box saving HOLDS AFTER CORRECTION.**
  The logged first integer crossings for 1/550 are a=10,19,37 at masses
  1,1/2,1/4. The script searches all integers; SH' at q=3/2 requires even a.
  The odd crossings cannot be used for that theorem without another bound.
  For comparison, the old 1/1650 crossings are 12,22,42. The next admissible
  candidates for SH' are 10,20,38; their thermal values were not recomputed
  here. If they pass, the savings would be 2,1,1 in ma and the volume
  savings 1-(5/6)^4, 1-(10/11)^4, 1-(19/21)^4, about 52%,32%,33%.
  The printed 40–52% claim used inadmissible odd times in two rows.
  Here m is the action's mass parameter; the exact inverse temporal
  correlation length is 2 asinh(m/2), so “correlation lengths” is approximate.

## Verdict register

HOLDS always refers to the displayed mathematical claim on its stated
domain, not establishment of an open input in SU(2). Rows marked recalled
or GUIDE retain that limitation. The detailed findings above supply the
corrections; no author file is changed.

| Source statement | Verdict | Scope or correction |
|---|---|---|
| 35–39: fixed-box objects, static inputs, GAP-R quotation | HOLDS | E2/B3/SH use their stated abstract transfer hypotheses; GAP-R remains conditional on BR-gap and the variance form of Lemma J. |
| 41: account's chessboard statement | HOLDS AFTER CORRECTION | CA-II's parameter s gives tiles of side s/2, not s. The lemma concerns rectangular tori; it does not cover arbitrary growth complexes. |
| J1, J2 (53–54) | HOLDS | Product Haar, isometry, conditional expectation and gauge intertwining. |
| J3 (55) | HOLDS AFTER CORRECTION | Eight centre sectors. |
| J4 (56) | HOLDS | For the specified insertion in direction 1. |
| J5 (57) | HOLDS AFTER CORRECTION | Composition and straight decimation hold; keep only the surviving translation symmetries. |
| Mixed kernels and polygon integral (60–64) | HOLDS | Positive preserving; adjoint maps between different spaces. |
| G1 (65) | HOLDS | Missing incidences and five-edge faces exclude the rectangular Wilson cellulation. |
| G2 (66) | HOLDS AFTER CORRECTION | Unit translation tau; this is the described shear torus, not a classification of every geometry. |
| G3 (67), projected-averaging exclusion | FAILS | Explicit normalized-Haar-average counterexample above; actual Balaban map not analyzed by that assertion. |
| G3, open restriction and weighted extension | HOLDS | Open faces leave the family; unital weighted pullback requires weight 1. |
| Lens identity, two reflection forms and CS (70–74) | HOLDS | Reflected half-paths, finite traces; no assertion of all mirrors on arbitrary complexes. |
| Static numerator/denominator description (76,80) | HOLDS | These are the ingredients of E2, not necessary forms of every possible proof. |
| DEN (82–85) | HOLDS | One E2 denominator substitution. |
| DEN's global “no room” use (86,152,214) | HOLDS AFTER CORRECTION | At most g/23 for that one-side, seed-time comparison; no universal exclusion. |
| L1, L2, L3, L4 (89–92) | HOLDS | L4 counts weights above a threshold; use finite small-box trace. |
| L5 inequality and coverage reading (93) | HOLDS AFTER CORRECTION | Conditional inequality holds; positive uniform coverage is impossible here, and nonzero weights need not be finitely supported. |
| NO-OP (95–96) | HOLDS | beta>0, the specified Y, at least one insertion, last step an insertion. |
| Linear trace loss / ideal-gas claim (97) | HOLDS AFTER CORRECTION | For matched times in the stated extensive-g model; not a bound for arbitrary t,t' or every geometry. |
| Product-direction transfer (100) | HOLDS | Direct construction on S^1 times M. |
| Schatten bound / zigzag (101) | HOLDS AFTER CORRECTION | Even n for literal zigzag partition functions. |
| “Only bounded side”, crossing and table of dominance (102–104,114–125) | HOLDS AFTER CORRECTION | The displayed inequalities give no new rectangular numerator bound. They do not prove absence of other comparisons. |
| Shear and momentum resolution (106) | HOLDS AFTER CORRECTION | Fourier weights for p other than zero; no gap-ordering or counting theorem. |
| Marginal LSI / local parent (108–113) | HOLDS | Conditional on the uniform LSI for the actual transported finite-T laws and the matching Dirichlet form. |
| E2 slack identity (129–132) | HOLDS | Three nonnegative slacks; ideal-gas inference limited to its model. |
| OVL formula / numerical seed-time consequence (136–138) | HOLDS | S<=0.3 and trial time exactly a. |
| OVL for all trial times or all lenses (138,214) | FAILS | Long trial times only require nonzero overlap when kappa(h)>0; C3 does not test all lens states. |
| Gluing / no crossing / sharpness reading (139–140) | HOLDS AFTER CORRECTION | Gluing is heuristic; (T) is sharp from one seed in the abstract class, not against extra geometric data. |
| Lemma Q, SH' and r=2 threshold/rate (142–146) | HOLDS | Integer j; pa,qa integers; even a for q=3/2; K=541.1. |
| Other-step comparison (147) | FAILS | q=8/5 is strictly better than q=3/2 on the interval just proved, not slightly worse. No optimality claim for the other exploratory choices is verified. |
| Integer-q correction and consumer threshold (148–149) | HOLDS | Lemma Q removes the integer-q restriction while retaining integer times. |
| One-particle size estimate (150) | HOLDS AFTER CORRECTION | log 3 is the leading exponential estimate; the prefactor and admissible times are extra costs, not verified by that estimate. |
| HC table and BR-J consequence (154–166) | HOLDS AFTER CORRECTION | Exact constants control sufficiency; r=24 uses its stricter old x_*; decimal rates are approximate. |
| Necessary energy and physical identification (167) | HOLDS AFTER CORRECTION | E_1>=K'_a holds conditionally; E_1=m_G at side 120 is additional unproved physics. |
| SEED-FP composition (168) | HOLDS | The r=4 SH recurrence followed by time doubling. |
| r=4 Gaussian rate test (169) | HOLDS | epsilon_min<pi/(2a)<1.6/a against K'_a>12.5/a at the stated couplings. |
| 5.1 Gaussian/photon bounds (174–177) | HOLDS | Exact Gaussian models; Wilson U(1) assertion remains recalled. |
| 5.2 frozen groups (179) | HOLDS AFTER CORRECTION | Fixed a,B, beta to infinity; no rate or joint-limit conclusion. |
| 5.3 SMALL-BOX (181) | HOLDS AFTER CORRECTION | Hypothesis retained; recalled SU(2) spectrum not verified. |
| 5.4 fixed-time countermodel (183) | HOLDS AFTER CORRECTION | No L-independent finite bound throughout the class; L-dependent extrapolation remains possible. |
| 5.5 “each valid in the whole class” (185) | FAILS | G3 is false; NO-OP needs injectivity and the specified gauge-link map, not just abstract transfer positivity. |
| GUIDE model (189) | HOLDS | Massive lattice scalar with Lebesgue integration. |
| C0, C3, C4 (192,195–196,202,205–206) | HOLDS AFTER CORRECTION | Logarithmic error, narrower state class and ranges, even-time restriction; no rerun claimed. |
| C1 and C2 (193–194,203–204) | HOLDS | Model formulas and saved-log arithmetic, with numerical limitations stated above. |
| Global no-gain / stop-queuing recommendation (152,208,212–218,253) | FAILS | The support does not exclude the advertised route family. The narrower result is that this note supplies no improving variable-geometry bound. |
| Open seed and LSI-J (247) | HOLDS | Neither is proved or attacked by this check. |

The failures are grouped, not ten separate new research problems: the
unsupported exclusion of geometry; the false averaging claim; the
overlap/time/state-class conflation; the unproved physical identification;
the GUIDE consumer's parity and range errors; the reversed q=1.6 comparison;
and the minor algebraic and source-scope corrections in the register.
The first three break the negative recommendation. None breaks Q, SH', or the conditional HC box
change.

## Source and verification limits

- Target SHA-256:
  `19f3c93e78fc77dd4757d0c8727cb203eed34e8fe248735968fd154d102550a4`.
  A 14-file hash/line inventory is in the scratch `source-manifest.json`.
- Outline lookups used README, chunk-02:86–108, chunk-03:8–37,
  chunk-05:62–72 and obligations:66–88. Primary excerpts read were
  2195–2257, 2313–2335, 2773–2832 and 5631–5652. These respectively supply
  the fixed-box coefficients, transfer identity, reflection geometry and
  actual averaging definition. No missing-proof claim about the entire
  account is made from an absence of title matches.
- CA-II `8.7:lem-chessboard-torus` was located through the full index and
  neighboring entries, then read at 108696–108795. Its statement, not its
  entire proof, was checked for faithfulness. The lens/product arguments
  above do not import it outside its rectangular domain. CA-I was downloaded
  as requested; no 4.12–4.19 result is needed in this check. No Balaban PDF
  or OCR text was used.
- The exact local predecessors read were SH 1.1–1.5 and its Gaussian-model
  formula; K/X/E' in `gap-crux-restate.md`; the transfer definition, gauge
  algebra and positive coefficients in `gap-transfer.md` and Lemma 1.1 of
  `gap-seed-check.md`; Proposition HC at `gap-direction-max.md:305–321`;
  BR-J at `gap-fc-max.md:487–527`; and GAP-R at
  `gap-lsij-scale-opus.md:122–128`. The full upstream BR theorem and Gaussian
  LSI are named inputs, not newly checked here.
- No numerical job, simulation, eigenvalue calculation or quadrature was
  rerun. All GUIDE verdicts are code/model/arithmetic checks against the
  saved artifacts. Claims of empirical Coulomb behavior, the SU(2)
  small-volume spectrum, and flux heaviness at side 120 were not verified.
- Only this report is changed in the repository. It is local and unpushed
  on `check/gap-vargeom-astra-9e785dd87`; no external post or status update
  is made. The user-requested research format and verdict vocabulary take
  precedence over the generic check-record/status procedure.

RESULT: HOLDS — Lemma Q, SH' with threshold 1/550 at ratio 2 and even a, and the conditional ratio-4 HC/BR-J seed route (K_30 approximately 0.811 at beta 2.3); HOLDS AFTER CORRECTION — the mapped symmetry, overlap, Hölder, model and GUIDE claims listed above; FAILS — the exclusion of projected averaging, the claimed q=1.6 ordering, and the support for the broad “varying geometry buys nothing” recommendation. The seed and LSI-J remain open; no status is granted.
