# Full compact connected two-source/two-boundary response at identity

Author synthesis, 2026-11-09; decisive independent check pending. This note
instantiates the fixed-reference density forest with the ACTUAL two-hidden-
layer SU(2) law, including its compact complement. Its claimed conclusion
is a finite-depth, identity-terminal, large-u connected response estimate.
It is not the Yang–Mills mass gap. The sources and the conditional orbit
covariance are retained below; a different coarse conditional denominator
continues to have its own response subtraction.

The inputs are the exact forest quotient, actual flat precision and nonlinear
chart covariance, full compact coercivity, the two-step compact decomposition,
its source-marked extension, the frozen Gaussian producers, and the new
fixed-reference density forest. The mathematical arguments and current check
reports are separate artifacts in this pack. An author-level dependency is
not silently upgraded by being composed here. The independent gate must
check their exact hypotheses and this composition before the result is
reported as checked. No new physical axiom or model identification is used.

## 1. Exact law, observables, and target

Fix odd L>=3, kappa>0, terminal torus side m>=3, and u>=1. The original
fine side is L^2 m. The joint hidden law at terminal V is proportional to

    q_u(U0) K_(kappa u)(U1|U0) K_(kappa u)(V|U1).       (R1)

There is one original Wilson action at beta=u and NO added intermediate
Wilson action. Both kernels use the original 24L^4 paired-root-leg word
means, with their input-dependent SU(2) radial normalizers. Every normalizer,
Haar factor and original normalization of q_u stays in (R1).

Use the fixed terminal-root fine forest from `compact-forest-exchange.md`.
At V=I, write the exact normalized measure as pi(da,dh)=nu(da) dh, where
h is the independent probability-Haar root-fixed gauge orbit and a contains
the retained fine non-tree links and ALL intermediate links. There are
M=3L^8+1+4L^4 group coordinates and k=3M scalar chart coordinates per terminal
cell. Quotient coordinates and the orbit reconstruction are independent of
terminal/source parameters.

For a terminal link c and a real tangent vector v_c, its score at V=I is

    A_c(a)=kappa u <i v_c dot sigma_Pauli,M_(1,c)(a)>,
    ||A_c||_infinity<=kappa u |v_c|.                    (R2)

It reads only the actual last-level mean's retained-coordinate support S_c,
of bounded size and diameter within a fixed distance of c's terminal anchor.
If c!=d, D_d A_c=0. With F,G independent of V, the exact fixed-terminal
response is therefore

    D_c D_d partial_s partial_t log N_V(s,t)|_(I,0,0)
                                =kappa_4,pi(F,G,A_c,A_d).          (R3)

The output-independent radial factors remain in pi; their independence of
V explains the score, not their deletion. Same-link differentiation has an
additional derivative-of-score insertion and is outside this statement.

First let F,G be real local C^2 quotient functions, invariant under global
simultaneous conjugation. Original observables invariant under the root-fixed
shared gauge group have this quotient interpretation; conjugation invariance
alone does not give it. Fixed support-cardinality, diameter and C^2 norm
bounds define the admitted class. Let S_F,S_G be valid nonempty reader sets.
Constant arguments give a zero cumulant and can be handled separately.
For these four sets define tau_4 as the minimum number of nearest-neighbor
terminal-cell edges in a connected subgraph meeting all four sets, allowing
Steiner vertices and periodic paths.

The intended bounded theorem is: there exist u0,C<infinity and mu>0,
depending only on L,kappa and the fixed source class, such that for every
finite m and u>=u0,

    |kappa_4,nu(F,G,A_c,A_d)|
       <= C |v_c||v_d| u^(-1) exp(-mu tau_4).          (R4)

For unit tangent vectors and every 0<=eta<mu, there are C_eta,b_eta>0 with

    sum_(c!=d) exp(eta tau_4)|kappa_4,nu(F,G,A_c,A_d)|
       <= C_eta u^(-1) exp[-b_eta d(S_F,S_G)].         (R5)

The proof below addresses the full compact nu, not nu conditioned on one
large-volume all-chart event. Section 5 extends the result to original
noninvariant sources with their orbit covariance explicit.

## 2. Fixed scales and exact compact/chart matching

Choose a fixed exponent A>5/2 and write

    sigma=u^(-1/2), p=log(2+u)^A, rho=sigma p,
    q=c_q rho^2, c_q=1/(2 pi^2).                      (R6)

The chart C_rho is the SAME product logarithm cube |a_i|<rho at every
appearance. For a cell X, T_X=sum_(e owned by X)(1-w(a_e)). The condition
T_X<q implies every owned principal angle is <rho/2, hence lies in this
cube. The compact shell construction uses this actual cell predicate.

Let alpha_shell=min(1,c_E/[4(2K_E+K_r)]) from the compact bounds, and K be
the LEAST positive integer satisfying

    (1+alpha_shell)^K q>2M(4K+1)^4.                   (R7)

The trial-value argument gives K=O(log(1/q))=O(log u); the least-K condition
is essential for this asymptotic use. Let D>=1 bound all four source reader
diameters in periodic l-infinity distance. The source-marked compact proof
uses d_conn=4K+2D+4, regions R_j=N_(2j+1)A0 for a bad core A0 and 0<=j<K,
and native readers Gamma_A0=N_(d_conn+D+2)A0. All N here are l-infinity
neighborhoods. Whole physical factors AND whole source factors are assigned
to their unique active regions. The separation >=2D+7 prevents a source
from reading two such regions.

Introduce fixed normalized insertions X=(F,G,A_c,A_d) with positive bounds
ell_i>=||X_i||_infinity; use ell_F=||F||_infinity, ell_G=||G||_infinity,
ell_c=kappa u|v_c| and ell_d=kappa u|v_d| when nonzero. A zero bound means
the desired coefficient is zero. Write xi_i=zeta_i/ell_i. Take
|zeta_i|<r with 4r<epsilon=1/16. Then sum_i|xi_i| ||X_i||<epsilon.
All fields, selectors, cubes, K and readers are fixed as zeta varies.

The source-marked construction gives the EXACT identity on this polydisc

    N_comp(xi)/N_chart(xi)
      = <sum_(Gamma-compatible F0) product_(g in F0)Theta_g(xi)>_(chart,xi),
    |Theta_g(xi)|<=exp[(log C_epsilon)V_K n_g-c_E u q n_g/4],       (R8)

where V_K=(4K+1)^4, n_g is the total distinct core-cell count, and

    |H_g|<=H_K n_g, H_K=(8K+4D+9)^4,
    |Gamma_g|<=(8K+6D+13)^4 n_g.                       (R9)

Theta_g is a bounded measurable function of all retained coordinates in
H_g, zero off their joint q-good cap, holomorphic in the source parameters.
Its native Gamma_g includes the FULL original support of every source
assigned to one of its regions. Field-free labeled insertions remain.

The regional denominator in each Theta_g is the actual SOURCE-DEPENDENT
chart integral. It is nonzero by the phase wedge
|I_R(xi)|>=cos(epsilon) exp(-epsilon) I_R(0). The corresponding numerator
is the literal compact chart-complement integral with the same density.
No source normalization is replaced by its zero-source value. In (R8),
<.>_(chart,xi) is a complex normalized integral, not a positive functional
assigned total variation one. The density forest will evaluate it exactly.

## 3. Discharging the frozen density-forest contract

At zero sources and V=I let S_u(a) be the complete chart negative logarithm
relative to Lebesgue coordinates, including coordinate Haar constants, the
fine normalization and both radial normalizers. The Gaussian supplier proves
grad S_u(0)=0 and supplies H_u=u^(-1) Hess S_u(0), with fixed uniform gap,
upper and finite-range bounds. Freeze C_u=H_u^(-1) at this point.

It has exponential scalar entries uniformly in u and m. Choose fixed beta>0
below that exponent, then a fixed covariance cutoff R0 sufficiently large
that P_u=C_u 1_(d<=R0) is positive with the stated fixed gap p0 and the
weighted remainder E_u=C_u-P_u has row norm e<=p0/4. Pick ONE deterministic
shortest nearest-neighbor path per UNORDERED scalar pair, and use its same
cell set in both directions. Its cardinality is d+1. The supplier's path
estimate, with its exp(beta) factor, proves a finite uniformly bounded
path-pinned norm B and the weighted row norm required by (F2). Those proofs
use only shortest-path length and endpoint containment, so this symmetric
choice has the same bounds. R0,beta,p0,e,B and all density-jet constants
are fixed independently of u, volume, source positions and K.

No covariance or center varies with xi. This is legitimate because (R3)
is the coefficient of FIXED score insertions at identity; it makes no claim
about finite terminal variations or a complex coarse-field neighborhood.

For each complete physical vertex the Taylor remainder of S_u(sigma x)
after its quadratic polynomial obeys |R_v|<=C sigma p^3 on its full chart
reader cube. Both normalizer levels enter this bound. Their radial log
derivatives of order j<=3 are O((1+kappa u r_c)^(-j)), canceling the chain
rule powers of kappa u when r_c>=1/2. The leading physical terms have
third derivatives O(u), while the Haar terms are uniformly smooth. Thus

    W_v=exp(-R_v)-1,  ||W_v||<=C sigma p^3.            (R10)

Promote every selected vertex reader to ALL scalar coordinates in its owner
cells, and extend W_v by zero outside that WHOLE-CELL cube. On the global
chart this changes no value. It retains every residual cell-body indicator
during activation, and its Gaussian price is K_g^(k|reader_cells|), even
if the original vertex read fewer coordinates. There are fixed arity and
incidence bounds per cell.

The four explicit source vertices are

    W_i^src=exp(zeta_i X_i/ell_i)-1, ||W_i^src||<=exp(r)-1.        (R11)

They receive the same whole-cell cube extension and full reader envelope.
Only their boundedness and source analyticity are used by the density
forest. C^2 field regularity is reserved for the chart estimate below.
Linear couplings to empty-support constants can instead be kept as their
common exp(V_vac) factor; this factor and its individual log contribution
are retained before its cancellation from the compact/chart ratio.

The exact Gaussian prefactor is

    P_vac=exp[-S_u(0)] sigma^n (2pi)^(n/2) (det H_u)^(-1/2).       (R12)

Here n is the number of scalar coordinates, and the scalar P_vac is distinct
from the covariance core P_u. It contains every coordinate-independent
physical normalization. The chart
integral is P_vac times the normalized Gaussian integral with its complete
cube and the factors (R10),(R11). Multiplying (R8) by that chart integral
gives precisely the same Gaussian integral with the compatible compact
insertions. Thus these are the two objects in (F3), with the SAME P_vac.
No extensive determinant or chart probability has been given a uniform
lower bound or silently bounded by one.

Here are explicit estimates of all primitive budgets. For weak vertices
and bad cells, finite incidence and fixed R0 collars give

    h_weak<=C sigma p^3, h_bad<=C exp(-a p^2/8).        (R13)

For the four source vertices, fixed support diameter and cardinality give
h_src<=C_D r for r<=1. Choose r>0 sufficiently small ONCE so that
4r<epsilon and h_src<=H/4, with H the small constant from the abstract
forest theorem. For large u, (R13) then gives h_base<=H/2. No source radius
shrinks with volume; the physical boundary-score radius is r/ell_c=O(1/u).

For compact insertions use S_g=N_R0(Gamma_g), still a connected full reader.
Put

    W_K=(8K+6D+13+2R0)^4,
    Delta_K=max(1,(16K+12D+25)^4-1),
    t_g=K exp[beta W_K+(log C_epsilon)V_K
                       +k log(K_g) H_K-c_Eu q/4].     (R14)

Then, if Delta_K^2 t_g<1,

    h_comp<=W_K t_g/(1-Delta_K^2 t_g).                (R15)

For clarity, the core union is connected at range
2(d_conn+D+2)=8K+6D+12. Its d_conn-components are unique, and shell choices
number at most K^(n_g). A root in S_g is within d_conn+D+2+R0 of some
core cell; summing that anchor costs at most W_K. At core size n, a
deterministic depth-first walk on a spanning tree gives at most
Delta_K^(2(n-1)) connected-set encodings rooted there. Equation (R14)+pays native readers, their fixed collar and ALL active H_g Gaussian costs.
The factor K pays shell labels. This proves (R15) without treating the
common chart measure as a product measure.

The positive exponent costs in (R14) are O(K^4)+O(log K)=O((log u)^4).
The retained negative term is -c_E c_q p^2/4. Since 2A>5, it dominates,
including the polynomial anchor and animal prefactors. For a fixed c_r>0
and a sufficiently large volume-independent u0,

    h_comp<=exp(-c_r p^2)<=H/2.                       (R16)

This uses only the energy charge still present in (R8); no Gaussian
large-field energy is charged again on H_g. All hypotheses (F1)–(F7) are
now matched with the actual two-step coefficients and exact normalizations.
The frozen Gaussian principal-inverse row bound is an additional checked
supplier; the simplified direct-density consumer does not need to spend it.

## 4. Rare connected correction plus the chart response

Apply (F8) to obtain the absolutely convergent connected correction

    Psi(zeta)=log N_comp(xi)-log N_chart(xi)=sum_Y Psi_Y(zeta),
    sup_x sum_(Y contains x) exp((beta/2)|Y|)
                         sup_(|zeta_i|<r)|Psi_Y|<=C exp(-c_r p^2). (R17)

Every coefficient carries all source labels actually read by its primitive
functions. In particular a term differentiated in all four labels includes
their FULL source supports. R0 collars and forest paths are paid in its
connected geometric Y. With Cauchy radius r/2 and (R2),

    |kappa_4,nu(F,G,A_c,A_d)-kappa_4,chart(F,G,A_c,A_d)|
       <= C ell_F ell_G kappa^2 u^2 |v_c||v_d|
                         exp(-c_r p^2) exp[-(beta/2) tau_4].       (R18)

This is a difference of the exact connected coefficients, not a difference
of unsigned four-point moments. The no-compact terms cancel in one common
coefficient indexing. Terms in log N_chart, including its source-dependent
normalization, are added back in the next step.

The chart-fourth proof applies UNIFORMLY to C_rho once rho lies below its
fixed admissible radius. Its Hessian and off-diagonal block bounds hold
throughout the larger fixed cube. The Neumann scalar and mixed one-form
face arguments use convex flat product faces, with constants from those
Hessian bounds rather than an inverse cube width. The discrete conjugation
symmetries still center every coordinate. Linear source tilts preserve
the same Hessian bound, giving local moments O(u^(-1/2)). For singlet F,G,
their differentials vanish at identity, so their centered moments are O(1/u)
and their gradients O(u^(-1/2)); score moments and gradients are respectively
O(sqrt(u)) and O(u). The complete 1|3 AND 2|2 cut cancellations therefore
give the same uniform chart bound

    |kappa_4,chart(F,G,A_c,A_d)|
       <= C |v_c||v_d| u^(-1) exp[-(alpha/3) tau_4].   (R19)

At each fixed u the cube is fixed during source/terminal differentiation;
there is no derivative of rho(u) in (R3) or (R18). The chart is allowed to
shrink with u because all the bounds just cited are uniform on its subsets.

Since u^3 exp(-c_r log(2+u)^(2A)) is bounded for u>=u0, (R18) is at most
C |v_c||v_d|/u times its tree decay. Combining with (R19) proves (R4) with
mu=min(beta/2,alpha/3)>0. For (R5), fix representatives in S_F,S_G.
The four-support tree obeys

    tau_4 >= [d(x_F,x_G)+d(x_F,x_c)+d(x_F,x_d)]/3-C_D.

Its proof adds the three pair-distance bounds from points on one connecting
tree, with fixed source and score reader radii. Summing exp[-(mu-eta)tau_4]
over the two terminal anchors is bounded by the product of two convergent
four-dimensional exponential sums. This is uniform on every finite torus,
and gives b_eta=(mu-eta)/3 after a fixed constant adjustment.

## 5. Original sources and the conditional orbit covariance

Return to original real local C^2 F(U),G(U), invariant under global
conjugation but not assumed invariant under the root-fixed orbit group.
For their original link readers define H_F,H_G as the nonterminal endpoint
gauge-variable readers. The exact reconstruction reads those endpoints and
the original retained links, without an extra root-path of h variables.
Define on the quotient

    f(a)=E_h F(a,h), g(a)=E_h G(a,h),
    C_FG(a)=E_h[F(a,h)G(a,h)]-f(a)g(a).               (R20)

These are local C^2 singlets with bounded norms inherited from the original
source class. The full source factor remains E_h exp(sF+tG). At zero sources
the EXACT identity is

    kappa_4,pi(F,G,A_c,A_d)
       =kappa_4,nu(f,g,A_c,A_d)+kappa_3,nu(C_FG,A_c,A_d).          (R21)

This follows by differentiating total covariance, since h is Haar at zero
sources and the scores read a alone. It is not a replacement of E_h exp(sF+tG)
by exp(sf+tg). If H_F and H_G are disjoint, product Haar independence gives
C_FG=0 identically. Orbit-invariant F or G also gives C_FG=0.

The first term satisfies (R4). For the second, run (R6)–(R18) with the THREE
fixed insertions (C_FG,A_c,A_d), omitting the unused fourth parameter. Every
step only becomes a smaller finite label list. At fixed support class its
compact/chart correction is bounded by
C u^2 exp(-c_r p^2) times the corresponding three-support tree decay.
On the chart, C_FG has zero differential at identity. Its centered moments
are O(1/u) and its gradient O(u^(-1/2)). The same cut-cumulant argument at
order three, with two scores, gives O(1) exp(-alpha tau_3/2), including the
bounded support-diameter correction for a geometric connecting tree. Hence

    |kappa_3,nu(C_FG,A_c,A_d)|
       <= C |v_c||v_d| exp(-mu_3 tau_3),              (R22)

for fixed mu_3>0. It is not replaced by O(1/u).

For uniform locality when C_FG may be nonzero, choose source-region supersets
T_F,T_G that include the retained reader cells AND the original endpoint
owner cells. If H_F intersects H_G, these two regions intersect and their
union has bounded diameter. It is a valid reader for C_FG. A tree meeting
this merged region, S_c and S_d can be joined within a bounded additional
length to meet both T_F and T_G. Thus its three-region tree length bounds
the four-region tree length up to a fixed additive constant. If the H sets
are disjoint, the entire second term is zero instead. Combining (R21),(R22)
therefore yields, with possibly smaller mu and fixed enlarged source regions,

    |kappa_4,pi(F,G,A_c,A_d)|
      <= C |v_c||v_d| [u^(-1)+1_(H_F intersects H_G)]
                   exp[-mu tau_4(T_F,T_G,S_c,S_d)].    (R23)

The matching weighted two-boundary sum has the same prefactor, by the
geometry used in (R5). The O(1) allowance is a retained conditional covariance
term; (R23) neither asserts it has a nonzero leading coefficient nor erases
it. If one of f,g,C_FG is constant, its own cumulant vanishes. Arbitrary
growing source supports or non-singlet sources are outside these improved
u-power bounds. At nonzero original source tilt the conditional h law
changes; (R20),(R21) as written are zero-source identities.

## 6. Exact remaining normalization and physical boundaries

For a normalized coarse conditional p=N/Q the full coefficient is

    D_c D_d partial_s partial_t log p
       =D_c D_d partial_s partial_t log N
                         -D_c D_d partial_s partial_t log Q.      (R24)

Equations (R4)–(R23) bound the specified fixed-terminal numerator law. A
denominator integrating variables or retaining exterior parameters can
have a different law and must be analyzed separately. It contributes zero
to these particular terminal derivatives only when it is independent of
the varied terminal coordinates. No blanket deletion of Q is justified.

This finite-depth theorem would close the compact-complement step of the
identity-terminal connected four-response attack. It does not give uniform
control at arbitrary terminal backgrounds, repeated-link jets, arbitrary
inherited effective actions, blocking depth tending to infinity, reflection
positivity/continuum reconstruction, or a positive physical continuum mass
gap. Its auxiliary pinned Hessian gap and fixed-cell decay rate have not
been identified with a physical mass. These remain separate proof tasks.

Author checkpoint: all statements here are a composed proof proposal until
the frozen dependency match and complete argument receive their independent
gate. No numerical fit, change of model, editable prompt, public write,
formal audit or retained-status promotion has been performed.
