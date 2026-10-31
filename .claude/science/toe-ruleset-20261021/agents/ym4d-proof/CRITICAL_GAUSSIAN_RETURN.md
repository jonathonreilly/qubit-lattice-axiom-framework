# Centered Gaussian return at the actual joint critical covariance

Author: root coordinator. This is a new bounded interface argument, with
independent review pending. It extends the centered Gaussian cutoff to
the actual source-dependent critical Hessian by verifying its small-tail
hypotheses. It does not prove a nonlinear or original-cut return.

The producer sources are the actual finite-u
[critical field](FINITE_U_CRITICAL_FIELD_ASTRA.md), the
[lift covariance](POSITIVE_READER_COVARIANCE_ASTRA.md), and the
[complete-reader Gaussian return](READER_LOCAL_GAUSSIAN_RETURN_ASTRA.md).
The last source has a [fresh scoped review](REVIEW_READER_LOCAL_GAUSSIAN_RETURN_ASTRA.md);
its proof is used only after checking the altered covariance below.
No nonlinear or shifted-chart draft is a premise.

Full continuum existence and a positive physical continuum mass gap
remain OPEN. All constants below belong to an auxiliary Gaussian reference.

## 1. Object, parameters and complete readers

Use FU1's exact phase F_epsilon, including the finite-t normalized compact
kernel and Haar logarithm, exactly once. Keep t=kappa u real and fixed when
the original Wilson coefficients epsilon_p vary. Fix N>=2, D=N^2-1,
odd L>=3 and the admitted compact positive kappa interval. Set
m0=3L^4+1, d=D m0 T^4, sigma^2=N/u, with T>=2 and real u>=1.
No scalar, colour, root or harmonic coordinate is removed.

The domain is the original product domain
V_c=exp(v_c)Vbar_c, max ||v_c||HS<eta, |epsilon_p|<rho,
with every real center Vbar of curvature at most delta_*. Its radii will
be chosen once, independently of u and T. In every coefficient norm,
suprema on projected joint domains are inside the sums. Labels contain
all original coarse/source readers and field endpoints; a solved
critical field is not new independent data.

Let b_*=b_*(V,epsilon) be FU's small actual critical point and set

    F_epsilon'(b_*)=0, K_*=F_epsilon''(b_*), C_*=K_*^-1,
    J_*(V,epsilon)=integral product_e 1_{||x_e||HS<=p_c} dmu_(C_*)(x),
    p_c=r_a/sigma.                                           (CG1)

Here r_a>0 is a fixed auxiliary radius smaller than the admitted fine
analytic radius. The Gaussian is centered and exactly normalized:
dmu_C=(2pi)^(-d/2) exp[-Tr Log(C)/2-x^T C^-1 x/2] dx.
The matrix logarithm is on the accretive branch. These are centered
balls in x, not the translated physical chart of FU30.

## 2. Simultaneous, nonempty choices

First fix PC's constants gamma,c0,g and the RG5 principal/masked inverse
row constant v. They do not depend on the patch radius R, u or T.
The reason is the partition-of-unity envelope
sum_A chi_A(i)chi_A(j)<=1:
P=sum_A chi_A K_A^-1 chi_A has the R-independent exponential entry
envelope of RG4. Weighted conjugation by exp(theta owner-distance)
changes every principal/masked P by at most c0/2. Its inverse therefore
has the summed entrywise-supremum row/column bound v from RG6.
This uses the full colour Gram mask, not a diagonal colour replacement.

Write

    a_P=c0/g^2, b_P=1/c0,
    e_0=min(c0/8, 1/(4v), a_P/(64v^2)).                    (CG2)

For PC's p_0=exp(1)Jg and r=exp(1)C_R/R choose a fixed R>=4 so that

    r<=min(1/4, c0/(32p_0), e_0/(4p_0)),
    beta=(16R)^(-4).                                      (CG3)

This is possible because p_0,C_R,e_0 are independent of R.
Do not retain a previous, larger beta after increasing R. PC then gives

    C_lift=P+E_lift,
    M_beta(E_lift)<=p_0 r/(1-r)<=e_0/3.                   (CG4)

Retain FU11's full atom budgets m_G,b_G,A_G at this same R, including
the marked norm that may grow with R. Strengthen FU17 to

    d_target=min(gamma/4, 1/(4m_G), c0/(32m_G^2),
                                      e_0/(4m_G^2)).      (CG5)

Choose the positive field radius tau and then the positive source radius
rho to obey FU18 with D_H(tau,rho)<=d_target. These choices exist:
N'(0)=0 and D_H(0,0)=0, while all prefactors have already been fixed.
If needed tau may also be chosen below r_a/(4sqrt(D)); this extra
restriction is not used to replace the translated chart in CG1.

Finally choose positive delta_* and eta inside FU19 and PC's coarse
tube so that A_G g_*(1+rho)(delta_*+8eta)<=tau/4, along with all of
FU's original branch-identification restrictions. The positive constants
A_G and g_* can be very large; they remain finite before this last choice.
Every radius stays positive and independent of u,T. No condition
delta_V<=sigma p and no limit in u is used for this critical-point step.
The joint tube retains delta_hat=delta_*+8eta. A delta_V substitution
is only the previously proved fixed-real-V slice bound.

FU's actual contraction, including H_epsilon b in its equation, now
constructs the same branch on this smaller domain. Pointwise uniqueness
identifies it with the original FU/SA/IC branches on their overlaps;
there is no new choice of center.

## 3. Actual critical tail and the Gaussian hypotheses

With G=K^-1, Delta=K_*-K and d_H=D_H(tau,rho), use the exact ordered
resolvent series from FU25:

    T_crit=sum_(j>=1) G(-Delta G)^j, C_*=P+E_*,
    E_*=E_lift+T_crit, h=d_H m_G<=1/4.                   (CG6)

All factors are the actual finite-u, Haar and source factors.
The complete-reader products meet at each contracted scalar index;
their unions are connected and contain both endpoints. Symmetrization
of each path retains its full reader and both endpoint budgets.
The source-dependent tail is not set to zero even at a flat center.

The endpoint and marked estimates are

    M_beta(T_crit)<=m_G h/(1-h)<=e_0/3,
    B_beta(T_crit)<=b_crit:=b_G h/(1-h)
                     +m_G d_H(m_G+b_G)/(1-h)^2,
    b_lift=n_R p_0[r/(1-r)+r/(1-r)^2],
    M_beta(E_*)<=2e_0/3<=e_0,
    B_beta(E_*)<=B_*:=b_lift+b_crit<infinity.              (CG7)

The first inequality uses (1-h)^(-1)<=4/3 and CG5.
The marked bound comes from marking each factor of G(-Delta G)^j:
b_G h^j+j m_G d_H(m_G+b_G)h^(j-1). Summing the two geometric
series gives CG7. Here n_R=D m0(16R)^4, as in FU6. These fixed upper
budgets are uniform in u,T. B_* need not be small. No global operator bound
is substituted for these sums of coefficient suprema.

The positive local core P is unchanged. It still has all RG4--RG7
principal/masked bounds, finite readers H_e, |H_e|<=h_R=J(16R)^4,
and incidence J_H=m0(32R+1)^4. It does not acquire source dependence
through a new principal compression of K_*.

For the actual C_* and every principal/Gram-masked version,

    Re C_* >=(c0-e_0)I >=7c0 I/8,
    ||C_*||op<=g+e_0.                                    (CG8)

This follows first from Re P>=c0 and the two endpoint sums in CG7,
then by the full-colour Gram isometry. In particular every required
normalized Gaussian and its principal covariance marginal exists on
the same joint domain. When T<16R the lift residual is zero, but the
critical tail generally is not; CG7--CG8 still apply. No small-torus
tail is discarded.

## 4. Explicit coefficient and convergence budget

Use e_0 as a common upper bound in the Gaussian coefficient estimates.
Set

    t_E=v e_0<=1/4,
    q_E=v^2 e_0/(1-t_E)<=a_P/48,
    ell_E=-(1/2)log(1-t_E),
    A0=v/[2(1-t_E)], A2=v^2/[2(1-t_E)^2],
    c_G=2b_P^2/a_P+b_P+q_E+1,
    K_M=A0+2A2(16/a_P+1), L_G=max(1,sqrt(2 exp(1)c_G)),
    q_c=(b_P/(2pi))^(D/2) exp[D ell_E-a_P p_c^2/16]
                   max{area(S^(D-1)) p_c^(D-1),(16pi/a_P)^(D/2)},
    Q=exp(beta h_R)q_c, c_row=D(g+e_0),
    lambda=4 L_G^2 c_row Q,
    eps_*=Q[J_H+K_M B_*+4B_* L_G^2 Q]/(1-lambda).         (CG9)

These are the RG14--RG25 constants with the complete critical residual.
The numerator in eps_* separately pays a core-collar mark, a density
residual mark and a tree-residual mark. B_* already sums both scalar
endpoint colours; the D in c_row sums the first endpoint's colours.
All constants except p_c,q_c,Q,lambda,eps_* are fixed before u grows.

For clarity, the mechanism still matches the changed object. On an
active set X the density ratio to P[X,s] expands as

    exp{sum_(k>=1)(-1)^k Tr[(P[X,s]^-1 E_*[X,s])^k]/(2k)
       +sum_(k>=1)(-1)^(k-1)
         x^T(P[X,s]^-1 E_*[X,s])^k P[X,s]^-1 x/2}.        (CG10)

Its signs, full determinant and ordered exponential factorials remain.
Each E_* occurrence is an actual lift or critical reader atom. The
bounds v e_0<=1/4 and q_E<a_P/16 supply precisely the absolutely
summable row algebra and Gaussian slack used in RG12--RG20.
The empty active marginal is one, with no loops or vacuum species.
Marking an occurrence retains its entire source/coarse label and costs
B_* through the same trace or two-sided resolvent estimates.

Endpoint-pair forest differentiation uses the actual C_* entries,
including its determinant derivative. Their coefficients are constant
with respect to these mask parameters; original sources are not varied
by that forest differentiation. The RG23 tree then connects all
H_e and all attached residual readers. Exact grouping of field-compatible
families by reader overlap, followed by the connected-logarithm tree
bound, spends beta/3 twice. This is why the same calculation works:
none of its steps requires E to be source-free, finite-range or small
in its marked norm.

Choose u_0 so that for all u>=u_0,

    p_c>=1, q_c<=1, lambda<=1/2, eps_*<=beta/3.            (CG11)

Such a finite u_0 exists since p_c^2=r_a^2 u/N and all other constants
are fixed. It may be enormous; no useful numerical size is asserted.
The result is

    J_*(V,epsilon)=exp[sum_(connected original readers Y) L_Y(V_Y,epsilon_Y)],
    sup_z sum_(Y contains z) exp(mu|Y|) sup|L_Y|<=eps_*,
    mu=beta/3>0, J_*(V,epsilon)!=0.                       (CG12)

Every source and coarse reader introduced by b_* or K_* remains in Y.
The branch is defined by this absolutely convergent series and tends
to zero as u grows. This also proves joint holomorphy. Uniform positive
majorants justify every atom sum, integration and grouping on the
projected domains. The threshold and bound are uniform in T.

## 5. Original-source derivatives and the physical boundary

Fix original source coordinates p1,...,pm, permitting repetitions.
On the inner source polydisc max |epsilon_p|<rho/2, coefficientwise
Cauchy on the full polydisc gives

    sup_z sum_(Y contains z) exp(mu|Y|)
       sup |partial_(p1)...partial_(pm) L_Y|
           <=m!(2/rho)^m eps_*.                          (CG13)

For a repeated coordinate the Cauchy factorial is its multiplicity
factorial; the product of those factorials is at most m!.
Each coefficient is independent of source variables outside its actual
reader, so those derivatives vanish. The coefficientwise upper bounds
are summed only afterward; there is no exchange of sup and sum.
This is a source-jet estimate for this Gaussian cutoff factor alone.

The exact real original-chart identity remains FU30:

    Z_a=h_N^(m0 T^4)(2pi sigma^2)^(d/2)det(K_*)^(-1/2)
          exp[-F_epsilon(b_*)/sigma^2]
          integral_((D_a-b_*)/sigma) dmu_(C_*)(x) exp[-R_*(x)]. (CG14)

Neither the translated domain nor exp(-R_*) was removed in deriving that
identity. CG12 concerns the separately defined centered Gaussian CG1.
It does not cancel the critical action or determinant in CG14, prove
the shifted-boundary or nonlinear estimates, normalize an unchanged
history, or establish the original-cut complement or next-scale law.
Those interfaces still need their own proofs and common constants.

Bałaban's constructions and Dimock's expositions provide the constructive
background. The normalized-marginal and reader-regrouping methods are
credited to the locally rebuilt RG/BF development and Martin Lohmann,
[arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1).
No external theorem is imported by that citation. This interface uses
the displayed producer estimates, not a new physical axiom or a numerical
experiment. Independent review of CG1--CG14 is required before adoption.
