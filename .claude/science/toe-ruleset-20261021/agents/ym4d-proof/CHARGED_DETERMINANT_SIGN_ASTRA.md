# A small-penalty sign for the actual bare charged determinant

This author unit derives a fixed-odd-L asymptotic of the charged function
in [DS15](DETERMINANT_SIGN_ASTRA.md). The coefficient of its logarithm is
computed below from the actual normalized arithmetic-mean kernel, an exact
full-mode Schur/Ward factorization, and a convergent lattice remainder:

    C_L(kappa)=-(7/(16 pi^2)) log(1/kappa)+c_L+O_L(sqrt(kappa)). (CH1)

The finite scheme constant c_L is specified by an absolutely convergent
integral. It is not evaluated numerically. A positive, explicitly defined
interval in kappa then gives b1(N,L,kappa)<0 for every N>=2. This is a
bare one-step result. The small parameter here is the block-penalty kappa,
not a change in the blocking factor L, and the logarithm is not substituted
for a universal running coefficient. The full finite-momentum action is
not a nearest-neighbor Wilson action.

The mathematical source is frozen for a different fresh source-first check.
Its receipt records the freeze identity. This is an author proof proposal;
no independent acceptance is asserted here.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Literal object and the order of limits

Fix odd L>=3 and N>=2. All original Wilson sources are zero. Retain the
actual 24L^4 paired-order paths, their separate forward/inverse arithmetic
means, the constrained SU(N) maximizer, the original internal tree, and
all m0=3L^4+1 free link types per coarse cell. HS fine coordinates satisfy
-tr(T_a T_b)=delta_ab. The projection colour is
H=i diag(h_i), sum h_i=0, sum h_i^2=N. These are the conventions of
[BD1--BD29](BARE_DETERMINANT_COUPLING_ASTRA.md), not continuum conventions
chosen after the calculation.

The source-zero order-one part of the full critical prefactor is exactly

    Gamma_1(V)=sum_c log A_c(U_T(V))+(1/2)TrLog K_intr(V),
    A_c=h_N(2pi)^((N^2-1)/2) det(H_c)^(-1/2),
    b_N(kappa)=beta_av[Gamma_1]=N^2 C_L(kappa)-B_L(kappa). (CH2)

H_c is the SU(N) Hessian of minus phi. BD3/BM23 have already combined the
original coordinate Haar Jacobian and coordinate Hessian into K_intr.
No ghost, gauge-volume factor, coarse Haar factor or extra Jacobian is
appended. All vacuum factors remain until the marginal kills them.

For each fixed positive kappa, take the fine/coarse finite-torus derivatives,
then volume to infinity, and only then external momentum P to zero as in
[BM26](BARE_COUPLING_MATCH_ASTRA.md). Only the resulting coefficient is
sent to kappa=0. The argument below uses identities on compact positive
kappa intervals before obtaining a uniform improper-integral estimate.
It does not exchange these limits or assert a common chart radius down
to kappa=0. The original large-u threshold may depend on N,L,kappa.

## 2. The on-shell constant-curvature jet

Fix a plane mu<nu and use a formal real Cartan curvature F H, with the
concrete H of BD9 when a colour basis is needed. Before tree fixing one
may take U_(z,mu)=exp(-F z_nu H/L^2) and all other links equal to I;
then use the original root-pinned tree gauge in each block. Coarse
V_(X,mu)=exp(-F X_nu H), with the other coarse links I. BM16 and DS17
identify this actual fine curvature profile. Its paired path integrals are

    T_(rho,y,pi)=exp(B_rho+F s_(rho,y) H),
    s_(mu,y)=-y_nu/L, s_(nu,y)=y_mu/L,
    s_(rho,y)=0 otherwise.                              (CH3)

They include both endpoint axial legs, in their same order pi. The y
average is symmetric. Consequently M^+=V R, M^-=R V^-1, where
R=avg exp(F s H) is positive diagonal for sufficiently small real F,
and R=I+O(F^2). Thus the ACTUAL constrained SU(N) maximizer is V:
V already has determinant one, and Re tr(W^-1 V R)<=tr R, with equality
at W=V. There is no replacement by a different group integral.

The Wilson gradient is zero, not merely small. For each fine link and
each incident curvature plane, the two commuting plaquette matrices
are equal and occur with opposite variations; the sine contributions
cancel. Tree gauge fixing preserves this statement. The mean residual
is zero, so the normalized-kernel gradient is also zero for every kappa.
This proves stationarity to every required finite jet of CH3.

This formal field is not put into a hard chart on a finite torus.
At fixed kappa, BM25 supplies absolutely summable original-reader second
moments for the actual coarse Hessian. Its Ward identity removes the
zero-momentum term. For A_mu(X)=-F X_nu H, the same-component quadratic
kernel Pi(r) therefore has curvature density

    -(F^2/4) sum_r r_nu^2 Pi_mu mu(r)
                                  = (F^2/2) beta_mu nu. (CH4)

This is an identity of jets, obtained from the volume-first kernel.
It includes the actual critical motion: CH3 solves the linear critical
equation, and BD10 removes the second Cartan critical variation. For the critical-motion detail, form the joint Hessian Pi_joint(q) of
log A(U)+(1/2)TrLog K_intr(U,V) before substituting U_T. Its first
derivative at identity is zero by colour invariance. Root-gauge covariance
gives Pi_joint(q) g(q)=0, where g(0)=0 and
partial_mu g(0)=i(E_mu,e_mu). Thus Pi_joint(0)(E_mu,e_mu)=0. If
J(q)=(Phi(q),I) is the linear critical pullback, J(0)e_mu=(E_mu,e_mu),
and the coarse Hessian is J(q)^*Pi_joint(q)J(q). Terms containing
J double-prime therefore vanish at q=0; the first-derivative terms
are exactly the affine profile CH3. This proves the claimed critical-motion
cancellation without deleting the remaining momentum derivatives.
All later constant-F formulas mean this finite-jet evaluation, not an
analytic continuation of an unbounded affine field through a cutoff.

## 3. Exact kernel and hard-mean Schur identities

Let P(U) be FK's actual local constrained maximizer, and Q_F=dP its
linear map from intrinsic fine link tangents to intrinsic coarse link
tangents. Put H_F=N H_c, a positive coarse link-colour matrix at real
CH3. Its flat value is I and its linear curvature coefficient is zero.
Indeed at CH3 its bilinear form is

    <xi,H_F eta>=-tr[R(xi eta+eta xi)]/2,
    H_F=I+O(F^2).                                      (CH5)

To derive the normalized Hessian, differentiate the identity
phi_star(M)-phi(P(M);M)=0 twice. The gradient in the maximizing variable
vanishes. The joint quadratic form in fine tangent x and output tangent
y is (y-Q_F x)^* H_F(y-Q_F x)/N. With output fixed, the full classical
fine Hessian is therefore exactly

    K_F=W_F+kappa Q_F^* H_F Q_F,                        (CH6)

where W_F is the intrinsic Wilson Hessian. The leading spread cancellation
is included in this identity; an unnormalized penalty would not give it.

Use the crossing injection E of BD8, with E^*E=L^3 I and Q_0 E=I.
Choose a cellwise orthonormal matrix R_0 whose range is ker E^*. Fix it
by keeping internal standard vectors and applying ordered Gram--Schmidt
to e_j-e_last in each lexicographically ordered crossing family. It is
chosen separately on each orientation, so it respects the root gauge
base of every tangent. Define

    J_F=(Q_F E)^-1,
    T_F(y,z)=E J_F y+(I-E J_F Q_F)R_0 z.                (CH7)

These are local formal curvature jets about Q_0 E=I; no positive-radius
analytic assertion about an unbounded magnetic potential is needed.
The formula also holds on the ordinary bounded small-field domain.
It satisfies Q_F T_F(y,z)=y and is invertible. At F=0 its determinant
relative to [E,R_0] is one; |det[E,R_0]|=L^6 per colour and coarse cell.
That fixed factor is retained as a vacuum, not normalized away.

Write T_F^* W_F T_F in y,z blocks, with lower-right block A_h,F. At flat
data z has m0-4=3L^4-3 entries per colour and coarse cell, and

    A_h,0 >= a_h I,
    a_h=1/max(4L^3(L+4)(60L^2)^2,2L^3)>0.              (CH8)

For Q_0 x=0, BD7 at kappa=1 bounds ||D x||^2 below by a_h||x||^2.
Also x=(I-EQ_0)R_0 z has ||x||>=||z||, since R_0 z is orthogonal to
range E. This proves CH8 without removing a root or harmonic mode.
The inverse A_h,F^-1 below is its formal curvature inverse at that gap.

Define the actual constrained Schur form

    S_F=W_yy-W_yz A_h,F^-1 W_zy,
    M_F=H_F^-1/2 S_F H_F^-1/2.                         (CH9)

Finite-dimensional Schur algebra, or its coefficientwise curvature
version, gives

    det K_F=(det T_F)^(-2) det A_h,F det(S_F+kappa H_F),
    Gamma_1=Gamma_h+(1/2)TrLog(M_F+kappa I)+vacuum,
    Gamma_h=(1/2)TrLog A_h,F-Log det T_F.                (CH10)

In the second line the actual amplitude det(H_c)^(-1/2) cancels the
factor det(H_F)^(1/2) in the last determinant. N and h_N constants remain
in the displayed vacuum. This is a Hessian factorization of the soft
model, not a replacement of its integral by a hard block-spin kernel.
The full fine dimension equals (m0-4)+4 per colour and cell throughout.

## 4. Coarse stationarity and retention of the longitudinal determinant

One can define the finite Taylor germ of the Wilson stationary value
subject to P(U)=V. Its constraint coordinates are CH7; CH8 uniquely
solves its internal critical equation recursively. Through four field
orders every coefficient is a finite sum of local vertices and A_h,0^-1.
This construction will also be used for the leading-symbol calculation.
At CH3 the full Wilson gradient vanishes, so the constraint multiplier
is zero. Hence the constrained COARSE gradient vanishes as well. Its
coarse Hessian at this on-shell jet is precisely S_F in CH9; away from
this stationary jet, a constraint-curvature term could not be omitted.

A block-constant fine root gauge transformation preserves the tree and
maps P(U) covariantly to the coarse link. Its infinitesimal fine tangent
d_f omega obeys W_F d_f=0 at the Wilson stationary jet, and
Q_F d_f=d_V omega, where d_V is the actual coarse covariant difference.
The internal Schur equation then implies

    S_F d_V=0,
    D_F=H_F^(1/2)d_V,
    M_F D_F=0.                                         (CH11)

This is an on-shell identity, not an off-shell assumption. Define

    A_F=M_F+D_F D_F^*, B_F=D_F^*D_F.                   (CH12)

For kappa>0, the matrix determinant lemma gives

    det(M_F+kappa I)
       =kappa^(n_s) det(A_F+kappa I)/det(B_F+kappa I),  (CH13)

where n_s is the COMPLETE coarse site-colour dimension. A kernel of D_F
causes no difficulty: its scalar eigenvalue kappa is retained and cancels
the corresponding vacuum factor exactly. No primed determinant appears.
These scalar factors arise from algebra of the original determinant;
calling them an additional Faddeev--Popov factor would double count.

CH13 is a finite-dimensional identity wherever the stationary background
is defined, and an identity of the local curvature jets. For the affine
projection the following resolvent proof is the one actually used; it
avoids a finite-torus constant-flux interpolation. Write R_A=(A_F+s)^-1 etc.
Woodbury and (M_F+s)^-1 D_F=D_F/s give

    tau R_M=tau R_A-tau R_B+n_s_per_cell/s.              (CH14)

Here tau is the covariant trace per coarse cell. At fixed s>0 its
curvature jets have summable kernels; cyclicity follows by summing the
diagonal of products. Taking [F^2] annihilates the last, field-independent
term only at this stage. Thus, with the twelve ordered-plane average,

    I_N(s)=(1/12) sum_(mu!=nu) [F^2] tau(R_A-R_B),
    b_N(kappa)=b_N(1)-int_kappa^1 I_N(s) ds.             (CH15)

The one-half in CH10 and the factor two in CH4 cancel. All formal
curvature coefficients in A_F,B_F are independent of kappa. On each
compact positive-kappa interval, fixed-gap differentiation justifies
CH15 for the literal BM coefficient. No estimate at kappa=0 has yet
been invoked.

## 5. Locality, original readers and ellipticity of the reduced symbols

Every entry of W_F,Q_F,H_F comes from the actual finite words. Q_F can
be computed by differentiating FK's constrained saddle, or BD14's
finite homogeneous recursion; through F^2 and two fine variations only
the displayed degree-four word polynomial is needed. After CH7--CH12,
the only inverse not based at the identity is A_h,0^-1. It has the
positive gap CH8 and finite Laurent range.

Here are the locality details needed by the new step. Let r_h be the
actual finite range of A_h,0 in original coarse cells and b_h its scalar
absolute row/column bound. Choose m>0 with
(exp(r_h m)-1)b_h<a_h/4. Conjugating any principal compression by
exp(m distance) changes its norm by less than a_h/4. Neumann inversion
about its positive compression therefore bounds its inverse entries by
2 a_h^-1 exp(-m distance). This is the same proved elementary mechanism
as IC8, now with CH8 and the actual r_h, not IC's soft gap.

Use boxes of side between R and 2R, with R>2r_h+4, and their enlarged
neighborhoods. Local inverses P and boundary residuals R_b obey
A_h,0 P=I-R_b. The scalar absolute row, column and marked-reader residual
sums are bounded by C (1+R)^c exp(-mR/2). Choose R so this is below 1/4,
and then a positive reader weight so the weighted bound is below 1/2.
The exact inverse sum P sum_(j>=0)R_b^j is absolutely convergent in both
row/column and full reader-incidence norms. Its supports are the actual
connected patch collars joined by residual paths. Multiplication marks
either factor, exactly as IC9--IC10. Principal compressions, boundary
faces and torus images are retained. This reuses that proof after checking
its gap, range and local-reader hypotheses; it imports no hard-constraint
covariance theorem for another model or dimension.

Only finite curvature/field jets are used here. Differentiating an inverse
inserts its actual local derivative between two such inverse words. The
finite homogeneous constraint recursion has the same property. Every
union retains the original Wilson/mean/source-owner reader, even at source
zero. A curvature insertion costs at most a fixed constant times the square
of its connected reader diameter; momentum derivatives cost powers of that
diameter. For every fixed k, |Y|^k<=k! eta^-k exp(eta|Y|). Spend part of
the reader rate for these polynomial costs. Thus all finitely many moments
used below exist with positive remaining ORIGINAL-cell rate. An R-box is
not renamed a microscopic cell. Coefficients agree when all their complete
readers agree. Torus-winding reader tails vanish before the affine or P limit.

This supplies smooth, indeed analytic-in-q, magnetic-symbol coefficients
through F^2. It does not assert analyticity in a finite unbounded magnetic
potential, nor a reader rate uniform down to kappa=0 for the final massive
inverse. The latter is used at each fixed kappa exactly as in BM/BD.

For the flat reduced vector use the actual Q,D,E of DS3. The constrained
quadratic form is

    <y,S_0(q)y>=min_(Q(q)x=y) ||D(q)x||^2.               (CH16)

For q!=0, let P(q)=d(q)d(q)^*/|d(q)|^2. DS25--DS32 retain the one root
null vector and bound the positive H block by
4|q|^2/(pi^2 L^2 C_T^2), C_T=2L^2(4L-3). Since ||Q(q)||<=10L,
CH16 gives S_0>=gamma_L |q|^2(I-P), with

    gamma_L=4/(100 pi^2 L^4 C_T^2).
    A_0=S_0+d d^* >= gamma_L |q|^2 I,
    B_0=d^*d >= (4/pi^2)|q|^2 I.                       (CH17)

Indeed project x onto the complement of the fine root null vector;
(I-P)y=Q_T x_H and apply that bound. Conversely S_0 d=0. The two
orthogonal parts in A_0 therefore have the asserted lower bound. At
q=0 use A_0=B_0=0 plus sI, retaining all harmonic directions. This proves
that there are no additional zero momenta, without replacing S_0 by Wilson.

## 6. Leading symbols from the actual constrained coarse action

The remaining leading-symbol identification is derived here rather than
assumed from a continuum beta function. Give a smooth bounded connection
the formal scaling A(x)=epsilon A_test(epsilon x). Then A has weight one,
a derivative has weight one and its curvature has weight two. Take the
actual path-ordered parallel transports along fine edges of length 1/L,
and tree-fix them. Coarse V is the straight unit-edge transport.

For each actual paired word, its difference from the straight coarse
transport first occurs at weight two and equals the curvature contracted
with the signed ribbon area of DS22. The mean of that area is zero:
its transverse entries are proportional to y_eta, whose average vanishes.
Therefore P(U_trial)-V has weight at least three. The constrained-saddle
expansion at the identity has derivative the arithmetic mean, so it does
not undo this cancellation. Since Q_0 E=I, the formal constraint recursion
corrects the fine field by weight at least three to enforce P(U)=V.

The original Wilson gradient at the trial transports has weight at least
three: opposing plaquette curvatures cancel at weight two, and the next
term is their covariant difference. The constraint correction leaves this
order unchanged. CH8 then solves the internal stationary correction with
weight at least three. Its change of Wilson action starts at weight six,
since its first variation already has weight three. These statements can
be read coefficientwise in the finite homogeneous recursion: products
preserve weight and A_h,0^-1 is bounded, with the moments just proved.
They require no full nonlinear inherited effective-class theorem.

The fine Wilson action at the trial has leading density

    (1/2) sum_(mu<nu) ||F_mu nu||HS^2.                   (CH18)

There are L^4 plaquettes in each plane, each with curvature F/L^2;
the factors cancel exactly. Its higher terms have weight at least five.
The actual constrained stationary action therefore has exactly CH18 as
its weight-four part. Differentiating twice in arbitrary slow fluctuation
connections gives its entire weight-two Hessian, including the non-Abelian
spin term, not only its commuting value. This also proves the tensor
normalization and excludes an unproved Wilson identification at general q.

For clarity, twice varying CH18 about a covariantly constant background
gives, with anti-Hermitian covariant derivatives nabla,

    S_lead,rs=-nabla^2 delta_rs+nabla_r nabla_s
                                      -2 ad(F_rs).

Adding d_V d_V^* cancels the nabla_r nabla_s term. CH5 has no linear-F
metric correction. Accordingly the magnetic symbols of CH12, in a root
of charge alpha=h_i-h_j, have

    a_vector,0(q)=|q|^2 I_4+O(|q|^3),
    a_vector,1(q)=-2i alpha J_mu nu+O(|q|),
    a_scalar,0(q)=|q|^2+O(|q|^3),
    a_scalar,1(q)=O(|q|),
    a_vector,2(q), a_scalar,2(q) bounded.                (CH19)

J_mu nu is the real antisymmetric matrix with J_mu nu=1, J_nu mu=-1.
Neutral colour blocks have alpha=0; all N-1 of them remain. The remainders
and their required q derivatives are bounded by the finite moments above.
The weight argument means an omitted F^j q^ell term has 2j+|ell|>=3.
In particular a bounded F^2 term is retained and need not vanish.
CH19 is a controlled leading expansion of the actual Schur operator;
no part of the high-momentum operator is declared small.

## 7. The constant-field product and explicit resolvent coefficients

Transport each coarse tangent to its cell root. This is an adjoint unitary
change, of determinant one. Constant Cartan curvature makes its kernel,
in a root of charge alpha, a translation kernel times the straight-segment
magnetic phase. Multiplying two kernels leaves the flux through their
triangle, alpha F(r_mu s_nu-r_nu s_mu)/2. Expanding that exponential
proves, through F^2, the lattice magnetic product

    a star b=ab+F B1(a,b)+F^2 B2(a,b),
    B1(a,b)=(i alpha/2)(a_mu b_nu-a_nu b_mu),
    B2(a,b)=-(alpha^2/8)(a_mu mu b_nu nu
                              -2a_mu nu b_mu nu+a_nu nu b_mu mu). (CH20)

Subscripts here are q derivatives. Reversing the phase convention reverses
B1 and the spin sign together; none of the result depends on that choice.
The same formula with alpha=0 applies to a neutral matrix block. This is
a direct discrete convolution proof; no continuum pseudodifferential
calculus theorem is imported. Exponential reader moments justify each
finite derivative and convolution. The trace per cell is the normalized
Brillouin integral of the matrix trace of its symbol.

For either actual symbol a_F=a0+F a1+F^2 a2, the inverse of a_F+s under
CH20 has the exact coefficients

    r0=(a0+s)^-1,
    r1=-r0[a1 r0+B1(a0,r0)],
    r2=-r0[a2 r0+a1 r1+B1(a0,r1)+B1(a1,r0)+B2(a0,r0)]. (CH21)

All products are matrix products in their displayed order. The seagull,
exchange and magnetic phase derivatives all survive. In particular the
exchange is not assigned a sign before the infrared projection.

For the leading scalar symbol put R=(|q|^2+s)^-1. Then

    r2_scalar=-alpha^2 R^3+2alpha^2(q_mu^2+q_nu^2)R^4.

For the leading vector add S_spin^2 R^3 to four scalar copies, where
tr S_spin^2=8alpha^2. Direct radial integration on R^4 gives

    int R^3 dq/(2pi)^4=1/(32pi^2 s),
    int R^4 dq/(2pi)^4=1/(96pi^2 s^2),
    int r2_scalar=-alpha^2/(96pi^2 s),
    int tr(r2_vector-r2_scalar)=7alpha^2/(32pi^2 s).     (CH22)

For example the scalar result uses rotational averaging
q_mu^2+q_nu^2 -> |q|^2/2 and |q|^2 R^4=R^3-sR^4.
These elementary integrals can also be obtained by one radial substitution;
no tabulated loop coefficient is being quoted.

Sum every ordered root and every neutral colour. DS10, or simply expanding
sum_(i!=j)(h_i-h_j)^2 with sum h_i=0 and sum h_i^2=N, gives 2N^2.
Neutral blocks have no leading singular term. Hence the leading value of
I_N(s) is

    c N^2/s,                  c=7/(16pi^2).             (CH23)

The scalar determinant occurs with the coefficient in CH13, not an
extra adjustable ghost multiplicity. Replacing it by a familiar continuum
gauge-fixing prescription would change this computation.

## 8. An explicit integrable lattice error

Here are finite constants for the comparison, defined without numerical
coefficient evaluations. For fixed N,L, form the actual a_j of CH7--CH12
and CH20, for every plane and root/neutral block. They are computed from
BD's finite words, Q_F's constrained recursion and the gapped A_h,0 inverse.
Let M_raw be the maximum of their operator norms and every individual
q partial derivative up to order three, on the real Brillouin cube, for
j=0,1,2. There are finitely many matrices; CH8 and the reader construction
prove M_raw<infinity. Put

    amax=sqrt(2N), M=2^12(1+M_raw+amax),
    rho=1/(4M), Z=1+M+2amax,
    Zfar=1+M+amax+(gamma_L rho^2)^-1,
    E_NL=5(N^2-1)[2^96 Z^48/(12pi^2)
                      +128 Zfar^16+7amax^2/(16pi^2 rho^2)]. (CH24)

The concrete H of BD9 has every |alpha|<=amax. These deliberately loose
constants are independent of kappa and volume. Their definitions involve
only gapped fixed-L symbols and compact-domain derivative suprema, not
the unknown sign of C_L.

We prove, for 0<s<=1,

    |I_N(s)-c N^2/s| <= E_NL/sqrt(s).                    (CH25)

On |q|<=rho let t=(|q|^2+s)^(1/2). CH19, Taylor's formula and the factor
2^12 in M give, for j=0,1,2,
||partial^j(a0-|q|^2 I)||<=M |q|^(3-j), and for j=0,1,
||partial^j(a1-S_spin)||<=M |q|^(1-j); ||a2||<=M.
Use S_spin=0 for the scalar or neutral block. The a0 lower bound here
is at least 3|q|^2/4. Resolvent differentiation and
r0-R=-r0(a0-|q|^2 I)R now give the following sufficient bounds:

    ||partial^j r0|| <=32 Z^2 t^(-2-j),         j<=2,
    ||partial^j(r0-R)|| <=128 Z^3 t^(-1-j),    j<=2,
    ||partial^j r1|| <=2^24 Z^12 t^(-4-j),    j<=1,
    ||partial^j(r1-r1_lead)||
                         <=2^24 Z^12 t^(-3-j), j<=1.   (CH26)

For the first two lines use d r0=-r0(da0)r0 and its two-derivative
product rule. The second line has exactly three factors before taking
up to two derivatives. For the last two lines insert these bounds into
CH21. The leading B1(|q|^2 I,R) is zero, as is its derivative. In its
difference each term therefore contains either a derivative of
(a0-|q|^2 I) or one of (r0-R), supplying one extra power of t.
The spin is constant. The displayed constants exceed the product-rule
sum, including both B1 contractions and t<=2.

Insert CH26 into r2. The a2 term has order t^-4. In the remaining terms
subtract the leading expression by changing one factor at a time. The
leading B1(a0,r1) also vanishes. In B2 use the second-derivative bounds
of CH26. Each difference has order at most t^-5. Counting the five
terms of r2, the two contractions of B1, and the four weighted contractions
of B2, with their product differences, is bounded by

    ||r2-r2_lead||<=2^96 Z^48 t^-5.                    (CH27)

For example r0 a1 r1 has one error factor of respective orders -1,1,-3
instead of -2,0,-4. B1(a0,r1) uses errors of orders 2 or -4 in its
first derivatives. B2(a0,r0) uses errors of orders 1 or -3 in its second
derivatives. The a2 term is absorbed using t<=2. These checks show the
power improvement; a generic unseparated norm of the original fine
inverse would not have it.

The normalized four-dimensional integral of (|q|^2+s)^(-5/2) over R^4
is 1/(12pi^2 sqrt(s)). Outside |q|<=rho, CH17 bounds each actual inverse
by (gamma_L rho^2)^-1. Differentiating twice and using CH21 bounds
||r2|| by 128 Zfar^16 there. The normalized Brillouin volume is one.
Finally the leading continuum tail outside that ball is bounded by
7alpha^2 int_(|q|>rho)|q|^-6 dq/(2pi)^4
=7alpha^2/(16pi^2 rho^2). There are 4(N^2-1) vector and N^2-1 scalar
entries in total. Summing these bounds, and taking the plane average,
proves exactly CH24--CH25. In particular both seagull and exchange errors
are integrable in s after the Ward factorization.

## 9. Actual charged asymptotic and a nonempty sign interval

Define I_C(s)=(I_3(s)-I_2(s))/5 and E_L=(E_3L+E_2L)/5. The exact DS
colour identity at every positive kappa and CH15 give

    C_L(kappa)=C_L(1)-int_kappa^1 I_C(s) ds,
    |I_C(s)-c/s|<=E_L/sqrt(s).                           (CH28)

Consequently the finite number

    c_L=C_L(1)-int_0^1 [I_C(s)-c/s] ds                  (CH29)

is an absolutely convergent, completely specified matrix/contour formula.
No value or sign is assumed for it. Equations CH28--CH29 prove

    |C_L(kappa)+c log(1/kappa)-c_L|
                                      <=2 E_L sqrt(kappa). (CH30)

This proves CH1 with a controlled error, not only a formal leading term.
Using DS34 also gives the actual bare-coefficient asymptotic

    b_N(kappa)=-c N^2 log(1/kappa)+N^2 c_L+g_L
                                      +O_(N,L)(sqrt(kappa)),
    g_L=(3L^2+1)/(16L^2).                               (CH31)

A useful sign interval can be specified without evaluating c_L. At
kappa=1 use the exact J_C of DS11--DS15 and define the finite positive bound

    A_L=a_L+(1/24)sum_(mu!=nu)
                int_BZ |[P^2]J_C(q;P e_nu;kappa=1)| dq/(2pi)^4,
    K_L=A_L+2E_L.                                       (CH32)

The fixed positive gap at kappa=1 proves A_L<infinity and
|C_L(1)|<=A_L, so CH28 gives C_L(kappa)<=-c log(1/kappa)+K_L.
For 0<kappa<=1, DS27--DS29 imply

    |B_L(kappa)|<=Bmax_L:=g_L+3d_L+2sqrt(3)r_L,
    d_L=(L^4-L^2-4)/(48L^4), r_L=(L-1)(L^2-1)/(8L).

Set

    kappa_sign(L)=min(1,kappa_star(L),
                   exp[-(K_L+Bmax_L/4+1)/c]),           (CH33)

where the positive rational kappa_star(L) is DS31. Every number in CH33
is defined by the actual fixed-L input matrices, finite suprema or
absolutely convergent integrals, and is finite before kappa is chosen.
Thus kappa_sign(L)>0 for every odd L>=3. It is a conservative analytic
domain, not an empirically located sign threshold.

For every N>=2 and 0<kappa<=kappa_sign(L),

    b_N=N^2 C_L-B_L
       <=-N^2(Bmax_L/4+1)+Bmax_L <=-N^2<0.             (CH34)

The same interval works for all N because DS's exact colour reduction
uses only N=2,3 to bound C_L. Each N is still fixed before its volume,
momentum and subsequent kappa limits. No uniform-in-N small-field or
finite-u domain is inferred from this algebraic sign comparison.

## 10. Scope, routes and literature rebuilt

The direct DS root-inverse estimate was tried first. Without CH11--CH14
it produces inverse-kappa losses and does not control the projected
charged exchange. The materially different route above preserves that
mode in an exact determinant ratio, then compares TWO elliptic operators.
The finite-kappa variational route was retained as a fallback; it was not
needed to derive CH25. These are research-route facts, not a no-go theorem
about other methods.

The result concerns the source-zero bare prefactor's infrared marginal.
BM and BR are the separate suppliers connecting it to the original-cut
bare coefficient u+b_N+O(1/u) at fixed positive kappa. This source neither
extends their domains nor makes that expansion uniform in a joint
u/kappa limit. It gives no small bound for the difference from Wilson at
general coarse momentum, no selected-history derivative theorem and no
inherited-class iteration. Full normalized history return, compatible
reserve regeneration, repeated flow, non-freeness, continuum existence
and a positive physical continuum mass gap remain OPEN.

The following primary methods were consulted at their actual versions.
Their needed pieces are rebuilt above, rather than imported as premises.

- M. Mantoiu and R. Purice, [The Magnetic Weyl Calculus, math-ph/0401043v1](https://arxiv.org/pdf/math-ph/0401043v1),
  section 3.2, Lemma 3.11 and section 4's (4.36): kernel phases and the
  triangle-flux product. CH20 is the discrete, constant-field, finite-jet
  convolution proof needed here; no general symbol-class theorem is assumed.
- D. Litim and J. Pawlowski, [hep-th/0203005v2](https://arxiv.org/pdf/hep-th/0203005v2),
  section IV, (4.1)--(4.10), (4.18)--(4.20): on-shell covariant operator
  identities and constant-curvature expansions. Their axial gauge and
  regulator differ. CH11--CH23 derive the present multiplicities and
  normalization directly, with no coefficient imported from their flow.
- D. Adams and W. Lee, [0709.0781v3](https://arxiv.org/pdf/0709.0781v3),
  section II, (7)--(15), and the displayed Appendix A theorem: positivity,
  absence of other zero momenta and an integrable power-counting remainder
  are necessary. CH17 and CH24--CH27 prove the required statements for
  this fixed-L matrix family. A lattice-spacing theorem is not substituted
  for the present small-kappa comparison.

Credit to Balaban and Dimock for the constructive localization and
marginal-extraction architecture. The actual local suppliers consumed are
FK's constrained saddle, BM's volume-first projection and critical
curvature profile, BD's intrinsic determinant/word conventions, IC's
local inverse proof, and DS's exact colour/scalar reduction. Review or
gate labels supply none of the mathematical steps.

The coordinator owns publication. The author owns only this source,
[its route state](parts/effective-flow--charged-coefficient.md), and the
charged_determinant_sign_* check prefix. No scientific numerical or
symbolic coefficient-evaluation job was run. No predecessor, frozen gate,
shared front, lock or Git state was edited. Source freeze precedes the
minimal read/receipt packet and a different fresh hostile check.
