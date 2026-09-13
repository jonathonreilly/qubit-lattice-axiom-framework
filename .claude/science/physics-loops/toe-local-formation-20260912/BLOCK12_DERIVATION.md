# Two-source Ward approximation and a finite diagnostic

Author derivation, conditional on the native primary Ward model. Native
alpha is now positively enclosed in hopping units by the separate-source witness below.
The earlier Block6 chart result is not used.

## 1. Exact two-source comparison

For each native pair A take D_A>=delta, R_A=-D_A^-1, J_A*=-J_A, and the
bounded Hermitian Ward field W_A satisfying [W_A,D_A]=-J_A. The source
proves the inverse commutator on the appropriate domain:

    [W_A,R_A]=-R_A J_A R_A.

Put x_A=R_A Omega, y_A=R_A W_A Omega and v_A=R_A J_A R_A Omega. Then

    v_A=y_A-W_A x_A.                                      (12.1)

For arbitrary vector approximants xhat_A,yhat_A, set vhat_A=yhat_A-W_A xhat_A.
If ||x_A-xhat_A||<=E_A and ||y_A-yhat_A||<=Y_A, the triangle inequality gives

    ||v_A-vhat_A|| <= Y_A+||W_A|| E_A.                     (12.2)

This is a direct replacement of the earlier nested-inverse bound
(||J_A||/delta)E_A plus an inner residual. Neither bound universally dominates
the other: the new source error Y_A must be certified independently. It is
not the vacuum error, and a large ||W_A|| or Y_A may erase the gain.

For any real polynomial p_A, choose

    xhat_A=-p_A(D_A)Omega,
    yhat_A=-p_A(D_A)W_A Omega.

Their difference is the local commutator trial

    vhat_A=[W_A,p_A(D_A)]Omega.                            (12.3)

For degree two,

    vhat_A=-p1_A J_A Omega-p2_A(D_A J_A+J_A D_A)Omega.      (12.4)

Using the actual native conventions B_A=i g gamma(d_A), ||d_A||²=2h²,
J_A=2i gamma(d_A), H0 Omega=0 and
[H0,gamma(f)]=i gamma(Kf), compute

    J_A B_A=4h² g,
    B_A J_A=-4h² g,
    H0 J_A Omega=-2gamma(Kd_A)Omega.

The B_A anticommutator cancels, so

    (D_A J_A+J_A D_A)Omega=-2gamma(Kd_A)Omega,
    vhat_A=-2i p1_A gamma(d_A)Omega
                +2p2_A gamma(Kd_A)Omega.                 (12.5)

Thus the new quadratic-polynomial Ward trial needs only a linear CAR source.
This conclusion is an operator-on-vacuum identity. It does not assert
{D_A,J_A}=-2gamma(Kd_A) on arbitrary states: the omitted J_A H0 term would
then remain. A literal finite CAR check is required before numerical reuse.

## 2. Separate spectral error certificates

For a source psi in the required polynomial domain define

    r_psi=(I-Dp(D))psi.

The inverse error is ||D^-1 r_psi||. A valid polynomial majorant Q(x)>=x^-2
on [delta,infinity) gives the independently computable bound

    ||D^-1 r_psi||² <= <r_psi,Q(D)r_psi>.                (12.6)

The gap majorant Q=delta^-2 and the preceding source's quadratic/quartic
majorants are admissible. For degree-two p and degree-q Q, moments
<psi,D^n psi> through n=6+q suffice. The coefficients of r are
(1,-p0,-p1,-p2); their exact convolution produces the residual moments.

Apply (12.6) separately to psi=Omega and psi=W_A Omega. The latter source
is generally not local or normalized. Its norm is ||W_A Omega||=||W_A||,
since W_A²=||w_A||²I in the relevant CAR normalization. No normalization
factor can be dropped. These are moments in the original reference state
and with the same D_A reference-energy subtraction.

For the fifteen-channel direct sum set

    E²=sum_A E_A²,
    F²=sum_A(Y_A+||W_A||E_A)².

The original posterior theorem, with these actual E,F and the new signed
nominal from (12.3), then encloses the SAME native alpha. Changing the trial
requires recomputing the nominal; the old nominal cannot be retained merely
because p is unchanged. All90 ordered disjoint pairs must be included.

## 3. Finite source moments and covariance table

Write O_n Omega=D_A^n Omega, with O_0=I and

    O_(n+1)=[H0,O_n]+B_A O_n.

The W-source obeys the analogous recurrence from initial operator W_A.
The identity [H0,W_A]=3J_A reduces its first free action to a local source.
Higher actions can be represented as one W field times local CAR words
plus local words, using [W_A,B_A]=2J_A. Products with two W fields may use
W_A²=||W_A||²I, but cross contractions with one W must be retained.

Here is the finite covariance table, derived from the actual
bipartite dispersion rather than a fitted Gaussian bank. Set h=1 for this
table, write a=e0, d=d_A, a_j=K^j a, d_j=K^j d and let w denote the REAL
coefficient vector of W (thus w=6K^-1 d and K w=6d). Define

    M_n=E omega^(2n), L_r=E omega^r,
    D_n=2M_n (P), or M_(n+1)/3 (O),
    F_r=2L_r (P), or L_(r+2)/3 (O).

M_0=1. Let <gamma(f)gamma(g)>=f dot g+i kappa(f,g). For i+j=2n,

    a_i dot a_j=(-1)^(i+n) M_n,
    d_i dot d_j=(-1)^(i+n) D_n,
    kappa(a_i,d_j)=(-1)^(i+n+1) L_(2n+1)/3.

For i+j=2n+1,

    a_i dot d_j=(-1)^(i+n+1) M_(n+1)/3,
    kappa(a_i,a_j)=(-1)^(i+n+1) L_(2n+1),
    kappa(d_i,d_j)=(-1)^(i+n+1) F_(2n+1).

The parity-complementary entries vanish; swap Euclidean arguments
symmetrically and kappa arguments antisymmetrically. These formulas use
K*=-K, -K²=omega²I in each doubled cell, and the six equal signed leg
contributions. Perpendicular-neighbor cross entries vanish by cell parity;
the opposite-neighbor difference contributes a radial power shift.

The extra Ward vector has entries

    w dot a_(2n)=2(-1)^n M_n,
    w dot d_(2n+1)=-6(-1)^n D_n,
    kappa(w,a_(2n+1))=-2(-1)^n L_(2n+1),
    kappa(w,d_(2n))=-6(-1)^n F_(2n-1),
    ||w||²=72 E omega^-2 (P), or12 (O).                  (12.7)

Again the other parities vanish. The only new nonlocal scalar types are
A0=E omega^-2 and C0=E omega^-1, both finite in three dimensions. For
example the first W-source moments reduce to

    m0_W=||w||²,
    m1_W=(L1/3)||w||²+12 F_(-1).                         (12.8)

Equation (12.8) follows directly from H0W Omega=3J Omega,
W B_A W=||w||² B_A+2J W and WJ=-JW. Its positivity is consistent with
D_A>=delta. It is not obtained by normalizing W Omega to unit norm.

The table passes literal native finite covariance checks. A separate finite
AP Fourier/SVD/Fock implementation checks all44 moments through order10 for
both classes and sources, with scaled errors below5e-14. These finite tests
challenge the algebra; the infinite claims rest on the displayed identities
and named premises. The copied scalar inputs are bound to source revisions
and hashes. The source truth is inherited conditionally, not independently
re-audited by this calculation.

## 4. Checked finite two-frequency soft diagnostic

The separate working plan derives a finite S6-symmetric active star with
frequency a on the uniform mode and b on the standard modes, a,b>0, plus
an auxiliary zero mode. In its two-mode frame the impurity determinants
are ab/3 and2ab/3. For disjoint pairs,

    x_A=(3/a+2/b)Omega-(3/b)u wedge v_A,
    y_A=3u/(2a)+(9/(2b)+3a/b²)v_A,

where this diagnostic y is D_A^-1 L_A D_A^-1 Omega, L_A=-i a b_(v_A);
it is distinct from the two-source y in section1. The soft derivative kernel is

    <x_C,x_A>+<y_C,g x_A>+<g x_C,y_A>
       =18/a²+27/(ab)+18/b²+6a/b³.

Multiplication by90/8 is strictly positive for every a,b>0. A literal
three-active-mode CAR inverse verifies the symbolic kernel, and a separate
four-mode construction with an actual zero mode verifies the derivative
at a=2,b=3. Nine exact checks pass. Omitting both impurity-resolvent
derivatives is rejected.

The ordinary regular-mode vacuum coefficient is instead
(135/8)(3/a²+3/(ab)+1/b²). At a=b it matches the source's L4 coefficient;
the soft derivative does not equal it. This is a diagnostic distinction,
not a deformation proof for the actual infinite native bath. No native
alpha value or sign follows, and this toy result is not a standalone
publication milestone.

## 5. Separate quadratic polynomials for the two sources

The first certificates now exist, with zero still inside every interval.
The refined Green calculation does not resolve the sign. A further structural
option is to allow a different real quadratic q for the Ward source:

    xhat=-p(D)Omega, yhat=-q(D)W Omega,
    vhat=W(p-q)(D)Omega-q1 J Omega+2q2 gamma(Kd)Omega.    (12.9)

Indeed[D,W]=J implies D²W Omega=W D²Omega+(DJ+JD)Omega. Applying the
already checked vacuum anticommutator proves(12.9). Its first term contains
W and MUST be retained when p differs from q. The previous local-linear
trial is recovered only at p=q. The same two-source error bound applies,
with E certified from p and Y from q. Any change of q changes the nominal.

For the two-channel contractions add W_A,W_C to the six local fields. If
n=|A intersect C| and m counts opposite leg matches, direct radial symmetry
of the signed neighbor sources gives

    d_A dot f(-K²)d_C=(n-m) E f(X)+(m/6) E[X f(X)].

For f=1 and f=X this recovers n and6n+m. For inverse powers it gives

    w_A dot w_C=36[(n-m)A0+m/6],
    kappa(w_A,d_C)=-6[(n-m)C0+m L1/6],
    w_A dot Kd_C=-6n, kappa(w_A,Kd_C)=0.

Also w_A dot a=2, kappa(w_A,Ka)=-2L1, with the other parities zero, and
kappa(w_A,w_C)=0. These relations include self-pairs: n=2,m=0 for P,
and n=2,m=2 for O. Thus the new signed kernels and trial norms still need
only A0,C0,L1,L3; no new scalar oracle is required. A direct finite native
covariance test of the enlarged table is required before using its nominal.

For a FIXED valid majorant Q define H_j=<W Omega,D^j Q(D)W Omega>.
The squared-error majorant of q is the quadratic form

    H0-2 sum_i q_i H_(i+1)+sum_(i,j)q_i q_j H_(i+j+2).

Its matrix is a Gram matrix of the three D^(i+1)Q(D)^(1/2)W Omega vectors.
It is positive semidefinite; strict positivity and invertibility must be
checked for the chosen numerical midpoint matrix, not presumed for arbitrary
sources. Solving that three-by-three system supplies a trial polynomial.
Its coefficients are not a proof: its actual error must still be evaluated
against the full supplied scalar intervals. Selection by error size does not
supply a scalar sign. The proposed bounded protocol is recorded separately
before any new native nominal or source-error evaluation.


## 6. Conservative positive rational witness

For h=1 retain the supplied variational p for each class and the distinct q
listed in BLOCK12_SIGN_WITNESS.json. Their degree-two coefficients were
chosen by the fixed separate-source protocol before evaluating the resulting
native nominal. The certificate uses the single quartic with delta=1/4,t=4,u=8
for all four source errors. The full formulas and source moment tables are
machine-readable mathematical expressions; the standalone verifier parses
and combines them using only rational polynomial arithmetic.

Let a bound||xhat||, b bound||vhat||, E bound||x-xhat|| and F bound||v-vhat||
in the direct sum of15 channels. The Kneser disjointness operator T has norm6,
and the center Majorana g has norm1 and commutes with T. The native source
identity, with J anti-Hermitian and ordered pair reversal retained, gives

    8alpha=Re[<x,T x>-<x,Tg v>].

Its trial nominal N replaces x,v by xhat,vhat. Expanding both differences,
using||x||<=a+E and||v||<=b+F, gives the sufficient bound

    |8alpha-N|<=6[E(2a+E+b+F)+aF].                      (12.10)

The refined certificate and the separate standard-library verifier establish

    a<234/25, b<2151/100,
    E<1143/1000, F<9623/1000,
    1345<N<1347.

The rational right side of(12.10), using these coarse upper bounds, is exactly
111269781/125000=890.158248<891. Therefore

    56 < h² alpha < 280.                                (12.11)

The scaling follows from D=h D_(h=1), R=h^-1 R_(h=1), J=h J_(h=1), while
W is dimensionless. The sharper author interval for the variational family
is approximately[57.04288,279.47052] in these units; (12.11) is the simpler
witness claim. The other fixed p family also independently of its coefficient
choice gives a positive interval, but shares all physical/scalar premises and
most algebra; it is not an independent review.

The earlier common-polynomial failures remain in the packet. No native
Hamiltonian, vacuum, denominator, zero-mode extraction or Ward term was
replaced. The tiny finite two-frequency diagnostic is not a premise of this
sign certificate. The conditional complete-sixth analysis in Block5 would
therefore have a nonzero infrared pole, but that consequence additionally
depends on its complete-sixth decomposition and does not identify a phase
at fixed nonzero coupling. Formal retained status and independent source
review remain outside this author result. No axiom update or TOE closure
follows from the scalar sign alone.
