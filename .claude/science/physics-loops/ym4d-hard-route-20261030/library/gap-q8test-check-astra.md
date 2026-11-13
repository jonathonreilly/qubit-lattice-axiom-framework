## Repo search

This is the check requested in FINISH row 854 of row 843, authored by Claude Opus 5.5.
The source checkout is pinned at `aa4aa2af728f5c3159fbd319b1e1fa520f2d09c8`.
No `library/prior/gap-q8test-check-astra.md` exists at that revision.
The lead's `prior/repo-search-2026-11-08.md` concerns the earlier RG targets, not this Q_8 check.
Its source table, search scope, relevant transfer locator and recovery decision were inspected;
neither it nor row 854 supplies a previous check of row 843.
The following bounded follow-up used actual source text, not that digest as proof:

| Hit checked | Source and closeness |
|---|---|
| Main, `bb4ec020d5ada57c630dd89acc98a68397ade423` | `docs/BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md:25–45,225–250` gives the Hurwitz-quaternion realization of 2T. Its group enumeration is not used. `docs/CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md:34–48` concerns a different fermion model. Neither proves this filter or its Wilson exposure. |
| PR 10114, `f76f6c649cff7dffbab664d8976e680e8f287fe9`; PR 10133, `89faef229ff6e6bde42baad15ed8270c2f4087d8` | Their `ym4d-proof/briefs_hrp/AUTHOR_BRIEF_HRP.md:55–75` requests finite-group reflection-positivity tests. It is a brief, not a filter result. PR 10114's `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–166`, located through EX and the prior digest, supplies the already-existing normalized Wilson convolution and full transfer. Credit its Codex author; this transfer is reused. |
| PR 10134, `1e70c7211a2cdbc39001e619f1dd89db45e25851`; PR 10141, `fb99b4dddc7254e6124ac124887d58eeb3a77802` | Searches for `gap-q8test`, `binary tetrahedral`, and `commutator contraction` found the same two general main-note paths, without a target-specific result. These are retrieval results, not an absence theorem. |
| Local AS, TR, VO, EX | `gap-assume-opus.md:350–411` already contains F1–F5, including the moment and contraction inputs. `gap-tree-astra.md` supplies (G3), pair filters, the earlier charged filter and the non-exposure example. `gap-vortex-astra.md:256–443` supplies the word and conditional argument; `gap-expose-astra.md:90–175` supplies (E1)–(E4). These are credited to their printed Codex and Claude authors and checked only where the requested source consumes them. |

Searches of `open-registry.md`, `open-core.md` and `l17c.md` for the target name, Q_8,
tetrahedral and high-spin rarity found no competing owner of this check. HS and LS were not attacked.
The intended prior result is row 843 itself; this lane checks it rather than redoing that research.

The SA index was consulted first: README, chunk 02's neighbouring rows and obligations 63–76.
They locate outline 2195–2243 (GL3–GL4) and 2313–2335 (half-kernel transfer, GL8), read directly.
These are proved inputs of **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**.
Searches of the 4.12–4.19 and full CA indexes for this representation target found no matching item.
Both requested TeX files were downloaded once at `31a47c543775`; no whole manuscript was read.
No Balaban formula is needed for this finite-group check. Search logs remain in the scratch directory below.

Checker: Codex, row 854 (requested model/effort: gpt-6-astra/xhigh), outside the Claude author session.
This is a line-by-line research check, not an audit or a grant of scientific status.
Source SHA-256: `832e393c384b0203aa182d85bc8ef189e5511274bca42199580aa075029c4c94`.

## Checkpoint

Completed the requested source reading and statement checks in the requested order.
The output was created first and extended after each check; only this output file was changed.
The core filters survive. Local proof repairs, the L2 restriction failure, the false maximality claim,
and the flat-plane normalization correction are recorded below. HS and LS remain open.
No numerical run, computer-assisted proof, new subagent, audit or external post was used.
GUIDE tables and empirical freezing values were not independently verified; no verdict relies on them.
The next action belongs to the source author: apply the explicit corrections, preserving the open Wilson estimates.
Downloaded sources belong to `/tmp/sa-gap-q8test-check-astra.045PfO`.
Delivery is local, uncommitted and unpushed, on `research/gap-q8test-check-astra-aa4aa2af7`.

## 1. Lemma 1.5 — HOLDS

Checked line by line. The character-average numerators, before division by the group order, are

| integer spin l | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Q_8: 2(2l+1)+6(-1)^l | 8 | 0 | 16 | 8 | 24 | 16 | 32 |
| 2T: preceding row +16b_l | 24 | 0 | 0 | 24 | 24 | 0 | 48 |

Here b_l is the repeating sequence 1,0,-1. Dividing by 8 and 24 gives both printed rows.
Clebsch–Gordan and the alternating form on V give n_G(j)=m_G(j-1/2)+m_G(j+1/2).
Thus all ten listed multiplicities agree. For Q_8 the only odd irreducible is V.
For 2T, the spin-3/2 character is (4,-4,0,-1,1) on the five trace levels;
its inner products with (V,V',V'') are (0,1,1).
The spin-5/2 character is (6,-6,0,0,0), giving (1,1,1).
This checks the restrictions used by both low-spin filters.

The same formulas give m_Q8(3)=m_2T(3)=1, needed for the sextic invariant.
The general least-spin assertion follows for half-odd-integer spins once the cited invariant degrees are supplied;
no integer-spin restriction is being claimed.

## 2. Theorem 3.4(v), all beta ranges — HOLDS AFTER CORRECTION

The separation inequality holds. The printed arithmetic needs two local repairs and one denominator correction.
All decimals in this section denote exact rationals.

For x>0 and integer n>=0 with x<n+2, use the elementary positive-series bound

\[
 \sum_{k=0}^n\frac{x^k}{k!}<e^x<
 \sum_{k=0}^n\frac{x^k}{k!}
 +\frac{x^{n+1}}{(n+1)!}\frac1{1-x/(n+2)}. \tag{A}
\]

The tail bound follows because each subsequent term ratio is at most x/(n+2).
For x=1,n=9 it gives e<271829/100000.
Squaring 16488/10000 gives 2.71854144>2.71829;
cubing 2.71829 gives a number below 20.086.
Hence e^(7/2)<20.086(1.6488)=33.1177968<33.12.
Therefore (7/2)^4 e^(7/2)<150.07(33.12)<4971<5760.
Monotonicity covers 0<beta<=7/2.

For 7/2<=beta<=6,

\[
 P(6)\le\frac{12^5}{15\cdot17\cdot19\cdot21\cdot23}
 =\frac{248832}{2340135}<\frac{107}{1000}<\frac12.
\]

The strict rational comparison is 248832000<250394445.
Lemma 3.3(b) supplies the comparison eigenvalue at least 1/2.

For beta>=6 put s=beta/2. The derivative of each
(c e^(-ks))(11+2s) is negative for s>=3.
The printed inference e^3>20.08 implies e^(-3)<0.04980 is invalid:
20.08(0.04980)=0.999984<1.
Repair it by the positive Taylor sum through degree 12:

\[
 e^3>\sum_{k=0}^{12}\frac{3^k}{k!}
 =\frac{9620848953}{479001600}>\frac{4017}{200}=20.085.
\]

The last comparison is the integer inequality
9620848953>9620747136. Writing q=200/4017, direct multiplication gives
q<0.04980, q^2<0.00248, q^3<0.000124, q^4<0.0000062.
Thus g(3)<0.2155804<0.2157, and 17g(3)<3.6669<11/2.
This supplies the full beta>=6 range. Lemma 1.4 then supplies Q_8.

For U(1), the small-beta bound has the larger threshold 11520.
On [7/2,7], the exact product is

\[
 P(7)\le\frac{14^5}{17\cdot19\cdot21\cdot23\cdot25}
 =\frac{537824}{3900225}<0.138.
\]

The printed denominator 121882.4... should be 121882.03125.
The k=3 term of I_0(7/2) is 117649/147456, which is below 0.7979.
Replace that lower bound by 0.7978. The first five terms then give
I_0(7/2)>1+3.0625+2.3447+0.7978+0.1527=7.3577>7.35.
Consequently I_1/I_0>1-2/7-1/7.35>0.57 throughout this interval.
For beta>=7, expand
(1/beta+64/beta^4)(11+beta)=1+11/beta+64/beta^3+704/beta^4;
it decreases, and at 7 equals 18/7+1152/2401<3.06<11/2.
There are no uncovered beta intervals or endpoint losses.

## 3. Corollary 3.7, the beta=2.2 endpoint — HOLDS

Let y=e^(11/10). Its Taylor sum through degree 5 is greater than
1+1.1+0.605+0.2218+0.061+0.0134=3.0012>3;
each displayed term is a lower bound, including the two small final terms.
With the numerator N and denominator D of Lemma 1.2,

\[
 4N-D=\frac32y^2-\frac52y^{-2}+4y-12y^{-1}-3.
\]

Its derivative is 3y+5y^(-3)+4+12y^(-2)>0.
At y=3 its value is 164/9>0. Since D>0, r_V^(2T)(2.2)>1/4.
Lemma 1.3 propagates this bound throughout [2.2,3.5].
The companion upper bound is 343/1680<41/200=0.205<1/4.

## 4. Proposition 2.2(v) — HOLDS

Read VO sections 4–5, lines 256–443. The finite-group extension keeps the same torus and word W_a.
Each selected link enters at most six plaquettes. A signed Wilson plaquette exponent has oscillation at most 2 beta.
For two links the total oscillation is at most 24 beta, whether or not some plaquettes are shared.
Thus the conditional density relative to two uniform G-variables lies between delta and delta^(-1),
where delta=e^(-24 beta). The based loops separately use one selected link once;
left and right multiplication by fixed elements of G preserve uniform measure.
Their law is therefore delta times product Haar plus (1-delta) times a probability law.

Haar commutator averaging in V is I/4 for both groups. Every residual average of unitary matrices has norm at most one.
Each conditional matrix expectation consequently has norm at most delta/4+1-delta=rho_beta.
Different selected pairs are conditionally independent: no plaquette meets two pairs.
The paths through the unselected layer stay fixed under this conditioning.
Therefore the ordered product of the expectations has norm at most rho_beta^N,
N=floor(a/4)^2. Normalized trace and exterior integration preserve the bound.
For a>=8, N>=a^2/64. This proves the exact (10) and its interval version.

The auxiliary L^2 bound (9) also follows from probability-convolution contraction.
Even its weaker bounded-function statement survives: for either finite group K=I/4 on all odd functions,
so the conditional sup-norm coefficient is at most 1-3delta/4, stronger than 1-delta/2.
The density comparison (7) is not used. Neither this word nor this calculation bounds the electric flux sector.

## 5. Lemmas 1.1–1.4, closed-form eigenvalues — HOLDS

The trace multiplicities are (1,1,6) for Q_8 and (1,1,6,8,8) for 2T.
The noncentral 2T elements with trace +/-1 have centralizers of order six,
so their conjugacy classes have size four; the quotient by Q_8 separates inverse order-six classes.
Q_8 is normal, the quotient is cyclic of order three, and commutators with its cyclic generator
produce i,j,k. Hence [2T,2T]=Q_8; [Q_8,Q_8]={+1,-1}.

For Q_8 the four even characters and V exhaust the dimension squares 4+4=8.
For 2T the even quotient A_4 has three characters and its irreducible three-dimensional rotation module.
The three distinct odd modules V,V tensor omega,V tensor conjugate(omega) then exhaust 3+9+12=24.
Irreducibility of V follows already from i and j having no common invariant line.
Schur averaging and trace determine each scalar, including multiplicity spaces.
With D_Q=cosh(beta)+3 and D_T=cosh(beta)+3+8cosh(beta/2), direct weighted sums give

\[
 z_Q=D_Q/4,\quad z_T=D_T/12,\qquad
 r_V^Q=\frac{\sinh\beta}{D_Q},\quad
 r_V^T=\frac{\sinh\beta+4\sinh(\beta/2)}{D_T},\quad
 r_{V'}^T=r_{V''}^T=\frac{\sinh\beta-2\sinh(\beta/2)}{D_T}.
\]

The twisted-character sum over either eight-element trace level replaces 8 by -4.
These formulas have the correct dimensions and normalization; in particular r_{V'}^T>0 for beta>0.
For a subgroup on which V is reducible, Lemma 1.3's r_V denotes the normalized character mean,
not automatically a scalar eigenvalue. Its stated mean and variance identity still holds.
For the groups used here V is irreducible, except U(1), whose two eigenvalues agree by symmetry.
The derivative is strictly positive for these groups because x has more than one value.

For Lemma 1.4, putting c=cosh(beta/2), the quotient of the Q_8 mean by the complementary-coset mean
is 2c^2/(c^2+1)>1 for beta>0. The positive mixture weights give the claimed strict ordering.
At beta=0 both means vanish, so the division argument is used only at beta>0.
The SU(2) and U(1) Bessel normalizations agree with outline (GL3) divided by c_0 and Fourier integration.

## 6. Proposition 2.1, including the 2T pair — HOLDS

For N>=2, pi/(2N)<1 forces both Q_8 generators to be the identity.
For 2T the same argument applies when N>=4, using its gap 1/2.
At N=3 a commutator lies in Q_8, which has no half-trace 1/2.
For the printed a,b at N=2, quaternion scalar-vector multiplication gives

\[
 ab=(1+i+j-k)/2,\quad ba=(1+i-j+k)/2,\quad
 ab(ba)^{-1}=j.
\]

The generator costs are 1/2, and the commutator cost is 2.
The bounds pi>3 and pi<4 suffice for every numerical comparison here.
In U(1) a commutator is the identity, whose half-trace never equals cos(pi/N) for finite positive N.

## 7. Proposition 2.2(i)–(iv), commutator contraction — HOLDS

For an irreducible unitary rho of dimension d, averaging A first gives
E_A rho(ABA^(-1))=chi_rho(B) I/d.
Matrix-coefficient orthogonality then gives E_B chi_rho(B)rho(B)^*=I/d.
Thus E rho([A,B])=I/d^2. This proof applies to both finite groups.
Their odd irreducibles all have d=2, so K=I/4 on the whole odd space, not just on V.
For Q_8, P(A central)+(P(A noncentral)/2)=1/4+3/8=5/8;
the other 3/8 of pairs have commutator -1. This verifies the measure and sup-norm statement.
Both commutator laws vanish outside their proper commutator subgroup,
where uniform Haar measure is positive. Hence the proposed lower density (7) fails for both.

## 8. Lemmas 3.1–3.3 — HOLDS

For Lemma 3.1 the beta integral gives the stated Bessel series with the correct Gamma factors.
The integration-by-parts boundary term vanishes exactly when nu>-1/2;
its differentiated integrand remains integrable in that full range.
The two expressions for I_(nu+1)/I_nu give E[t]. Its derivative is Var(t)>0,
and reflection of the negative half-interval makes its numerator strictly positive.
Using E[t^2]>=E[t]^2 yields
m^2+(2nu+1)m/x-1<=0, whose positive root is U_nu.
Since sqrt(a^2+x^2)<=a+x, the stated lower bound for 1-U_nu follows.
Differentiation and integration interchange on compact x-intervals by dominated convergence.

For Lemma 3.2 the five adjacent ratios telescope to I_6/I_1.
Each factor is positive, strictly increasing and below one. The three majorants follow respectively
from (GL4), the five U_n bounds, and just the final U_5 bound.
All three are increasing, hence so is their minimum M.
The strict ordering of the half-odd-integer spin eigenvalues follows by removing positive factors below one.

For Lemma 3.3(a), Haar averaging chi_V^n is the dimension of the invariant tensors.
Thus the numerator's Taylor coefficients are nonnegative, with linear term beta/2;
division by 2z<=2e^beta gives beta/(4e^beta). The U(1) argument uses E cos^2=1/2.
For (b), 2N-D=y^2/2-3/(2y^2)-8/y-3 is increasing, and at y=5 equals 196/25.
The degree-four Taylor sum for e^(7/4) exceeds 5, as required.
For Q_8, solving the quadratic in e^beta gives exactly 3+sqrt(12).
For (c), subtracting the closed-form numerators gives
D_T-N_T=e^(-2s)+3+2e^s+6e^(-s); D_T>=e^(2s)/2 gives g(s).
The Q_8 subtraction gives the printed bound as well.
For (d), split the arcsine law at t=0: the positive half costs at most E(1-t^2)<=1/beta;
the negative half costs at most 2P(t<0)<=1/I_0(beta).
The k=2 positive series term is beta^4/64. No large-beta asymptotic is assumed.

## 9. Theorem 3.4(i)–(iv),(vi), and Remark 3.6 — HOLDS

Schur's lemma and the checked restrictions give (i)–(iii), with no missing multiplicity factor.
The polynomial xy(x^4-y^4) is fixed by both displayed Q_8 generators:
the first fixes xy and both fourth powers; the second changes the signs of both factors.
The one-dimensional Q_8 and 2T invariant sextic spaces therefore coincide.
V tensor h_6 is a two-dimensional copy of V; the word “line” in (iii) refers to the invariant factor only.
The U(1) weights in (iv) are exactly +1 and -1 as claimed.
The ratio in (vi) is continuous on a compact interval and strictly below one by section 2 above.
Monotonicity gives its stated explicit endpoint bound.

For Remark 3.6 take k to be a positive integer. Binary forms have no zero divisors,
so h_6^k remains a nonzero invariant. The two SU(2) summands have spins 3k-1/2 and 3k+1/2;
the first has the larger eigenvalue. Its factorial bound tends uniformly to zero for bounded beta.
On a compact interval bounded away from zero, beta/(4e^beta) has a positive lower bound.
This proves the claimed arbitrary compact-interval suppression.

## 10. Corollaries 3.5 and 3.7 — HOLDS

All finite-group restrictions and the two quartic Q_8 invariants agree with section 1.
The SU(2) norm on V tensor Sym^4 V is the larger of r_(3/2) and r_(5/2), hence r_(3/2).
Its 2T copy of V comes from spin 5/2; no invariant quartic for 2T is being asserted.

Here is an arithmetic check of every remaining range, with beta>0.
Bound (A) gives e^2<7.3891 (n=13), e^(1/5)<1.2215 (n=4),
and e^(3/5)<1.8222 (n=6). Their products give e^(11/5)<9.03 and e^(13/5)<13.47.
Thus beta^2 e^beta<48 for beta<=11/5, and beta^2 e^beta<96 for beta<=13/5.
For the Q_8 middle range, e^(11/5)>1+11/5+(11/5)^2/2+(11/5)^3/6>7>3+sqrt(12).
The product at beta=6 is 1728/4845<357/1000<1/2.
For beta>=6, every term of (6e^(-beta)+2e^(-2beta))(7+beta) decreases.
At 6, e^6>400 gives the upper bound
13(6/400+2/160000)=0.1951625<0.2<7/2.
This checks all three Q_8 ranges of Corollary 3.5.

For Corollary 3.7's 2T comparison, section 3 checks [11/5,7/2].
The small range and [7/2,6] use the just-checked bounds and Lemma 3.3(b).
On beta>=6, each term of g(s)(7+2s) decreases for s>=3,
and its initial value is below 13(0.2157)=2.8041<7/2.

For U(1), the interval [13/5,4] uses
512/2145<0.239 and the exact lower series bound
I_0(13/5)>1+1.69+0.714+0.134=3.538>3.53.
Consequently 1-5/13-100/353>0.33.
On [4,7], 2744/6783<0.405 and
I_0(4)>1+4+4+1.777+0.444>11.2, giving a lower eigenvalue bound above 0.66.
On beta>=7,
(1/beta+64/beta^4)(7+beta)=1+7/beta+64/beta^3+448/beta^4
is decreasing; at 7 it is 2+896/2401<2.38<7/2.
These complete the U(1) comparison mentioned in Corollary 3.5's heading but proved only later.

The statement about spin 3/2 having no V copy for 2T is correct.
It excludes that particular fixed-copy mechanism, not every possible spectral separation from 2T.
Indeed its V' eigenvalue already exceeds the SU(2) value for sufficiently small positive beta, as section 12 checks.

## 11. Propositions 2.3–2.6 — HOLDS AFTER CORRECTION to the cited covariance proof

**Proposition 2.3 — HOLDS.** Read SX's definitions of D1 and (C1)–(C7).
They use the unit S^3 metric, three-dimensional link tangent spaces and infinitesimal gauge rotations.
There is no such derivative on the finite configuration set. A replacement finite-chain inequality would be another statement.
The beta<11/48 range and the vanishing U(1) bracket are correctly quoted.
The statements about freezing at order one remain GUIDE, as in AS F6, not established phase theorems.

**Proposition 2.4 — HOLDS AFTER CORRECTION.** The local covariance expansions hold as printed.
The first missing justification is inherited from AS F5: its two-vertex limit proves only that the Q_8 supremum is at least 1/2.
Here is the missing analytic upper bound, which completes the stated equality.

Write c_i=cosh(F_i), s_i=|sinh(F_i)|, S=sum_i c_i, for four coordinates.
After conjugating by coordinate signs, the covariance matrix has entries
C_ii=c_i/S-s_i^2/S^2 and C_ij=-s_i s_j/S^2 for i!=j.
Fix i and put c=c_i,s=s_i,C=sum_(j!=i)c_j,T=sum_(j!=i)s_j.
The absolute row sum is R_i=c/S-s^2/S^2+sT/S^2. Direct expansion gives

\[
 \frac12-R_i=\frac{(s-T)^2+C^2-T^2-1}{2S^2}\ge0,
 \qquad C^2-T^2
 =3+2\sum_{j<k,\,j,k\ne i}\cosh(|F_j|-|F_k|)\ge9.
\]

For an eigenvector, use a coordinate of maximum modulus to bound its eigenvalue by the largest absolute row sum.
Hence Cov_F<=I/2. For F=f(1,1,0,0)/sqrt(2), the transverse vector in AS F5 gives variance
cosh(f/sqrt(2))/(2cosh(f/sqrt(2))+2) tending to 1/2. The supremum is exactly 1/2.
This repair uses no numerical search.

For 2T, moments through degree five equal those of S^3:
all odd ones vanish; at degree four E q_i^4=1/8 and E q_i^2 q_j^2=1/24 (i!=j),
by the axis vertices and sixteen half-coordinate vertices. All other fourth moments vanish by signs.
Taylor expansion of the finite exponential integral and its positive denominator therefore matches covariance through degree three.
In the Q_8 example E[(u.q)^2(F.q)^2]=f^2/8, against f^2/24 on S^3.
Taking half these fourth moments and subtracting the denominator correction f^2/32
gives +f^2/32 and -f^2/96, respectively.
Central symmetry improves the remainder to O(f^4), exactly as claimed.
The SU(2) upper quarter is the cited Theorem V of `gap-vmf-lip.md:58–196`;
the covariance specialization takes phi(h)=h.e. It is attained at F=0.

**Proposition 2.5 — HOLDS.** The triplet averages are scalars:
for Q_8, cyclic permutation of axes and the diagonal rotations give the printed t_Q;
for 2T, irreducibility of the triplet gives
 t_T=(cosh(beta)-1)/(cosh(beta)+3+8cosh(beta/2)).
Both lie strictly between zero and one. The singlet overlap remains -I/2, independent of the averaging group.
Thus the norm bound and strict finite-beta contraction of the two pair filters survive.
Strictness follows because a norm-one vector would have to lie in both singlet ranges, whose intersection is zero.
The degree-twelve invariant dimensions are 4 and 2 by section 1, and their powers are nonzero.
The factorial SU(2) bound and positive fundamental comparison extend the compact-interval filter as stated.

**Proposition 2.6 — HOLDS.** Read JO (J1)–(J10), FL (F11), and RT (R13).
The sign-cochain average, closed-surface decomposition, telescoping identity and uniform polymer majorant
use only the same lattice and |x|<=1. Their sums and normalizations remain unchanged for these groups.
For the leading plane integral, matrix-coefficient orthogonality for the irreducible two-dimensional V gives
integral product(x_p)=4^(-A), just as for SU(2); this supplies (J10)'s leading coefficient.
The finite-group transfer remains positive, so the nonnegativity in (J9) is retained.

For Q_8, E x^(2l)=1/4 for l>=1. For 2T it is (2+16/4^l)/24.
These give every entry of the table. The S^3 recurrence
(2l+2)M_l=(2l-1)M_(l-1) gives 1/4,1/8,5/64.
The sixth-root comparisons reduce to the printed integer inequalities;
the fourth-moment cost in (R13) is shared by 2T and not Q_8.
This is a statement about the proof's moments, not a refutation of any group-specific surface theorem.

## 12. Small-beta expansions in sections 2.4 and 3.3 — HOLDS

All relevant group integrals are entire in beta, and their denominators equal one at beta=0.
Their quotients are analytic near zero; central symmetry makes r_V odd.
The partition functions through their first differing term are

\[
 z_{SU(2)}=1+\frac{\beta^2}{8}+\frac{\beta^4}{192}
                  +\frac{\beta^6}{9216}+O(\beta^8),
\]
\[
 z_{2T}=1+\frac{\beta^2}{8}+\frac{\beta^4}{192}
                  +\frac{\beta^6}{7680}+O(\beta^8),\qquad
 z_{Q_8}=1+\frac{\beta^2}{8}+\frac{\beta^4}{96}+O(\beta^6).
\]

Taking logarithms and then differentiating gives exactly
r_V^(2T)-r_(1/2)=beta^5/7680+O(beta^7) and
r_V^(Q_8)-r_(1/2)=beta^3/48+O(beta^5).
For example 1/7680-1/9216=1/46080 before differentiation.
There is no lost factor of two from x=chi_V/2.

For the spin-3/2 comparison,
sinh(beta)-2sinh(beta/2)=beta^3/8+O(beta^5), while D_T=12+O(beta^2).
Hence r_(V')^(2T)=beta^3/96+O(beta^5).
The Bessel series gives I_4/I_1=beta^3/192+O(beta^5), so their ratio tends to two.
The two character-integral numerators mentioned in section 3.3 both start with (beta/2)^3/6;
the representation dimensions account for the different normalized eigenvalues.
The full-vector covariance expansions were checked in section 11 above.

## 13. Section 4.1(a),(c), exposure in EX (E1) — HOLDS

Read EX lines 90–175 and its prior-transfer locator; read PR 10114's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–166` at f76f6c649cff7dffbab664d8976e680e8f287fe9.
The existing transfer keeps the spatial multiplier and all normalization factors.
The outline's half-kernel transfer (2313–2335) is the same construction before normalized bond convolution.
For unshifted Wilson weights, EX uses exactly

\[
 L_m=z^{|E|}K^{1/2}B_mK^{1/2},\qquad K=\bigotimes_e C_\beta.
\]

On a fixed edge, Pi_j C_beta=r_j Pi_j. Thus the kinetic convolution already contains the high-spin scalar.
The two half factors carry sqrt(r_j); across a kinetic step they give r_j.
No Haar projection is replaced by a contraction, so (G19)'s factorization cost does not apply to this observation.
This does not give an upper bound for the full L_m by M: B_m mixes edge spins.
The global factor z^|E| remains present.

For finite G, expansion of exp(beta chi_V/2) in tensor characters has nonnegative multiplicities.
Every irreducible of Q_8 or 2T occurs in some tensor power of V (faithful matrix coefficients separate the finite group).
Thus every convolution eigenvalue is strictly positive for beta>0.
The same gauge-averaged half-kernel construction gives L_m^G with z_G^|E| retained.
The temporal twist is the central-sign operator Theta; the untwisted and twisted traces give EX (E3).

Each Pi_j commutes with left and right translations, hence with gauge projection and all edge signs.
For any spin-bin projection Pi, Q=P_-Pi is an orthogonal projection on the physical Hilbert space.
Positivity and trace class of L_m give, for integer t>=1,

\[
 \|L_m^{t/2}Q\|_{HS}^2
 =\operatorname{Tr}(Q L_m^t Q)=\operatorname{Tr}(Q L_m^t)\ge0.
\]

No commutation between Pi and L_m is needed. Summing a finite or countable orthogonal resolution
and using positivity/trace convergence gives the claimed one-slice law, in either parity sector.
It is not a positivity statement about products of noncommuting selectors at several time slices.

## 14. Section 4.1(b), the restriction identity — FAILS as an L2 statement; corrected identity HOLDS

There is no restriction map R:L2(SU(2))->L2(G) for a finite subgroup G.
The functions zero and the indicator of G represent the same SU(2) L2 vector but have different restrictions.
Even on continuous functions restriction has no bounded L2 extension:
f_n(g)=((1+x(g))/2)^n has SU(2) L2 norm tending to zero by dominated convergence,
whereas f_n(1)=1 makes its L2(G) norm at least |G|^(-1/2).

The precise repair is to define R only on the algebra of finite sums of SU(2) matrix coefficients.
For such f, the displayed double sum is finite and

\[
 RC_\beta f-C_\beta^G Rf
 =\sum_{j,\,\rho\subset V_j|_G}(r_j-r_\rho^G)\Pi_\rho R\Pi_j f.
\]

Indeed restriction of a spin-j matrix coefficient is a matrix coefficient of V_j restricted to G.
Decomposing that finite representation gives exactly the rho-blocks in this sum.
Both convolutions act by their respective scalars on those blocks.
The (5/2,V) component is nonzero: restrict matrix coefficients of an embedded V submodule of V_(5/2).
The coefficient gap is strictly positive by Theorem 3.4(v).
This corrected algebraic identity does not compare the two full L2 transfers or their normalized Gibbs laws.

## 15. Section 6, item 8: “largest at (5/2,V)” — FAILS

For both Q_8 and 2T the spin-7/2 restriction also contains V:
the multiplicities are respectively four and two in Lemma 1.5.
For beta>0, Lemma 3.1 gives

\[
 0<r_{7/2}<r_{5/2}<r_V^G,
 \qquad r_V^G-r_{7/2}>r_V^G-r_{5/2}.
\]

Thus even the next eligible spin has a larger coefficient defect.
There is no maximum at spin 5/2. The valid statement is that spin 5/2 already has a nonzero V-channel defect
(and is the first half-odd-integer spin above 1/2 with that copy for 2T).
The guide comparison with the fundamental block is not a comparison with all blocks.

## 16. Section 4.2, fusion and plaquette coefficients — HOLDS with its stated scope

For (a), repeated Clebsch–Gordan gives
V^tensor4=2V_0+3V_1+V_2 and V^tensor6=5V_0+9V_1+5V_2+V_3.
The dimensions are 16 and 64. Applying the checked invariant table gives the stated fourth- and sixth-moment dimensions,
including the eleven extra Q_8 channels in degree six. Averaging any group-fixed vector fixes it exactly.
The sextic invariant and its tensor product with V give the claimed eigenvalue r_V^G in (b).
This tensor-product equality is on V tensor span(h_6); convolution does not generally factor over tensor products.
The ensuing description of a frozen vacuum remains ARGUED, not a theorem about its Wilson distribution.

For (c), the generating identity
sum_(n in Z) I_n(beta)t^n=exp((beta/2)(t+t^(-1)))
gives sum_(n in Z) n^2 I_n(beta)=beta e^beta.
Symmetry in n then proves

\[
 \sum_{j=0,1/2,\ldots}\frac{2}{\beta}(2j+1)^2 I_{2j+1}(\beta)e^{-\beta}=1.
\]

Every term is positive. This is the normalized list of character-expansion coefficients evaluated at the identity.
It is not the interacting one-slice spin law in section 4.1(c), as the source correctly says.
The listed percentages and finite-group freezing locations remain GUIDE and were not used or numerically rerun.
“Exposure density” must retain that single-plaquette coefficient meaning.

## 17. Section 4.3, no mandatory high-spin exposure — HOLDS AFTER CORRECTION

The singlet map J_k and the single flat plane are already TR (G20)–(G21), read at lines 524–585.
They do avoid all distinguishing high-spin channels at arbitrary periods.
However, section 4.3 omits the common vacuum factor when it says that the plane contributes
2r_(1/2)^A to Z^m-Z^(m+v). TR explicitly gives this number only after dividing by that factor.
In EX's unshifted convention the actual contribution is

\[
 2z(\beta)^{N_p}r_{1/2}(\beta)^A,
\]

where N_p is the total spacetime plaquette count. For the shifted Wilson convention multiply also by e^(-beta N_p).
The correction does not change the non-exposure example, but is required when claiming original normalization.
It gives no bound on the whole partition ratio.

## 18. Section 4.4 and the concluding scope — HOLDS only as labelled OPEN/ARGUED

The proposed HS and LS estimates are not proved in the source or in this check.
A trace inequality for a positive test X does hold on odd spins at least 5/2:
Pi_e K<=r_(5/2) Pi_e tensor K_rest. The printed
X=(BK)^(t-1)B is positive, since it equals
B^(1/2)(B^(1/2)KB^(1/2))^(t-1)B^(1/2).
The right side of that inequality lacks the edge kinetic factor, exactly as the source notes.
It cannot be normalized by Tr(KX) to obtain the asserted HS estimate.
No supplied implication turns HS into LS or the target twist bound.
The suggested finite-group “alias” reading also requires a separate definition;
section 14 rules out using L2 restriction as that definition.

The mathematical conclusions about the earlier inputs follow from the checks above.
Claims about frozen phases, binding couplings, and which mechanism would prove confinement retain their GUIDE/ARGUED labels.
No mass-gap or order-one flux estimate follows from the filters, their coefficient law, or this check.

RESULT: HOLDS AFTER CORRECTION for the low-spin filter theorems and their kinetic exposure; FAILS for the unrestricted L2 restriction map and the claim of maximal defect at spin 5/2. The restriction table, finite-group eigenvalues, LC pair, commutator bounds, Bessel lemmas and small-beta expansions hold; exact proof repairs and the missing plane-normalization factor are given above. HS, LS and the mass-gap target remain open. Research check only; no status granted.
