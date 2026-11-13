# Original-source fourth response with the orbit covariance retained

Research derivation, 2026-11-09, independent check pending. Same base and exact
compact law as `full-compact-fourth-scaling.md`. This new note alone is written;
the previous proof is unchanged. No numerical, network or Git operation.
Inputs: exact reconstruction/source factor from `compact-forest-exchange.md`
sections 1–2,5; moment theorem from `full-compact-fourth-scaling.md`; chart
(C1),(C7),(C8) and its specified cube from `nonlinear-chart-response.md`.
The latter supplier is provisional and is used with its actual restricted law,
not as a statement about the full compact posterior.

## 1. Readers, orbit averages, and the exact identity

At terminal V=I write pi(dU)=nu(da) dh using the rooted fine forest. For a
hidden original link e=(x,y), reconstruction is

    U_e=h(x)^* a_e h(y),

with a_e=I on fine forest edges, h(q)=I at terminal roots, and all
intermediate links retained as a_e. In these independent product coordinates,
no root-to-endpoint path of additional h variables is read by U_e: exactly its
nonfixed endpoint h variables and, if retained, its own a_e are read.

For original source F with link reader set E_F, define S_F=E_F intersect J,
and H_F={nonterminal endpoints of links in E_F}; define S_G,H_G likewise.
These are valid reader supersets; cancellation may reduce actual supports.
Thus F_a(h) reads only a_{S_F},h_{H_F}. Original fixed local supports give
fixed finite sets, with owner-cell diameters enlarged by at most the local
link endpoint range. Arbitrary nonlocal original sources have no such uniform
support-size promise. Set

    f(a)=E_h F_a,  g(a)=E_h G_a,
    C(a)=E_h(F_a G_a)-f(a)g(a).

Then f reads S_F, g reads S_G, C reads S_F union S_G. Haar product independence
implies C=0 identically whenever H_F and H_G are disjoint. This is a sufficient
condition, not a necessary one. It remains true when one H reader set is empty.
The full source factor is E_h exp(sF_a+tG_a), not exp(sf+tg) in general.

Boundary scores X=A_c and Y=A_d read a alone, since their terminal endpoints
are roots. The ordinary law of total covariance gives
Cov_pi(F,G)=E_nu C+Cov_nu(f,g). Differentiating twice at distinct terminal
links c,d, with F,G independent of V, gives exactly

    kappa_4,pi(F,G,X,Y)
      = kappa_4,nu(f,g,X,Y)+kappa_3,nu(C,X,Y).              (1)

Indeed D_c E_nu C=Cov_nu(C,X), D_d X=0, and the second derivative is
kappa_3(C,X,Y); similarly the two derivatives of Cov(f,g) give the fourth
cumulant. The reconstruction, f,g,C have no V dependence. Equivalently,
first differentiate log E_h exp(sF_a+tG_a) in s,t, obtaining f,g,C,
and differentiate the exact quotient integral. This proves (1) without
assuming independent original sources or suppressing conditional covariance.
It applies to the fixed quotient-chart conditional law too, since the
conditioning event reads only a and does not change dh.

## 2. Smoothness, symmetry, and the full compact bound

Assume F,G are real C^2 on their original finite compact link products.
Multiplication by fixed h is an isometry in each retained link, so
reconstruction has uniformly bounded derivatives of orders <=2 (indeed it
is coordinatewise isometric on these variables). Compact Haar integration
commutes with these derivatives. Thus f,g,C are C^2 with uniform local norm
bounds depending on the original C^2 norms and support sizes. The product
rule controls C through the same data, including F,G sup norms.

If F,G are invariant under simultaneous conjugation, so are f,g,C. For
example substitute h'=k h k^* into the integral defining f(kak^*); probability
Haar is unchanged and reconstruction is conjugated by k. The same argument
applies to E_h FG, hence C. This does NOT assert F_a(h) is h-independent.
The adjoint SO(3) representation has no invariant linear functional, so
at a=I each of df,dg,dC vanishes. Global compact geodesic Taylor therefore
gives, for q=f,g,C,

    |q(a)-q(I)| <= (pi^2/8)||Hess q||_infinity
                                  sum_{e in S_q} d(a_e,I)^2.

Apply the proved full-compact local moments and the score bound
||A_c||_p<=K_p |v_c| sqrt(u). For every fixed p>=1,

    ||f-f(I)||_p + ||g-g(I)||_p + ||C-C(I)||_p <= K_p/u.

Fourth-cumulant partition Hölder, and its third-order version whose absolute
coefficient sum is 1+3+2=6, yield

    |kappa_4,nu(f,g,A_c,A_d)| <= K |v_c||v_d|/u,
    |kappa_3,nu(C,A_c,A_d)| <= K |v_c||v_d|.               (2)

Thus the complete original-source response is bounded by K(1+u^-1), uniformly
in volume and locations with fixed support sizes. If H_F intersect H_G is
empty, its bound improves to K/u exactly by (1). The O(1) term is not
silently replaced by O(1/u); its nonvanishing leading coefficient is not
asserted either. For arbitrary C^2 sources without global conjugation
invariance, (1), the reader claims and smoothness still hold, but the zero
first differentials need not hold and (2) does not follow as stated.
These full-compact statements give no spatial decay.

## 3. Local chart moments at terminal identity

Here and only here let mu be the actual quotient law conditioned on the
supplier's fixed Cartesian logarithm cube Omega_delta, at V=I, u>=u_*.
Write z_e in R^3 for its retained logarithm coordinates. (C7) states
Hess S>=m I with m=u g_*/2, and (C8) supplies the covariance/Poincare method.
The following local moment consequence is needed to retain powers of u in
the cut argument; it does not follow by conditioning a rare global event
using the full-law tail alone.

The cube and complete density are invariant under global conjugations that
rotate tangent coordinates by pi about each coordinate axis. Each such
rotation flips two components, preserves the cube, all means/normalizers,
and the identity terminal field. Hence E_mu z_{e,r}=0 for each component.
For every linear tilt exp(t ell dot z), the Hessian remains >=m I and the
same cube boundary argument proves Var_t(ell dot z)<=||ell||^2/m. Integrate
this bound twice in t from zero to obtain

    log E_mu exp(t ell dot z) <= t^2 ||ell||^2/(2m).

The moment-generating function exists for every real t on the bounded cube.
Chernoff and layer cake now give ||z_{e,r}||_p<=K_p/sqrt(u), for every finite
p, uniformly in volume. Fixed local coordinate vectors have the same bound
with constants depending on their dimension. No continuous rotation
invariance of the Cartesian cube is assumed; the stated discrete rotations
suffice to center every component.

For invariant q=f,g,C, q_0=q-q(I) and the bounded local Hessian in logarithm
coordinates imply

    ||q_0||_p<=K_p/u,   ||grad q_0||_p<=K_p/sqrt(u).       (3)

The logarithm-chart Hessian bound follows from the global C^2 norm and bounded
first/second chart derivatives on the fixed cube. For B_c=A_c/u,

    ||B_c||_p<=K_p |v_c|/sqrt(u),
    ||grad B_c||_p<=K_p |v_c|.                            (4)

The first uses B_c(I)=0 and word telescoping; the second bounded local word
derivatives. All norms here are under mu, with the actual radial/Haar factors.

## 4. Cut cancellation and connected tree bounds on the chart

We give the finite-cumulant cut argument explicitly. For n=3 or 4 let
X_i be local functions supported on cell sets T_i. For every nonempty
proper cut I|I^c of their labels, put

    r(I)=d(union_{i in I}T_i, union_{j notin I}T_j).

For a block B in a moment partition, write m_B=E product_{i in B}X_i.
Replace it by m'_B=m_{B intersect I}m_{B intersect I^c}, with m_empty=1.
These are precisely the moments of the product law formed from the two
marginal families. Its joint cumulant vanishes, since its log generating
function splits into two functions of disjoint source lists. Consequently
the original cumulant equals the difference of its moment-partition
polynomial evaluated at m and m'.

Only blocks crossing the cut change, and their difference is exactly

    m_B-m'_B=Cov(product_{i in B intersect I}X_i,
                 product_{j in B intersect I^c}X_j).

(C1) bounds this by K/u * exp(-alpha r(I)) times the two L2 gradient norms.
The product gradient rule and Hölder with exponents 2n bound each gradient
norm by a sum of products of local L^{2n} norms, one factor differentiated.
For example each product of k<=n functions is controlled in L2 by their
L^{2k} norms, which are at most their L^{2n} norms. Telescoping the difference
of the products over partition blocks and applying ordinary moment Hölder
to unchanged blocks bounds the whole polynomial. There are finitely many
blocks/partitions for n<=4, so its combinatorial constant is fixed.

More explicitly, suppose for all i and p<=2n,

    ||X_i||_p<=K_i u^(-a_i),
    ||grad X_i||_p<=K_i u^(-a_i+1/2).

A crossing covariance has the u power u^(-sum_{i in B}a_i): its two
gradients supply +1 and (C1) supplies -1. Remaining blocks supply their
ordinary moment powers. Thus every cut yields

    |kappa_n(X_1,...,X_n)|
       <= K_n product_i K_i * u^(-sum_i a_i)
                                      exp(-alpha r(I)).       (5)

This is an actual cancellation estimate, not an unsigned product-moment
bound used as a connected weight.

To express connected decay, make the complete graph on insertion labels
with edge weight d(T_i,T_j), and let tau_n be its minimum spanning-tree
weight. Set r_*=max_I r(I). An MST's largest edge has weight at least
tau_n/(n-1). Deleting that edge gives a cut whose every crossing edge has
at least that weight, by the MST exchange property. Therefore
r_*>=tau_n/(n-1), even when some supports overlap and edge weights are zero.
Taking the strongest cut in (5) gives exp(-alpha tau_n/(n-1)). No triangle
inequality for distance between sets is needed for this graph argument.

Apply (5) first to (f-f(I),g-g(I),B_c,B_d), with exponents (1,1,1/2,1/2),
and then to (C-C(I),B_c,B_d), with exponents (1,1/2,1/2). Restore the two
factors u from the scores. The complete chart response obeys

    |kappa_4,pi_chart(F,G,A_c,A_d)|
      <= K |v_c||v_d| [u^-1 exp(-alpha tau_4/3)
                       + exp(-alpha tau_3/2)],                (6)

where tau_4 uses supports (S_f,S_g,S_c,S_d), while tau_3 uses
(S_C,S_c,S_d), with S_C subset S_F union S_G. If H_F,H_G are disjoint the
second term is absent. Constant arguments can be discarded since their
cumulants vanish; an empty support does not require defining its distance.
The estimate holds using any finite valid support supersets, which only
weakens the bound. Constants depend on fixed support sizes, C^2 norms,
L,kappa,delta and tangent speeds as displayed, not on total volume.

The orbit term has a merged source support and does not automatically give
four separately connected insertion labels. If original F,G have uniformly
bounded local diameters and share an H reader, their endpoint supports meet,
so their enlarged source-region union has uniformly bounded diameter. In
that overlapping case one may charge a bounded internal connection to the
merged source region and obtain a four-region tree bound with a changed
constant. Without that locality/overlap control it is only the displayed
three-insertion tree involving C; treating it as a four-source decay theorem
would be unjustified. Disjoint H readers instead kill C exactly.

For precision, a sufficient four-region comparison is the following. Choose
nonempty valid source-region supersets T_F,T_G also including each original
link's endpoint owner cells, and replace S_C in (6) by T_F union T_G.
Let tau_3^merge be this enlarged-region MST weight and tau_4^reg the MST
weight on (T_F,T_G,S_c,S_d). Splitting the merged vertex in a minimizing
three-vertex tree, assigning each incident edge to whichever source region
realizes its distance, and adding an edge F--G constructs a connected
four-vertex graph. Hence

    tau_4^reg <= tau_3^merge + d(T_F,T_G).

If shared H readers occur, T_F and T_G intersect by construction, so the
last distance is zero; more generally a fixed bound D suffices. Applying
(5) using these enlarged supports gives an orbit bound
K exp(alpha D/2) exp(-alpha tau_4^reg/2). This is a region-support tree
statement; it asserts no decay within a single enlarged source region and
no uniformity for growing source sizes/norms. These qualifications prevent
an orbit overlap from being hidden by relabeling its support.

## 5. Normalization and scope

For full or fixed-chart integrals N_V(s,t), source-independent reconstruction
and distinct terminal links give the identity

    partial_s partial_t D_c D_d log N_V(s,t)|_{s=t=0,V=I}
      = kappa_4(F,G,A_c,A_d),

with the law specified by that integral. If a normalized coarse conditional
is Q=N/D, its complete coefficient is the numerator's coefficient MINUS
partial_s partial_t D_c D_d log D. A normalization obtained by integration
over all terminal V is independent of those terminal coordinates, so that
particular D_c D_d term vanishes. A denominator retaining the varied exterior
or terminal parameters must not be omitted. Neither (2) nor (6) asserts an
estimate for an arbitrary different denominator law or rough exterior; its
own reader/collar hypotheses need checking. Same-link derivatives also retain
the derivative-of-score term, absent only for the distinct-link case here.

At nonzero real source tilt the conditional h law is itself tilted. Formula
(1) as written is the zero-source identity with Haar conditional h; extension
to nonzero sources requires f_st,g_st,C_st from that tilted conditional law.
No such extension, complex analyticity or arbitrary terminal background is
claimed in this note. On the fixed chart, (6) follows from the actual C8
covariance supplier and exact cut cancellations. On the full compact law,
only (1) and (2) have been shown here; the chart does not carry full-law
spatial decay through the rough complement.

Recovery checkpoint: exact response decomposition and reader bookkeeping
proved; invariant original sources yield the O(u^-1) quotient-mean term and
O(1) orbit-covariance term; disjoint H readers eliminate the latter. Fixed
identity chart gives the connected bounds (6), with the explicitly merged
source support or the justified enlarged-region comparison. Independent
verification of this new proof is pending; no retained status or full compact
spatial gluing is asserted. No editable prompt file changed.

Source SHA-256 identities at derivation:

| Source | SHA-256 |
|---|---|
| full-compact-fourth-scaling.md (unchanged) | 549757b9574e7d50b8626ac0421889152cd2fae284f3d8589fe01309c3f86094 |
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |
