# An explicit Brillouin formula for the bare determinant coupling

This unit reduces BM's unevaluated determinant marginal to one absolutely
convergent integral over the finite coarse Brillouin zone. Every matrix entry
is specified by the actual paired contour words, degree-four matrix
polynomials, and four explicit traceless saddle-recursion steps. The fine
critical response is an explicit gapped matrix inverse. Its second variation
vanishes for the Cartan backgrounds used in the projection, by a symmetry
argument for the actual constrained SU(N) action.

The result is an analytic integral formula, not an evaluated number or a
sign theorem. It retains the actual tree-action scheme and all free modes.
It assumes neither a perfect action nor a nearest-neighbor coarse quadratic
symbol. No continuum beta-function constant is inserted. Inherited-class
closure, a repeated trajectory, non-freeness, continuum existence and a
positive physical continuum mass gap remain **OPEN**.

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

## 1. Literal one-loop quantity and the intrinsic measure

The local sources are [BM](BARE_COUPLING_MATCH_ASTRA.md),
[CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md),
[FK](FINITE_COUPLING_KERNEL_ASTRA.md),
[IC](INTERACTING_SELECTED_CORE_ASTRA.md), and
[BR](BARE_COUPLING_REMAINDER_ASTRA.md). Their mathematics, not review labels,
supplies the bounded interfaces used below.

Fix N>=2, D=N^2-1, odd L>=3, and 0<kappa_-<=kappa<=kappa_+.
All original Wilson sources are zero. The underlying finite-u density,
probability Haar convention and full critical prefactor are BM1--BM2.
Its actual normalized paired-contour tree phase is

    F_T(U,V)=sum_p tr(2I-U_p-U_p^-1)/2
                         +N kappa sum_c [phi_star(M_c)-phi(V_c;M_c)],
    phi(W;M)=[tr(W^-1 M^+)+tr(M^- W)]/(2N).                (BD1)

M^+ is the average of the 24L^4 actual words and M^- the average of their
inverses. The two means are distinct. At real fields phi_star is the SU(N)
maximum; near I it is FK's actual constrained holomorphic saddle. No U(N)
polar factor or unnormalized quadratic penalty is substituted.

Let U_T(V)=exp(b_T(V))U0(V) be the classical stationary branch on the fixed
small original-coarse domain of IC/BM. There are m0=3L^4+1 free whole links
per block after the original internal tree quotient. Its gauge volume and
Jacobian are one. Put d=(N^2-1)m0 T^4 on a coarse torus of side T.
In right-translated free-link coordinates, define

    K_intr(V)=partial_x^2 F_T(U_T(V) exp(x),V)|_(x=0),
    Gamma_1(V)=sum_c log A_c(U_T(V))+(1/2)TrLog K_intr(V),
    A_c=h_N(2pi)^(D/2) det(H_c)^(-1/2).                  (BD2)

H_c is the FULL D-colour Hessian of minus phi at its SU(N) maximizer in
HS-orthonormal group coordinates. These quantities include all root,
crossing, harmonic and colour modes. No extra gauge or ghost determinant
is appended to this tree quotient.

Here is the exact Haar accounting from IC30/BM23. If K_coord is the Hessian
in the original a coordinates, the differential into U_T exp(x) is

    E_e=Ad_(U0_e^-1) (1-exp(-ad b_T,e))/(ad b_T,e),
    det E=product_e j_N(b_T,e), K_coord=E^T K_intr E,
    (1/2)TrLog K_coord-sum_e log j_N(b_T,e)
                                      =(1/2)TrLog K_intr. (BD3)

The second differential of the coordinate map multiplies the full tree
gradient and vanishes. The real positive branch continues locally. Thus
Haar has combined with the coordinate determinant, not been omitted.
The constants h_N, (2pi)^(D/2), the Gaussian vacuum and normalizer vacuum
remain in the literal prefactor and BD2 until differentiation. Coarse V is
an argument, not a new integration variable, so no coarse-chart Haar
Jacobian is introduced by the plane-wave test.

The target is BM's coefficient

    b1=beta_av[Gamma_1],
    b_det,intr,mu nu=beta_mu nu[(1/2)TrLog K_intr],
    beta_av=(1/12)sum_(mu!=nu) beta_mu nu.                 (BD4)

BM26 defines beta with FLOW-unit colour, a phase-averaged cosine wave,
volume first and then P->0, divided by lambda(P)=4 sin^2(P/2).
Section 7 derives every factor of that normalization in the new formula.
The actual finite-u prefactor error is BM's separate O(1/u) result. BR's
original-cut remainder has the same literal P_u; it is not recomputed here.

## 2. The exact finite cell, words and flat propagator

All ingredients below are finite and deterministic for specified N,L,kappa.
Let h=(L-1)/2 and B={-h,...,h}^4. A positive fine link has unique tail
LX+y, y in B, and orientation rho. Its owner is X. The internal rooted tree
joins each nonroot y to the site obtained by moving its highest nonzero
coordinate one step toward zero. Delete precisely these undirected tree
edges from the set of 4L^4 positive owned links. List the remaining
m0=3L^4+1 types e=(y,rho) lexicographically. An absent tree-link field is zero;
a tree-link group matrix is I. No other free type is removed.

Every signed path edge is reduced to a positive edge with its actual owner
X+delta, type e and sign s=+1 or -1. Negative edges mean inverse group
matrices in the reversed position, not a sign inserted after multiplication.
This rule also defines periodic words without deleting repeated occurrences.

For each coarse link c=(X,rho), each y in B and pi in S4, define its word:
start at LX, move in coordinate order pi to LX+y, move L positive rho steps,
then return from L(X+rho)+y to L(X+rho) along the reverse of the SAME pi
axial path. Denote it T_(c,y,pi). Thus

    M_c^+=(1/(24L^4))sum_(y,pi) T_(c,y,pi),
    M_c^-=(1/(24L^4))sum_(y,pi) T_(c,y,pi)^-1.           (BD5)

Internal axial legs stay in their endpoint blocks. The supplied paired
order, arithmetic averaging and all crossing links are explicit here.
The plaquette list consists of the 6L^4 positively oriented fine plaquettes
with tail in B_X, using pairs rho<sigma. Its signed edge word is the usual
four-edge product in its displayed orientation.

From these same lists construct scalar Laurent matrices. For q in the
coarse Brillouin zone [-pi,pi]^4, set

    D(q)_(p,e)=sum_(signed occurrences (delta,e,s) in p) s exp(i q.delta),
    Q(q)_(rho,e)=(1/(24L^4))sum_(y,pi)
                  sum_(occurrences (delta,e,s) in T_(0,rho,y,pi))
                                                    s exp(i q.delta),
    K0(q)=D(-q)^T D(q)+kappa Q(-q)^T Q(q),
    G(q)=K0(q)^-1.                                       (BD6)

D has 6L^4 rows and Q has four rows; both have m0 columns. For real q,
minus-transpose is conjugate transpose. For complex q the displayed
Laurent expression is its analytic continuation. The counting inner product
is used, with no hidden L^-4 Fourier factor: q labels coarse cells, and
there are m0 actual fine types per cell.

At flat data the full intrinsic precision is K0(q) tensor I_D. To verify
BD6 from the normalized kernel, write ell_r for the first path variation.
The first saddle variation is Y1=average ell_r. Its quadratic maximum
cancels average ||ell_r||^2-||average ell_r||^2. The kernel quadratic form
in F_T is therefore kappa||B-QA||HS^2/2, and the Wilson form is
||DA||HS^2/2. This is BM4--BM5's actual leading-normalizer cancellation.

CB6's lifted-brick recovery gives, on every real q,

    K0(q)>=a_gap I,
    a_gap=1/max(4L^3(L+4)(60L^2)^2,2L^3/kappa_-)>0.       (BD7)

It holds on the full free space, including q=0. Inverting BD6 never requires
a prime, an infrared regulator or a deletion of a root/harmonic direction.
The same signed-word construction periodized to a torus keeps the T=2
lifted-brick convention; no far-seam edge is added to an averaging brick.

For a coarse plane polarized in direction mu, let e_mu be its four-vector
and define the absolute fine linear response

    Phi_mu(p)=kappa G(p) Q(-p)^T e_mu.                    (BD8)

Indeed the full first critical equation is K0 A=kappa Q^* B. If E inserts
B on every outgoing crossing link, then Q(p)E=I and the original relative
critical response is Phi_mu(p)-E e_mu. This retains the critical motion;
using only the brick lift E would give different vertices below. At p=0,
D(0)E=0, so Phi_mu(0)=E e_mu. Constant external harmonics are retained.

## 3. Cartan critical motion is commuting and odd

Choose once the concrete FLOW-unit colour

    H=i sqrt(N/2) diag(1,-1,0,...,0), -tr H^2/N=1.         (BD9)

At quadratic field order the global-SU(N)-invariant colour bilinear form is
a multiple of -tr(AB), as in BM's flat extraction. Thus this concrete choice
computes the same normalized projection as any FLOW-unit colour. More
generally the following argument works for any real Cartan-valued coarse profile. At sufficiently small real profile amplitude, the actual
classical branch is unique in a fixed pointwise neighbourhood. Shrink the
coarse domain once so its compact diagonal-adjoint orbit stays within that
uniqueness neighbourhood; HS norms and the internal tree are preserved.

Every constant diagonal g in SU(N) fixes Cartan coarse V. Simultaneous
fine conjugation maps the exact action BD1, its SU(N) maximizer and its
tree section to themselves. Therefore uniqueness forces every critical
fine link to commute with the diagonal torus: U_T(V) is diagonal. This
argument uses the whole diagonal torus and does not require H to be regular.

Entrywise complex conjugation preserves SU(N), every ordered path product,
the real Wilson action and the constrained maximum: the bijection
W->conjugate(W) gives phi_star(conjugate M)=phi_star(M) at real data.
It also preserves the pinned tree. For a real Cartan profile B and real t,
V(-t)=conjugate V(t). Uniqueness implies

    U_T(V(-t))=conjugate U_T(V(t)),
    A_T(-t)=-A_T(t), A_T(t)=Log U_T(V(t)),
    b_T(-t)=-b_T(t), b_T''(0)=0.                         (BD10)

The last equality follows because diagonal matrices commute and
A_T=b_T+t EB. Log uses the common near-I traceless branch. Quadratic
critical derivatives also vanish between ANY two Cartan profiles: polarize
the zero diagonal quadratic map, then complexify that finite Taylor identity.
This justifies independent external momenta p and -p below.

Thus for z_+,z_- close to zero and p=P e_nu, mu!=nu, the critical fine
background to the order needed is exactly

    A_(X,e)= [z_+ exp(i p.X) Phi_mu,e(p)
                         +z_- exp(-i p.X) Phi_mu,e(-p)] H +O(z^3),
    B_(X,rho)=delta_(rho,mu)
                         [z_+ exp(i p.X)+z_- exp(-i p.X)] H. (BD11)

Terms O(z^3) cannot contribute to a Hessian in two fine fluctuations with
at most two external insertions. They are not set to zero at higher order.
The physical coarse and fine matrices still use their actual exponentials;
their second matrix variations, such as B^2, are retained. This removes the
implicit b_T'' term in BM29 without removing any nonlinear word variation.

## 4. A finite polynomial for every actual tree vertex

This section replaces unspecified derivatives of the saddle by explicit
matrix operations. Use commuting formal scalar variables (s,t,z) or
(s,t,z_+,z_-), retaining total degree at most four in those variables.
Matrix factors remain noncommutative. Put

    Exp_4(Z)=I+Z+Z^2/2+Z^3/6+Z^4/24,
    P0 Z=Z-(tr Z/N)I.                                    (BD12)

On a free positive link use the INTRINSIC order

    U_(X,e)=Exp_4(A_(X,e)) Exp_4(x_(X,e)),
    U_(X,e)^-1=Exp_4(-x_(X,e)) Exp_4(-A_(X,e)).            (BD13)

Set tree links to I. For the coarse link use V_c=Exp_4(B_c) and its inverse
Exp_4(-B_c). Compute each plaquette and each T word by its actual ordered
list, truncating after products. Compute the two arithmetic means BD5
separately. Inverting a mean is never an instruction in this recipe.

For EACH of the four kernel means rooted at cell 0, perform the following
four homogeneous steps. If [.]_n denotes total homogeneous degree n, set

    Y_<1=0,
    Y_n=(1/2)P0[Exp_4(-Y_<n) M^+ - M^- Exp_4(Y_<n)]_n,
    Y_<n+1=Y_<n+Y_n,                 n=1,2,3,4,
    Y=Y_1+Y_2+Y_3+Y_4.                                  (BD14)

No equation remains to be solved in this rule. Its validity follows by
expanding FK4: at degree n the new unknown Y_n occurs only as -2Y_n.
Consequently BD14 is the unique Taylor recursion for
P0(exp(-Y)M^+-M^- exp(Y))=0, with tr Y=0. FK's fixed analytic saddle domain
identifies these coefficients with the ACTUAL SU(N) maximizer branch.
The scalar residual (exp(-Y)M^+-M^- exp(Y))/2=lambda I is retained;
it is not replaced by zero as in an unconstrained U(N) prescription.

The required local phase polynomial is now completely specified:

    F_loc= sum_(fine plaquettes with tail in B_0)
                             tr(2I-U_p-U_p^-1)/2
       +(kappa/2) sum_(rho=1)^4 tr[
           Exp_4(-Y_rho) M_rho^+ + M_rho^- Exp_4(Y_rho)
          -Exp_4(-B_(0,rho)) M_rho^+
                                  -M_rho^- Exp_4(B_(0,rho))]. (BD15)

It is the degree-four Taylor polynomial of the actual BD1 contribution
owned by cell 0. There are 6L^4 plaquettes and four kernel terms, each with
exactly 24L^4 words. All field-independent terms are still present in the
underlying phase; coefficient extraction below simply differentiates them
to zero. The normalized-kernel saddle enters BOTH cubic and quartic vertices.

For full colour coordinates use the explicit HS-orthonormal real basis

    T_r=i diag(1,...,1,-r,0,...,0)/sqrt(r(r+1)), 1<=r<N,
    T_ij^a=(E_ij-E_ji)/sqrt(2),
    T_ij^s=i(E_ij+E_ji)/sqrt(2),                 1<=i<j<=N. (BD16)

All N-1 diagonal generators and N(N-1) off-diagonal real generators occur.
The projection colour H has HS norm sqrt(N); it is not silently normalized
to one in these fine-loop coordinates.

## 5. Explicit cubic and quartic momentum matrices

For each entry (e,alpha;f,beta), insert the following link fields into BD15.
The owner X in the formulas is the actual integer displacement of that
positive link from cell 0. Coarse and fine background fields are always
built using BD8 and BD11. Fourier tests on negative path edges are obtained
by BD13, not assigned independently.

For the cubic matrix V_mu(q;p), use only z_+ = z and set z_-=0. Put

    x_(X,g)=s delta_(g,e) exp[-i(q+p).X] T_alpha
                            +t delta_(g,f) exp[iq.X] T_beta,
    V_mu(q;p)_(e alpha,f beta)=[s t z] F_loc.              (BD17)

For the quartic matrix W_mu(q;p), use both external variables in BD11 and

    x_(X,g)=s delta_(g,e) exp[-iq.X] T_alpha
                            +t delta_(g,f) exp[iq.X] T_beta,
    W_mu(q;p)_(e alpha,f beta)=[s t z_+ z_-] F_loc.        (BD18)

Even for repeated indices the parameters s,t are independent. The coefficient
[st] of a quadratic action is its bilinear Hessian, so neither definition
has an additional factor 2. Both matrices have size Dm0. Their entries are
finite sums of products of the explicitly listed N-by-N matrices, phases
and entries of Phi_mu(plus/minus p). They contain no implicitly defined
critical-field derivative, no unsolved SU saddle and no unspecified vertex.

The total momentum of each extracted monomial is zero. Translating its
owning cell therefore multiplies it by one. On a compatible torus, summing
BD15 over cells gives exactly T^4 times each displayed coefficient.
Consequently V_mu(q;p) is the coefficient of z_+ mapping fluctuation
momentum q to q+p. The other linear coefficient maps q+p back to q and is
V_mu(q+p;-p). W_mu(q;p) is the coefficient of z_+z_- at momentum q.
By BD10 these are the total derivatives of the actual intrinsic Hessian,
including its critical motion, through the required order.

Colour mixing is genuine even though the flat propagator is scalar in
colour. To make all multiplicities independently checkable, the equivalent
complex weight decomposition is as follows. Use the neutral basis T_r and
the root vectors F_ij=i E_ij, i!=j. Their bilinear HS duals are F_ji because
-tr(F_ji F_ij)=1. A neutral vertex entry is obtained from BD17--BD18 with
row T_r and column T_s. A root entry of weight ij uses row F_ji and column
F_ij. The Hessian commutes with the full diagonal torus because every
background in BD11 does. Thus its operator has one neutral (N-1)m0 block
and N(N-1) root blocks of size m0. For example the two traces below mean

    tr(G_D W)=sum_r tr_m0(G W_rr)+sum_(i!=j) tr_m0(G W^ij),
    tr(G_D^+ V G_D V^-)
       =sum_(r,s) tr_m0(G^+ V_rs G V^-_sr)
                        +sum_(i!=j) tr_m0(G^+ V^ij G V^-,ij). (BD19)

Here G_D=G tensor I_D, G^+=G(q+p), and V^- is the return-momentum vertex.
This is a change of basis in a full trace, not a deletion of neutral modes.
No assertion that the answer is D copies of a scalar determinant is made.

## 6. An integrand requiring only finite matrix operations

Define, with normalized coarse Brillouin measure dq/(2pi)^4,

    J_mu(q;p)=tr_(Dm0)[
        G_D(q) W_mu(q;p)
       -G_D(q+p) V_mu(q;p) G_D(q) V_mu(q+p;-p)],
    I_mu nu(P)=(1/2)int_[-pi,pi]^4 J_mu(q;P e_nu) dq/(2pi)^4. (BD20)

BD5--BD18 specify every entry of this integrand. For further explicitness,
the infrared coefficient can be obtained with a FINITE momentum polynomial;
there is no remaining need to differentiate an implicit branch. All of the
following identities are formal rules, not executed numerical calculations.

Set p=P e_nu and retain degree at most two in P, independently of the
fourth-order field-tag truncation above. In every finite Laurent entry use

    exp(iP delta_nu)=1+iP delta_nu-P^2 delta_nu^2/2 mod P^3.

If K0(q+P e_nu)=K0(q)+P K1(q)+P^2 K2(q) mod P^3, its inverse coefficients are

    G0(q)=G(q),
    G1(q)=-G0(q) K1(q) G0(q),
    G2(q)=G0 K1 G0 K1 G0-G0 K2 G0.                       (BD21)

The K_j are obtained directly from BD6's finite signed-word Laurent sum;
K2 includes its Taylor factor 1/2. Write
Q(-P e_nu)^T=Qtilde_0+P Qtilde_1+P^2 Qtilde_2. Then the three required
external-response coefficients are

    Phi_0=kappa G0(0) Qtilde_0 e_mu,
    Phi_1=kappa [G1(0)Qtilde_0+G0(0)Qtilde_1] e_mu,
    Phi_2=kappa [G2(0)Qtilde_0+G1(0)Qtilde_1
                                      +G0(0)Qtilde_2] e_mu. (BD22)

Use Phi(-p)=Phi_0-P Phi_1+P^2 Phi_2. These rules also expand the shifted
momentum in the return vertex V(q+p;-p), including its fluctuation phases.
After ordinary finite matrix multiplication define

    J_(mu nu),2(q)=[P^2] J_mu(q;P e_nu).                  (BD23)

This is an explicit continuous function of q, rational in the gapped matrices
K0(q) and K0(0), and polynomial in the finite contour phases and listed
colour matrices. It has no unspecified response or third/fourth derivative
symbol. Only the four-dimensional compact-domain integral remains.

## 7. Finite-volume derivation, convergence and the exact coefficient

Initially take P/(2pi) rational and tori compatible with that period; the
continuous symbols also allow compatible P_T tending to any fixed real P.
At such a torus momentum p, introduce independent z_+,z_- and the actual
critical intrinsic Hessian K(z). Its Taylor coefficients have the form

    K(z)=K0+z_+ K_+ +z_- K_-+z_+z_- K_+-
                              +pure-square terms+O(z^3).

They are exactly the matrices BD17--BD18 in momentum space. Expanding the
analytic trace-log at the positive K0 gives

    [z_+z_-] (1/2)TrLog K(z)
       =(1/2)Tr[G K_+- -G K_+ G K_-].                   (BD24)

This identity only proves the trace weights; all its entries have already
been evaluated to the finite recipes above. The equality of the two ordered
cross terms uses cyclicity of the FULL trace. Dividing by T^4 converts it
exactly to (1/2) times the finite q-grid average of J_mu(q;p). No modes or
normalization factors have been removed in this step.

For the real cosine wave set z_+=epsilon exp(i theta)/2 and
z_-=epsilon exp(-i theta)/2. Its phase-averaged epsilon^2 coefficient per
cell is therefore I_mu nu(P)/4 after the volume limit. This agrees with
BM26's convention F^(2)/T^4=epsilon^2 Pi_mu mu(P e_nu)/4: the determinant
contribution to that Pi is precisely I_mu nu(P), not twice that value.

For clarity, convergence here needs no massless loop regularization. BD7
bounds ||G(q)||<=a_gap^-1. Write the finite Laurent sum K0(q)=sum_delta
K_delta exp(iq.delta), and let

    M_K=max_(kappa in [kappa_-,kappa_+],nu)
          sum_delta |delta_nu| exp(|delta_nu|) ||K_delta||,
    r=min(1/2,a_gap/(4(1+M_K))).

For real q and complex |P|<=2r, the inverse of K0(q+P e_nu) has norm at
most 2/a_gap by its Neumann perturbation of K0(q). The same bound holds for
the external inverse at plus/minus P e_nu. The finite word products and BD14
therefore give finite uniform bounds M3 for BOTH V(q;p), V(q+p;-p), and M4
for W(q;p), throughout that disc. They can be obtained by summing the absolute
coefficients of the displayed finite polynomials, using the inverse bound
and |exp(iP delta_nu)|<=exp(2r|delta_nu|). They are uniform over the stated
kappa interval and compact real q zone. Cauchy on |P|=r gives, for example,

    |b_det,intr,mu nu|
       <=(Dm0/(2r^2))[M4/a_gap+2 M3^2/a_gap^2].          (BD25)

This also proves absolute convergence and permits momentum differentiation
under the integral. Finite compatible q-grid sums converge to BD20 by
continuity, with the same bound. The infinite-volume limit is taken at each
fixed nonzero external P before P tends to zero. A complex momentum symbol
is only an algebraic/Green-function continuation here; no unbounded complex
plane wave is inserted into a global field domain.

The full determinant functional in BD2 is invariant under real coarse root
gauges. The induced transformation of right fine-link tangents is blockwise
orthogonal Ad at the endpoint, with determinant one. Uniqueness identifies
the classical branches. Its first coarse derivative at I vanishes by global
SU(N) invariance. The intrinsic determinant inherits BM22--BM25's fixed-domain
reader bounds through BD3: the coordinate determinant has those bounds, and
each local log j_N(b_T,e) has the same canonical critical-substitution bound.
Their original-reader second moments therefore give the Ward identity for
its volume-first symbol,
Pi(P)d(P)=0 with d_rho(P)=exp(iP_rho)-1, and hence Pi(0)=0. Real Hessian
symmetry and translation invariance make its diagonal axis symbol even.
Equivalently these conclusions follow from the exact finite-grid identity
BD24 and the same local thermodynamic limit. Finite-torus holonomy responses
remain until that limit; they are not set to zero at finite T.

All original readers are those of the actual critical/determinant functions.
The finite-cell Fourier representation is only an evaluation of their flat
Hessian. BM's canonical local-coefficient agreement and exponential seam
bound identify the finite-grid limit with its original-reader moment limit.
No coarse cell is renamed as a larger reader and no extensive trace bound
is substituted for that local moment statement. The analytic bounds above
also show directly that the required derivatives of the explicit symbol exist.

Consequently the promised determinant formula is

    b_det,intr,mu nu
       =lim_(P->0) I_mu nu(P)/[4 sin^2(P/2)]
       =(1/4)int partial_P^2 J_mu(q;P e_nu)|_0 dq/(2pi)^4
       =(1/2)int J_(mu nu),2(q) dq/(2pi)^4.              (BD26)

The zero-momentum cancellation is a property of the integrated symbol.
One must not set J_mu(q;0) to zero pointwise. BD21--BD23 implement the
last equality with only finite Taylor coefficients and gapped inverses.

## 8. Normalizer amplitude, colour normalization and relation to BM's trace

For completeness the other term of BD2 also has a finite-momentum formula.
Let ell_(rho,r)(p) be the signed path current of the absolute response
Phi_mu(p) along the r-th actual word of coarse direction rho. It is obtained
from the same signed occurrences as Q. Put

    v_rho(p)=average_r ell_(rho,r)(p) ell_(rho,r)(-p)
                      -(average_r ell_(rho,r)(p))
                                         (average_r ell_(rho,r)(-p)). (BD27)

For real p this is nonnegative. At the commuting background BD11, the
saddle-recentered matrix S=(exp(-Y)M^++M^- exp(Y))/2 obeys S_+=S_-=0 and
S_+-=v_rho(p) H^2. FK10 gives

    (H_c)_alpha beta=-tr[S(T_alpha T_beta+T_beta T_alpha)]/(2N),
    H_c(0)=I_D/N, sum_alpha T_alpha^2=-(D/N)I.

Thus [z_+z_-] log A_c=D v_rho(p)/2, with no absent colour trace or change
of probability-Haar normalization. The amplitude symbol is

    I_amp,mu nu(P)=(D/2)sum_rho v_rho(P e_nu),
    alpha_amp=beta_av[sum_c log A_c]
                              =D(L^2-1)/(12L^2).        (BD28)

The last evaluation is BM16--BM17's constant-curvature current calculation:
each path current differs from its mean by -L sum_sigma y_sigma
F_fine,rho sigma; the two orientations of the selected plane give variance
2[(L^2-1)/12]L^-2 times its coarse curvature squared. The gapped response
identifies that affine calculation with the small-P derivative. This uses
the actual arithmetic paired words and the actual Phi; it is not a perfect-
action value inserted into BD27.

Combining the explicit integral with the amplitude gives the main reduction

    b1(N,L,kappa)=D(L^2-1)/(12L^2)
       +(1/24)sum_(mu!=nu) int_[-pi,pi]^4
                                  J_(mu nu),2(q) dq/(2pi)^4. (BD29)

This is the same b1 as BM27. In BM28's original coordinate determinant,

    b_det,coord,av=b_det,intr,av-alpha_Haar,
    alpha_Haar=N^2(L^2-1)(L+1)/72.                        (BD30)

Indeed beta[sum log j_N(b_T)]=-alpha_Haar by BM17 and
log j_N(b)=-N||b||HS^2/12+O(b^4); BD3 gives the displayed sign.
BM18's alpha_act=alpha_amp+alpha_Haar then reproduces BD29 exactly.
The large coordinate Haar contribution has not survived as an artificial
physical loop term. No coarse Haar or extra Faddeev--Popov term is missing.

## 9. What remains, and primary literature comparison

BD29 is a completely specified, convergent finite-Brillouin-zone formula
for the actual bare coefficient, not a value or sign evaluation. In particular
it replaces BM29's unspecified total K derivatives by BD8, the proven zero
second critical motion, and finite noncommutative polynomial vertices.
The compact normalized kernel and its SU(N) scalar constraint remain present
in those vertices. All modes and all colours are explicitly traceable.

There is no sign deduction from the minus sign of the exchange term in BD20.
Both vertices vary with external momentum, the seagull term also contributes,
and the projection uses their second momentum coefficient. An exact remaining
condition for a negative coefficient on a specified N,L,kappa domain is
that the integral term in BD29 be strictly less than
-D(L^2-1)/(12L^2) throughout that domain. A separately preregistered numerical
study would need controlled errors for these explicit finite matrices,
Taylor coefficients and the integral, as well as coverage of any claimed
parameter interval. Point samples would not establish a sign for all odd L
or all kappa. No scientific numerical calculation has been run here.

The literature checks were limited to transferable derivations and their
actual hypotheses. They do not assign the value of BD29.

* Luescher--Weisz, [hep-lat/9504006](https://arxiv.org/pdf/hep-lat/9504006),
  PDF dated 11 April 1995, section 5.1, (5.1)--(5.7), uses a multiplicative
  lattice background/quantum decomposition and its adjoint gauge law. Its
  background gauge fixing and ghosts differ from the rooted probability-Haar
  quotient. BD3 and BD13 retain the actual measure and fluctuation order here.
* Luescher--Weisz, [hep-lat/9505011](https://arxiv.org/pdf/hep-lat/9505011),
  PDF dated 12 May 1995, section 4.1 (4.1) and section 5 (5.1)--(5.3),
  organizes lattice background vertices and one-loop seagull/exchange
  Brillouin integrals. It treats standard Wilson-to-MS matching with its
  own gauge/ghost terms. Our propagator is the gapped fine conditional tree
  matrix, and BD14--BD18 include this blocking kernel's saddle derivatives;
  neither their integrands nor their continuum matching coefficient is used.
* DeGrand--Hasenfratz--Hasenfratz--Niedermayer,
  [hep-lat/9506030v1](https://arxiv.org/pdf/hep-lat/9506030),
  sections 2--4, (4)--(11) and (15), retains an SU(N) normalization and its
  saddle maximum in a blocked action. Their scale-two staple/fuzzy kernels
  and fixed-point input differ from the present odd-L paired arithmetic
  average and incoming Wilson action. The same normalization issue is rebuilt
  by BD14--BD15; no fixed-point or one-loop perfection conclusion is imported.

Bałaban and Dimock are credited for the constructive gauge/localization and
coupling-extraction architecture behind the local producers. The exact local
inputs here are CB's tree/coercivity construction, FK's constrained saddle,
IC/BM's critical branch and measure identity, and BM's original-reader,
volume-first marginal convention. BR is the separate O(1/u) original-cut
remainder supplier. No new all-history or multiscale estimate follows.

The source freezes before its compact
[read manifest](checks/bare_determinant_coupling_read_manifest.json) and
[author receipt](checks/bare_determinant_coupling_receipt.json). A DIFFERENT
fresh hostile reviewer must check the Cartan argument, finite word/saddle
recipe, colour duals, intrinsic measure and Fourier/Taylor factors. The
coordinator owns review dispatch, publication, Git, shared fronts and audits.
No predecessor or original packet is edited, and the author assigns no
independent verdict or retained status.
