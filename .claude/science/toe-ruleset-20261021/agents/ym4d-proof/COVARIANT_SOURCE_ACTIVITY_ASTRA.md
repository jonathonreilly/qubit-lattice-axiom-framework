# A connected source sector with curved coarse holonomies

**Author research unit; fresh independent review required.** This constructs a
finite-volume, level-zero sector of the actual normalized soft SU(N) transform.
The covariant background input [CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md), frozen at
SHA-256 `87119008ccf754022b5da0836bb1bea8e0455a5535e589a4207ee49193682b74`,
now has a scoped independent [LAND review](REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md),
SHA-256 `3c39ed64cffd800bb930eda9ee8d7dbde20612e307cd90e512896f1aee34d549`,
read completely here. Its receipt is SHA-256
`079cd8eb2d122d727774299681396e87ef20675cc90a8f2081d6e90e14287532`.
This new activity unit itself is unreviewed. Continuum existence and a physical
mass gap remain open. An auxiliary conditional precision gap is not a physical mass gap.

The new part is the connected **original-coarse-data** construction at arbitrary
compatible holonomy, followed by an explicit interior sector of the actual good
event. The near-identity version, the product-measure cluster argument, and the
normalized cube-contour flux are already proved in
[SOURCE_LOCAL_RETURN](SOURCE_LOCAL_RETURN_ASTRA.md),
[its continuation](SOURCE_LOCAL_RETURN_CONTINUATION_ASTRA.md), and
[CX-R](RECOVERY_CLUSTER_ASTRA.md), with their linked independent reviews. They
are reused below with their actual hypotheses checked; they are not new theorems
by renaming. Bałaban's constructions and Dimock's expositions are the antecedents
of the local inverse/whitening and small-field organization. Literature is
attribution; the mathematical steps used here are rebuilt below or in these
explicit local library entries.

## 1. Model, exact dependency, and conclusion

Fix d=4, N>=2, odd L>=3, coarse side T>=2, u>=1 real, and kappa in a compact
positive interval. Put D=N^2-1, sigma^2=N/u, and n_0=D(3L^4+1). Use CB's fixed
internal block trees, with each block-root gauge left explicit. There are
n=(3L^4+1)T^4 free links and n_d=Dn scalar coordinates. All four harmonic
directions, crossing links, colour directions and root degrees of freedom
remain. The tree-Haar Jacobian is one and its integrated gauge volume is one;
there is no extra Faddeev--Popov determinant or zero-mode deletion.

For real coarse V write delta_V=max_P ||I-V_P||op. Its links need not be close
to I. CB's lift U0 has internal links I and crossing-face links V_c, with every
actual paired S4-prime transporter equal to V_c. Its nontrivial fine plaquettes
are precisely the double-face plaquettes, carrying the corresponding coarse
plaquette; there are L^2 of them per coarse plaquette. Use left coordinates

    U_e(a)=exp(a_e) U0_e(V),     a_e in su(N),                 (SA1)

with tree coordinates zero and a fixed HS-orthonormal real scalar basis. The
chart is the image of the traceless su(N) HS ball of radius
r_ch<min(injectivity radius,pi/sqrt(N)); its smaller analytic radii below also
obey CB's explicit normalizer/Haar conditions. Matrix principal logarithms are
used only on that image. No SU(3) centre element is added to this chart.

Let W_p(a;V)=tr(2I-U_p(a)-U_p(a)^(-1))/2. On real links this is
Re tr(I-U_p). Denote the EXACT conditional negative logarithm of Wilson times
the normalized kernel by S_eff, and define

    F_epsilon(a;V)=sigma^2[S_eff(U(a);V,epsilon)-sum_e log j(a_e)]
                 =F_0(a;V)+sum_p epsilon_p W_p(a;V).         (SA2)

Only the original Wilson coefficients vary. The kernel t=kappa*u is fixed.
At complex a, all inverses and bilinear transposes are analytic continuations;
complex conjugation of a is never used. The finite-u single-normalizer and the
Haar logarithm occur exactly once. At a=0 the kernel and Haar forces vanish;
the Wilson force is O(delta_V). In particular (SA2) is not the classical/tree
phase.

The exact CB input used here is: for delta_V<=delta_CB, the scalar matrix
K_b(V)=F_0''(0;V) has range 2 in coarse blocks, gap gamma>0, uniform block
row/column bound b, and actual entries depending on a radius-3 coarse stencil.
One can take CB's delta_CB=delta_star, gamma=a_gap/2, b=b_1, r_CB=r and
rho_CB=rho_star, decreasing the domain when necessary. Its local analytic
vertices, after their value at zero is subtracted, have a common scalar polydisc radius and bound uniform in real u>=1 and such V. CB
proves the gap by flat lifted two-block fillings, including the T=2 seam
qualification, plus the Wilson second-variation error. Its exact K_b contains

    covariant principal term + Wilson curvature error
      + kappa(1-c_N(kappa*u)) B_V + N^2/(6u) I.              (SA3)

The spread B_V and Haar term are retained. Real positive principal compressions
of K_b inherit the same gap. This assertion concerns compressions of THIS
coordinate matrix, not the Hessian of an arbitrarily frozen nonlinear collar.

Here is the result constructed below. For any fixed support rate mu>=0 there
are finite constants R,C_b,M_C,B_C and positive delta_A,rho_0, independent of
T,u, such that the actual critical branch b(V,epsilon), its precision and
inverse square root have connected atoms in ORIGINAL V and epsilon, with
full row/column and marked-support incidence bounds. In particular
||b||_v<=C_b delta_V for |epsilon|<=rho_0. For a fixed real V satisfying

    delta_V<=min(delta_A,c sigma p),  p>=1,
    h=A_0 sigma p^3+A_src(c)rho p^2<=1/4,                   (SA4)

and the chart/cut margins below, the fixed reference white cube is a nonempty
subset of the actual strong-good event and original cut. Its raw integral
Z_sec(V,epsilon) is zero-free and has an original-source connected logarithm.
Its source action at the background is explicitly factored and separately
bounded. This does not establish a logarithm for the original full Z_cut.

Only epsilon is asserted to range over an independent complex product domain.
V is real in the admitted curvature class. An atom labelled S reads only V_S
and epsilon_S: two admitted V agreeing there give the same atom. Suprema over
that real class do not require replacing it by a product of arbitrary coarse
link values. Local holomorphic formulas exist on their invertibility/chart
neighborhoods; no unproved global complex coarse-data polydisc is asserted.

## 2. Actual original-V inverse atoms, not decay alone

Set beta=mu+4. Partition the coarse torus into product R-boxes of side between
R and 2R, using one interval in directions shorter than R. A box contains at
most n_R=n_0(2R)^4 scalar free coordinates. Let s=J=9^4. For each box q,
Omega_q is its R-block neighborhood, and D_q includes its whole matrix-entry
read collar, radius R+4. Then D_q is connected, |D_q|<=s, and any box v belongs
to at most J of these labels. Periodic identifications reduce counts; labelled
periodic images are summed before a bound, not erased.

To include the determinant homotopy, use K_theta=(1-theta)cI+theta K_b with
c=b, increasing b first if necessary so b>=1,gamma. These real matrices and
all principal compressions have gap gamma, range 2, and block row bound <=2b.
Choose m>0 so (exp(2m)-1)2b<=gamma/2. Conjugation by exp(m distance) gives
resolvent norm <=2/(gamma+a), hence each scalar entry satisfies

    |(K_theta,Omega+a)^(-1)(i,j)|
                  <=2 exp(-m d(i,j))/(gamma+a),  a>=0.      (SA5)

This follows by a Neumann inverse of the weighted perturbation, whose norm
is <=gamma/2; it is uniform in arbitrary holonomies because the supplied
compression gap is. Let Q_m=n_0 coth(m/2)^4 and choose S_m to bound the scalar
weighted row and column sum of K_theta; D exp(2m)2b suffices. The full scalar
colour density n_0 and the scalar D conversion in S_m are explicit.

For theta=1 define, with complements inside the integrated matrix indices,

    P_q(a)=(K_b,Omega_q+a)^(-1)1_q,
    R_q(a)=-1_(Omega_q^c) K_b (K_b,Omega_q+a)^(-1)1_q.       (SA6)

Both read only V in D_q. Assign that entire connected label, including every
endpoint and coefficient-read collar. Set w=exp(beta*s),

    p(a)=2w Q_m/(gamma+a),
    r(a)=2w S_m n_0 coth(m/4)^4 exp(-m R/2)/(gamma+a).

Choose the integer R>=4 large enough that r=r(0)<1/2. This is possible because
s is independent of R in R-box units. It does not assert a useful numerical
size for R. The density n_R and all subsequent R-dependent constants remain.
For matrix atoms use

    M(A)=max{sup_i sum_(j,S) e^(beta|S|)|A_ij;S|,
             sup_j sum_(i,S) e^(beta|S|)|A_ij;S|},
    B(A)=sup_v sum_(i,j,S containing v)e^(beta|S|)|A_ij;S|,
    Q(A)=M(A)+B(A).                                        (SA7)

The symmetric entrywise bounds from (SA5) give M(P)<=p(a), M(R)<=r(a).
There are at most J relevant q and at most n_R nonzero columns per P_q,R_q;
therefore B(P)<=Jn_R p(a), B(R)<=Jn_R r(a). The residual has d(i,j)>R;
summing its exponential with half the rate gives exactly the displayed r(a).
Thus both endpoint sums, not just an operator norm, have been paid.

The identity (K_b+a)sum_q P_q=I-sum_q R_q yields

    G_a=(K_b+a)^(-1)=sum_(k>=0) P R^k,
    M(G_a)<=p(a)/(1-r(a)),
    B(G_a)<=Jn_R p(a)/(1-r(a))^2,
    Q(G_a)<=A_G/(gamma+a),
    A_G=2w Q_m[(1-r)^(-1)+Jn_R(1-r)^(-2)].                  (SA8)

For every nonzero product, consecutive labels share the summed matrix index;
their union is connected and includes all original V read. The inequalities
M(AB)<=M(A)M(B) and B(AB)<=B(A)M(B)+M(A)B(B) follow by marking which factor
contains v; the second case needs the column bound of A. This proves (SA8)
as absolutely convergent connected coefficient families. Integrating each
family against a^(-1/2)/pi supplies the actual square-root atoms. This rebuilds
the predecessor's parametrix for the new, covariant tree-coordinate operator.
No subtraction of an augmented projector is involved.

The same construction holds for K_theta. Jacobi's identity, proved by
differentiating the finite determinant, gives

    log det K_b=n_d log c+
        integral_0^1 Tr[(K_theta)^(-1)(K_b-cI)] dtheta.       (SA9)

Closed products have connected labels. With Q_K a finite local-atom bound for
K_b-cI, the nonconstant trace term has rooted norm <=A_G Q_K/gamma. The scalar
constant is assigned per box, costing <=n_R exp(beta)|log c|. All D colours
are already scalar indices here; no operator norm is substituted for a trace.
This is a generally non-small determinant budget. For T<R the single box is
the entire finite torus, residual R=0, and n_R still pays every mode. The
arbitrary-holonomy gap, rather than a small-link gauge, handles this case.

## 3. A support-norm critical point at small curvature

For vector atoms use the maximum of their component-root sum and their full
support-incidence sum, as in SOURCE_LOCAL_RETURN (30). Multiplication obeys
||Ah||_v<=Q(A)||h||_v by the marked row/column proof above. Denote A=A_G/gamma.

All constants in the following selection are constructive finite stencil
bounds. Choose a>0 so the scalar polydisc |a_i|<a lies strictly within CB's
local analytic radius. Let H bound each vacuum-subtracted local phase vertex
there, enlarged to bound a Wilson vertex separately as well. Put q=(8L^4+8)D, v_0=9L^4+5 and

    d_0=v_0(2R+6)^4,  d_1=q d_0,  d_2=q^2 d_0,
    f(t)=H(1-t/a)^(-q),
    S(t)=f'(t)-f'(0)-t f''(0),
    N(t)=d_1 e^(beta*s)[S(t)+t S'(t)],
    g_*=d_1 e^(beta*s) 6 sqrt(N),
    B_*=2d_2 e^(beta*s) f''(0),
    D_K(t,rho)=2d_2 e^(beta*s){f''(t)-f''(0)+t f'''(t)
                                 +rho[f''(t)+t f'''(t)]}.   (SA10)

There are 6L^4 Wilson, 4 kernel, and 3L^4+1 Haar vertices per coarse block.
Each reads a radius-3 stencil. The bounds d_0,d_1,d_2 respectively count all
vertices, force outputs and ordered Hessian entries incident to a box. They
also bound fixed row/column counts. They intentionally overcount q scalar
inputs and all actual S4-prime colours. A larger common H or q can be used;
none depends on volume or u. The normalizer input is STEP55's fixed-real-t
single-normalizer theorem after vacuum subtraction, not a complex-t claim.

The local force has the exact decomposition

    -F_epsilon'(a)+K_b a = -g_V-g_(epsilon,V)
                         -H_(epsilon,V) a-N_0(a)-N_epsilon(a). (SA11)

At zero, each Wilson plaquette force is bounded by sqrt(N) delta_V, since its
trace pairs a traceless insertion with P0-I. Kernel and Haar forces vanish
separately. Hence ||g_V||_v<=g_* delta_V and
||g_(epsilon,V)||_v<=rho g_* delta_V. The source Hessian has Q<=rho B_*.
All coefficients of the nonlinear forces, of degree at least two in a, are
majorized by (1+rho)N(t). In particular a force of order rho independent of
curvature has not been introduced or silently discarded.

Here is the marked coefficient proof. Taylor-expand each actual local vertex
first at a=0. Differentiating its scalar Cauchy series gives f'. Its constant
and linear force terms are exactly the terms subtracted in S. Substituting
vector atoms of norm t, a marked support vertex belongs to the root stencil
or one of the attached factors, giving S+tS'. All attached labels meet the
root at their output coordinate. The difference of two substitutions has
majorant N'(t), by telescoping one factor and then marking. Original epsilon
occurs only in its plaquette's root coefficient; repeated iteration keeps
that original coordinate. Original V occurs in the root coefficient and the
inverse atoms and is never treated as a new independent solved field.

Select tau,rho_0,delta_A, in that order, strictly positive, so

    tau<min(a/8,r_CB/(4sqrt(D))),  rho_0<=min(1,rho_CB),
    A[B_*rho_0+(1+rho_0)N'(tau)]<=1/2,
    A g_*delta_A(1+rho_0)<=tau/2,
    delta_A<=delta_CB,
    A_G D_K(tau,rho_0)<=gamma/2.                            (SA12)

Shrinking tau first and rho_0 second achieves the two derivative/Hessian
conditions because N'(0)=0 and D_K(0,0)=0; delta_A is then positive. The
CB scalar/local uniqueness radii r_CB,rho_CB are retained when identifying
this point with that independently reviewed branch.

Iterate a_0=0 and a_(n+1)=G_0[-F_epsilon'(a_n)+K_b a_n]. Equations
(SA8),(SA10)--(SA12) make this a contraction of ratio <=1/2 in the complete
absolutely summable vector-atom space. It converges with the bound

    F_epsilon'(b)=0,
    ||b(V,epsilon)||_v<=C_b delta_V,
    C_b=2A g_*(1+rho_0).                                   (SA13)

Every iterate has connected original-(V,epsilon) labels. Uniform convergence
proves epsilon holomorphy; real data yield a real b. The pointwise contraction
identifies it with CB's actual finite-u critical point, not its tree analogue.
The uniformity follows from the stated norms, not a fixed-volume implicit
function theorem. At flat coarse V, b=0 even for nontrivial compatible holonomy
and complex epsilon. Here that identity follows directly from (SA11).

Set K_epsilon=F_epsilon''(b), Delta_epsilon=K_epsilon-K_b. The same root/marked
composition of f'' gives Q(Delta_epsilon)<=D_K(tau,rho_0). Therefore

    (K_epsilon+a)^(-1)=G_a sum_(n>=0)(-Delta_epsilon G_a)^n,
    Q((K_epsilon+a)^(-1))<=A_G/(gamma+a-A_G D_K),
    Q(C_epsilon)<=Q_C:=A_G/sqrt(gamma-A_G D_K),
    C_epsilon=K_epsilon^(-1/2).                             (SA14)

The last formula follows from the resolvent integral. Every term retains both
matrix endpoints, original sources and full connectors. For real epsilon,
K_epsilon is positive: its operator perturbation is at most D_K<=gamma/2
(the displayed A_G is >=1). For complex epsilon the same series fixes the
symmetric bilinear branch; C_epsilon^T K_epsilon C_epsilon=I. The actual
full-colour determinant is localized by (SA9) and
Tr log(I+G_0 Delta_epsilon); the marked series costs at most
B(G_0 Delta_epsilon)/[1-M(G_0 Delta_epsilon)]. No independent-colour determinant
or omitted global modes are substituted.

The background action is also a connected composition, with a separate
budget. At a=0 its exact field-dependent part is
L^2 sum_(coarse P) W(V_P), plus 4T^4 sigma^2 log Ntilde_t(I). Its increment
to b is O(delta_V^2) in rooted norm: the linear coefficients are O(delta_V),
||b||_v=O(delta_V), and the remaining series starts at degree two. The uniform
normalizer estimate excludes its vacuum, which stays in this displayed main
term. After division by sigma^2 the action need not be small.

## 4. A fixed actual sector and its coefficientwise interaction

Fix real V in the above class. Let b_0=b(V,0), K_*=F_0''(b_0), C_0=K_*^(-1/2)
and define a(W)=b_0+sigma C_0 W, W in [-p,p]^(n_d). Keep this sector fixed as
epsilon varies. Choose any bounds M_C>=M(C_0), B_C>=B(C_0) from (SA14), and
put t_*=C_b delta_V, x=sigma p M_C, y=sigma p B_C. Require t_*+x<=a/2.
Let mu_p be the normalized independent truncated scalar Gaussian, with
z_p=(2pi)^(-1/2) integral_(-p)^p exp(-w^2/2)dw. Define

    M_epsilon(V)=sigma^(-2) sum_p epsilon_p W_p(b_0;V),
    U_0(W)=sigma^(-2)[F_0(b_0+sigma C_0W)-F_0(b_0)]-|W|^2/2,
    U_epsilon=U_0+sigma^(-2) sum_p epsilon_p
                          [W_p(b_0+sigma C_0W)-W_p(b_0)].  (SA15)

The cube is an actual real Haar sector in the fixed tree gauge. With the
chart margin, its exact raw integral (no additional retained history) is

    Z_sec=h_N^n(2pi sigma^2)^(n_d/2) det(K_*)^(-1/2) z_p^(n_d)
          exp[-F_0(b_0;V)/sigma^2-M_epsilon(V)]
          E_mu_p exp(-U_epsilon).                          (SA16)

Here h_N is the normalized Haar constant in HS coordinates. F_0 has already
absorbed all j factors once, so no second product j is inserted. The kernel
vacuum Ntilde_t(I), the full colour determinant and scalar n_d Gaussian
normalization remain. This is an ordinary real affine change of variables
for every complex epsilon on the fixed domain, not a contour-shift assertion.
For a retained history, insert its exact tree average/pullback in (SA16);
no analyticity or zero-freeness for that insertion follows automatically.

For the baseline remainder, define

    T_3(t,x)=f(t+x)-f(t)-x f'(t)-x^2 f''(t)/2.

Criticality and the actual K_* cancel the sum of linear and quadratic terms,
including Haar and normalizer, exactly. Expanding each vertex at zero before
substitution proves

    ||U_0||_beta <=sigma^(-2)d_0 e^(beta*s)
                  [T_3+t_* partial_t T_3+y partial_x T_3]
                <=A_0 sigma p^3,
    A_0=d_0 e^(beta*s) H 2^(q+3)/(6a^3)
         [((q)_3+(q)_4)M_C^3+3(q)_3 B_C M_C^2].             (SA17)

The mark can lie in the root, the background atom, or the fluctuation atom;
all three contributions are present. This is an all-order support estimate,
not a bound inferred from CB's first coarse derivative.

At a=0 a Wilson plaquette has |W_p|<=N delta_V^2/2 and scalar gradient sum
<=G_W delta_V, G_W=4D sqrt(N). Choose q_W=4D and a common analytic bound H_W
for its higher coefficients, and put

    f_2(t)=H_W[(1-t/a)^(-q_W)-1-q_W t/a],
    Q_W=H_W q_W(q_W+1)2^(q_W+2)/a^2,
    d_W=6L^4(2R+6)^4,
    T_delta(t,x)=G_W delta_V x+f_2(t+x)-f_2(t).              (SA18)

A choice H_W=N[1+exp(4sqrt(D)a)] is sufficient on the scalar polydisc.
Unlike the trivial-background formula, the first term of T_delta is present.
Applying the same three marks gives the actual source bound

    h_src<=rho sigma^(-2)d_W e^(beta*s)
       [T_delta+t_* partial_t T_delta+y partial_x T_delta]
          <=A_src(c) rho p^2,  if delta_V<=c sigma p,
    A_src(c)=d_W e^(beta*s){G_W c(M_C+B_C)
           +Q_W[2C_b c M_C+M_C^2/2+B_C(C_b c+M_C)]}.        (SA19)

For example f_2''<=Q_W on t_*+x<=a/2, which bounds its increment by
Q_W(t_*x+x^2/2). The other marks give Q_W t_*x and
Q_W y(t_*+x). The linear term gives G_W delta_V(x+y). This explicitly pays
the canonical force sqrt(u)*rho*delta_V*p. No source kernel normalization
was varied, and no linear source was subtracted from the integral by fiat.

The factored source vacuum has the distinct bound

    ||M_epsilon||_beta <=C_vac rho delta_V^2/sigma^2,
    C_vac=d_W e^(beta*s)[N/2+2G_W C_b+(3/2)Q_W C_b^2].      (SA20)

Indeed its majorant is N delta_V^2/2+G_W delta_V t_*+f_2(t_*), plus the
background incidence mark t_*[G_W delta_V+f_2'(t_*)]. On (SA4) this is
<=C_vac c^2 rho p^2. It is not charged to h, not erased, and not the
exponentially small returned-defect gas activity of H24.

## 5. Connected logarithm and complex saddle return on this sector

Equations (SA17),(SA19) instantiate CX-R with beta=mu+4 and output rate
nu=mu+2. Its elementary proof is worth identifying: expand e^(-U_S)-1 into
overlap-connected collections, integrate disjoint collections using the
product measure, then take the hard-core gas's connected graph series.
The first rooted-tree recursion costs one unit of support weight, the
repulsive connected-graph/tree bound costs another. For h<=1/4 both are
absolutely summable and give

    E_mu_p exp(-U_epsilon)=exp(sum_Y F_Y(V_Y,epsilon_Y)),
    sup_v sum_(Y containing v)e^(nu|Y|)||F_Y||<=2h.           (SA21)

The finite connected-graph identity near zero interaction, then analytic
continuation in its scalar multiplier, identifies the exponential with the
integral. Nonvanishing is a conclusion, not a premise. V is fixed real in
this argument; the external holomorphic product variables are the original
epsilon. Uniform V suprema of the constructed atoms preserve the bound.

Thus the EXACT source difference on the selected original Haar sector is

    log[Z_sec(V,epsilon)/Z_sec(V,0)]
       =-M_epsilon(V)+sum_Y[F_Y(V,epsilon)-F_Y(V,0)],
    rooted norm at nu <=C_vac rho delta_V^2/sigma^2+4h.       (SA22)

The remaining main action, determinant, gauge and cutoff constants cancel
only in this source ratio because the reference is fixed. They are still
present in (SA16) and have the separate connected budgets of §§2--3.

The stated norm is in FIXED R-box units. To express an activity in the
original level-zero block graph, fill every box in its label: the resulting
connected label has at most (2R)^4|Y| blocks and contains every original
variable read. For mu>0, the common output rate

    mu_block=mu/(2R)^4>0

therefore has a rooted block norm no larger than the displayed R-box norm.
A block root belongs to one box, so this direction introduces no population
factor. Choose mu first, then R, then this reduced rate. No arbitrary
prescribed block rate is promised; taking mu proportional to R^4 before
choosing R would destroy the residual argument. Conversely coarsening H24
from blocks to R-boxes costs the box population as stated in §7. These
explicit conversions prevent an entrywise diameter bound from being
misrepresented as the consumer's exp(mu_block*|X|) support-size bound.

The source-dependent complex critical point is also available, but does not
remove the boundary. For rho<=rho_0/2, atomwise Cauchy projection in epsilon
and (SA13),(SA14) give, with d=b_epsilon-b_0, E=C_epsilon-C_0,

    ||d||_v<=D_b delta_V rho, D_b=2C_b/rho_0,
    Q(E)<=D_C rho,           D_C=2Q_C/rho_0.                (SA23)

Let Q_D bound Q(C_0^(-1)) using C_0^(-1)=K_* C_0. If Q_D D_C rho<=1/2,
C_s=C_0+sE is invertible by its atom Neumann series, Q(C_s^(-1))<=2Q_D.
For b_s=b_0+sd the exact white velocity is

    v_s(W)=C_s^(-1)[sigma^(-1)d+E W],
    ||v_s||_v<=V_*=2Q_D(D_b c+D_C)rho p.                   (SA24)

This includes the sum over ALL output coordinates incident to a fixed
support box, as required when summing faces.

For completeness the action input on every interpolating contour is checked,
not assumed. Local Hessian composition gives Q(H_s)<=H_2 and
Q(H_s-H_1)<=H_3||b_s-b_1||_v, where H_s=F_epsilon''(b_s). One may use

    H_2=2d_2 e^(beta*s)(1+rho_0)[f''(tau)+tau f'''(tau)],
    H_3=2d_2 e^(beta*s)(1+rho_0)[2f'''(tau)+tau f''''(tau)].

Then g_s=F_epsilon'(b_s)=-integral_s^1 H_t d dt. Subtracting the EXACT
C_1^T H_1 C_1=I before bounding yields

    Q(C_s^T H_s C_s-I)<=A_Q rho,
    A_Q=2Q_C H_2 D_C+Q_C^2 H_3 D_b delta_A.

The interaction U_s=sigma^(-2)[F_epsilon(b_s+sigma C_sW)-F_epsilon(b_s)]
-|W|^2/2 contains its linear force, quadratic mismatch and cubic remainder.
Its norm is at most

    h_bar=A_3 sigma p^3+(H_2 D_b c Q_C+A_Q/2)rho p^2,        (SA25)

with A_3 given by (SA17) using H(1+rho_0), M_C,B_C enlarged to Q_C. Require
h_bar<=1/4 and the same analytic chart margin. These are nonempty uniform
conditions, not a claim for fixed delta_V>0 as sigma tends to zero.

Write I_s=h_N^n det(sigma C_s) integral_(cube)
exp[-F_epsilon(b_s+sigma C_sW)/sigma^2]dW. Its exact factorization is

    I_s=h_N^n(2pi sigma^2)^(n_d/2) det(C_s) z_p^(n_d)
                  exp[-F_epsilon(b_s)/sigma^2] Z_s,
    Z_s=E_mu_p exp(-U_s).

The determinant here is that of the ACTUAL intermediate affine map; it is
not replaced by det(H_s)^(-1/2). All its connected atoms follow from the
same inverse/trace series. The source-dependent main action is local too:
subtract its common kernel vacuum, and the coefficient bound is O(delta_V^2)
because the zero-order Wilson vertices are O(delta_V^2), their first
coefficients are O(delta_V), and ||b_s||_v<=C_b delta_V. A sufficient explicit
constant for this action bound is

    C_act=(1+rho_0)e^(beta*s){d_W N/2+
            d_0[2q sqrt(N) C_b+(3/2)Q_F C_b^2]},
    Q_F=H q(q+1)2^(q+2)/a^2.

The source difference of this main action divided by sigma^2 is therefore
<=2C_act delta_V^2 rho/(sigma^2 rho_0), by the same atomwise homogeneous
projection as (SA23). It remains an explicit vacuum budget, not part of
h_bar. The just proved product cluster bound, complete determinant and
main factor prove I_s!=0. Direct
differentiation gives

    partial_s[J_s f(a_s(W))]=div_W[J_s f(a_s(W))v_s(W)],
    J_s=det(sigma C_s), f=exp(-F_epsilon/sigma^2).           (SA26)

Here div v_s=Tr(C_s^(-1)E)=partial_s log J_s; the Jacobian minors are not
missing. Integrating each outward face gives the continuation's exact
normalized flux. Its common positive cluster majorant is independent of
whether one coordinate is Gaussian or pinned at a face. Changing measures
on A cancels all connected coefficients disjoint from A, leaving normalized
log ratio <=4h_bar|A|. Expanding these pinned ratios about each velocity atom
and marking either the root or one attached cluster gives the additional
factor 1+4h_bar. The remote mark is essential. Consequently

    log(I_1/I_0)=sum_Y Psi_Y(V_Y,epsilon_Y),
    ||Psi||_mu <=2 phi(p)/z_p (1+4h_bar)V_*,
    phi(p)=(2pi)^(-1/2)exp(-p^2/2).                         (SA27)

This rebuilds C25--C37 of the reviewed continuation on the new support-atom
input. I_0=Z_sec; I_1 is a holomorphic contour integral. Equation (SA27) is
an extensive connected logarithm with a bounded rooted norm. It does not
move an actual nonlinear hard indicator through a complex contour or say
that the raw side integral has a volume-independent absolute ratio.

## 6. A proved nonempty good-event margin, and a sharp scope obstruction

Let G be CB's strong event: ALL fine plaquettes have op defect <delta_f,
and every coarse V_c differs from its actual root-straight transporter by
<eta. It is the empty/empty history in [Sea7/11](SOURCE_SEA_CONSTRUCTION_ASTRA.md).
Choose delta_f<=epsilon_1 so G implies the original interior-only cut.
In scalar cube coordinates, the actual link HS norm is bounded by

    A_box=sqrt(D)[C_b delta_V+sigma p M_C].                  (SA28)

The sqrt(D) scalar-to-link conversion must not be omitted. For real a,
||exp(a_e)-I||op<=||a_e||HS. Telescoping the four unitary factors of an actual
plaquette and the L links of an actual root-straight path gives

    ||I-U_p(a)||op<=delta_V+4A_box,
    ||V_c-S_c(U(a))||op<=L A_box.                           (SA29)

The same bound for any S4-prime path is (5L)A_box. Hence sufficient strict
margins for the whole reference cube are

    A_box<r_ch,
    delta_V+4A_box<delta_f,   (5L)A_box<eta.                 (SA30)

They imply Omega_(V,p) subset G subset original cut, with positive real Haar
measure, and Z_sec(V,0)>0. They also place the smooth critical point itself
inside G on this explicitly narrower domain. No assertion of that kind is
made for CB's broader curvature class without (SA30).

The conditions are jointly nonempty. Fix small positive eta,delta_f satisfying
Sea9's delta_f<=min(epsilon_1,epsilon_loc/2,eta^2/(8N A_L)),
eta<=epsilon_loc/2, A_L=3L(L-1)/2, and the desired chart radii. Take, for example,
p(u)=max(1,sqrt(log u)), delta_V<=min(delta_A,c sigma p), and rho(u)p(u)^2
sufficiently small. Then sigma p^3 tends to zero, (SA30) eventually holds,
and all constants were fixed before u. A fixed physical Wilson-energy source
epsilon=-h/u on a fixed h disc also obeys this smallness condition. These
choices do not provide estimates on excluded coarse data. Alternatively keep
p fixed and choose a fixed positive rho satisfying (SA4),(SA25); this supplies
a fixed relative-coefficient disc for the selected sector, with
delta_V<=c sigma p. Neither choice supplies all-coarse-field coverage.

There is a decisive geometric obstruction to assuming broad-class G
nonemptiness. Filling the root coarse square by its L^2 fine plaquettes and
telescoping its four mismatches gives the NECESSARY condition

    G nonempty at V  ==>  delta_V<=L^2 delta_f+4eta.         (SA31)

For SU(2), take constant V_0=exp(i alpha sigma_3),
V_1=exp(i b sigma_1), V_2=V_3=I. Their coarse plaquette has defect
2|sin alpha sin b|. Fix alpha=0.7 and any 0<d<=delta_A; choose
b=arcsin[d/(2sin alpha)] (decrease d if needed). This has delta_V=d while
V_0 and its compatible winding holonomy need not be small. If

    delta_f=eta=d/[2(L^2+4)],

(SA31)'s right side equals d/2, so G is EMPTY. This exact family can be made
as small in curvature as any positive CB radius. It refutes an inference
from smooth critical-point existence alone to G nonemptiness. It is not a
counterexample to the sufficient margins (SA30) or to Sea's integrated prices.
It can also obey Sea9's threshold relations: instead take eta=d/16 and
delta_f=min(d/(4L^2),eta^2/(16N A_L),epsilon_1/2,epsilon_loc/4),
with d small enough that eta<=epsilon_loc/2. Then the right side of (SA31)
is still <=d/2. The balanced-threshold example is used in the finite checker;
this stricter variant follows from the displayed exact inequalities.

## 7. Exact hard-cut return and the remaining consumer mismatch

At every admitted fixed real V with (SA30), let the sector include all tree
variables and the cube in the free-coordinate quotient. Gauge-invariant cuts,
G, sources and kernels have the exact unit tree-gauge factor above. Then

    Z_cut(V,epsilon)=Z_sec(V,epsilon)
       + integral Haar chi_cut 1_(G minus Omega) w_epsilon
       + integral Haar chi_cut 1_(G^c) w_epsilon.           (SA32)

The original Z_cut(V,0) is positive for EVERY real V by H5, even where G
is empty; the emptiness example concerns the stronger event only.
All integrals use the ORIGINAL Wilson times normalized S4-prime kernel.
There is no use of integrated kernel normalization at fixed V. For any
non-invariant retained history its exact tree average remains as an insertion.
The second term in (SA32) is not empty merely because the cube lies inside G;
the third retains all fine-defect, mismatch and dirty-coarse histories.
For coarse V outside the admitted window, the original transform remains
untreated, even if G happens to be nonempty there.

Since Z_sec is nonzero, define the exact normalized complement B_comp by
dividing the last two terms of (SA32) by Z_sec. A full source logarithm would
require a proved zero-free, connected original-source control of

    1+B_comp(V,epsilon),
    log Z_cut=log Z_sec+log(1+B_comp).                      (SA33)

Neither (SA21), smooth saddle existence, nor the CT gap proves (SA33)'s
missing bound. Real positivity at epsilon=0 is insufficient on a complex
source disc. The boundary flux (SA27) is for two selected analytic cubes;
it is not a bound on B_comp.

The existing [H14/H24/H25 return](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md) must
also retain its exact domain. H24 controls the pointwise returned completion-
good gas at FIXED real sea U,V, with full collar/source labels, by d_q tending
exponentially to zero in u on D_(rho,lambda)(u). Grouping it into these R-boxes
costs at most (2R)^4 d_q, or the actual smaller maximum box block count.
It supplies no clustering of the normalized original sea average and does
not price completion failures. The new sector's interaction norm is h and
its source-main norm is (SA20); neither is relabelled as d_q.

In particular H24 is holomorphic in ORIGINAL epsilon with real U,V. After
U=b_0+sigma C_0W in group coordinates, its hard completion/history factors
are generally neither product events nor analytic local interactions in W.
The coefficientwise composition proof (SA17)--(SA19) cannot be applied to
such a factor without a new domain/regularity estimate. A simple exact
obstruction is the actual SU(2) plaquette indicator
1_{2|sin(a/2)|<=delta_f}. At a threshold a_*=2arcsin(delta_f/2), a nonzero
remote response h changes it from one to zero between a_*-h/2 and a_*+h/2,
for arbitrarily small h. Thus an exponential tail in a field map does not
imply an exponentially small UNIFORM-NORM error of the hard indicator.
This is not an integrated lower bound or a proof that boundary estimates
are impossible. It identifies why a measure-sensitive boundary/completion
producer, rather than the analytic Taylor lemma, is still needed.

LIB1's fixed-mask saturation algebra is not needed for this global cube.
Its reviewed mathematical statements remain conditional on their actual
input norm; the package HOLD/checker repair reported by the coordinator is
not overridden here. Arbitrary holes/collars, reference integration, all
coarse fields, interacting RG induction, continuum existence and physical
gap remain outside this unit.

## 8. Primary-source comparison, checks, and freeze

The fresh primary reading is version-specific. Bałaban--Feldman--Knörrer--
Trubowitz [1609.01748v1](https://arxiv.org/abs/1609.01748v1), Appendix A,
pp.41--42, states a field-map contraction with both output and marked-input
kernel norms. Its weights and finite-degree bosonic maps differ from ours;
(SA10)--(SA14) rebuild an all-order analytic contraction with the actual
S4-prime normalizer and full connected-support incidence. No theorem for
d=4 nonabelian links is imported from that bosonic model.

Their [1609.01747v1](https://arxiv.org/abs/1609.01747v1), pp.1--3 and 12--15,
keeps a separate Stokes side and outside-domain remainder when moving to a
complex critical point; the paper explicitly says its full nonperturbative
error argument is incomplete. It therefore supplies no theorem for (SA33).
The exact selected-cube flux is instead rebuilt in (SA23)--(SA27). Dimock's
[1410.2798v3](https://arxiv.org/abs/1410.2798v3), §§3.7--3.10, pp.16--21,
and [1212.5562v2](https://arxiv.org/abs/1212.5562v2), Appendix F, pp.91--92,
were already read completely at those loci in this author context. Their
local coordinates/independent Gaussian and product-interaction mechanisms
are reused through the explicit d=4 finite-kappa scalar dictionary above;
their d=3 abelian/scalar hypotheses do not supply a Yang--Mills hard-history
bound. Full PDFs/text stay in /tmp; hashes and exact coverage are recorded.

Numerical checks were registered before new scripts. The scientific checks
are author diagnostics, not independent review or a proof of uniform
constants. The receipt binds their final source and outputs;
failed attempts remain named. The new exact conditional-fibre check keeps
the actual one-link group normalizer, the three-colour Haar chart density,
a noncommuting coarse plaquette, and the original Wilson source. It tests
fixed-reference factorization and normalized complex-contour flux by distinct
integration routes. It does not integrate the other fine links or colours
and does not claim to numerically certify the very conservative sufficient
radii in (SA12).

The checked fibre also has a concise exact formula. For L=3, vary the free
crossing edge ((1,1,0,0),0) at the crossing lift of constant coarse
V_0=exp(0.55 i sigma_1), V_1=exp(0.11 i sigma_2), V_2=V_3=I. Write its
noncommuting coarse plaquette as P=qI+i s n.sigma, s>0, and vary that link
by exp(i a n.sigma). Exactly 72 of 1944 paths read it, each once, so
f=1/27 and M=[(1-f)I+f exp(i a n.sigma)]V_0; every other kernel is constant.
The six incident Wilson plaquette terms sum to
5(1-cos a)+1-q cos a+s sin a. Put the original epsilon only on that curved
plaquette. With all other links and the other two HS colour coordinates
fixed, the density in da, up to a source-independent frozen factor, is
(4pi^2)^(-1)exp[-ell(a;epsilon)] da, where

    ell=u[5(1-cos a)+(1+epsilon)(1-q cos a+s sin a)]
          +log Z_0(t r(a))-t(1-f+f cos a)-2log(sin(a)/a),
    r(a)^2=1-2f(1-f)(1-cos a),    Z_0(z)=2 I_1(z)/z.        (SA34)

The analytic value at a=0 is understood. The last term is the FULL
three-colour exponential Haar Jacobian restricted to the fibre, not the
Haar measure of a U(1) subgroup. Its constant includes the change from the
HS coordinate sqrt(2)a to a. Z_0 is the normalized SU(2) Haar tilt integral;
its scalar radial formula follows by its convergent invariant power series,
and is continued analytically for the complex contour. Thus the diagnostic
is a literal conditional colour fibre of the prescribed model. Its chosen
curvature is not claimed to satisfy the very conservative (SA12) constants.

The actual-model checker passed **36/36** registered predicates at 55 decimal
working precision. The affected kernel has 72/1944 varying-edge paths; all
27,216 words of the other endpoint kernels contain that edge zero times.
Independent matrix products reproduce all six incident plaquettes. At
u=20,kappa=1.3 the real fibre center is about -0.01899405 and the source
center is -0.01931082-0.00023636i. The complete precision is 120.645512;
omitting the field-dependent normalizer changes it by +0.874193 and omitting
the Haar term by -0.666715. The contour log ratio is approximately
-0.00095343-0.00070813i; integrated normalized flux agrees within 1.3e-57.
Fixed-reference factorization agrees within 2.1e-56. The nonzero source
vacuum and canonical linear term are separately detected.

The separately written finite matrix/atom checker passed **32/32** predicates.
It uses noncommuting three-colour transports, different local coefficients,
actual local inverse matrices and patch residuals. The wrong residual sign,
wrong noncommuting multiplication order, missing remote source/connector or
column-incidence count, and three-identical-colour determinant alternatives
are rejected. Its complete logdet is 26.628490 versus 26.922393 for the wrong
colour replacement. These finite checks supplement the all-order proof;
they do not certify astronomical sufficient radii or replace uniform norms.

Both registered scientific runs completed on their first execution with empty
stderr. The primary-source retrieval first encountered Python certificate
configuration and an unavailable pdftotext executable; native curl with normal
TLS checking plus PyMuPDF succeeded. These are retrieval/tool failures, not
scientific failures. The original outputs are preserved. The exact numerical
registration, scripts, outputs, source/dependency hashes, read coverage and
primary versions are bound in
[the author receipt](checks/covariant_source_activity_receipt.json).
Fresh hostile review of this new unit is required before promotion.
