# Independent hostile review of LOCOP

**LAND as a finite-support and conditional research note. No binding
mathematical defect was found.** This verdict does not close the actual
all-history extraction, uniform coefficient estimates, or EXTCONT E19.
LC1–LC6 remain OPEN, as the source states.

Reviewed on 2026-10-30 under `PROCESS_LIGHT.md` rule 3 and the LOCOP author
lane's ownership restriction. This is a fresh-context, same-family Codex
review, not cross-family verification. I did not author LOCOP or inherit
the author's reasoning transcript. I independently reconstructed the
load-bearing calculations below. No reviewer subagents or new numerical
runs were used. Only this report was written; no source file was edited
and no commit was made.

The reviewed source is `LOCOP.md:1–601`, SHA256
`0295d071a60d0ba3abfa23e4722634c7c2ea54921423cd0451aec7381e2c9253`.
Unqualified line numbers below refer to that version. The report reviews
the whole substantive argument, not just its status table. The author
brief, light process and author log were read, together with the necessary
actual source sections listed below. The snapshot's lack of usable git
metadata prevents a current-main or commit-ancestry certification.
The first complete pass reviewed SHA256
`2cc456556d3a092ba7d21f98a31abc249f70b5d07e5214a05857f39fb74153da`.
The author then applied the two nonblocking clarifications described
below; I re-read and confirmed the affected source/log paragraphs before
issuing this verdict on the current bytes.

## Per-item findings

PASS means that the stated finite result or conditional implication is
valid. It does not mean the actual gauge model supplies its antecedents.

| Item and LOCOP lines | Verdict | Fix or required scope |
|---|---|---|
| Contract, additive-action representation, real domain and complete readers, 33–78 | PASS. The derivative orders, original-source convention and norm distinction agree with REALRGA/REALRGB. The principal-log restriction is sufficient. | No binding fix. The exact local logarithm, enlarged supports and actual history representation remain inputs. |
| L1, normalized-kernel and S4′ covariance, 82–117 | PASS. Endpoint cancellation and Haar substitution give an exact identity, including the normalizer. | No binding fix. A fixed blocking origin and complete selected histories/readers are essential qualifications. |
| L2, Ward identity and local dimension classification, 119–163 | PASS on a finite contractible single-connection patch with no untransformed spurion. The Hessian factors through curvature. | No binding fix. This excludes a local physical connection mass; it is not a uniform rough-field estimate or a theorem about nonlocal mass projectors. |
| L3, relative fields and Haar chart term, 165–196 | PASS. Both quadratic terms have the stated coefficients and are compatible with their actual covariance. | No binding fix. They cannot be removed by the single-connection Ward argument. |
| L4, tensor tests, colour form and origin independence, 200–235 | PASS. The tests recover a real symmetric six-plane tensor, with the declared colour normalization. | No binding fix. Tests are finite-box derivatives at the identity, not constant magnetic fields imposed on a torus. |
| L5, clover reconstruction, idempotence and scalar reduction, 237–284 | PASS. Both maps are idempotent on their respective ranges. The tensor map retains all constant-curvature quadratic tests. Scalar reduction requires the full B4 bulk orbit. | No binding fix. The trace-free anisotropic example correctly rules out a scalar-only contraction for individual nonsymmetric activities. |
| L6–L7, beta normalization and real coefficient estimate, 286–337 | PASS under the stated summability and coordinate-norm conditions. The factor two and the loss h^-2 are correct. | No binding fix. Scheme conversion and summed/unweighted Hessian estimates remain distinct obligations. |
| L8, spatial quadratic remainder, 339–356 | PASS as a linear finite-path identity and engineering count. | No binding fix. Nonabelian transports, original readers and their derivatives remain to be bounded. |
| L9 and displayed L10, full real Taylor norm, 358–401 | PASS. The bound is 4/L+8/L^2; the curvature-only zero-jet bound is 8/L^2. Supremum placement and derivative orders are respected. | No binding fix. The displayed mixed bound gives no contraction at L=3 or L=5. Actual retained fields do not acquire these dimensions automatically. |
| L10, actual return comparison and E19, 403–431 | PASS as an OPEN interface. Its norm comparison and invariant-ball inequalities are sufficient algebra, not estimates supplied here. | No binding fix. Selected-return, hole, support, chart and weight costs must be paid exactly once on the same norm. |
| L11, action split, signs and standard normalization, 433–470 | PASS conditional algebra. The returned marginal sign and u=2N/g_std^2 conversion are correct. | No binding fix. The numerical standard one-loop value is used only for conversion; kernel universality is explicitly not derived. |
| L12, FP and T-tel, 472–516 | PASS at the cited admissible critical Gaussian/source scope. Both determinant cancellations check algebraically. | No binding fix. T-tel explicitly carries FLOW §94(W3)'s invertibility assumptions and its log-absolute-determinant convention. No all-history C^(6,4) estimate follows. |
| L13, uniform flow bracket and logarithmic refinement, 518–556 | PASS on an admitted trajectory satisfying the displayed antecedents. The 2R0 defect and the logarithmic bound are correct. | No binding fix. The partial-sum theorem, C/u error, stable trajectory and causal tuning remain OPEN actual-model tasks. |
| L14 and disposition, 558–601 | PASS. The coefficient-ball test and vacuum recursion are correct conditional forms; LC1–LC6 preserve the remaining obligations. | No binding fix. LAND is for this partial result, not completion of the author brief's actual induction target. |

## Independent reconstruction

### 1. Covariance and the domain of the Ward argument

For a directed path, each internal gauge factor appears once as g^-1 and
once as g. Reversing a link replaces its transporter by its inverse and
preserves the same cancellation. Every contour contributing to one S4′
coarse link therefore transforms as a T b^-1 with the same endpoint
matrices a,b. Its arithmetic mean does too. The trace identity

    Re tr[(a V b^-1)^* (a M b^-1)] = Re tr(V^* M)

uses unitarity. Substitution W=a W' b^-1 in probability Haar proves the
normalizer identity without assuming a polar branch or a nondegenerate
maximizer. The exact normalized transfer is thus covariant for all real
fields. A coarse root gauge extends to a fine gauge by choosing values at
the other vertices; Haar substitution then proves invariance of the
complete transferred single-field density. This step fails for a
noninvariant selected piece unless the selection labels also transform,
exactly as lines 110–112 state. S4′ uses paired axial orders and all
offsets, so a signed coordinate permutation relabels the finite path
family, including reversal of a coarse link when appropriate. It does
not give translations that change the fixed partition.

At the identity, constant conjugations act independently on each link's
tangent copy of su(N). An invariant linear functional vanishes on
commutators, which span su(N), so DK(1)=0. Differentiate the identity
DK(U)[the infinitesimal gauge direction at U]=0 in a link direction A.
The derivative of that gauge direction is multiplied by DK(1)=0. What
remains is H(d omega,A)=0. A nonzero multiple of the link identity form
does not annihilate gradients, so it cannot be the complete local
single-connection Hessian.

Fixing a spanning tree gives an explicit linear right inverse for the
curvature data on the gauge quotient: subtract the tree-path primitive
lambda, then express each remaining edge's fundamental-loop circulation
as a sum of elementary plaquette circulations. Cubical contractibility
is used here. Thus A-d lambda=R dA, and applying the Ward identity in
both slots yields H(A,B)=H(RdA,RdB). The finite R need not have a
support-independent norm.

Nonlinearly, tree gauge makes the remaining edges based loop holonomies,
with simultaneous conjugation at the root. For a fixed finite lattice
path sampled from a smooth connection at spacing epsilon, the closed
holonomy is 1+epsilon^2 times its oriented-area contraction with F, plus
O(epsilon^3). Expansion of a link product cancels the order-epsilon
closed-path sum; adjacent-step commutators and first spatial differences
give the plaquette curvature at order two. The invariant linear
functional in these based holonomies again vanishes. The first possible
nonconstant scalar is consequently quadratic in curvature, of engineering
dimension four. This argument requires a smooth shrinking patch, as the
source explicitly says; it provides no estimate on arbitrary rough
fields. In the summable translation-invariant version, Pi(tv)d(tv)=0 and
d(tv)/t tends to i v. Continuity at zero gives Pi(0)v=0 for every v. A
nonanalytic transverse mass projector is outside this locality argument.

The mixed-field counterexample survives these checks. At fine U=1 the
normalizer has no dependence on V, and

    -log k_t(exp(z t_a);1) - [-log k_t(1;1)]
      = t[1-Re tr exp(z t_a)/N] = t z^2/2+O(z^4).

Simultaneous covariance relates fine and coarse variations; it does not
say that varying the coarse field while freezing the fine field is a
gauge motion. The linear residual QA-B is invariant under the composite
variation precisely because Qd=d ev. BFT_A retains this residual.

For the chart measure, expanding
log[(1-exp(-z))/z]=-z/2+z^2/24+O(z^4) and tracing at z=ad A gives no
linear trace. On traceless matrices,
tr_ad(ad A)^2=2N tr A^2, so log j(A)=(N/12)tr A^2+O(A^4). For
A=i z sigma_3 this is -z^2/3+O(z^4), agreeing with
j=(sin z/z)^2. The sign in -log j is positive. This term is a chart
measure contribution and must be combined with the rest of the exact
action/measure before applying a physical Ward argument.

### 2. Tensor extraction and the scalar bulk coefficient

For the displayed affine potential,
Delta_mu A_nu^F-Delta_nu A_mu^F=F_mu,nu. Translating the chosen origin
adds a constant link field, which is an exact gradient on the box.
Likewise, a geometric symmetry maps this test to the transformed test
up to a gradient. The Ward identity therefore removes origin dependence
and gives two-form covariance of C.

An invariant colour bilinear is represented, using -tr(AB)/N, by an
endomorphism commuting with every adjoint action. Complex diagonal
adjoint actions preserve the one-dimensional root lines E_ij. The
relations T[X,Y]=[X,TY]=[TX,Y] equate the corresponding root eigenvalues
and determine T on the diagonal traceless subspace; the E_12,E_21 pair
already gives this in N=2. Thus T is scalar, real on the real algebra.
The average over D=N^2-1 orthonormal colours in L4 returns that scalar,
and Hessian symmetry makes the plane matrix symmetric.

Every clover loop is based at x, so its principal logarithm transforms
by Ad(g_x). The angle restriction ensures that the principal log is
traceless: its eigenangle sum is a multiple of 2pi with absolute value
less than pi. Reversal gives minus the logarithm, and swapping the two
axes reverses the based loop. Thus the signed four-orientation average
transforms exactly as a two-form under B4. On the affine one-colour test
with field parameter tau and loop orientation signs s,t, all link
exponents commute and the loop log is exactly tau s t F_mu,nu near
zero. Their signed average is tau F. For general colour tensors only the first-order
identity is needed: Fcal=tF+O(t^2).

It follows directly that the Hessian of the tensor reconstruction on
two constant-curvature tests is C_ab. Its value at identity is a_X.
Applying extraction again gives the same tensor reconstruction. For the
scalar reconstruction the recovered tensor is b_X times the identity,
whose plane trace divided by six is b_X, so that map is idempotent too.
The tensor projector, unlike the scalar one, matches every test of the
original K.

For two distinct planes there is an axis in exactly one of them. Its
reflection reverses exactly one factor, killing the off-diagonal entry
of the B4-invariant aggregate. Permutations equate all six diagonals.
The dual-curvature term changes orientation sign and is excluded by
the reflections. This proves the scalar classification only after the
complete bulk orbit is formed. The trace-free tensor
diag(1,-1,0,0,0,0) is a valid adversarial control: scalar extraction
annihilates it, while L^4 times its evaluation at L^-2 F is itself.

Normalization can be checked without the numerical script. A single
Wilson plaquette in plane a has C_aa=1 and all other entries zero, so
b=1/6. The six unoriented plaquettes per translation site give b=1.
The clover density has C=identity because its spatial weights sum to
one, also giving b=1. A rectangular loop of area A in one plane has
C_aa=A^2, which checks the area-square convention rather than a
linear-area one.

Summing the finite Hessian factorizations over translates gives
Pi(p)=d(p)^* h(p)d(p). Only h(0) contributes to its degree-two term.
The constant-curvature tests determine h(0); B4 symmetry makes the
aggregate b times the plane identity. Thus the 12 entry starts as
-b p_1 p_2. The mixed momentum derivative of
sum_z exp(i p.z)Pi_12(z) is -sum_z z_1 z_2 Pi_12(z), proving beta=b
with FLOW's normalization and sign. The stated absolute moment/test
summability justifies the exchange for the infinite family. Since
|F|^2=-tr F^2/N, writing the quadratic density instead as
c_bar sum_a[-tr F_a^2] gives b=2N c_bar.

### 3. The real coefficient estimate and spatial Taylor bound

Let M_(2,r) denote the weighted operator norm of the two-field,
r-source derivative at the reference point. Each affine test has field
direction norm at most A_X/h. Hence every tested Hessian entry and its
r-source derivative is bounded by (A_X/h)^2 M_(2,r). Averaging over six
planes and D colours adds no factor. The norm contains
M_(2,r)/(2! r!), so summing over source orders gives exactly

    sum_(r<=4) |D_J^r b_X|/r! <= 2 A_X^2 h^-2 H_X^T.

The same argument works for a mixed plane entry and for each labelled
source subset. The estimate uses the reference point in the declared
evaluation domain, with the same frozen source units. It is a direct
Hessian estimate. In particular, h_j^-2=u_j/N converts an O(1/u_j)
weighted activity bound only to O(1) at coefficient level. Nothing in
the projector recovers the missing power of u_j.

The spatial quadratic identity is exact:

    <F(p),F(q)>-<F(o),F(o)>
      = <F(p)-F(o),F(q)>+<F(o),F(q)-F(o)>.

One nearest-neighbour telescoping difference is bounded by its path
length times sup|nabla F|. This supplies engineering degree at least
five, but no smallness for rough fields. Nonabelian comparisons require
the recorded transports and their derivative/support costs.

For the full Taylor lemma, apply every included source derivative first;
the zero-jet assumptions hold identically in J. The degree-two field
polynomial has only bidegrees (1,1) and (0,2). Their dilation factors are
L^-1 and L^-2. A bidegree (i,j) coefficient reconstructs in the full
split norm with cost

    sum_(a<=i,b<=j) binom(i,a) binom(j,b)=2^(i+j)=4.

The coefficients are all tested at the same (0,J), so the polynomial
part costs at most 4L^-1 sup_D T(G), without exchanging a sum and a
domain supremum in the wrong direction.

Set R=G-P_2G and S=diag(L^-2,L^-3). Jets of R through order two vanish;
its derivatives of orders three through six equal those of G. For a
derivative of total field order r<3, radial Taylor integration at Sx
uses precisely 3-r additional field derivatives. Each differentiated
input and radial vector contracts by at most s=L^-2. After factorial
division, a third-order bidegree (i,j) contributes
binom(i,a)binom(j,b) to a+b=r. Summing gives binom(3,r).
Consequently orders zero, one and two cost
(1+3+3)L^4s^3=7L^-2 times the common domain supremum. At orders three
through six, all derivatives are evaluated at the single point Sx and
their factors L^4s^r are at most L^-2. Their entire sum costs one more
L^-2, not four independently charged suprema. This proves

    ||D_L G||_T <= (4/L+8/L^2)||G||_T.

No bound on ||R||, seventh field derivative or fifth source derivative
was used. Labelled source subsets carry through unchanged. If the
whole quadratic polynomial is absent, the first contribution is absent
and the bound is 8/L^2. The mixed bound is 20/9, 28/25 and 36/49 at
L=3,5,7 respectively. This finite lemma does not supply LC2's coordinate
dictionary or LC3's actual activity derivative of the return map.

### 4. Exact action bookkeeping, FP and transverse telescoping

Since beta[W_tree]=1, linearity gives
u'=u+beta[F_bulk]=u-b+beta[R_other]. Setting rho=-beta[R_other] gives
u'=u-b-rho. A returned contribution +delta beta to the log density
therefore contributes -delta beta to the action and +delta beta to rho.
Subtracting (u'-u)W_tree gives an exact residual; projecting that
residual into C' and K' is another exact identity. Neither identity
gives a norm bound. The beta-zero difference W_cl-W_tree still requires
LC2's real bound. FLOW's SU(N) maximizer correction starts at degree
six, so a six-field-derivative contract cannot discard it merely
because beta is blind to it.

With tr(T^a T^b)=delta_ab/2, the plaquette expansion is
s(exp(i a^2 F^a T^a))=a^4 sum_a(F^a)^2/(4N)+higher orders. The
unoriented plane sum is half the ordered one, giving u/(8N). Matching
1/(4g_std^2) proves u=2N/g_std^2, and multiplying the stated standard
slope 2b_0 by 2N gives 11N^2/(12pi^2). This verifies the unit
conversion, not the actual kernel's partial-sum/universality theorem.

For FP, write n=dim E, g=dim gauge, p=dim range h and
q=dim range chi_2, so g=p+q. The orthogonal orbit decomposition
A=s+Gamma omega has Jacobian det(Delta')^1/2. Changing omega to
z=chi A contributes |det(chi Gamma)|^-1. The h delta function and
chi_2 Gaussian leave

    I = det(Delta')^1/2 |det(chi Gamma)|^-1
        (2pi)^((n-g+q)/2) det_S(Q)^-1/2.

Linear coarea gives the same integral as

    I = det(hh*)^-1/2 (2pi)^((n-p)/2) det_H(O)^-1/2.

The exponents agree because n-g+q=n-p. Equating them yields exactly
the FP identity at lines 483–485. Omitting either the coarea factor
or the orbit metric changes the background-dependent determinant.
The injectivity, positivity and slice admissibility hypotheses are
essential, and are present in the statement.

For T-tel, the stated intertwining maps Ran D_k into Ran D_(k+1),
so P_(k+1)T_k(1-P_k)=0. Compression therefore closes the covariance
recursion on the transverse spaces. In an orthogonal basis whose
first block is an orthonormal longitudinal frame V, write

    Y = [[A,B],[B*,C]].

When the blocks required by the source are invertible, the longitudinal
block of Y^-1 is (A-BC^-1B*)^-1. The Schur determinant formula gives
det(V*Y^-1V)=det C/det Y. Also, if D_n=VR, then
det(D_n*Y^-1D_n)=det(D_n*D_n)det(V*Y^-1V). Substitution into the
complete critical Gaussian expression cancels the full log det Y,
leaving the transverse determinant and the ghost determinant. At a
critical background the initial transverse covariance is H_perp^-1,
so its initial log determinant cancels log det H_perp and the remaining
differences telescope to one half the sum of Phi_k^T plus G_gh,n.
No level remainder survives this identity. It does not bound the
local coefficient of the surviving steps. The phase-weighted Cartan
derivative, current-field projector and C-part/M-part distinction in
lines 513–516 agree with the actual FLOW source.

### 5. AF arithmetic and the remaining recursions

Put delta_n=B_n-n b_*. Summing u_(k+1)=u_k-b_k-rho_k from j through
n-1 gives

    u_j-u_n=(n-j)b_*+delta_n-delta_j+sum_(k=j)^(n-1) rho_k.

The hypotheses give |delta_n-delta_j|<=2R0 and
|rho_k|<=C/u_min. These prove both sides of L15 and the one-step
absolute-increment bound. They do not imply monotonicity of every
step. Since b_->=b_*/2>0, if U=u_n-2R0>0 then
u_k>=U+b_-(n-k). For m=n-j,

    sum_(k=j)^(n-1) 1/u_k
      <= sum_(ell=1)^m 1/(U+b_- ell)
      <= integral_0^m dx/(U+b_- x)
      = b_-^-1 log(1+b_- m/U).

This proves L16 with its stated condition U>0. It is not a uniform
O(1) accumulated error: the admitted estimate permits logarithmic
growth in the number of UV steps. The source states this correctly and
does not use a future terminal coupling to obtain an earlier step's
input estimates. The h_j/h_(j+1) identity also has the correct direction.

For v'=A_jv+f_j+r_j(K), triangle inequality immediately gives the
displayed sufficient invariant-ball condition. A vacuum constant per
fine site is multiplied by L^4 when expressed per coarse site, giving
e'=L^4e+a. Neither result supplies the actual nonvacuum coefficient
budgets or permits source-dependent vacuum functions to be deleted.

## Source and evidence checks

The necessary upstream readings were EXTCONT §§1–2,5 and its review;
REALRGA §§1–4, including RGA3/RGA4/RGA7 and H0–H6; REALRGB §§1,6–7;
LINEAR_PACKAGE §§1–2; FLOW §§0,3,8–9,15,52,94/96,105–110;
BFT_A §§7.1,8.0–8.2; BFT_B §2.4; and SF §3.2 and its latest outcome.
These confirm that no cited linear action contraction, fixed-sector
four-jet bound or one-step pinned decomposition supplies the actual
all-history comparison. In particular BFT_B's general-depth extension
at lines 403–410 is expressly withdrawn.

| Source | SHA256 |
|---|---|
| EXTCONT.md | `b10015bbd6be5fac97fd636fdc79f665800fe9921651575b9d03b0167b534b6e` |
| REVIEW_EXTCONT.md | `e202cb50bdf0db2853bb7b68a3b59e48caa3c9cdda21c6aaad76097ec96783d1` |
| REALRGA.md | `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` |
| REALRGB.md | `80d4f1216e39c9d5cd661c7eced48f3ac480c0d1443e556208a1b2684890d640` |
| FLOW.md | `085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| BFT_A.md | `553d56f46ea457aa1b6a97c2a53f435739d3fadb6c9af0cf89676f41a7266902` |
| BFT_B.md | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| SF.md | `e966acccb5410b8aa86c55ccad6054bc7ac39265f41bdf8945f5eb83cd9ff847` |

The criteria, script and saved numerical report were read, not rerun.
Their recorded criteria/script hashes match the present files:
`11af948015c8993a931699c39901d8410f272a1f18b3cfa9ba107e6af4d24c78`
and `fd859ed206ce35076f43c0e5adb1e666d74ffec053d2c0397f63606a2c694993`.
The code checks finite path covariance, one rational tensor orbit,
commuting loop areas, monomials and a synthetic flow. It does not
numerically construct a general nonabelian Loc or test an actual AF
trajectory; the log and note describe that limited role honestly. The
monomial regression is not a proof of the norm lemma, which was checked
independently above. No independent numerical reproduction or historical
preregistration-timing certification is claimed by this review.

Two nonblocking clarifications were applied by the author and confirmed
in this review:

1. `LOCOP_LOG.md:80–87` now distinguishes the requested `nice -n 10`
   increment from effective nice 20 in every saved resource sample.
   The effective value satisfies the registered nice>=10 guard. This
   corrects the execution description without changing the mathematics
   or numerical guard result.
2. `LOCOP.md:493–509` now states the invertibility/zero-mode subspaces
   and log|det| convention of `FLOW.md:4243–4244,4269–4274`, and defines
   Ytilde, Phi_k^T and G_gh,n. These additions agree with the reconstructed
   cancellation and avoid assigning ordinary positive logarithms to
   FLOW's indefinite transverse sector. They assert no continuation
   across a zero eigenvalue and no T-tel result at noncritical backgrounds.

## Binding fixes and disposition

**Binding fixes: none.** All substantive finite constructions and
conditional algebra reviewed above can land at their stated scope.
The actual representation, nonabelian spatial/transport estimates,
extracted return, uniform bulk flow coefficient, stable causal AF
trajectory and remaining coefficient budgets remain OPEN LC1–LC6.
No assertion in this review certifies Yang–Mills existence, a mass gap,
retained status, an audit verdict, or actual E19 closure.

VERDICT: LAND
