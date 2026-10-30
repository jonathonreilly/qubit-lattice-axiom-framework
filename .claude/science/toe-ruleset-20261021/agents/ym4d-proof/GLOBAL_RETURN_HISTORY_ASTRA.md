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

## 10. A third colour keeps the ORIGINAL cut complement

There is a further one-step extension of the same construction. Impose
4 sqrt(Nq)<epsilon_cut, with epsilon_cut the original interior-plaquette
operator-norm threshold (or its minimum if the admitted thresholds vary).
An interior plaquette at Q_X<q has each free chord within sqrt(Nq) of I;
its tree links equal I. Unitary telescoping therefore gives
||I-U_p||op<4 sqrt(Nq)<epsilon_cut. Consequently

    Q_X<q implies chi_X=1.                              (GH33)

Every failure of the ORIGINAL cut lies in the actual q-bad set. On a fixed
GH10 history, all such failures lie in its cores A, because R_j minus A and
O_h are q-good. No cut is deleted: this implication determines exactly where
its complement can occur. The additional inequality is compatible with the
fixed positive original cutoff and shrinking q; if a supplied cutoff shrinks,
it is a displayed extra condition, not automatic.

Introduce one auxiliary variable t_B per original owner block and define

    Z_orig(t;V,J)=int w_J product_B[chi_B+t_B(1-chi_B)]dH,
    Z_orig(0)=Z_cut, Z_orig(1)=Z_all:=int w_J dH.          (GH34)

All kernel normalizers and gauge-fixed modes are the original ones. This
polynomial is an exact sum of disjoint ORIGINAL hard-cut sectors. It is not
obtained by declaring chi_cut=1 in an estimate.

For a selected current core A with chosen shell j let

    L_a(t)=I_R^-1 int ell_a w_R,J
          {product_(B in A)[chi_B+t_B(1-chi_B)]-chi_R}dH_R. (GH35)

On ell_a every B in R minus A is q-good, so chi_R=product_(B in A)chi_B.
At each real configuration the expression in braces is zero if all original
cuts hold, and is product_(B failed in A)t_B otherwise. For |t_B|<=2 its
absolute value is <=2^|A| 1_(chi_R=0). Thus it is a bounded measurable marked
insertion in the FULL compact fibre. Its derivatives do not hit an original
cut: under WR15 those cuts are fixed. Denominator and zero-off-annulus
conventions are the same as GH12. The exact local decomposition is now

    C_a^orig(t)=A_a+D_a+L_a(t).                         (GH36)

The real upper proof of GH16 applies to L_a without the factor chi_R. All
coercivity and mean-spread inequalities used there are pointwise on compact
fine fields on ell_a; they do not assume chi_R. The normalizer cap and upper
Haar volume use only a subset of the compact fibre. Hence GH18 holds with
no regulator, a_a=2^|A|, for L_a. There is no derivative of the nonsmooth
maximum m(M); original smooth densities are differentiated as in GH17.
Equivalently absorb 2^|A| in the colour count: D_a+L_a has positive majorant
at most (1+2^|A|) times the common coefficient, and 1+2^n<=3^n.

Repeat the finite GH12--GH13 bijection with L_a(t) as marked colour. The
phase, original-a chart, physical critical prefactor, readers, Gaussian
forests and real moving-center jets are identical to the previous construction.
Use GH23 with b_in=0 and the same log3 colour allowance. No new covariance
or stationary point is introduced. Every surviving log species contains
an L_a reader and vanishes at t=0. It follows that

    Z_orig(t;V,J)/Z_cut(V,J)=exp[sum_Y Phi_Y(t;V,J)],
    Phi(0)=0,
    ||Phi||_(beta/2;T^(6,4); |t_B|<=2)
                         <=exp[-kappa_f p_cut^2].       (GH37)

Here retained-input fine derivatives are zero unless actual smooth insertions
of section6 are included; current fine fields have all been integrated out.
The absolute smallness and actual coarse/source jets are those proved in
GH20--GH29, not a derivative of a newly chosen independent center. Uniform
convergence holds on compact subsets of |t|<2; the displayed bound is the
majorant on the closed radius-two polydisc. Formula GH37 establishes a
one-step FULL compact/bare-cut comparison at the stated narrow real coarse
class. It still does not give a rough coarse boundary estimate.

Under the full one-step real normalized compact law, the probability generating
functional of the ORIGINAL bad-block set is therefore exactly

    E_(nu_all,J) product_(B originally bad)t_B
                         =exp[sum_Y(Phi_Y(t)-Phi_Y(1))]. (GH38)

Its all-cut probability is exp[-sum Phi_Y(1)], with the entire extensive
absence factor retained. Each original bad-set probability is the coefficient
of its multiaffine monomial; zero-mass sets remain zero. Every original hard
cut, source, compact normalizer and mode belongs to this identity.
The hard RD completion test is not determined by this bad set: GH38 does
not claim its retained-field jets or an arbitrary complete-history theorem.

There is nevertheless a direct earlier-level application of the IDENTITY.
At the first step let b_eff,1(U_1;J)=int exp(-S_0^J)K_0 dU_0. For the
refinement recording ONLY the original bad set B at that step,

    rho_B(U_1;J)=b_eff,1(U_1;J)
                     [t^B]exp[sum(Phi_0(t)-Phi_0(1))],
    rho_B/b_1=(b_eff,1/b_1)
                     [t^B]exp[sum(Phi_0(t)-Phi_0(1))].   (GH39)

This applies where U_1 is in GH9's actual small-curvature domain. Its complete
bad-set law is now constructed globally at one bare step. The genuine
b_eff,1 equals the full P_*, chart/cut remainders and exp(sum Phi_0(1)); it
is NOT the prescribed Wilson b_1. The ratio b_eff,1/b_1, any completion
selector depending on U_1, and the next integration remain explicit.
No reference factor is assigned a rare bound merely by writing GH39.

## 11. An actual earlier-history obstruction to current-root-only coverage

The preceding restriction is necessary for a particular proposed extension,
not a global impossibility claim. Use RD R2--R3 with a finite old size
threshold n0, an old original cutoff 0<epsilon_cut,0<2, and a compatible
finite torus containing a connected block set Y with |Y|>n0. Choose the
old fine variables as follows. In each block of Y put one free interior
chord at a diagonal SU(N) element with eigenvalues exp(i theta),exp(-i theta),
1,...,1 and 2|sin(theta/2)|>epsilon_cut,0. Set all other free links to I.
A plaquette containing that chord, and otherwise identity links, fails the
interior cut. Such a chord exists for odd L>=3 in the fixed tree quotient;
an elementary interior plaquette cannot have all four edges in a tree.
Blocks outside Y have every interior plaquette equal I. A sufficiently small
product neighborhood has exactly bad set Y and positive Haar measure.

On this neighborhood a_0(Y)=0 by SIZE for every U_1; there is no other bad
component to generate another failure. Thus the actual complete failure
history h=(F_0={Y}) has Xi_h=1 there, regardless of U_1. Every original K_0
is continuous and strictly positive on all compact real fields, including
arbitrary means. At real original sources in |J_p|<=rho_0 u_0,

    rho_h(U_1)=int Xi_h exp(-S_0^J)K_0 dU_0>0
                                      for every real U_1.          (GH40)

This is an actual positive contribution to a legal earlier history, not an
invented independent selector. Choose the next V=I and U_1=I. Then all current
Q_X vanish, all current interior cuts hold, and

    b_1(I)=exp[-u_1 sum_p s(I)]=1, J_h(I)=rho_h(I)>0.    (GH41)

A sum supported only on nonempty CURRENT q-bad cores vanishes there. It cannot
be this nonempty earlier J_h. For a proposed literal 1+current-corrections
representation one can also prove J_h(I) differs from1 in a nonempty window.

Here is the full normalizer estimate needed for that assertion. For t0>=2,
a translate of the operator ball of radius1/t0 has Haar mass at least
(1+4 sqrt(2)N t0)^(-2N^2), by RD's entry-grid covering argument. On that ball
h(W;M)>=h(U_1;M)-1/t0 for every ||M||op<=1. Thus the EXACT normalized kernel
obeys, uniformly in M and its output,

    k_t0<=Kcap(t0):=exp(1)(1+4 sqrt(2)N t0)^(2N^2).

On Xi_h=1 all blocks of Y fail their original interior cuts. Distinct blocks
supply distinct plaquettes with s_p>=epsilon_cut,0^2/(2N). If n_c is the
TOTAL number of original K_0 factors on this finite torus, positivity and
probability Haar give

    rho_h(I)<=Kcap(t0)^n_c
        exp[-u_0(1-rho_0)|Y|epsilon_cut,0^2/(2N)]<1      (GH42)

whenever the displayed negative exponent exceeds n_c log Kcap(t0).
For fixed finite torus, size threshold, positive cutoff, kappa and rho_0<1,
this is a nonempty large-u_0 window. If those data vary with u_0, retain that
inequality; do not silently assert its asymptotics. The source-free case is
included. Combining GH41--GH42 yields 0<J_h(I)<1, disproving that literal
1+current-bad-only identification on these actual data.

The partition sum over old histories equals b_eff,1, NOT b_1. It cannot be
used to infer rho_h<b_1 without a reference calculation. GH41 uses only the
exact value b_1(I)=1, and GH42 retains ALL old compact normalizers. The result
does not exclude an analytic/earlier-root contribution or a suitably charged
mixed class. It shows why that additional contribution cannot be omitted.
It also does not claim this history lies in an as-yet-unconstructed stable
admissible subclass; its complement would still require an exact estimate.

## 12. Original-cut witnesses give a stronger charged coefficient norm

The literal cut convention is CS1: ||I-U_p||op<epsilon_cut on every
block-interior plaquette. A failed block B has an internal witness p_B with
s(U_pB)>=epsilon_cut^2/(2N). Distinct blocks supply distinct plaquettes,
and every witness in A belongs to P_R. All other centered-energy terms are
nonnegative. For F the failed ORIGINAL blocks in a selected core,

    E_R^e >= e_cut |F|,
    e_cut=(1-rho_0)epsilon_cut^2/(2N).                  (GH43)

This bound and E_R^e>=c Q(I_j) concern the SAME energy. They are not added
as though two independent reserves existed. In section10 no input regulator
was inserted. Allocate exactly theta_cut=1/32 of that energy and set

    r_cut=exp[u e_cut/32].

For |t_B|<=r_cut the exact cut-sector polynomial in GH35 has absolute
coefficient sum r_cut^|F| at each configuration with F nonempty. Thus
log(r_cut)|F|<=u E_R^e/32. The remaining density and reset satisfy

    E_R^e-A_ref^e-u^-1 log(r_cut)|F|
             >=(31/32)E_R^e-A_ref^e
             >=(23/32)E_R^e >=(c/2)Q(I_j).             (GH44)

The compact normalizer, determinant and Haar price is still p(u)|R|.
This leaves the SAME c u q/2 local reserve used by GH23. The subsequent
c u q/16 real-buffer translation, finite jets, shape and reader costs are
paid only from that retained reserve. For simultaneous input regulators
one must replace the condition by a_reg M C_reg+theta_cut<=1/32; the two
previous allocations cannot both be spent at their maximal values.

There is no factor r_cut^|A| left in the local estimate: the actual number
of failed blocks was paid pointwise by GH43. Its positive value bound is
the old bound with a_a=1. All cut-sector coefficients are disjoint before
integration. The ordered density-jet bound in GH17 is common to them, so
the sum of the absolute physical Taylor coefficients with t weight
r_cut^|F| obeys the SAME GH18. The two selected colours cost at most2 per
core; retaining the previous log3 allowance is conservative.

Carry these nonnegative cut-monomial weights through the two density and
two reader trees BEFORE taking coefficient absolute values. A product of
marked primitives multiplies t monomials and multiplies their weights.
Repeated labels in a logarithmic term are kept with their multiplicities;
no original action is respent in a single physical integral. The standard
repeated-activity products in the logarithm use already bounded integrals.
Since every log term has at least one marked primitive, write canonically

    Phi_Y(t)=sum_(n nonzero) phi_(Y,n) t^n,
    n=(n_B) finitely supported, n_B nonnegative integers,
    supp n subset Y,
    sup_x sum_(Y contains x) exp[(beta/2)|Y|]
          sum_(n nonzero) r_cut^|n| sup T^(6,4) phi_(Y,n)
                         <=exp[-kappa_f p_cut^2].       (GH45)

Here and only here T includes the actual current coarse and original-source
jets (or an explicitly admitted smooth retained input as in section6).
It is not a claim that an unintegrated hard retained predicate has such jets.
The r_cut power-series estimate follows directly from the positive majorants,
not from summing Cauchy estimates over exponentially many unspecified labels.
For u sufficiently large r_cut>=2, so it also contains GH37's polydisc.
If a shrinking original cutoff is supplied, r_cut retains its displayed
u epsilon_cut^2 value and GH33 must still hold.

For a nonempty finite set C of distinct original cut labels put

    v_C=sum_Y phi_(Y,1_C)=partial_(t_C)sum_Y Phi_Y(0).

Keep the finer Y-decorated coefficients whenever full readers are needed.
They have at least one ORIGINAL failed-block label, each paid by r_cut^-1.
For an exact bad set B the ratio to the SAME all-cut reference is

    rho_B/Z_cut=sum_(pi partition B) product_(C in pi)v_C,
    rho_empty/Z_cut=1.                                (GH46)

This is coefficient extraction of exp(Phi), not a product-probability
assumption. Multiindices with repeats do not enter this distinct-label
coefficient; they remain in the full log and its norm. Formula GH46 is a
constructive complete-reader charged library for ALL original bad-set
sectors at ONE bare step. Its void factor under nu_all is exp[-sum Phi(1)],
as in GH38. The physical Wilson-source normalization at J=0 is still GH30.
All original kernel vacua, Haar/mode powers and the extensive critical
prefactor remain in Z_cut and b_eff,1. Nothing in GH45 bounds b_eff,1/b_1.

This supplies actual earlier ORIGINAL-cut charges after their fine fields
have been integrated, instead of trying to attach them to a later current
q-bad event. It does not supply the RD completion/size-history selector
when that selector still depends on retained fine/coarse fields. Summing
those history selectors before the first transfer gives the same Z_all
exactly, but controlling the next step outside the present small-curvature
window and controlling the resulting full prefactor are additional tasks.

## 13. Keep the actual first-level failure selectors inside the integral

This is an unchecked continuation proposal, not acceptance of GH11--GH46.
It addresses the first complete RD failure record, including completion
failures and absences, rather than only its original bad-block refinement.
The finite identities below are direct algebra. The proposed quantitative
extension still depends on the unreviewed density-forest estimates above.

Use exactly RD R2--R3 at level zero, with H_0 empty, its G_2 components,
size threshold n_0 and completion test from H11 of
[SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md).
Match its original cut to GH33. The source conventions agree after
J_p=u_0 epsilon_p; kernel parameters remain fixed in either convention.
At fixed U_0,U_1 let B be the original bad-block set and

    F(U_0,U_1)={Y in C_2(B): a_0(Y;U_0,U_1)=0}.

Introduce t_B for original blocks and z_Y for nonempty G_2-connected
candidate components. The exact finite generating integral is

    Z_RD(t,z;U_1,J)=int w_J(U_0,U_1)
                product_(B originally bad)t_B
                product_(Y in F(U_0,U_1))z_Y dH(U_0).    (GH47)

Thus Z_RD(0,z)=Z_cut, Z_RD(1,1)=b_eff,1, and
[z^F]Z_RD(1,z)=rho_(1,F). The last coefficient specifies the COMPLETE
failure list: successful bad components are summed, and every other
failure marker has power zero. Incompatible lists have zero coefficient.
This is RD R3, including its absence conditions, not an independent
probability assignment. No history mass is divided out.

On a current auxiliary q-history GH10, GH33 puts every original bad block
in a q-bad core A. Different such cores have distance greater than
r=4K+4>=4. Consequently each G_2-component of the ORIGINAL bad set lies
in a unique A. Its completion test reads N_1(Y), the original outside
links relative to I(Y), and the output U_1 links C(Y). All these readers
lie in Gamma_A. Maximality of Y also reads its G_2 boundary; the actual
goodness factors on N_r(A) retain that absence information. The size test
reads Y itself. No additional failure predicate is substituted for RD's.

Let B_A be the original bad blocks in A and F_A their completion/size
failures, evaluated before integrating any of their readers. Define

    P_A(t,z)=product_(B in B_A)t_B product_(Y in F_A)z_Y,
    L_a^RD(t,z)=I_R^-1 int ell_a w_R,J
                                  [P_A(t,z)-chi_R]dH_R. (GH48)

On the actual auxiliary history, product_A P_A is exactly GH47's marker.
At a local fibre whose exterior does not meet the required good annulus,
use the same zero extension as GH12. The global absence factors in GH13
remain necessary; a local factor alone does not impose them. On ell_a,
all blocks of R minus A are originally good. The bracket in GH48 is
therefore zero when B_A is empty, and otherwise is the single monomial
P_A. In particular it is not a signed difference of two large weights.
The local decomposition is exactly A_a+D_a+L_a^RD. Summing unselected
histories and retaining all Gamma_A readers gives the same finite
common-chart identity as GH13. There is still only one global normalizer.

There is a useful joint coefficient price. Let r_cut be GH43--GH44's
exp[u(1-rho_0)epsilon_cut^2/(64N)] and assign radii

    |t_B|<=sqrt(r_cut),       |z_Y|<=r_cut^(|Y|/2).

The failed components in F_A are disjoint subsets of B_A, so
sum_(Y in F_A)|Y|<=|B_A|. At each integration configuration, the absolute
coefficient sum of GH48's nonzero bracket at these radii is at most
r_cut^|B_A|. GH43 pays this from the SAME u E_R^e/32 already allocated in
GH44. There is no new action reserve, no sum over all candidate labels at
a fixed configuration, and no r_cut^|A| factor. Any other regulator must
share the single allocation as specified after GH44.

That pointwise coefficient sum alone does not justify the coefficientwise
output supremum in GH49. For the latter first fix the pulled-back original
bad set B_A and its G_2-components Y_1,...,Y_k. These original cut predicates
depend on the integrated interior Z variables and not on U_1 or J. As
output and buffer data vary, the completion outcomes lie among the subsets
of these k components. Take a common uniform positive normalized-density
and ordered-source-score envelope, as in GH16--GH18, BEFORE taking the
coefficientwise suprema. The sum of possible marker weights is then bounded by

    r_cut^(|B_A|/2) product_(i=1)^k [1+r_cut^(|Y_i|/2)]
       <=2^k r_cut^|B_A| <=2^|A| r_cut^|B_A|.

The fixed original-bad-set indicators can still be summed inside that
common integral. Pay r_cut^|B_A| from GH43--GH44 once. The additional
completion-outcome count costs at most 2^|A|, which must remain in the
marked primitive envelope. Including the unmarked D colour gives
1+2^|A|<=3^|A|. Thus use the direct D-plus-mark count of GH36--GH37,
with b_in=0 and the existing log 3 term in GH23. Do not also insert an
independent radius-two lambda multiplier or a second colour allowance.
Every subsequent positive forest majorant uses this coefficientwise
envelope; the preceding pointwise disjointness estimate is insufficient
for that purpose. This repairs the changed-selector count, while the
unreviewed forest bounds themselves remain the proposed input to GH49.

The completion selector is source independent but can be discontinuous
in the OUTPUT U_1. For this extension use only

    T_J^4(F)=sum_(c<=4) sup |D_J^c F|/c!

with RGA3's original source weights. Hold U_1 real and fixed. After the
same real Haar pullback, neither the original cuts, auxiliary history
tests nor completion tests move with J. Ordered source derivatives hit
the actual density and its full normalizers; they do not hit P_A. The
positive local jet bounds therefore use the source-only subcalculus of
GH17--GH18. In the forest step deform J only, keeping U_1 fixed. Density
differentiation in the integrated buffer still permits bounded measurable
insertions. A completion marker is never differentiated in a fine
coordinate or evaluated at a complex coarse field in this construction.

The proposed consequence of repeating the positive coefficient majorants
in GH22--GH29 and GH45 is a connected expansion on the SAME small-output
domain D_0 supplied by GH9:

    Z_RD(t,z;U_1,J)/Z_cut(U_1,J)=exp[sum_X Phi_X^RD(t,z)],
    Phi_X^RD(0,z)=0,
    sup_x sum_(X contains x) exp[(beta/2)|X|]
      sum_(n,m) r_cut^((|n|+sum_Y |Y|m_Y)/2)
        sup_(D_0) T_J^4(phi_(X,n,m)) <=epsilon_RD,       (GH49)

where Phi_X^RD=sum phi_(X,n,m)t^n z^m and every term has |n|>0.
Use epsilon_RD=2 exp(3) R_h^-6 R_J^-4 epsilon_F, with the same positive
majorants and parameter restrictions as GH28--GH29; the proposed bound is
then at most exp[-kappa_f p_cut^2] above that large-u threshold. Keeping
the larger finite-field-jet price is an overestimate, not additional
field regularity. Source and
completion readers, repeated auxiliary labels in the logarithm, and
the original graph units are retained. This estimate is a PROPOSAL
awaiting independent verification of the existing forest argument and
this changed-species application. It is not a proved six-field-jet bound.

At fixed finite volume and admitted real original sources J, the exact
coefficient C_F^exact is defined on ALL real U_1 by the positive-denominator
polynomial ratio

    C_F^exact(U_1,J)=[z^F] Z_RD(1,z;U_1,J)/Z_cut(U_1,J).

Only on D_0 may the proposed GH49 be used to write it as
[z^F]exp[sum_X Phi_X^RD(1,z)]. For that representation put
Theta(z)=sum_X Phi_X^RD(1,z). Then

    C_F^exact=exp[Theta(0)]
                 sum_(pi partition F) product_(C in pi)partial_(z_C)Theta(0).
                                                               (GH50)

The extensive empty-failure factor exp[Theta(0)] is retained, including
for F empty. At real sources the probability generating function under
the full first step is exp[Theta(z)-Theta(1)]. Neither expression is a
product law.

The exact consumer at the second step is consequently

    R_F(V,J)=int K_1(V,U_1) Z_cut,0(U_1,J)
                                      C_F^exact(U_1,J)dH(U_1),
    J_(1,F)=[Z_cut,0(U_1,0)/b_1(U_1)]
             [Z_cut,0(U_1,J)/Z_cut,0(U_1,0)] C_F^exact(U_1,J). (GH51)

This matches JMBRA A2--A5 and RD R5 literally. All current second-step
outcomes are summed in R_F. The source-free reference, its source
compensator, and the complete effective-density factor remain explicit.
On U_1 outside D_0 keep the original compact integral for C_F^exact;
GH49 does not estimate that complement. Although the U_1 completion
selectors are integrated at this next full transfer, this fact alone
does not yield a volume-uniform connected estimate for GH51.

The next unresolved mathematical task is thus quantitative, not an
identification of current q-bad events with earlier failures: control
the full Z_cut,0/b_1 factor together with this inherited
marked family, its complement, and the next integration. Original action
already paid in GH44 cannot be charged again. Stable reader margins,
field jets after the next integration, reserve regeneration and all
later scales remain open. No existence or physical-gap conclusion follows.

Continuation provenance: coordinator OpenAI/Codex/host-runtime
01a1873f-103a-7f01-b924-4455238d8a86, 2026-10-30; procedure revision
53f2c0af7eb59438389b4c2fe75952932d4e95fe. The preceding 860-line author
snapshot is preserved at b1979a0173. This continuation used the actual
RD R2--R5 and H11 selector definitions, not a new literature import.

## 14. The previous small-output complement inside the next ordinary chart

This coordinator continuation submits a finite-volume lower bound for
independent checking. It concerns the actual second posterior, including
both normalized kernels. It tests a proposed use of the first-step rare
price on the previous output-domain complement; it does not assume that
such a use is part of GH49.

Fix N>=2, odd L>=3 and one compatible three-level finite torus. Fix
kappa>0, let u_0=u tend to infinity, and assume
0<c_-<=u_1/u<=c_+<infinity. This is a declared test family of RD R1,
including u_1=u; it does not establish the physical running-coupling law.
Use zero original sources, the actual pinned-tree quotient and normalized
Haar measures. Put p_i=log(2+u_i)^alpha_cut, sigma_i^2=N/u_i,
q_i=c_q sigma_i^2 p_i^2, and retain GH9's first output domain

    D_0(u)={U_1: max_P ||I-U_(1,P)||op < delta_0(u)},
    delta_0=d_delta sqrt(q_0)/(4K_0+1)^2.                    (GH52)

SC7 gives K_0 asymptotic to a positive constant times log u. Let Omega_1(I)
be the next literal product chart with every free whole-link logarithm of
HS norm <r_a,1=sigma_1 p_1. Let G_1(I) be its next auxiliary q-good sector:
every Q_X^(1), measured relative to U0(I)=I, is <q_1. Define the ACTUAL
backward probability at second output I by

    rho_1(U_1)=int exp[-u W_0(U_0)] K_0(U_1,U_0)dH_0,
    rho_2(I)=int K_1(I,U_1)rho_1(U_1)dH_1,
    nu_2(dU_1)=rho_2(I)^-1 K_1(I,U_1)rho_1(U_1)dH_1.        (GH53)

This sums the first history masses, rather than normalizing a selected
history separately. There are constants c_T,C_T>0 and M_T<infinity,
independent of u in this fixed-volume test, such that for all large u

    nu_2(D_0^c intersect Omega_1(I) intersect G_1(I))
        >= c_T u^(-M_T) exp[-C_T u delta_0(u)^2].            (GH54)

The proof gives the same lower bound with D_0^c replaced by the failure
of its curvature bound at one fixed witness plaquette.
The lower integration region may also be restricted to the first original
cut sector. Hence first original bad-block failures are not needed for
this complement to occur. The same lower bound holds if that original
cut is included in the initial density and its actual posterior is used.

Proof. Choose an interior level-one plaquette in a level-two block and
one edge e_* of it which is not in the pinned tree; a tree cannot contain
all four edges. Write H=diag(1,-1,0,...,0), t=4 delta_0, and choose U_1^t
with exp(i t H) on e_* and identity on every other free link. That
plaquette has defect 2sin(t/2)>2 delta_0 for all sufficiently large u.
Its whole-link logarithm has HS norm sqrt(2)t. Since

    delta_0/r_a,1=O(K_0^-2),
    delta_0^2/q_1=O(K_0^-4),
    u^(-1)/q_1=O(p_1^-2),

this configuration lies strictly inside Omega_1(I) and G_1(I), while
lying outside D_0. The implicit constants depend only on the fixed
coupling-ratio bounds and other fixed data, not u.

Around U_0=I and U_1=U_1^t integrate product Haar balls of radius
a u^(-1/2) in each free Lie-algebra coordinate, with fixed a>0 small.
Their joint volume is at least c_T u^(-d_T/2), where d_T is the total
number of integrated real coordinates. Because
delta_0 sqrt(u) is of order (log u)^(alpha_cut-2) and tends to infinity,
the whole U_1 ball remains outside D_0. The preceding ratios put it
inside both Omega_1(I) and G_1(I). All level-zero plaquettes in the
U_0 ball have defect O(u^(-1/2)), so it is inside every fixed original
positive cut, and also every shrinking original cut satisfying GH33.

For any of the actual convex path means M=sum_s w_s P_s, w_s>=0,
sum_s w_s=1, the literal SU(N) maximizer gives the elementary bound

    0<=psi_M(V)=m(M)-Re Tr(V^*M)/N
       <=sum_s w_s ||V-P_s||HS^2/(2N).

Here m(M)<=1; no scalar replacement of the SU(N) maximizer is made.
Finite products of unitary links are Lipschitz with their actual word
lengths, by telescoping. On the chosen balls this bounds the complete
nonnegative exponent by

    u W_0(U_0)+kappa u sum_c psi_(M_0,c)(U_1,c)
            +kappa u_1 sum_c psi_(M_1,c)(I)
        <= C_T u delta_0^2+C_T.

The bound uses every actual path; at their centers all relevant link
displacements from I are either zero or O(delta_0). Since
0<Ntilde_(kappa u_i)(M)<=1, the normalized kernels are bounded below by
their displayed exponential factors. Thus the joint numerator restricted
to these balls is at least c_T u^(-d_T/2) exp[-C_T u delta_0^2].

Conversely SC27 applies to every compact M, including singular means.
Every kernel is at most C(1+u_i)^(D/2), D=N^2-1. There are finitely many
level-zero and level-one kernels on the chosen torus, W_0>=0, and the
actual Haar total volume is one. Therefore rho_2(I)<=C_T u^(b_T) for
a finite b_T. Division gives GH54 with M_T=d_T/2+b_T. No saddle-point,
Gaussian substitution, partition-function cancellation or discarded
determinant has been used. Restricting the initial density to its original
cut preserves the same lower region and the same upper denominator bound.

In particular, u delta_0^2 is of order (log u)^(2alpha_cut-4), while
log u=o(u delta_0^2) because alpha_cut>5/2. Hence GH54 implies

    lim_(u->infinity) [-log nu_2(D_0^c intersect Omega_1(I)
                                           intersect G_1(I))]/p_0^2=0. (GH55)

For every fixed eta>0, C>0 and finite m, an upper bound
C u^m exp[-eta p_0^2] for this event is therefore false already on this
one torus. Its lower probability can instead be written
exp[-C_T' (log u)^(2alpha_cut-4)]; this is a lower bound, not a sharp rate.

GH49 remains confined to D_0. Its complement is present even in the next
ordinary q-good chart and cannot be assigned GH49's same p_0^2 rare
price. A valid second transfer must estimate that complement at an
adequate weaker rate, enlarge the real output domain, or supply another
matched representation. GH54 does not rule out any of those repairs,
nor a differently proved running-coupling regime. It does not prove a
connected complement estimate, stable domains, reserve regeneration,
continuum existence or a physical mass gap. All other obligations persist.

Coordinator continuation, 2026-10-30, same procedure revision as section 13.
The proof uses RD R1, SC7, SC27 and the literal chart/mean definitions;
no outside theorem is imported. Independent review is pending.
## 15. A wider auxiliary chart for the actual second-step input

Coordinator construction, procedure 6243acc936982e945732793bf641442c03abbfea.
Independent checking is pending. This changes auxiliary integration radii;
it changes neither the physical original cut nor RD's completion decisions.
Section 14 remains valid for its original logarithmic-radius family.

The antecedent distinction is explicit in Dimock, [1108.1335v2, section 3.2,
Definitions 1--2 and Lemma 8](https://arxiv.org/pdf/1108.1335): the physical
small-field set and the larger analytic set have different bounds. Its
three-dimensional scalar estimates are not imported here. The following
argument instead rechecks the actual RF/RC/WR bounds for this compact model.

### 15.1 Radius choice and the existing proof's quantitative conditions

Keep the single RF/NR/MK ambient family, its fixed R,beta,rho and every
preliminary analytic ceiling. Fix 0<theta<1/2. Define

    p_w=u^theta, sigma^2=N/u, r_w=sigma p_w,
    q_w=c_q r_w^2, K_w=K(q_w) from SC7,
    delta_w=d_delta sqrt(q_w)/(4K_w+1)^2,
    xi_w=d_xi sqrt(q_w)/(4K_w+1)^2.                    (GH56)

The constants c_q,d_delta,d_xi satisfy the SAME RC17, SC5--6 and WR34--35
restrictions; take tau=c_tau r_w and the corresponding RC17 boundary cap.
Require, for the original physical cutoff and all sufficiently large u,

    8 r_w<epsilon_cut(u), 4 sqrt(N q_w)<epsilon_cut(u). (GH57)

A fixed positive cutoff meets GH57. So does
epsilon_cut(u)>=c_e u^(-1/2+epsilon), if theta<epsilon and c_e>0 is fixed.
No such claim is made for an arbitrary cutoff shrinking faster than r_w.
All source jets keep u, these radii and the kernel parameter kappa u fixed.

Here r_w->0, p_w->infinity, q_w->0 and

    K_w=(2/g)(1-2theta)log u+O(1),
    delta_w,xi_w=Theta(sigma u^theta/(log u)^2),
    u q_w=N c_q u^(2theta).                            (GH58)

Thus delta_w/tau and xi_w/tau are O(K_w^-2). Every RF contraction,
active-chart, exterior-cap and transported-coarse margin eventually holds
with the same fixed preliminary constants. SC12 and WR35 still hold
algebraically, with q=q_w and K=K_w; neither debit is discarded.

The parameter substitution is made in the estimates BEFORE their former
logarithmic-profile corollaries. In RC12--13, tau/sigma=c_tau p_w, the
bad/side terms and their translation pins are polynomials in u,p_w times
exp(-a p_w^2/64), while h_v=O(sigma) and h_2=O(sigma^2). All Taylor and
covariance constants are fixed at the preliminary ceilings. RC18's proof
therefore gives its same C1 sigma^2 plus Gaussian-tail bound; its stated
conditions p->infinity and sigma p->0 hold for p_w. In particular, no
uniform smallness of the phase on the entire enlarged chart is presumed.

SC27--29 retain every kernel normalizer, Gaussian mode and Haar factor.
Their local entropy is still p(u)=p0+p1 log(1+u), independent of the
auxiliary cutoff. In WR19--21 the score is polynomial in u for the
declared polynomial field/source weights, so D_jet=O(log u+log K_w).
The complete-reader and shell factors in WR36 are consequently

    beta W_K+p(u)V_K+D_bulk H_K+D_J+log K_w=O((log u)^5).

This is o(u q_w), including D_bulk=O(log p_w)=O(log u). The full-buffer
mean-translation payment remains WR35. WR37's denominator tends to one;
both marked rescalings still satisfy their strict smallness bounds. The
remaining K_tr t_d and inverse Cauchy-radius factors are at most polynomial
in u, hence are absorbed by any fixed unused fraction of u q_w.

For h<=C_h sigma and r_*<=C_J u, xi_w/h tends to infinity. Thus R_h=1
eventually, R_J is bounded away from zero, and the weighted six-field/four-
source remainder retains its O(sigma^2) estimate after the same beta/8
tensor-reader payment. The constants and thresholds depend on theta and
the declared physical-cut margins, but not on the torus volume.

### 15.2 The full unmarked first density, with its prefactor retained

Let rho_1(V,J)=int w_J(U,V)dH(U), including ALL original cut sectors.
It is the actual RD first density, not a Wilson reference. For a regional
core a, let D_a be its compact-minus-chart term WITH the original cut, and
let L_a(1) be GH35 at all original-cut markers equal to one. Since the
regional product chart is inside the original cut, their exact sum is

    D_a^all=D_a+L_a(1)
           =I_R^-1 int ell_a w_R,J (1-1_chart,R)dH_R. (GH59)

This is one positive outside-chart integral at real sources. It does not
erase a cut from a cut-sector numerator: the omitted original sectors
are explicitly restored by L_a(1). On the global real Haar pullback the
q_w selectors, product chart and original interior cuts are fixed. The
local real bound in GH16, without a regulator, applies pointwise to its
full compact domain; it never required chi_R=1. Consequently WR20--21's
ordered Bell-score bounds apply to D_a^all, with the same denominator and
all normalized-kernel derivatives. No derivative hits a completion test.

Replacing D by this single D^all in the exact selected-core resummation
gives rho_1 relative to the SAME global chart integral. It changes no
outside factor, dummy chart variable, annulus cap or covariance reader.
The WR density-only forest and both rescalings then use precisely the
same positive primitive bounds, now with GH56. Thus, on the admitted real
output family with curvature <delta_w,

    rho_1(V,J)=P_*(V,J) exp[sum_Y R_Y^all(V,J)],
    ||R^all||_(3beta/8;T_abs^(6,4))
       <= C_beta sigma^2+exp[-kappa_w u^(2theta)]       (GH60)

for some fixed kappa_w>0 and all sufficiently large u, with
h<=C_h sigma,r_*<=C_J u. R^all is the transported chart remainder plus
the D^all return. P_* is EXACTLY the actual critical-action/determinant/
Haar prefactor in WR40, using this auxiliary chart's admitted family;
it is not counted in the small norm and is not replaced by b_1. The
critical branch depends on the phase, not on the choice of an integration
radius containing it; uniqueness identifies that branch on overlapping
old/new domains. No equality of differently grouped polymer coefficients
is needed. This claim retains the full compact integral and all modes.

For the actual RD failure markers, keep their original definitions and
all completion/absence readers. GH57 gives GH33, so their assignment to
q_w cores and the corrected coefficientwise count in section 13 are
unchanged. The source-only GH49 proof now has u q_w=N c_q u^(2theta);
its compact charge and combined D/F translation pin are unchanged.
Hence its norm is <=exp[-(c N c_q/256)u^(2theta)] on this larger real
domain, with the same original-cut marker radii and four source jets.
No field derivatives of individual failure coefficients are inferred.

Writing Theta(z;V,J)=sum_X Phi_X^RD(1,z;V,J), the normalized first-failure
generating function is exactly

    G_RD(z|V,J)=Z_RD(1,z;V,J)/rho_1(V,J)
              =exp[Theta(z;V,J)-Theta(1;V,J)].          (GH61)

Its connected source norm costs at most twice the preceding GH49 bound.
The extensive void factor and all zero histories are kept by coefficient
extraction from GH61. This is not a product law for the old failures.

### 15.3 Containment of the next ordinary chart and the remaining integral

Return to the next ordinary chart of section 14, with
r_1=sigma_1 log(2+u_1)^alpha, sigma_1^2=N/u_1, fixed alpha>5/2 and
0<c_-<=u_1/u<=c_+<infinity. Let U_1=Z U0(V_2), each free-link principal
log of Z having HS norm <r_1. The tree links stay fixed. Each plaquette
of the lift U0(V_2) is I or a transported coarse plaquette. Telescoping
the four unitary factors therefore gives

    max_P ||I-U_1,P||op <= delta(V_2)+4r_1,
    [delta(V_2)+4r_1]/delta_w ->0
        if delta(V_2)<=C_2 r_1, C_2 fixed.              (GH62)

The limit is uniform over the declared ratio interval, since its upper
bound is a constant times (log u)^(alpha+2)/u^theta. The same inherited
real-center admissibility restrictions of RF/WR remain in force. In
particular the entire ordinary chart at V_2=I lies strictly inside the
new output domain, with a growing relative margin. Six weighted field
positions of size O(sigma_1) also fit its xi_w radius. This removes the
artificial inside-chart complement exhibited in section 14 for the old
radius choice. It does not prove that a larger physical G set is contained.

On this ordinary chart the actual second-step marked integrand is now

    K_1(V_2,U_1) P_*(U_1,J) exp[sum_Y R_Y^all(U_1,J)]
                  exp[Theta(z;U_1,J)-Theta(1;U_1,J)]. (GH63)

Its Haar integral over the chart, PLUS the original compact integral over
the chart complement, is exactly the full two-step marked density. The
same zero-source full density normalizes the actual posterior; it is
not removed from the problem. This writes the complete inherited factor
on a domain containing this consumer's chart, not a bound on its integral.

Still required: localize and estimate K_1 P_* with its actual nonlinear
critical action and determinant; control the ordinary-chart complement;
integrate the original-history marks with their full readers; and prove
stable domains, reserve/rate regeneration and the physical coupling law
at every later step. Reusing GH56 as though the input were bare Wilson
would not prove these statements. There is no all-depth, native mu+2,
continuum-existence or physical mass-gap conclusion in this section.

## 16. Convexity of the actual inherited density on the second chart

This coordinator-authored continuation awaits independent review. It concerns
the full zero-original-source density, conditioned on the ordinary second
chart, at terminal V_2=I. It does not condition on a first-step return history.
The original chart complement is still present in the full compact integral.
The new input is SAP15's already proved coarse-energy allocation, not a new
energy estimate. The action and determinant producers CA and CD are also reused.

Use two actual normalized steps on a finite torus with terminal side T>=2,
the same odd L>=3, N>=2, and kappa in its admitted positive compact interval.
Put D=N^2-1, sigma^2=N/u and lambda=u_1/u in [c_-,c_+]. Impose GH56--GH57
and all common RF/WR domain restrictions. At the second level retain the exact
rooted tree quotient, all free links and every colour. Its chart is

    Omega_1={a: max_free e ||a_e||HS<r_1},
    r_1=sqrt(N/u_1) [log(2+u_1)]^alpha, alpha>5/2,
    U_1,e=exp(a_e), with tree links I.                  (GH64)

For sufficiently large u, GH62 puts its closure strictly inside GH60's real
domain. All constants below are independent of T,u,u_1 in the stated ratio
interval; they may depend on the fixed producer domains, L,N and kappa bounds.
The first bare critical phase and precision on this domain are
`A_1(U_1)=F_0(b(U_1);U_1)` and `K_*(U_1)=F_0''(b(U_1);U_1)`.
Let `R_1(U_1)=sum_Y R_Y^all(U_1,0)`. Keep the exact GH60 identity

    rho_1(U_1,0)=C_0 exp[-A_1(U_1)/sigma^2]
                      det K_*(U_1)^(-1/2) exp[R_1(U_1)],
    C_0=h_N^(n_f) (2pi sigma^2)^(d_f/2).

Here n_f is the number of first-step free links and d_f=D n_f. With n_1 second-step
free links, define the exact coordinate phase

    Phi_2(a)=-sigma^2 log[rho_1(exp a,0) K_1(I,exp a)
                              h_N^(n_1) prod_e j_N(a_e)]
       =A_1(exp a)-sigma^2 log K_1(I,exp a)
          -sigma^2 sum_e log j_N(a_e)
          +(sigma^2/2) LogDet K_*(exp a)-sigma^2 R_1(exp a)
          -sigma^2 log[C_0 h_N^(n_1)].                 (GH65)

This includes the full first critical action, full determinant, both kernel
normalizers and both Haar conventions. Constants remain in the identity even
though their field derivatives vanish. The induced simultaneous change of
first-step variables when fixing the second tree is the exact quotient
change from section 14, with gauge volume one.

### 16.1. The cold Hessian and the moving lift

At cold data the first critical field is zero: every local first derivative
vanishes, and FU's critical branch is unique. Let v be a coarse-link variation
and a a free first-step fluctuation variation. Write `x=a+E v` for the actual
physical fine-link variation. E is the derivative of the canonical lift:
it copies v onto the relevant crossing links and is zero on internal links.
It preserves the tree slice. The exact joint second derivative is

    D^2 F_0(0;I)[(a,v),(a,v)]
       =||d_0 x||^2+kappa||Q_0 x-v||^2
          +kappa[1-c_N(kappa u)]||Z_0 x||^2
          +N^2/(6u)||a||^2.                            (GH66)

Here d_0 denotes the first-level lattice curl. Q_0 is the actual averaged
contour linearization, and
`||Z_0 x||^2=sum_c average_tau||theta_(c,tau)(x)-Q_0 x(c)||^2`.
To verify GH66, differentiate the actual normalized kernel as in
[F5--F8](SOFT_FLUCTUATION_COVARIANCE_ASTRA.md): allowing its output to vary
replaces the numerator's average `||theta||^2` by `||theta-v||^2`; the
normalizer is independent of that output. Haar invariance gives its same
`c_N` variance cancellation, with 0<c_N<1. The first Haar term is in a,
not x. Thus a moving-lift change of coordinates does not justify simply
adding a Haar diagonal in absolute fine coordinates. GH66 retains it exactly.

Let `C_F=10L^2+1920[3L(L-1)/2]^2` and
`c_S=min{1/C_F,kappa_-/120}`. Differentiating the all-compact zero-source
[SAP15](SQUARED_ALIGNMENT_PRICE_ASTRA.md) at the identity gives, for every
fine x and coarse v,

    ||d_0 x||^2+kappa||Q_0 x-v||^2 >=2c_S||d_1 v||^2.

The factor 2 follows from `E_0>=c_S sum_P ||I-V_P||HS^2/N` and
`N E_0=(||d_0 x||^2+kappa||Q_0 x-v||^2)/2+O(3)`.
Near I the maximizing mean is smooth; its quadratic alignment cost is
`||Q_0 x-v||^2/(2N)`. This also follows by minimizing the quadratic
average `||theta-v||^2` over its traceless Lie-algebra tangent variable.
The Schur formula for the stationary value and the last two nonnegative
terms of GH66 therefore prove `D^2 A_1(I)[v,v]>=2c_S||d_1 v||^2`.
Taking the infimum over a is legitimate because FU's fine Hessian is positive;
for fixed v, a ->x=a+E v is a bijection of the fine tree slice.

For the next kernel the same finite-u calculation gives at a=0
`lambda kappa(||Q_1 a||^2+[1-c_N(kappa u_1)]||Z_1 a||^2)`.
The next Haar Hessian is `N^2/(6u) I`, also positive. Put

    B_2=A_1-sigma^2 log K_1-sigma^2 sum_e log j_N,
    a_gap=1/max{4L^3(L+4)(60L^2)^2,2L^3/kappa_-},
    gamma_2=a_gap min{2c_S,c_-}>0.
    D^2 B_2(0)>=gamma_2 I.                             (GH67)

The last inequality uses F9--F12's gap for the actual tree-quotient form
`d_1^*d_1+kappa Q_1^*Q_1`. No root, winding or colour direction is removed.

### 16.2. Paying the determinant and the nonlinear remainder

Fix one common preliminary CA/CD/FU product domain about coarse center I,
with the same already chosen R and beta as GH56. Its positive analytic
radii are fixed before u. This is an analytic domain for the critical phase
and precision; it is not an assertion of GH60's integral identity outside
its narrower domain. FU uniqueness identifies the two branches on their
overlap. Choose a fixed scalar coordinate polydisc radius b>0 inside those
coarse radii and the next step's fine local-vertex radius. On the half disc,
CA13 multiplied by sigma^2 gives a uniform rooted bound C_A for A_1's
complete scalar atoms. Its exact vacuum obeys
`sigma^2 |log z_(kappa u)|<=2N kappa`, so this budget is uniform in u.
CD19 gives a uniform rooted bound C_D for all atoms of LogDet K_*.

Here is explicit volume-independent differentiation. Let n_c=4D and
`B_j(beta)=sup_(m>=1) m^j exp(-beta m)<infinity`. Each original reader
S contains at most n_c|S| coarse scalar coordinates. Cauchy estimates on
the half disc, with each coefficient supremum taken before summation, give

    max(row,col)sum_j |partial_i partial_j LogDet K_*|
         <=8 b^(-2) n_c B_1(beta) C_D=:M_D,
    max(row,col)sum_j |partial_i partial_j A_1(a)
                                      -partial_i partial_j A_1(0)|
         <=48 b^(-3) n_c^2 B_2(beta) C_A max_e||a_e||HS.

For the second line integrate the third derivative along t a, 0<=t<=1.
The two summed slots cost `(n_c|S|)^2`; the fixed i marks its owner in S.
These are absolute row and column bounds, hence operator bounds for the
real symmetric Hessians. No bound on an extensive scalar is substituted.
For the next kernel and Haar vertices the same argument uses FU's uniform
local analytic bound H, finite arity q=(8L^4+8)D and incidence
`nu<=(9L^4+5)9^4`. The scaling factor is lambda<=c_+, so their combined
third-derivative row budget is at most `48 b^(-3) nu q^2 c_+ H`, after
enlarging H to cover their exact scalar vacua. Consequently a fixed C_B gives
`||D^2 B_2(a)-D^2 B_2(0)||op<=C_B r_1` on GH64 for sufficiently large u.

For the actual all-cut R_1 use GH60's absolute field tensor norm at h=sigma,
zero source positions, and original source zero. Its budget
`E_u=C_beta sigma^2+exp(-kappa_w u^(2theta))` is at most
`(C_beta+1)sigma^2` for large u. Passing from left Lie derivatives to the
coordinates exp(a_e) uses the bounded exponential differential and its
first derivative, each acting on just one link. The second derivative
contains a two-field tensor and a same-link one-field correction. Thus,
with a fixed finite C_exp(N) absorbing the component sums,

    ||D^2 R_1(exp a)||op
        <=C_exp[2 E_u/sigma^2+E_u/sigma]<=M_R.
    D^2 Phi_2(a)
        >=[gamma_2-C_B r_1-sigma^2(M_D/2+M_R)]I
        >=(gamma_2/2)I                                  (GH68)

for all sufficiently large u, uniformly in volume. Whole-link coordinate
conversion preserves the original readers. In particular the determinant
has been estimated after its correct sigma^2 prefactor, not called small
as an unscaled logarithm. Both r_1 and sigma^2 tend to zero.

### 16.3. Actual chart-conditioned variance and simultaneous tails

Let nu_ch be the actual second posterior conditioned on Omega_1. In these
coordinates its probability density is proportional to
`1_(Omega_1) exp[-Phi_2/sigma^2]`. The normalization is the actual chart
integral of GH65. It includes rho_1; no bare replacement is made. The
Euclidean, infinite-dimension-parameter case of
[Kolesnikov--Milman, Theorem 1.2(1)](https://arxiv.org/pdf/1310.2526v7)
applies to its convex potential. For the product-ball corners, first use
the smooth convex domains
`Omega_p={sum_e (||a_e||HS/r_1)^(2p)<1}`, integer p>=1. These increase to
Omega_1 and have smooth boundary with nonnegative second fundamental form.
The phase is smooth on a neighborhood of their closures. Normalized
dominated convergence gives, for C^1 functions on the closed chart,

    Var_(nu_ch)(f)<=sigma^2 E_(nu_ch)
                      <(D^2 Phi_2)^(-1) grad f,grad f>
                 <=(2sigma^2/gamma_2) E_(nu_ch)||grad f||^2.
                                                               (GH69)

No boundary restriction on f is imposed. The cited primary theorem was read
in its smooth convex-boundary form; the exhaustion above supplies this
chart's specific boundary match. This is a finite-dimensional probability
inequality, not the physical Hamiltonian mass gap.

Global SU(N) conjugation preserves the actual model, terminal I, exact tree
slice and whole-link balls. Hence each traceless Lie-algebra coordinate has
mean zero under nu_ch. Real linear tilts preserve GH68 and the convex domain.
Applying GH69 to a linear functional under each tilt and integrating its
log moment generating function twice gives
`E exp(t<v,a>)<=exp[sigma^2 t^2||v||^2/gamma_2]`.
In particular `E||a_e||HS^2<=2D sigma^2/gamma_2`. For m distinct free
links A and any s>0, choose for each large link one of D coordinates and
its sign. The associated sum has coefficient norm sqrt(m), and is at
least ms/sqrt(D). Chernoff's inequality and the (2D)^m choices yield

    nu_ch{||a_e||HS>=s for every e in A}
        <=min{1,(2D)^m exp[-gamma_2 m s^2/(4D sigma^2)]}.  (GH70)

This supplies actual inherited chart control at two steps and terminal I.
It does not bound the full compact posterior's probability of Omega_1^c,
integrate discontinuous first-history marks with their full connected
reader norms, extend the terminal background domain, identify a physical
running coupling, or iterate the estimates uniformly in depth. Those
obligations, continuum existence and the physical mass gap remain OPEN.
