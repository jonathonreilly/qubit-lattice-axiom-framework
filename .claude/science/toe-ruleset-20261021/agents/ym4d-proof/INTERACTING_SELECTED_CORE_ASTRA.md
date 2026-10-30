# A connected finite-coupling remainder on an actual selected Haar sector

Author construction, requested Astra/max, awaiting a fresh independent review.
In the supplied four-dimensional SU(N) Wilson / normalized paired S4-prime
model, this proves a **one-step, source-free** connected `O(1/u)` fluctuation
remainder on a fixed complex neighborhood of sufficiently small-curvature
coarse data. Real holonomies need not be small. It covers SA's scalar white
cube and, separately, a covariant product of white HS balls. The latter has
exact coarse root-gauge Ward identities. Every Haar, kernel vacuum, Gaussian
determinant and cutoff probability is retained.

The result concerns the indicated selected integral. It does not estimate
its hard-cut complement, integrate source histories, prove closure of an RG
input class, or give an all-depth finite-u coupling map. Full continuum
existence and a positive physical continuum mass gap remain open.

Bałaban's small/large-field and localization constructions, Dimock's
expositions, and the Bałaban–Feldman–Knörrer–Trubowitz field-map work are the
antecedents. The specialized steps used here are rebuilt below; literature
does not supply a missing Yang–Mills hypothesis.

## 1. Model, actual predecessors, and theorem

Fix `d=4`, `N>=2`, `D=N^2-1`, odd `L>=3`, coarse torus side `T>=2`, and
`0<kappa_-<=kappa<=kappa_+`. Kappa is fixed while u varies. All link Haar
measures are probability measures. Lie-algebra coordinates are orthonormal
for the **unnormalized** HS metric `-Re tr(XY)`, and site sums use counting
measure. Set

    m0=3L^4+1, n=m0 T^4, d0_scalar=Dn, nc=4T^4,
    sigma^2=N/u, t=kappa u.                                 (IC1)

The block-root-pinned internal tree quotient has n free links and gauge
volume one. Root gauge and harmonic link directions are retained. There is
no additional zero-mode deletion or independent-colour determinant.

For coarse V use the actual brick lift U0(V): internal links are I and
crossing-face links equal the corresponding V_c. Each of the `24L^4` paired
contours is exactly V_c at this lift, including wrapping labels; its two
endpoint coordinate orders are the same. A contour has length at most
`5L-4`. Its lifted two-block brick excludes the extra far seam at T=2.
Free-link coordinates are `U_e=exp(a_e) U0_e(V)` with zero tree displacements.
Negative edges always use the exact inverse. Complex means are
`M_c^+=average T_tau` and `M_c^-=average T_tau^-1`, independently continued;
neither inverse of the mean nor complex conjugation is substituted.

Write `W_p=tr(2I-U_p-U_p^-1)/2` and let j_N be the exponential Haar Jacobian,
`dHaar(exp a)=h_N j_N(a) d^D a`, `j_N(0)=1`. The exact, unsubtracted phase is

    F_u(a;V)=sum_p W_p(a;V)
             +sigma^2 sum_c[-log k_t(V_c;M_c^+,M_c^-)]
             -sigma^2 sum_(free e) log j_N(a_e).             (IC2)

Thus `exp(-F_u/sigma^2) h_N^n da` is the original source-free Wilson times
normalized-kernel Haar density in this tree chart. Only a specified sector
will be integrated. No original source has been redefined.

The consumed internal results are precise:

* [CB1–CB15](COVARIANT_SOFT_BACKGROUND_ASTRA.md) and its
  [scoped review](REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md) identify the
  actual lift, tree quotient, real curvature-uniform precision gap, local
  complex vertices and finite-u critical branch. Its local third-derivative
  estimate is not being promoted to all-order source locality.
* [SA5–SA17](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), with its complete
  [review](REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md), supply the explicit
  original-reader parametrix, marked row/column algebra and real-V analytic
  composition. Sections 2–3 below extend these to a proved common complex
  original-V domain. SA itself explicitly did not assert that domain.
* [FK2/FK16–FK24](FINITE_COUPLING_KERNEL_ASTRA.md), source SHA256
  `c85ce075fdae1249b520089a462c8cf3107c0b26901d4dcd55a78c48b78ebc8b`, has a
  [fresh scoped LAND review](REVIEW_FINITE_COUPLING_KERNEL_ASTRA.md), SHA256
  `87d532f6505f7f80edb85c2a397d5fd6a33f27d99c19de5919cf397ffbfebc96`.
  It supplies an actual uniform scalar remainder, including Haar, rather
  than a formal expansion. Section 7 matches its action units exactly.
* The two-stage product-measure proof in
  [CX-R](RECOVERY_CLUSTER_ASTRA.md), §§1–4, is rebuilt in section 4.
  Its support means original readers, not just final field endpoints.

Neither the fixed-source-radius FR packet nor a claimed hard-history
regularity estimate is imported. The older source-return and BFT material
was inspected only at the read scopes recorded in the manifest. Existing
SA gives `O(sigma p^3)` for this fluctuation logarithm. Improving that bound
by parity **and** a p-independent coefficient estimate is the new part.

Here is the conclusion. There are positive `delta_*,rho_V`, a finite u_*,
a fixed R-box size R, and finite constants, all independent of T and u, such that
the following holds. About every real reference `Vbar` with
`max_P ||I-Vbar_P||op<=delta_*`, take the independent complex domain

    V_c=exp(v_c) Vbar_c,  v_c in sl(N,C),
    max_c ||v_c||HS<rho_V.                                  (IC3)

For any fixed output support rate `mu>0`, the constants can be chosen for
that rate in R-box units. For every real u>=u_* and p>=1 obeying the
explicit inequalities in IC20, there are actual holomorphic critical and whitening maps

    F_u'(b_u;V)=0, K_u=F_u''(b_u;V), C_u=K_u^-1/2,
    C_u^T K_u C_u=I.                                        (IC4)

The threshold u_* includes all CB and FK thresholds and the later
large-u inequalities. The constants are chosen jointly for F_u and the
tree phase F_T of section 7, after its real gap is identified there.

For either product domain `D_p=cube [-p,p]^(Dn)` or
`D_p=product_(free e){W_e in R^D: ||W_e||<=p}`, define the moving contour
`a=b_u+sigma C_u W`. Its real image is an actual selected Haar sector.
Its complex continuation is defined by this parameterization, including
its determinant, not by moving a hard indicator through a complex field.
The interaction logarithm has original-coarse-data connected coefficients:

    H_u(V)=log E_(mu_p) exp(-U_sigma(W;V))=sum_Y H_(u,Y)(V_Y),
    sup_x sum_(Y containing x) exp((mu+2)|Y|) sup_(IC3)|H_(u,Y)|
                                                       <=C sigma^2. (IC5)

Here mu_p is the normalized product Gaussian on the chosen domain, and
`U_sigma` is defined in IC14. All Y include their actual matrix-entry read
collars and connecting paths. Fixed-order original coarse derivatives have
both rooted and anchored-input bounds at rate mu, given in IC22. Filling
R-boxes gives the positive original-block rate `mu/(2R)^4`; an arbitrary
prescribed original-block rate is not promised.

The full selected negative logarithm has the exact tree/one-loop form
IC29, with an additional connected remainder of rooted norm `C/u` on the
same complex domain. This is a statement about the **unscaled** action.
The ball sector is coarse root-gauge covariant, with Ward identity IC24.
The cube theorem has no corresponding colour-rotation claim.

## 2. A fixed complex original-coarse-data domain

The neighborhood is constructed before u or volume is chosen. This is
stronger than a fixed-volume implicit-function germ. The following recipe
also makes its dependence on the real curvature bound explicit.

First choose common local scalar radii a0 for fine and coarse coordinates,
strictly smaller than CB9's joint radii, FK20's joint fine/coarse radius
divided by `4sqrt(D)`, and a traceless exponential-chart radius. On twice
these smaller polydiscs, the actual local vertices, after their scalar
vacua are removed, are uniformly bounded for
`u>=u_FK=max(1,2t0/kappa_-)`. The bound also holds separately for the tree
vertex, log amplitude, Haar log Jacobian and `sigma^-2 E_t`; FK16 proves
the last assertion. Let H0 be a common enlarged bound. Each vertex has at
most `q=(8L^4+8)D` scalar slots and radius-three coarse read stencil.
One fine coordinate is read by at most six Wilson terms, eight means and
one Haar term. These are finite local counts, independent of T.

For example, after decreasing a0 again if needed,
`J0=1000 q^3(H0+1)/a0^3` bounds both scalar absolute matrix row and column
norms of a coarse variation of `K_b(V)=F_u''(0;V)`:

    max(row,col)||K_b(exp(v)Vbar)-K_b(Vbar)|| <=J0 max||v_c||HS.
                                                                    (IC6)

To see the count, differentiate a local vertex twice in fine coordinates
and once in a coarse coordinate, use its joint Cauchy bound `6H0/a0^3`,
and sum the at most 15 incident vertices and at most q^2 remaining scalar
slots. The displayed constant overcounts those terms and the conversion
from HS to scalar rows. The same argument bounds every fixed derivative.
No derivative is taken through a conjugated complex argument.

CB8 gives the real gap `gamma>0` and a scalar row/column bound b, uniformly
at every real Vbar in its curvature class; enlarge b so `b>=1,gamma`.
Choose a preliminary radius

    rho_pre<min(a0/4,1/100,gamma/(4J0),rho_CB,V),
    (exp(2m)-1)(b+gamma/4)<=gamma/4                         (IC7)

with m>0. For complex data in that radius, the Hermitian part of K_b is
at least `3gamma/4`. Every actual principal compression has the same
lower bound, since it is a compression of the perturbed matrix. Conjugating
by `exp(m distance)` changes the matrix by at most gamma/4 in operator
norm, using both absolute row and column bounds and range two. For every
`lambda>=0`, every compression Omega, and
`K_theta=(1-theta)b I+theta K_b`, `0<=theta<=1`, this proves

    |(K_(theta,Omega)+lambda)^-1(i,j)|
                     <=2 exp(-m d(i,j))/(gamma+lambda).    (IC8)

This proof uses a Neumann inverse around an accretive matrix. It does not
assume a complex matrix is positive or infer a joint domain from real
smoothness. The constants remain valid for arbitrary real holonomies.
Here `rho_CB,V=min(q_CB/4,r_CB/(8R_CB C_CB))` is CB's explicit coarse
neighborhood after CB13. It is retained to identify overlapping solutions
in its common complex HS uniqueness ball, not substituted for the new
support-norm construction.

For clarity, the Wilson force is also controlled on this product domain.
A coarse plaquette has complex defect at most
`delta_hat=delta_*+8rho_V` when `rho_V<=rho_pre`. Indeed telescope its four
perturbed factors and use `exp(4rho_V)-1<=8rho_V`. A transported fine
insertion has HS norm at most `exp(8rho_V)`. Differentiating
`tr(2I-P-P^-1)/2` then bounds each incident Wilson force by
`2sqrt(N)delta_hat`. There are six incident plaquettes. Kernel and Haar
forces at the brick lift are exactly zero also on this complex domain:
their first mean variation is tangent to the common-path pair
`(G exp(sX),exp(-sX)G^-1)`, and FK's complex Haar translation fixes its
normalizer, stationary value and amplitude. Thus no force of order rho_V
independent of `delta_hat` has been discarded.

All analytic local formulas are functions of the actual V readers. A
labelled atom is defined on the projection of IC3 to those readers. Any
tuple in that projection can be completed with Vbar outside the label,
so the estimates genuinely hold there. The theorem does **not** assign
these atoms to arbitrary locally specified links without such a domain.
There is no global logarithm of Vbar or restriction on its flat winding.

## 3. Connected inverses, critical maps and determinants on that domain

Here the original-data argument of SA is repeated with IC8. Set
`beta=mu+4`. Use a fixed R-box partition with sides between R and 2R,
using one interval in a direction shorter than R. Put
`n0=Dm0`, `nR=n0(2R)^4`, `s=J=9^4`. For each box q, let Omega_q be its
R-block neighborhood and D_q its connected radius-R+4 read collar.
Then `|D_q|<=s` in R-box units and a box belongs to at most J such labels.
The collar is anchored at the **inside** index of a residual matrix entry:
the outside endpoint and its actual Wilson/kernel readers lie within its
two-block reach. It is not an independent second radius-three addition.

Define, with complements among the integrated coordinates,

    P_q(lambda)=(K_(b,Omega_q)+lambda)^-1 1_q,
    R_q(lambda)=-1_(Omega_q^c)K_b(K_(b,Omega_q)+lambda)^-1 1_q.

For labelled scalar matrices set M equal to the maximum absolute weighted
row and column sum, B to the sum of all entries whose support contains a
fixed box, maximized over that box, and Q=M+B. Each weight is
`exp(beta|S|)`. Both endpoints and every original reader are in S. IC8 and
the scalar lattice density give the finite bounds

    M(P)<=p(lambda)=2exp(beta s)n0 coth(m/2)^4/(gamma+lambda),
    M(R)<=r(lambda)=C_R exp(beta s)exp(-mR/2)/(gamma+lambda),
    B(P)<=JnR p(lambda), B(R)<=JnR r(lambda).               (IC9)

One explicit `C_R` is `2 S_m n0 coth(m/4)^4`, where one may take
`S_m=exp(2m)(b+gamma/4)` for the weighted scalar row/column of K_b.
Both constants are finite before R is chosen. Residual entries have
separation greater than R;
summing their IC8 bound spends half the rate. Periodic images are summed
with their multiplicities. For a one-box small torus the residual is zero.
Choose R large enough that `r(0)<1/2`.

The exact sign is `(K_b+lambda)P=I-R`. Hence

    G_lambda=(K_b+lambda)^-1=sum_(j>=0) P R^j,
    Q(G_lambda)<=A_G/(gamma+lambda),
    A_G=2exp(beta s)n0 coth(m/2)^4
           [(1-r(0))^-1+JnR(1-r(0))^-2].                 (IC10)

For products, consecutive labels meet at the summed index, and
`M(AB)<=M(A)M(B)`,
`B(AB)<=B(A)M(B)+M(A)B(B)`. Marking the second factor needs the column
bound of the first. These inequalities prove IC10 as an absolutely
convergent connected family, not just an operator estimate.

Here are concrete contraction choices. Vector norm means the maximum of
component-root sum and full support-incidence sum. Choose a<a0, use the
local majorant `f(t)=H(1-t/a)^(-q)` with H enlarged from H0, and put

    d0=(9L^4+5)(2R+6)^4, d1=q d0, d2=q^2 d0,
    S(t)=f'(t)-f'(0)-t f''(0),
    N(t)=d1 exp(beta s)[S(t)+t S'(t)],
    D_K(t)=2d2 exp(beta s)[f''(t)-f''(0)+t f'''(t)],
    g*=12sqrt(N)d1 exp(beta s), A=A_G/gamma.

Choose tau>0 first, and then delta_*,rho_V>0, such that

    tau<min(a/8, r_CB/(4sqrt(D))), A N'(tau)<=1/4,
    A_G D_K(tau)<=gamma/4,
    rho_V<=rho_pre, delta_*<=delta_CB,
    delta_hat=delta_*+8rho_V<=delta_CB/2,
    A g* (delta_*+8rho_V)<=tau/2.                          (IC11)

These choices are nonempty: N'(0)=D_K(0)=0, and delta_*,rho_V are chosen
last. They also retain the real CB uniqueness ball. The initial force has
vector norm at most `g*delta_hat`. Expand actual local vertices at a=0
before substituting vector atoms. A mark in the root or one substituted
factor gives respectively S and tS'; a difference of substitutions gives
N'. The iteration

    a_(j+1)=G_0[-F_u'(a_j)+K_b a_j], a_0=0

therefore contracts in this complete atom space. It proves

    ||b_u||_v<=C_b delta_hat, C_b=2A g*, uniformly on IC3.  (IC12)

The iterations are holomorphic in every original coarse coordinate and
converge uniformly. At real V this is the actual CB critical point by
uniqueness. At an exactly flat complex V the force vanishes and b_u=0.

Composition of the Hessian gives `Q(Delta)<=D_K(tau)` for
`Delta=K_u-K_b`. Thus

    (K_u+lambda)^-1=G_lambda sum_(j>=0)(-Delta G_lambda)^j,
    Q(C_u)<=Q_C=A_G/sqrt(gamma-A_G D_K(tau)),
    C_u=(1/pi)int_0^infinity lambda^-1/2(K_u+lambda)^-1 dlambda.
                                                                  (IC13)

Uniform absolute integration preserves connected labels and both marks.
For a scalar number in the right half-plane the integral is its principal
inverse square root, by substitution on positive numbers and holomorphic
continuation. Applying the identity to a triangular matrix, including
derivatives on its Jordan blocks, proves the matrix identity. Hence C_u
is symmetric and `C_u^T K_u C_u=I`; on real data it is positive. This
defines the branch without a finite-volume radius or determinant choice.
Local patch formulas and the unique pointwise solution agree on overlapping
coarse charts; no branch depending on an arbitrarily chosen Vbar is added.

The same construction for K_theta gives
`log det K_b=d0_scalar log b+int_0^1 Tr[K_theta^-1(K_b-bI)]dtheta`.
Together with `Tr log(I+G_0 Delta)` this localizes the complete log det K_u.
A diagonal trace is a subsum of the full marked scalar-entry norm, so no
unpaid volume or colour trace occurs. Its rooted budget is generally O(1),
not part of the small interacting remainder.

## 4. Auxiliary parity and a coefficientwise connected logarithm

Fix u,p and hold **the actual** F_u,b_u,C_u fixed. With original V still
variable on IC3, define homogeneous white-field polynomials

    J_l(W;V)=F_u^(l)(b_u;V)[C_u W]^l/l!, l>=3,
    U_z(W;V)=sum_(l>=3) z^(l-2) J_l(W;V)
       =z^-2[F_u(b_u+z C_u W)-F_u(b_u)]-|W|^2/2.           (IC14)

The apparent z=0 singularity is removable by stationarity and whitening.
At z=sigma this is the exact nonlinear interaction in the selected integral.
The auxiliary z does not vary u, the kernel stiffness, the center,
precision, physical cutoff p or Gaussian law.

Expand vertices at zero and then substitute the connected b_u and C_u
families. Each labelled J_(l,S) is homogeneous of degree l in W and reads
only W_S and original V_S. Denote its absolute scalar monomial coefficient
sum by j_(l,S); permutations may be collected or left as an overcount.
Let `M>=M(C_u)`, `B>=B(C_u)`, `t*=C_b delta_hat`. The same three marks as
SA17 give

    A_l:=sup_x sum_(S containing x)e^(beta|S|) sup j_(l,S)
      <=d0 e^(beta s)/l! * {
          [f^(l)(t*)+t* f^(l+1)(t*)] M^l
                 +l f^(l)(t*) B M^(l-1)}.                 (IC15)

The marks are respectively in the original root stencil, a background
atom, and a white-map atom. The remote mark in the last term is B, not
merely a row bound. In particular A_3,A_4 are finite independently of p.
Criticality cancels the complete linear and quadratic sums; their local
Taylor terms were subtracted before this expansion, not individually
declared zero. Every higher term keeps its original reader label.

Choose r_z>0, independently of p,u,T, with `r_z M<=a/4` and

    h(r_z):=sum_(l>=3) A_l r_z^(l-2)<=1/4.                 (IC16)

The geometric majorant in IC15 ensures such a choice. On either selected
domain every scalar |W_i|<=p. If `|z|<=R_p=r_z/p^3`, then
`|z|^(l-2)p^l <=r_z^(l-2)` for l>=3 and p>=1. Therefore
`||U_z||_beta<=h(r_z)<=1/4`, throughout the SAME fixed V domain.

For completeness, the connected logarithm is built as follows. For each
support set S put `f_S=exp(-U_S)-1`; its norm is at most `2||U_S||`.
Expand the product of `(1+f_S)` and group chosen supports by overlap
components. Disjoint components depend on disjoint white variables, so
their integrals factor for either product law. If w(P) sums the connected
collections with union P, it is a hard-core polymer gas. Assign the weight
`exp((mu+3)|S|)` and bound rooted trees by the recursion
`T(S)<=v(S)exp(sum_(S' meets S)T(S'))`. The hypothesis
`sup_x sum_(S contains x)e^|S| v(S)<=2h<=1/2` makes
`T(S)<=v(S)e^|S|` stable under iteration. Thus
`sup_x sum_(P contains x)|w(P)|e^((mu+3)|P|)<=2h`.

For the logarithm, the signed connected graph coefficient is bounded by
the number of spanning trees of the overlap graph. Order its edges and
group each connected subgraph by its Kruskal minimum spanning tree. For a
fixed tree the possible extra edges form an interval of graphs; their
signed sum is either zero or one in modulus. A second rooted-tree iteration
spends the next unit of support weight. Marking a polymer containing x
cancels the corresponding factor in the factorial. This gives

    H(z,V)=sum_Y H_Y(z,V_Y),
    ||H(z)||_(nu)<=2h<=1/2, nu=mu+2, |z|<=R_p.             (IC17)

The usual finite connected-graph polynomial identity near zero interaction,
followed by analytic continuation in its multiplier within these bounds,
proves `E exp(-U_z)=exp H(z)`. Nonvanishing is consequently proved before
taking the logarithm. Finite-volume sums over all connected supports may
be extensive; the stated bound is a rooted norm. Infinite atom sums follow
by absolute convergence, not by an assumed thermodynamic identity.

Now `J_(l,S)(-W)=(-1)^l J_(l,S)(W)`. Hence
`U_S(-z,W)=U_S(z,-W)` for each original support. Both laws are even.
Every integrated overlap collection is therefore even in z; so is each
hard-core connected coefficient H_Y. This preserves the reader labels,
rather than proving only parity after summing the whole volume. Also
H_Y(0)=0. Write its first coefficient as H_(2,Y).

## 5. Uniform Gaussian moments pay the first nonzero coefficient

For the scalar cube, each normalized coordinate is a standard Gaussian
conditioned on |W|<=p. Its absolute moments are no greater than the full
Gaussian's: conditioning a nonnegative random variable to be below a
threshold lowers the expectation of every increasing function. Independence
then applies to products. Log convexity of Gaussian absolute moments, or
positive covariance of powers of |W|, bounds any product of total degree q
by `E|G|^q`. In particular the degree-four and degree-six bounds are 3 and
15. No factor `z_p^-Dn` is introduced by this normalized comparison.

For the ball law the equally explicit proof is useful. Write a standard
D-vector as R theta, with theta uniform on the unit sphere and independent
of R. Radial conditioning leaves the angular law unchanged and decreases
every radial moment. Every absolute monomial is a nonnegative angular
factor times a radial power; its conditional expectation is bounded by its
full Gaussian expectation. Product independence between free-link balls
then gives the SAME bounds 3 and 15 for total degrees four and six.

More precisely, for a single ball, odd tensors vanish and

    E_p[W_(i1)...W_(i_(2j))]
       =a_j(p,D) sum_pairings product_pairs delta_(i_r,i_s),
    a_j(p,D)= E[R^(2j) | R<=p]/[D(D+2)...(D+2j-2)],
    0<a_j(p,D)<=1, j=1,2,3.                               (IC18)

Equivalently `a_j(p,D)=z_(p,D+2j)/z_(p,D)`, with the normalized radial
integrals z defined in IC21. This retains their exact finite-p values.
To derive the angular tensor, expand the full Gaussian generating function
`exp(|z|^2/2)`, or integrate one-dimensional Gaussian moments by parts,
giving its pairing sum. Polar integration gives
`E R^(2j)=D(D+2)...(D+2j-2)` by the same integration by parts. Dividing the
two identifies the angular tensor; radial truncation gives IC18. Products
over different link balls use their separate a_j factors. This is not an
assertion that a truncated law is Gaussian or has unchanged Wick constants.

Differentiating the convergent connected expansion at z=0 yields

    H_2=-sum_S E J_(4,S)
        +(1/2)sum_(S,T) Cov(J_(3,S),J_(3,T)).               (IC19)

Each cubic mean is zero by parity. A pair on disjoint labels is independent
and has zero covariance. Thus the second term can be labelled by the
connected union S union T with S meeting T. This identity includes S=T.
At this order the two-stage graph construction gives exactly these labels:
the single-support exponential contributes its own quadratic term, two
distinct overlapping supports contribute their product, and the logarithm
subtracts the product of means. No disconnected vacuum pair remains.

Let `Delta=beta-nu=2`. For a fixed root x, mark whether it lies in S or T.
The factor two cancels the 1/2 in IC19. An overlapping partner has at most
|S| choices for a marked intersection, each costing A_3. Finally
`|S| exp(-Delta|S|)<=1/Delta`. Consequently

    ||H_2||_nu <=3 A_4+(15/Delta) A_3^2=:B_2.

This is a rooted, support-size estimate. It is neither a pointwise moment
bound nor an extensive bound divided informally by volume. The positive
rate loss pays the overlap incidence, including remote original readers.

Banach-valued Cauchy estimates in IC17 and coefficientwise evenness give
for `sigma<=R_p/2`

    ||H(sigma)-sigma^2 H_2||_nu
       <=(2/3) sigma^4 p^12/r_z^4,
    ||H(sigma)||_nu
       <=sigma^2[B_2+2/(3r_z^4)]
          if sigma^2 p^12<=1.                             (IC20)

The first inequality sums the even powers of order at least four from
the bound 1/2 on the circle R_p. The two requirements are
`sigma p^3<=r_z/2` and `sigma^2 p^12<=1`; in addition require
`t*+sigma p M<=a/2`. The choice
`p(u)=max(1,A_cut sqrt(log u))` with any fixed A_cut>0 satisfies all three
for sufficiently large u. This establishes IC5. Cauchy alone would instead
leave a first coefficient of size p^6; that insufficient argument has not
been used. Nor has a sup-norm quartic estimate of order sigma^2 p^4 been
called O(1/u).

## 6. Exact selected integrals, coarse derivatives and the covariant variant

The exact raw selected integral for either law is

    Z_sel(V)=h_N^n (2pi sigma^2)^(Dn/2) det(K_u)^-1/2
             Z_p exp[-F_u(b_u;V)/sigma^2] exp H_u(V),
    Z_p=z_p^(Dn)                         (cube),
    Z_p=z_(p,D)^n                        (balls),
    z_p=(2pi)^-1/2 int_(-p)^p exp(-w^2/2)dw,
    z_(p,D)=Gamma(D/2)^-1 int_0^(p^2/2) s^(D/2-1)e^-s ds. (IC21)

The corresponding full fine-group sector is the preimage of this quotient
sector under the pinned tree gauge, so all its pinned gauge variables are
integrated with volume one. No source vacuum occurs because the source is
exactly zero. The kernel vacuum remains in F_u; the Haar factors j_N
already occur once in IC2.
All scalar modes and the full colour-coupled determinant remain. For real
V this is a change of variables on a real sector with positive Haar
measure. For complex V it is the holomorphic integral of the pulled-back
top form on a fixed real W domain, including `det(sigma C_u)`. It is not
the integral over a fixed original hard-cut sector at complex V. IC17 and
the analytic nonzero prefactors prove nonvanishing of this selected integral.

There is a nonempty fixed-curvature domain inside the original cut. For
real V, the scalar atom bounds give
`A_box=sqrt(D)[C_b delta_V+sigma p M]`. Choose delta_* and the real-domain
cap smaller, if necessary, so that with positive fixed `delta_f,eta`

    A_box<r_ch, delta_V+4A_box<delta_f, (5L)A_box<eta,
    delta_f<=epsilon_1,

hold for all sufficiently large u. This is possible at fixed delta_* by
choosing it first with strict margins, then using sigma p->0. Telescoping
the actual nonabelian plaquette words and root-straight paths proves the
two defect inequalities; all baseline plaquettes have defect <=delta_V.
Both selected domains are therefore inside SA's strong G and the original
interior cut. No condition `delta_V<=c sigma p` is needed here: that was
SA19/25's source-linear condition. No positivity or price for G minus the
selected sector or G^c is supplied by these margins.

To state coarse derivatives precisely, work in the half HS tube of IC3.
It contains a simultaneous scalar-coordinate Cauchy polydisc of radius
`r_V=rho_V/(4sqrt(D))`. An R-box contains at most
`q_V=4D(2R)^4` original coarse scalar coordinates. If a coarse multi-index
reads outside Y, its derivative of H_Y is zero. Otherwise Cauchy bounds a
q-th derivative by `q! r_V^-q sup|H_Y|`. For q>=1,

    sup_(i0) sum_(Y contains i0) e^(mu|Y|)
       sum_(i1,...,i_(q-1)) |partial_(i0)...partial_(i_(q-1)) H_Y|
       <=q! r_V^-q q_V^(q-1) C_(q-1,2) C sigma^2,
    C_(j,delta)=sup_(k>=1) k^j exp(-delta k)<infinity.      (IC22)

The same bound with any other input anchored is the column estimate, by
symmetry of mixed derivatives. The stronger rooted-box norm with ALL q
indices summed costs `q_V^q C_(q,2)` instead. Thus every original input
incidence is paid. This applies also to the total O(1/u) action remainder
in section 7. For a fixed number of derivatives nothing depends on T,u,p.
Filling each R-box costs at most `(2R)^4` original blocks and keeps all
readers. Periodic identifications are summed and can reduce distinct readers;
they do not delete multiplicities from a coefficient sum.

**Separate covariant-ball theorem.** Under exactly the preceding domain and
large-u conditions, IC5, IC18–IC22 hold for the product of D-dimensional
balls with its stated z_(p,D)^n normalization. In addition, the selected
sector and its integral are covariant/invariant under arbitrary real
coarse root gauges. Here is the actual map proof. Extend a coarse gauge
g_X constantly within each fine block. It preserves internal tree links,
and

    U0(V^g)=g U0(V)g^-1,
    a^g_e=Ad_(g_(X_e)) a_e=: (R_g a)_e,
    F_u(R_g a;V^g)=F_u(a;V),
    b_u(V^g)=R_g b_u(V), C_u(V^g)=R_g C_u(V) R_g^T.         (IC23)

R_g is block orthogonal, with determinant one. The phase identity follows
from the actual group words and the Ad-invariant Haar Jacobian. The b
identity follows by uniqueness in CB's HS ball; the square root identity
follows directly from its resolvent integral. IC3 is carried into the same
radius about Vbar^g because its HS norm is Ad-invariant. Every complete
colour block is retained in patch inverses and compressions.

The product of white HS balls is invariant under R_g. Thus its actual real
sector is mapped onto the sector at V^g, preserving Haar and the original
density. The equality continues holomorphically in V on overlapping tubes.
For any real site algebra field omega, differentiation gives the finite-
volume Ward identity

    sum_c D_c log Z_ball(V)
              [omega_x-Ad_(V_c)omega_y]=0, c=(x,y).       (IC24)

Its tree and one-loop terms below obey the same identity, so their exact
O(1/u) remainder does as well. At the identity global colour invariance
sets its one-jet to zero, and IC24 then gives `R''(1)d=0`. This is an
actual Ward consequence, not a statement about all infrared limits.

For the scalar cube, R_g generally rotates the cube to a different set.
Its evenness and IC5 remain valid, but IC23 does not identify the selected
domains. No finite-u Ward identity for that cube is asserted. The ball
theorem does not assert all spatial symmetries of a preferred axial tree,
an infinite-volume polarization construction, or the P->0 marginal estimate
needed by a coupling consumer. Those additional identifications cannot be
replaced by the small size of a symmetry error.

The exact cutoff probabilities have harmless but extensive vacuum costs.
For p large enough, integration of the radial density gives
`1-z_(p,D)<=C_D p^(D-2)e^(-p^2/2)` and
`-log z_(p,D)<=2(1-z_(p,D))`; for the cube
`1-z_p<=2 phi(p)/p`. For the radial estimate use
`r^(D-2)<=p^(D-2)exp((r^2-p^2)/4)` for r>=p and
`p^2>=2(D-2)`, then integrate `r exp(-r^2/4)` explicitly.
These are per-link constants. Neither `n log z_(p,D)` nor `Dn log z_p`
has been erased or bounded as an absolute volume-independent number.

## 7. The exact tree / one-loop / finite-u action dictionary

FK17 gives on the proved joint complex domain
`-log k_t=t psi_c-(D/2)log t+log A_c+E_(t,c)`, with
`A_c=h_N(2pi)^(D/2)(det H_c)^-1/2` and the full SU saddle Hessian H_c
in HS coordinates. Define

    F_T(a;V)=sum_p W_p(a;V)+N kappa sum_c psi_c(a;V),
    F_1(a;V)=sum_c log A_c(a;V)-sum_e log j_N(a_e),
    R_u(a;V)=sigma^-2 sum_c E_(kappa u,c)(a;V).

Then the following is an EXACT identity, with no formal expansion:

    F_u=F_T+sigma^2 F_1+sigma^4 R_u
                         -sigma^2 (D nc/2)log(kappa u).   (IC25)

The vacuum is displayed separately; F_1 still includes `nc log A_0` and
R_u includes `nc sigma^-2 E0(kappa u)`. FK16 makes the local vertices of
R_u and all fixed derivatives uniformly O(1). At the brick lift,
`F_1'(0)=R_u'(0)=0`: log j has zero derivative and common-path invariance
does the same for log A and E. Their Hessians need not vanish.

The real tree precision at a=0 is `H_V+E_V` from CB8. Its gap follows
already from CB6 and the Wilson curvature error; the nonnegative finite-u
spread and Haar terms are not needed. Equivalently it is the uniform local
u->infinity limit in IC25. Apply sections 2–3 to F_T with the same enlarged
local bounds and smaller common constants. This constructs b_T and K_T
with the same complex atom domain. Let `d_u=b_u-b_T`. Integrating the tree
Hessian along the segment between the two centers and inverting it by the
same atom Neumann series gives

    ||d_u||_v<=C sigma^2 delta_hat,
    d_u=-sigma^2 K_T^-1 F_1'(b_T)+O_v(sigma^4 delta_hat),
    Q(K_u-K_T)<=C sigma^2.                                (IC26)

Indeed the exact stationarity equation is
`[int_0^1 F_T''(b_T+s d_u)ds] d_u
 =-sigma^2 F_1'(b_u)-sigma^4 R_u'(b_u)`.
The bracket is within the small Hessian perturbation of its brick value;
its inverse has a uniform Q bound. The two right-hand gradients are
O(delta_hat), because they vanish at zero and `||b_u||_v=O(delta_hat)`.
One further substitution proves the displayed first-order shift. These
are one-step connected norms, not an all-depth hidden inverse.

Taylor's formula about the actual tree critical point yields the exact
remainder

    E_act= [F_T(b_u)-F_T(b_T)]/sigma^2
                  +F_1(b_u)-F_1(b_T)+sigma^2 R_u(b_u),
    ||E_act||_beta<=C sigma^2.                             (IC27)

The linear tree term vanishes by the COMPLETE stationary equation. Its
remaining expression is the integral of `d_u^T F_T'' d_u`, so it has
connected labels and norm O(sigma^4) before division by sigma^2. This
avoids assigning false separate stationarity to individual local vertices.
For scalar contractions, a mark lies in the matrix or either vector;
the bound `3 Q(A)||h||_v||k||_v` controls `h^T A k` and pays both endpoints.
The F_1 increment is O(sigma^2 delta_hat^2). R_u's full vacuum remains in
the O(sigma^2) term. These operations use the same analytic majorants as
IC15 and have no total-volume estimate substituted for their rooted norm.

Likewise, putting `B=K_T^-1(K_u-K_T)` and increasing u_* so M(B)<=1/2,

    E_det=(1/2)log det K_u-(1/2)log det K_T
            =(1/2)sum_(j>=1)(-1)^(j+1)Tr B^j/j,
    ||E_det||_beta<=B(B)/[2(1-M(B))]<=C sigma^2.             (IC28)

Marking a factor in the trace costs j and cancels 1/j. All D colours and
all retained root/harmonic coordinates are present. The branch is fixed by
the already constructed accretive square roots and agrees at u=infinity.

Combining IC21 and IC25–IC28 proves

    -log Z_sel(V)=F_T(b_T;V)/sigma^2
                 +F_1(b_T;V)+(1/2)log det K_T(V)
                 +V_vac(u,p)+E_core(V),
    V_vac=-(D nc/2)log(kappa u)-n log h_N
                           -(Dn/2)log(2pi sigma^2)-log Z_p,
    E_core=E_act+E_det-H_u,
    ||E_core||_(mu+2)<=C sigma^2=C N/u.                    (IC29)

The already retained `nc log A_0` in F_1 and the E0 term in E_core are
additional displayed scalar vacua, not missing constants in V_vac. They
may be separated into single-box atoms, but are never discarded. This
identity defines the logarithm branch by the real positive sector and its
holomorphic extension. All fixed original coarse jets of E_core satisfy
IC22. In the scaled phase `(N/u)(-log Z_sel)` the new error is O(u^-2).

There is a necessary coordinate cancellation before comparing with UL.
At a_T=b_T, the differential into the right coordinates `U_T exp(X)` is
`E_e=Ad_(U0_e^-1)[(1-exp(-ad a_T,e))/(ad a_T,e)]`, with the removable
value at zero understood. Its determinant is j_N(a_T,e), by the exact
exponential differential and unimodularity; the Ad factor has determinant
one. If K_T,intr is the tree Hessian in
right-translated free-link coordinates at U_T, stationarity implies

    K_T=E^T K_T,intr E,
    (1/2)log det K_T-sum_e log j_N(a_T,e)
                                    =(1/2)log det K_T,intr. (IC30)

Terms involving the second differential of the coordinate map multiply
the tree gradient and vanish. The logarithm identity uses the real positive
branch and continues on the common small domain. Thus the unscaled one-loop
term is exactly
`sum_c log A_c(a_T)+(1/2)log det K_T,intr`. Haar has not been deleted; it
has combined with the coordinate precision as required.

The root-tree gauge Gaussian has its own exact measure dictionary. In full
intrinsic link tangents at REAL data, let D_r be the differential of
root-pinned gauge transformations, and let J insert free-link tangents. The square matrix
`[D_r,J]` has determinant of modulus one: its tree-link block is the rooted
tree incidence minor, triangular with unit colour blocks, and its free-link
block from J is identity. The full tree Hessian annihilates D_r. On its
orthogonal complement write J=U_G A+U_perp B. Then

    det K_T,intr=det H_perp / det(D_r^*D_r).                (IC31)

Indeed `|det[D_r,J]|^2=det(D_r^*D_r)|det B|^2=1` and
`J^*H J=B^*H_perp B`. This accounts for the half ghost when changing
slices; appending another Faddeev–Popov determinant to the tree integral
would be wrong. This finite-dimensional identity transports the slice
**and its induced measure**. It is not a fixed-free-complement invariance
claim of the kind corrected in UL's review.
Complex continuation uses the corresponding bilinear transpose and
transported analytic slice; a Hermitian orthogonal projector depending on
complex-conjugated V is not asserted to be holomorphic.

In FLOW convention, `a_HS=sqrt(N)a_FLOW` and
`F_T,HS(a)=N F_tree,FLOW(a/sqrt(N))`. Hence
`F_T(b_T)/sigma^2=u T_1(V)` and the hidden quadratic precision K_T in HS
coordinates equals the corresponding FLOW Hessian. Probability Haar has
`h_FLOW=N^(D/2)h_N`. For a normalizer,
`H_c,FLOW=N H_c,HS`, so

    log A_c=log[h_FLOW(2pi)^(D/2)]
                                  +(1/2)log det C_c,FLOW,
    C_c,FLOW=H_c,FLOW^-1.                                  (IC32)

This is the positive half-log of the normalizer covariance already in
[UL9–UL12](UNIFORM_ONE_LOOP_COUPLING_ASTRA.md). IC30–IC32 match the actual
one-step Gaussian integral to that dictionary near its identity branch.
UL's further relative-gauge/root Schur reorganizations retain their two
different harmonic Grams and prescribed complements; this unit neither
replaces nor adds those factors. At general coarse backgrounds we claim
the intrinsic one-step formula IC30, not a new all-depth version of UL.

## 8. Boundary, failed shortcuts, literature and evidence

The whole fixed-curvature source-free construction uses original V and its
proved complex tube. It is a useful advance over the single-kernel lemma:
the nonlinear fine-field expectation itself has a zero-free connected log
of order 1/u. The selected white-ball variant also has actual finite-u
root-gauge covariance. Several further consumer obligations remain:

* The two exact terms over `G minus Omega` and `G^c` in SA32 are still
  present in the original cut transform. Neither parity nor a local
  scalar normalizer prices their normalized sum.
* Sources, dirty collars and hard history/completion factors change the
  product/even structure. This theorem does not extend IC5 to those
  insertions. No unreviewed FR reader-domain claim is used.
* IC29 is a bare Wilson, one-step formula. Subsequent effective actions
  have inherited interactions; a uniform input-class induction, marginal
  extraction and finite-u flow estimate have not been constructed here.
* The ball Ward identity and coarse jets do not by themselves supply the
  additional volume-first polarization limit, its P->0 estimate, the
  needed spatial-symmetry dictionary, or a multilevel every-increment
  nonlinear bracket. UL's Gaussian result has its separate reviewed scope.

The following unsuccessful shortcuts were rejected analytically, before
writing the theorem: an even Cauchy estimate without computing H_2 leaves
a p^6 factor; a quartic cube supremum leaves p^4; an extensive variance
bound misses overlap incidence; real positivity alone supplies no complex
reader domain; and colour-cube parity does not imply adjoint invariance.
They are not negative-route verdicts or numerical failures.

Primary comparison was checked at the stated loci.
[Dimock, 1212.5562v2](https://arxiv.org/html/1212.5562v2), introduction,
section 3.14 and complete Appendix F, treats d=3 scalar phi4 and requires
independent fluctuation variables and local small interactions. Its two
connected-expansion stages and auxiliary analytic parameters motivate the
organization here. IC9–IC20 rebuild the actual support and parameter proof,
with original gauge-field readers and a separate moment estimate.
[Bałaban–Feldman–Knörrer–Trubowitz, 1609.01748v1](https://arxiv.org/html/1609.01748v1),
Appendix A, uses both output and marked-input norms, but its quoted
contraction has finite maximum nonlinear degree. IC11 and IC15 instead
sum the actual infinite analytic series. Their
[Part 3, 1609.01747v1](https://arxiv.org/html/1609.01747v1), introduction and
the displayed contour construction, keeps side and outside contours and
explicitly does not complete its full-error proof. It supplies no complement
estimate here. The moving contour of IC21 is a definition of the selected
complex continuation, with its real-sector identification proved directly.

This unit uses written proofs and metadata checks; no new numerical
experiment was run merely for packaging. Prior finite diagnostics are not
relabelled as evidence for IC5. FK's review includes a surviving author
checker mutation deleting lambda from one Weyl routine, independently
covered there by its separate SU(3) lambda calculation; it remains a
recorded coverage limitation, not a newly detected mutation here.

The [read manifest](checks/interacting_selected_core_read_manifest.json)
records actual full/partial/reused coverage and source hashes. The
[freeze receipt](checks/interacting_selected_core_receipt.json) binds this
argument and owned evidence. No frozen predecessor, shared status, Git,
lock, audit or ledger was changed. Fresh hostile review of this unit is
required; this author text does not assign itself LAND or a retained grade.
