# Global normalized return: sustained construction attempt

This is a living author attempt, not a completed return theorem. The target is
[REALRGA RGA14--RGA16](REALRGA.md) for the actual [JMBRA A2](JMBRA.md)
ratio, with original sources, six total retained-field derivatives, four source
positions, full readers, and the native support rate mu+2. The physical
existence and positive continuum Hamiltonian-gap claims remain open.

Started 2026-10-30 16:30:34 UTC; authorized budget checkpoint 18:00:34 UTC.
Requested configuration: gpt-6-astra/max, author /root/chart_boundary_forest.
No independent backend-model attestation is available. The required preflight
returned go (30 GB free disk, 48% free memory, load 1.6, model floor allowed,
nice works, origin reachable); ulimit memory capping was unavailable. This is
analytic work without scientific computation. Root owns publication and stopping.
The selected procedure is Lab Operation at c93fcb388b60ad7974433b2aa1cb1d366aec52ff.
The prior RT/MEAN sources retain their own procedure pins and are not edited.

## 1. Actual law and the unchanged normalization obligation

Fix the supplied d=4 SU(N) model, N>=2, odd L>=3, probability Haar and positive
u,kappa,t=kappa u. In the fixed rooted block-tree quotient let E be all free
whole links, with every colour and crossing mode retained. At one bare step

    w_J(U,V)=exp[-sum_p (u+J_p)s(U_p)]
               product_c exp[t h(V_c,M_c(U))]/Z_t(M_c(U)),
    Z_cut(V,0)=int chi_cut(U) w_0(U,V)dH_E.                  (GH1)

Here J labels ORIGINAL Wilson coefficients, s=1-Re tr/N, M is the actual
paired-word arithmetic mean, and the kernel normalizer is its full compact
Haar integral. Every derivative in J leaves t and all kernels fixed. The bare
cut is the original product of interior block-plaquette cuts. It is not G,
Omega, the original-a chart, or a translated Gaussian cutoff.

For a union R of whole owner blocks, place each physical plaquette or normalized
kernel touching E_R once in w_R,J; put the other factors in W_out,J. Each
original cut belongs to its owner block. Exactly

    chi_cut w_J=chi_out W_out,J chi_R w_R,J,
    D_R^0(U_out,V)=int chi_R w_R,0 dH_(E_R)>0.             (GH2)

The inequality follows from an open identity/lift cap in each block, while the
remaining continuous physical factors are strictly positive on compact real
fields. Thus no outside factor is used to establish positivity. For an actual
factorization L=L_R L_out, Fubini gives

    int chi_cut L w_J/Z_cut(V,0)
       =int nu_out,R^0 L_out E_out(J) A_R^0,
    nu_out,R^0=chi_out W_out,0 D_R^0 dH_out/Z_cut(V,0),
    E_out(J)=exp[-sum_(p outside P_R)J_p s(U_p)],
    A_R^0=int chi_R L_R w_R,J dH_(E_R)/D_R^0.             (GH3)

On chi_out=0 a conditional quotient of full weights is 0/0; GH2's positive
inside fibre defines its extension, agreeing on the original support. All
outside-only factors and sources remain in GH3. For entangled L, no artificial
factorization is inserted. This independently rederives RT27's identity, not
its provisional estimates. The frozen RT source has SHA256
920865b2ee1f528c1a3134858023b725fd5c69849d84af372d094bf00c22ce12 and is under a
different fresh check at this attempt's start.

At two levels the actual history numerator is instead
int Xi_h exp(-S_0^J) K_0 K_1 dU_0 dU_1 and the denominator is
int chi_A b_1 K_1 dU_1. The complete earlier history Xi_h contains absences;
all current outcomes have already been summed. It is not b_1. JMBRA A3--A5
matches this to the all-cut reference through joint replacement operations,
not independent component laws. A new integration estimate must act on that
same joint density. Positivity alone supplies neither locality nor jet bounds.

## 2. First route: integrate the rough insertion before expanding the mean

This route first examines a real normalized Gaussian, not GH1. Let C>0 be
real, G=C^-1, G<=B Id, m real, and f bounded measurable on R^d. Put

    T_f(m)=int f(x)g_C(x-m)dx.                            (GH4)

The mean is an independent argument in this formula. It is not yet the actual
nonlocal critical mean b(V,J)/sigma. For a complex displacement z,

    T_f(m+z)=int f(x)g_C(x-m)
          exp[z^T G(x-m)-z^T Gz/2]dx.                    (GH5)

This is entire, by Gaussian domination on compact complex sets. Integrating
the absolute Gaussian density directly gives

    |T_f(m+a+ib)|<=||f||infinity exp[b^T G b/2],
    |partial_m^nu T_f(m)|
       <=||f||infinity B^(|nu|/2) sqrt(product_i nu_i!).  (GH6)

There is no cost for the real m, no cost per merely activated coordinate, and
T_1=1 with all nonzero derivatives zero. For the derivative bound define Z=G(X-m)
and the Hermite generating function exp(t.Z-t.Gt/2). Add independent Gaussian
noise of covariance B Id-G. Conditional expectation expresses the correlated
Hermite coefficient as a conditional expectation of the product Hermites for
independent variance-B variables. Their squared norm is B^|nu| product nu_i!,
by multiplying generating functions and integrating. L2 contraction and
Cauchy--Schwarz prove GH6. This rebuilds the RJ2 mechanism; the mathematical
Hermite estimate itself is prior work, not a new closure result.

A fixed hard selector can be included as q(x), 0<=q<=1. If
Z_q(m)=int q g_C(x-m)>0, its normalized rough insertion is T_(qf)/Z_q.
The exact density quotient gives

    |Z_q(m+z)/Z_q(m)-1|
       <=sqrt((exp[z*Gz]-1)/Z_q(m)).                     (GH7)

Indeed the shifted density ratio R has E_g R=1 and
E_g|R-1|^2=exp(z*Gz)-1, while E_g q^2<=Z_q. Consequently a sufficient
zero-free ellipsoid is z*Gz<=log(1+Z_q(m)/4). This estimate loses the sector
mass; it does not provide a uniform all-cut complex mean domain. For a purely
imaginary displacement ib a more informative exact identity is

    T_(qf)(m+ib)/Z_q(m+ib)
      =E_(nu_q)[f exp(i b^T G(X-m))]
                       /E_(nu_q)exp(i b^T G(X-m)).       (GH8)

The Gaussian quadratic prefactor cancels EXACTLY. Center the scalar phase at
its conditional mean. The elementary bound |exp(it)-1-it|<=t^2/2 proves that
the denominator has modulus at least
1-(1/2)b^T G Cov_(nu_q)(X)G b. This is useful only with a covariance bound for
the SAME conditioned law. A principal ambient covariance bound does not by
itself bound this conditional covariance for arbitrary q. For example q can
select two distant Gaussian caps and make its conditional variance large.
No such example is asserted to be the actual Yang--Mills cut.

Thus smoothing really removes fine-analyticity and the real-mean magnitude
from GH6. It does NOT remove the actual cut normalizer, prove complete readers,
or replace GH3's interacting outside law by a Gaussian. These distinctions
are the first route result, not the end of the sustained attempt.

## 3. Routes listed at the first checkpoint

1. Localize GH4 after substituting the actual critical mean, using its canonical
   RF/MEAN atoms and SG's whole finite-range core. Quantify any growing base
   collar and its cost per original input support; a bounded-size result must
   not be relabelled a uniform inherited class.
2. Construct a common-law expansion with marked rough insertions whose own
   original rare reserve pays their density continuation and all source jets.
   Test exact cancellation of the common bare-cut denominator at the connected
   expansion level, not by independently averaging region-dependent fibres.
3. Compare a direct conditional-response route. MGX section4 already rebuilds
   elementary Dobrushin comparison under a strong global oscillation bound.
   Its Wilson estimate scales with u, so that existing sufficient hypothesis
   is not established in this large-u problem. This failure of a criterion is
   not failure of actual mixing. Small-chart convexity plus rare excursions
   may be a different route, but needs a matched conditioned-law argument.

## 4. Status at the first checkpoint

The global target remains a gap. GH2--GH8 are written author derivations, not a
research-gate finding. The hardest remaining step is a connected, full-reader
bound for the SAME correlated normalized-law integration with inherited
multiplicities and all ten derivative positions. Current bare-source or
conditional estimates do not supply it by naming a new hypothesis. No
continuum or physical spectral conclusion is drawn.

Credit: Bałaban's gauge localization and Dimock's large-field organization are
antecedents. Relevant Gaussian integration and norm mechanisms in
[Brydges--Slade, 1403.7244v2](https://arxiv.org/html/1403.7244v2), and block
comparison methods in [Rebeschini--van Handel, 1308.4117](https://arxiv.org/abs/1308.4117),
are being checked at their actual hypotheses. No theorem is imported by title,
and no scalar/d3 or normalized Gaussian result stands in for GH1.

## 5. A common-law current-history construction

The next route works on GH1 itself. Use ONE complete RF/RC/MK/WR family,
its fixed cover R_amb and beta=(16R_amb)^(-4), not SG's different core.
All restrictions of [WR24--WR35](WEIGHTED_RETURN_JETS_ASTRA.md) are imposed
on that same family. In particular r_a=sigma p_cut,
q=c_q sigma^2 p_cut^2, p_cut=log(2+u)^alpha_cut, alpha_cut>5/2,
K is the original SC hard-shell value, and

    delta=d_delta sqrt(q)/(4K+1)^2,
    xi=d_xi sqrt(q)/(4K+1)^2,
    t_d=2 A_G g_*(1+rho)(delta+8xi).                       (GH9)

The constants d_delta,d_xi are strictly positive and satisfy WR34--35.
Keep all other SC/RC cap, source, fine-chart and sweep margins. Real
original sources obey |J_p|<u rho/4. No coarse or source domain belonging
to an independently constructed covariance family is identified with this one.

Let r=4K+4. A current history h is the ACTUAL range-r connected q-bad
components A, each with its first successful shell index j<K. Set
I_j=N_(2j)A, R_j=N_(2j+1)A, S_j=N_(2j+2)A minus R_j.
Its local selector ell_Aj enforces bad on A, good on R_j minus A,
the successful Q(S_j)<=alpha Q(I_j), and every earlier shell failure.
With O_h the complement of union R_j, exactly

    Pi_h=1_good(O_h) product_(A,j in h)ell_Aj,
    sum_h Pi_h=1.                                         (GH10)

Q_X and alpha,c are the actual SC/QC constants. Compact shell growth proves
existence of j; distinct R_j have distance at least seven, so no physical
plaquette or normalized kernel touches two. All predicates are kept. This
uses the original HARD partition, not RT's newer smooth shell representation.
Under the REAL global Haar pullback U_e=Z_e U0_e(V), Q_X becomes
sum_(e owned X)||Z_e-I||HS^2/N. All GH10 selectors are then fixed. Interior
plaquette cuts are fixed too because their links have U0=I. This argument
does not freeze G, Omega, or a predicate of a retained earlier field.

For each core label a=(A,j), choose a measurable insertion f_a in its compact
fine variables E_Rj and touching exterior S_j. It may also depend on retained
original group variables eta and original source labels. The full original
reader must be contained in Gamma_A=N_(r+2)(A); this is an explicit input
restriction, not permission to project an earlier reader onto Gamma_A.
All membership and earlier data actually used must be listed there. No f_a
reads current integrated variables in another separated R_k. The insertion
is C^(6,4) in the RETAINED eta/coarse/source variables AFTER the actual real
Haar pullback, with dominated derivatives on compact parameter subsets.
It may be merely measurable in integrated Z. Hard predicates of retained
eta are excluded unless their required derivatives actually exist.

Define the actual finite-volume functional, with independent auxiliary
activity parameters lambda_a,

    Z_f(lambda;eta,V,J)=int chi_cut w_J
                       sum_h Pi_h product_(a in h)(1+lambda_a f_a) dH,
    Z_f(0;eta,V,J)=Z_cut(V,J).                             (GH11)

This modifies an observable in one fixed physical law. It does not redefine
its action, kernel, cut, gauge quotient, or denominator. The earlier Xi_h
chain law in JMBRA A2 is not assumed to have this product form.

Let I_R be the ACTUAL regional original-a chart fibre with the same physical
exterior, sources and kernel normalizers. Write C_a=N_a^c/I_R,
A_a=N_a^a/I_R, D_a=C_a-A_a, and

    F_a=N_a^c[f_a]/I_R,
    C_a+lambda_a F_a=A_a+D_a+lambda_a F_a.                (GH12)

N^c[f] integrates chi_R ell_a f w_R over the full compact fibre; N^a is
its unmarked chart restriction. There is NO division by N^c[f], by a rare
sector mass, or by a history probability. A marked term is the FULL compact
F_a, including its part inside the chart; using D_a f instead would be wrong.
These fibres are evaluated only on their q-good touching exterior annulus.
Off that annulus extend D_a and F_a by zero BEFORE evaluating I_R. Its fixed
Z selector causes no coarse/source/retained-eta derivative; the exact annulus
cap is still present in every selected group.

Expand GH12 within each history before summing unselected chart terms.
For a fixed selected coloured family s, colour0 means D_a and colour1 means
lambda_a F_a. Put R_s=union_(a in s)R_j and
H_s=(union_(a in s)N_r A) minus R_s. Conditional chart integration on R_s
cancels exactly product I_R. The remaining chart histories are precisely
those bad components at distance >r from selected cores. Their full partition
sums to one, retaining goodness on H_s. If an unselected R_k intersects a
selected N_r A, that intersection contains no bad core and was already good
in ell_Bk. For a SELECTED R_k it must instead be removed from H_s: its chart
variables are dummy variables, and leaving a cap there would change I_R.
This is the same explicit finite bijection as CG12--13, with its selected
factor replaced by either colour of GH12. It uses no estimate.

Group selected cores by overlap of their FULL Gamma_A, retaining colours
and shell indices. For g put Gamma_g=union Gamma_A, n_g=|union A| and
H_g=(union N_r A) minus union R_j. Then

    Theta_g^lambda=1_good(H_g) product_(a in g)X_a,
    X_a=D_a (colour0), or lambda_a F_a (colour1),
    Z_f(lambda)/Z_a=< sum_(Gamma-compatible coloured g)
                                      product_g Theta_g^lambda >_a. (GH13)

Every original absence reader is internal to its group. Coexistent groups
have disjoint Gamma_g; their physical R_j are separated. The right side uses
ONE actual normalized global chart law. Empty selected family is exactly one
AFTER the unselected histories have been summed, not the all-good cap before
that sum. At lambda=0 the entire formula is the original bare-cut formula.
This eliminates GH3's region-dependent outside laws for this specified class,
while integrating their correlated outside variables exactly.

## 6. A joint current-regulator price, including mean spread

The following makes the input class stronger than an unregulated bounded
insertion. Let T=T^(6,4) be RGA3: a+b<=6 retained-fine/coarse positions and
c<=4 ORIGINAL-source positions, with 1/(a!b!c!) and the actual fixed weights.
Assume, on the real pulled-back domain,

    T f_a <= a_a G_(m^a),
    G_m=exp[a_reg sum_B m_B E(B)],
    E(B)=sum_(p owned B)u s(U_p)
                  +sum_(c owned B)t[1-h(V_c;M_c(U))].     (GH14)

The multiplicities are retained, not replaced by union indicators. For this
construction m is supported on I_j, or more generally every positive-weight
owned factor must actually belong to P_R or C_R. This condition must be checked
on the original stencils. Regulator terms on earlier retained levels remain
outside GH14's absorption. For products at one root require the TOTAL
multiplicity sum m_i(B)<=M, with M fixed as below. Different selected R_j have
disjoint physical factor sets, so their original-energy debits do not overlap.

For real e=J/u, |e|<=rho_0<1, put E_R^e=sum_(P_R)(1+e_p)s_p+
 kappa sum_(C_R)psi_c, psi_c=m(M_c)-h(V_c;M_c). Rebuild QC6--7 as follows.
For the actual paired words P_tau and root-straight word S_c,

    average_tau ||P_tau-S_c||HS^2/N
                       <=2(30L^2)^2 sum_(p in brick(c))s_p.

This is the original rectangle filling in the chosen two-block brick.
Also m(M)>=||M||HS^2/N, by averaging the competitors P_tau, and variance
about S_c bounds 1-||M||HS^2/N. Each fine plaquette is in at most eight
LABELLED bricks, including the chosen T=2 seam. A brick plaquette outside
P_R has only exterior free inputs in S_j, has U0_p=I, and satisfies
s_p<=4 sum_(its free occurrences)||U_f-U0_f||HS^2/N.
Each free edge is in six plaquettes. Therefore

    sum_(C_R)(1-h)<=A_E E_R^e+A_Q Q(S_j),
    A_E=1/kappa_-+16(30L^2)^2/(1-rho_0),
    A_Q=384(30L^2)^2,
    sum_B m_B E(B)<=M u C_reg E_R^e,
    C_reg=1/(1-rho_0)+kappa_+ A_E+kappa_+ A_Q alpha/c.    (GH15)

The last line uses Q(S_j)<=alpha Q(I_j)<=alpha E_R^e/c on the selector.
It includes the mean-spread deficit 1-m(M), not only psi. No normalizer is
replaced by its unitary-mean vacuum. Choose a_reg M C_reg<=1/32.
Then multiplication by the JOINT regulator spends at most u E_R^e/32.

At REAL sources/coarse data, the actual chart critical action obeys
A_R/sigma^2<=u A_ref^e, with A_ref^e<=c Q(I_j)/4. The first inequality
uses the real critical minimum of the Haar-inclusive phase and the retained
log Ntilde<=0 at the reset. Its determinant/Haar bound and the original
compact normalizer cap give the exact SC p(u)=p0+p1 log(1+u) price. Thus

    (31/32)E_R^e-A_ref^e >=(23c/32)Q(I_j),
    int chi_R ell_a G_m w_R,J/I_R
            <= exp[p(u)V_K |A|-(c/2)u q|A|].             (GH16)

The weaker c/2 exponent deliberately leaves slack. All D m0|R| chart modes,
h_N powers, determinant, critical action and original kernel normalizers
are included through SC27--29. This is a REAL local estimate; it does not
reuse SC's complex-coarse debit. The later finite Taylor lift avoids making
rough f analytic. No retained-level or unbounded-multiplicity regulator has
been absorbed by GH15.

To bound local jets, differentiate the smooth normalized weight w_R,J/I_R
on its fixed real pulled-back domains. With ell=5L (a safe word overestimate),
h=h_c, r_*=max original source weight, and WR17's positive ordered Bell
polynomials M_n,I_n,C_n,L_n, set

    S=1+2r_*+sum_(b=1)^10[u(1+rho_0)(4h)^b
          +t((ell+1)h)^b+(ell h)^b L_b(t)+r_*(4h)^b],
    B_R=d0 |R| S, d0=(9L^4+5)9^4,
    Q_mix(B)=sum_(a+b<=6,c<=4)C_(a+b+c)(B)/(a!b!c!).     (GH17)

An ordered logarithmic score of a kernel contains both its output term and
its full compact-normalizer derivative; the latter is bounded by L_b(t)
using its positive normalized Haar integral. Original source log scores are
linear, so two such hits vanish. Retained eta derivatives of this bare weight
are zero; keeping them in Q_mix only enlarges the positive bound. Ordered
Leibniz, the inverse-normalizer Bell formula and GH14 give

    T F_a <= a_a Q_mix(d0 V_K |A| S)
                   exp[p(u)V_K |A|-(c/2)u q|A|].        (GH18)

This estimates derivatives of a SIGNED numerator by its absolute differentiated
integrand; it never divides by that numerator. It includes all mixed six/four
positions, and all15 nonempty subsets for four labelled sources after the
usual at-most4! comparison. Hard integrated predicates stay fixed. A hard
retained predicate does not meet GH14 merely because it is bounded.

For finitely many inherited pieces at this root with T f_i<=a_i G_(m_i),
F_a=product_i(1+f_i)-1 satisfies GH14 with
 a_a=product_i(1+a_i)-1 and m=sum_i m_i. This follows by expanding the product,
using G_m G_n=G_(m+n), and G_m>=1. Countable families require sum a_i<infinity.
A convenient size budget is

    a_a<=exp[b_in |A|],   b_in<=c u q/32.               (GH19)

For example at most n_in|A| factors with a_i<=A0 u^M0 give
b_in=n_in log(1+A0 u^M0); n_in=O(K^4), A0,M0 fixed, is allowed eventually.
This is an explicit inherited-size condition, not a theorem that rho_h/b_j
satisfies it. Empty-support factors still contribute to this bill.

## 7. Global density forests with the additional marked species

The changed primitive is F_a, a bounded measurable function of the SAME real
buffer after its compact integration. Let h_f be the actual collection of
retained eta weights; it is already included in a_a. At a real parameter
point use up to six field positions (a fine eta positions and b coarse
positions, a+b<=6) and four original-source positions. The coarse path is
the ACTUAL ordered group path of WR22 with

    R_h=min(1,xi/(64 sqrt(N)h_c)),
    R_J=min(1,u rho/(32r_*)).                            (GH20)

Fine eta parameters can have radius1 since the bare chart density does not
read eta. Replace each rough group by its square-free Taylor polynomial in
these at most ten formal parameters. Coefficients are genuine real derivatives;
no rough argument is evaluated at a complex eta, coarse field or source.
On the radius-two formal polydisc its absolute bound gains at most
C_T=2^10 6!4!, and GH18's positive Q_mix. This is bounded by exp(D_jet n_g),
where

    D_jet=log C_T+log Q_mix(1)+10 log(1+d0 V_K S).        (GH21)

All eta/source labels remain in the insertion's original reader. In the
chart density itself, V and J follow the analytic WR22 path: b, P, E, their
full readers, and the global physical prefactor all MOVE. The same RF fixed
point and geometry-only patch formulas give canonical agreement on overlapping
real parameter charts. Choosing new centers independently would not prove it.
At finite volume differentiation of the exact GH13 integral is justified by
compact domination. Its rough factors and these Taylor polynomials have the
same square-free class. Thus the auxiliary integral has the same normalized
log jets once its convergent log below is constructed.

Here are the all-order density steps being used, including the changed-species
check. For an active scalar set I, use C[I]=P[I]+E[I], the PRINCIPAL covariance.
The untouched coordinates are integrated to one. Every component includes its
whole finite-core collar. With G=P[I]^-1 the exact normalized list exponent is

    -1/2 sum_(j>=1)(-1)^(j-1)Tr((GE)^j)/j
       +1/2 sum_(j>=1)(-1)^(j-1)x^T(GE)^j Gx.           (GH22)

It contains both determinant loops and inverse chains. WR25 gives the same
positive/accretive core and the same independent pair-mask disc; no independent
weakening of large SG core atoms is used. Scalar Cauchy on this density and
sqrt((nu_i+j)!)<=2^((nu_i+j)/2)sqrt(nu_i!)sqrt(j!) give WR28's bound
A_I exp(-a||x||^2/8) L_hat^|nu| product_i sqrt(nu_i!), multiplied by
2^(k(|M|+|H|)/2) exp[L_hat^2 s_d^2(|M|+|H|)], s_d=k t_d/sigma.
The critical shift on a marked buffer is kept real until this density
translation expansion. Every b occurrence retains its full reader.

A bounded F_a changes no Gaussian derivative factorial or polynomial degree:
the forest differentiates ONLY the density. The degree90 estimate still
concerns the DISTINCT original nonlinear vertices with scalar incidence15;
it is not falsely assigned to the rough insertion or an inherited vertex.
The exact chart bodies, all side/corner chains and normals, ternary flags,
original Gamma incompatibility and all presence/absence constraints are
unchanged. The integral is zero off the marked joint cap before a nonlinear
vertex is evaluated there. Complete core components still factor at a
disconnected forest mask, including field-free marked groups.

Put L_M=K_g^k 2^(k/2)(1+s_d)^(90k)exp(C_bar s_d^2), as in WR29.
For every coloured group, the resulting primitive weight is bounded by
exp[D_jet n_g] exp[p(u)V_K n_g-c u q n_g/2] L_M^|H_g|
times product_(marked a)|lambda_a| a_a. The unmarked D factors are already
bounded by the same expression without a_a. For |lambda_a|<=2,
GH19 gives the colour sum product_a(1+2a_a)<=exp[(b_in+log3)n_g].
The marked-only sum is at most this sum and vanishes exactly when all f vanish.
With H_K=(8K+9)^4, W_K=(8K+13+32R_amb)^4 and
Delta_K=max(1,(16K+25)^4-1), define

    D_bulk=k log K_g+(k/2)log2+90k log(1+p_cut),
    t_col=K exp[beta W_K+p(u)V_K+D_bulk H_K+D_jet
                                 +b_in+log3-7c u q/16]. (GH23)

WR35 pays C_bar s_d^2 H_K<=c u q/16, ONCE from the local c/2 reserve.
Counting connected cores, their unique range-r component partition, shells
and colours gives for the marked primitive norm h_F and unmarked h_D

    h_F<=W_K t_col/(1-Delta_K^2 t_col),
    h_D<=W_K t_col/(1-Delta_K^2 t_col).                  (GH24)

This is a conservative bound; h_F itself is the actual positive sum of only
colour-bearing primitive weights. A marked original block has at most W_K
choices of a core anchor; connected n-sets have at most Delta_K^(2(n-1))
depth-first encodings. It does not assume independent activities or remove
complete readers in favour of H_g.

For completeness the four tree sums preserve the new mark as follows. Write
zeta_beta=beta/8, and take WR31's SAME h_c,C0=1+K_m B_E,L_hat,h_0,h_s,j_s.
Require h_0,h_s,h_D,h_F<=h_c/8. Primitive overlap recursion has supersolution
weight times exp(beta|reader|), since the child sum is <=h_c|reader|.
For Gaussian children at each scalar use sum y^j/sqrt(j!)<=exp(2y) and
sum sqrt((j+1)!)y^j/j!<=exp(4y), y<=1/2. WR's h_c ensures both conditions
and pays a second zeta_beta margin. Every E pin is paid by the SAME B_E.
The marked translation pin keeps its root:

    sum_(marked g) e^(beta|widehat_Gamma_g|)a_g K_tr
                   sum_(X in H_g)d_x^b(X) <=K_tr t_d h_F. (GH25)

It is not a volume-wide mean price. Rescale only marked primitive bounds by
h_c/(2h_F); background h_0+h_s+h_D<=3h_c/8 remains fixed. The total is below
h_c, and every marked raw species gains at least one such multiplier.
The density-list, side and translation mark estimates then give

    epsilon_F=2[C0+L_hat^2 B_E h_c+j_s/h_c+K_tr t_d]h_F. (GH26)

The background raw bound epsilon_B is precisely WR's epsilon_a+epsilon_D
with the same parameters, since at zero marks NOTHING in the base changes.
Require epsilon_B<=zeta_beta/4 and epsilon_F<=zeta_beta/4. Group raw species
by overlap of full readers while retaining base disjointness. Its rooted
recursion spends the third zeta_beta. The connected incompatibility-graph
sum is bounded by Kruskal trees (the remaining alternating edge sum has
modulus at most one), spending the fourth. Rescaling marked raw bounds by
zeta_beta/(4epsilon_F) leaves the total raw bound at most zeta_beta/2. Each
rooted tree supersolution then bounds the final logarithm by zeta_beta/2
on the reduced rate. Undoing the surviving marked multiplier gives

    ||Psi_f||_(beta/2;formal parameter sup)<=2 epsilon_F. (GH27)

Every coefficient of Psi_f contains a marked compact primitive. These are
exactly the terms left after subtracting the log at lambda=0, coefficient
by coefficient on ONE canonical list. The actual normalized identity is

    Z_f(lambda;eta,V,J)/Z_cut(V,J)=exp[sum_Y Psi_f,Y],
    Psi_f(0)=0,
    ||Psi_f||_(beta/2;T^(6,4))
                    <=2 exp(3)R_h^-6 R_J^-4 epsilon_F.  (GH28)

The global P_*=h_N^n(2pi sigma^2)^(d/2)
exp[-LogDet K_*/2-F(b)/sigma^2] is identical in both integrals and cancels
EXACTLY, as do all unmarked connected species. This is not subtraction of
unrelated extensive estimates. Multiplying all marked amplitudes by a count
parameter proves the exponential identity first in an absolutely convergent
neighbourhood of zero and then throughout the indicated activity polydisc.
For real data/insertions its branch is the real log continued from lambda=0;
for complex insertions it is the specified nonzero branch. Individual history
masses, which can be zero, are never logged or divided by.

Cauchy extraction on unit formal circles recovers each actual mixed derivative.
The three factorial sums are bounded by exp(3); original labelled sources
retain all subsets and no extra distinct-label factorial. Uniform convergence
of all included jets on real compact subsets proves jets of the SAME actual
functions. The output readers contain every inserted eta label, original
source, fine stencil, core collar, covariance and critical-mean atom. This
proves retained INPUT-field jets; a hard retained-field selector still fails
GH14. The already integrated current buffer fields are not called retained.

## 8. Parameters, actual history probabilities, and the source-free reference

All constants, R_amb,beta,rho and preliminary analytic ceilings are fixed
first. Choose GH9 with the same WR34--35 restrictions; then q,K and chart
radii, and lastly the large-u threshold. Impose D_jet<=c u q/32 and GH19.
With polynomial-in-u h_c,r_* and a stated polynomial input-jet allowance,
D_jet=O(log u+log K). The positive shape/value costs in GH23 are O(log^5 u),
whereas u q=N c_q p_cut^2 and 2alpha_cut>5. Therefore a finite threshold,
uniform in T, makes all GH24--GH27 smallness conditions valid and, after
paying the finite factors in GH28,

    ||Psi_f||_(beta/2;T^(6,4))<=exp[-kappa_f p_cut^2],
    kappa_f=c N c_q/256                                 (GH29)

is one conservative choice. This also pays any fixed polynomial in u from
retained-input jet sizes that has been entered into b_in. It does not pay
arbitrary depth-dependent input growth or a missing regulator estimate.
Every bound before this asymptotic simplification remains explicit in
GH14--GH28. The source-free physical reference is restored as

    Z_f(lambda;eta,V,J)/Z_cut(V,0)
       =[Z_cut(V,J)/Z_cut(V,0)] exp[sum_Y Psi_f,Y].        (GH30)

The first factor retains its full critical action, determinant, Haar/mode
powers, source vacuum and chart/cut remainders, as in WR40. Its derivatives
are not declared zero, rare, or absorbed into epsilon_F. Thus the operation
does not silently replace the reference in RGA2 by its sourceful version.

A particularly concrete case is f_a=1 for every label. Then

    Z_hist(lambda)/Z_cut(V,J)
        =sum_h P_(nu_cut,J)(h) product_(a in h)(1+lambda_a). (GH31)

The complete CURRENT auxiliary-history law, including absences, is present.
At all lambda_a=-1, this is exactly Z_good(V,J)/Z_cut(V,J), not one.
Let Psi_hist denote the log in GH28. For any specified finite history h,
multiaffine coefficient extraction gives exactly

    P(h)=exp[sum_Y Psi_hist,Y(-1)]
           sum_(pi partition h) product_(B in pi)
                  partial_(lambda_B) sum_Y Psi_hist,Y(-1). (GH32)

The empty history uses the empty partition and retains the extensive void
factor. Invalid or zero-mass histories give zero by the original polynomial
identity. No independence of selected components is inferred. For finitely
many marks differentiation is legitimate within the activity polydisc; no
uniform all-mark derivative bound is asserted from the (6,4) physical jets.
The physical field/source derivatives in GH28 act on this SAME generating law.

The class is nonempty beyond constant markers. For a block-interior current
plaquette p and a retained original plaquette p0 whose FULL readers fit
Gamma_A, take f_a=lambda0 1_(s(U_p)>=s0) s(eta_p0), with
0<s0 below the original interior-cut threshold. Its integrated predicate is
fixed by the real Haar pullback; its retained factor is smooth, with explicit
polynomial bounds in its actual h weights. It needs no fine analyticity of
the integrated indicator and has m=0. Multiplying a smooth regulated input
by this same fixed integrated predicate is permitted when GH14--GH15 and
its literal reader/size conditions are satisfied. This is an actual insertion
in GH1, not an assumed representation of a general inherited density.

## 9. What this route does and does not discharge

GH11--GH32 construct a GLOBAL common-normalizer connected return for the
specified current-history decorations, with bounded total CURRENT regulator
multiplicity and genuine retained-input/source jets. Unlike GH3 alone, there
is no unproved outside-expectation estimate within this bounded construction:
GH13 integrates the same outside variables and GH22--GH28 sum their full
reader correlations. It is an unchecked author theorem until separately gated.

It supplies a strict piece of the normalized-return problem, not its full
statement. Its output rate is beta/2 on the original microscopic reader graph.
It does NOT supply exp[(mu+2)|Y|] at a positive mu. WR43--45 already rebuild a
consumer with two SMALL positive rate margins; changing the native interface
and regenerating those margins is a lead/consumer obligation, not a notation
change here. An optional absolute tensor norm pays |Y|^(a+b+c) with its actual
fine/coarse/source label counts and a further rate loss; dense RGA3 jets alone
do not give those counts for unspecified retained ancestry.

Nor is the general Xi_h exp(-S_0^J)K_0... density known to factor into GH11's
local decorations or satisfy GH14/GH19. Retained earlier hard absences are not
made smooth by summing CURRENT histories. Earlier regulators and already
spent original energy have not been reset. Uncharged arbitrary finite-jet
inputs, arbitrary inherited multiplicities, full G/Omega history return,
repeated effective steps, non-free continuum existence and the physical mass
gap remain open. The next sustained route is to test the uncharged mean-smoothed
class and to identify whether an actual inherited decomposition can retain
these current charged roots without spending their reserve twice.
