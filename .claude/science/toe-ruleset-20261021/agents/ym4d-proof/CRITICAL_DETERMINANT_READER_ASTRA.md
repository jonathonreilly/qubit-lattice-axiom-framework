# The full critical determinant on the joint original-reader domain

This is a narrow continuation of the determinant construction already in
SA9/SA14 and IC section 3. Those sources already localize the **complete**
actual finite-u determinant, respectively for real coarse data with complex
sources and for complex coarse data without sources. The result here checks
that construction on FU's joint coarse/source domain, with connected readers
and coefficient suprema in **original coarse-block units**. It supplies a
uniform per-block budget for the determinant retained outside NRR37. It does
not discover a new determinant mechanism or a small full determinant.

The source is an author proposition awaiting fresh independent review.
Four-dimensional continuum existence and a positive physical continuum mass
gap remain **OPEN**. All statements are for the specified bare one-step model.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Checked joint-domain, original-block continuation of the existing full finite-u determinant expansion, with an explicit critical-Hessian correction."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Existing producers and the exact remaining match

| Inspected source | Existing result | Match required here |
|---|---|---|
| [Residual determinant](RESIDUAL_DETERMINANT_ASTRA.md), sections 1 and 3; [full-colour residual](RESIDUAL_FULL_COLOUR_ASTRA.md), opening and section 3.1 | Regulated Schur/gauge identities and a grouped perturbative residual coefficient, with their stated depth and limit conventions | These are different determinant objects; no full finite-u joint-domain reader norm for the present critical precision is inferred |
| [SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), SA5--SA14 | Principal-patch inverse atoms, the full lift determinant homotopy SA9, and its critical ratio; actual finite-u phase with complex original Wilson sources | V is real in SA's admitted curvature class, and the displayed support weights are in R-box units |
| [IC](INTERACTING_SELECTED_CORE_ASTRA.md), IC6--IC13 and the following determinant paragraph | Complex-coarse continuation of the same full determinant construction, including the critical ratio | Source-free; its support rate is also specified in R-box units |
| [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md), FU1--FU26 | Actual joint critical field, lift inverse and complete-reader critical Hessian perturbation at beta=(16R)^(-4) in original blocks | The full extensive scalar determinant family is not explicitly constructed there |
| [RD3](RD3.md), D24--D26; [RD4](RD4.md), I3 and its dictionary | Exact prefactor accounting; an actual uniform full log-determinant/source-support budget is an outstanding producer input | Only the present bare one-step Hessian is supplied below; inherited actions, histories and the full return remain separate |

The [reviewed NRR theorem](NONLINEAR_READER_RETURN_ASTRA.md) supplies a
small logarithm of its normalized centered nonlinear expectation. Its active
marginal loops do not include the full extensive determinant in NRR37.
The present argument reuses the finite homotopy of SA/IC and rebuilds its
matrix estimates at FU's actual joint domain and original-block rate.
Neither a larger box rate nor an arbitrary prescribed original-block rate
is silently transferred. The full supplied action and kernel remain premises;
no new physical axiom, empirical input or observable identification is added.

## 2. Actual phase, common domain, and one fixed patch scale

Fix N>=2, D=N^2-1, odd L>=3, T>=2, real u>=1 and kappa in its admitted
positive compact interval. Write

    m0=3L^4+1, n=m0 T^4, n0=Dm0, d=n0 T^4, sigma^2=N/u.

Use FU's rooted tree coordinates, with all n free links and d scalar colour
coordinates, including crossing, root and harmonic directions. The integrated
tree gauge volume and Jacobian are one. In the original left chart the exact
phase, lift Hessian and critical Hessian are

    F_epsilon=F_0+sum_p epsilon_p W_p,
    F_0=sigma^2[-log w_0(U(a),V)-sum_free e log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2,
    K=F_0''(0;V), b=b_*(V,epsilon), F_epsilon'(b)=0,
    K_*=F_epsilon''(b;V)=K+Delta.                         (CD1)

Only original Wilson coefficients vary. The compact kernel parameter t=kappa u
is fixed real at each u. Its finite-t normalizer, the nonnegative finite-u
spread term and the Haar logarithm remain in F_0. Negative complex edges use
inverses, not conjugates. The constant h_N is outside F_0. The tree phase is
not used as a substitute for this phase or its Hessians.

Here are the actual uniform constants from FU2--FU5:

    a_gap=1/max(4L^3(L+4)(60L^2)^2,2L^3/kappa_-),
    gamma=a_gap/2, delta0=min(1/24,a_gap/48),
    B=25+24kappa_+(5L)^2+N^2/6, b_row=D B,
    c=B, c0=1/(2B), r0=8,
    b_c=b_row+gamma/4, m=(1/8)log(1+gamma/(4b_c)),
    g_inv=(2n0/gamma)coth(m/4)^4,
    vK=n0*5^4, b_abs=vK*(B+gamma/4).                      (CD2)

For real curvature delta_V<=delta0, gamma I<=K<=B I; the scalar row and
column bounds are b_row, the field range is two in coarse sup distance,
and its original-data read stencil has radius three. All compressions retain
every colour. FU's explicit form is
`K=H_V+E_V+kappa(1-c_N(kappa u))B_V+N^2/(6u)I`, with H_V>=a_gap I,
B_V>=0 and the actual Wilson curvature error. No term has been deleted.

Take the same independent joint product domain as FU:

    V_c=exp(v_c)Vbar_c, max_c||v_c||HS<eta,
    |epsilon_p|<rho, delta_(Vbar)<=delta_*.               (CD3)

FU's local analytic vertex bound H on a scalar fine-coordinate polydisc of
radius a and its coarse derivative bound J0 are uniform in u,T. In particular
`max(row,col)||K(V)-K(Vbar)||<=J0 eta`. Restrict the preliminary eta below
FU's radii and gamma/(4J0). The Hermitian part of every K_A is then at least
3gamma/4. This is a perturbation bound; complex matrices are not called
positive. Joint suprema retain delta_hat=delta_*+8eta. A replacement by the
actual delta_V is allowed only on a fixed real-V slice.

Use one geometry-only cover throughout. Choose R>=4. For T<16R use a single
whole-torus patch. Otherwise partition each periodic direction into intervals
of lengths R to 2R. For each product box Q use FU's nonnegative cutoffs chi_Q
with sum_Q chi_Q^2=1, support inside N_(R+1)(Q), and Lipschitz constant
C_chi/R. Their principal patches and full readers are

    A_Q=N_(2R)(Q), S_Q=N_(2R+4)(Q),
    J=16^4, s_R=(16R)^4, n_R=n0 s_R,
    C_chi=16(1+sqrt(2J)), beta=1/s_R, w=exp(1),
    p=w J g_inv,
    r=w(2J C_chi r0 b_abs g_inv)/R.                      (CD4)

Every S_Q is connected, |S_Q|<=s_R, and at most J labels contain a fixed
cell. The collars contain both endpoints of every original coarse-link datum
read by a matrix coefficient. The cutoffs vanish before the principal-patch
boundary by more than K's range. For the small torus chi=1 and its cardinality
is <s_R; this retains a bounded cost for all modes. Periodic coincidences only
reduce these counts. None of the choices depends on V, epsilon or u.

Choose R once so

    r<=min(1/4,c0/(32p)).                                (CD5)

Both p and the numerator of r are R-independent, so this choice is possible.
For composition with NRR take its more restrictive NR6 choice of R; no later
enlargement is needed for this determinant argument. The output beta is then
recomputed from that R and never held at its former value while R grows.

For matrix atoms A_(ij;S), define M_beta as the maximum weighted absolute row
and column sum and B_beta as the weighted sum of all scalar entries through
a marked reader cell, maximized over the cell. Weights are exp(beta|S|), with
the suprema of individual coefficients on CD3 **inside** all sums. Labels
contain both field endpoints and every original coefficient reader. Then

    M_beta(AB)<=M_beta(A)M_beta(B),
    B_beta(AB)<=B_beta(A)M_beta(B)+M_beta(A)B_beta(B).      (CD6)

Products sum over the actual scalar intermediate index. Adjacent labels
meet there, so their union is connected. Marking a product in either factor
proves CD6; marking the second requires the column bound of the first.
No operator norm is substituted for an absolute reader-atom sum.

## 3. Uniform finite homotopy on the same patches

For 0<=theta<=1 put

    K_theta=(1-theta)cI+theta K.                          (CD7)

At real data gamma I<=K_theta<=B I because c=B>=gamma. On CD3 it is
accretive by 3gamma/4 and has scalar row/column bound <=b_c. It has the same
range and readers as K, and its entrywise supremum envelope costs at most
b_abs. In particular the supremum over theta introduces no new volume or
reader factor.

For any principal patch A, conjugate K_theta,A by the scalar diagonal weight
exp(m d_1(X_i,X_j0)), with a fixed column owner X_j0. The two absolute endpoint
sums of the change are bounded by
`(exp(m r0)-1)b_c=gamma/4`. Cauchy--Schwarz bounds its operator norm by the
geometric mean of those endpoint sums. The original inverse has norm at most
4/(3gamma); after conjugation the inverse norm is at most 2/gamma. Undoing
the weight gives, uniformly in theta and CD3,

    sup |K_theta,A^-1(i,j)|
                  <=(2/gamma)exp[-m d_1(X_i,X_j)],
    max(row,col)sum_j sup |K_theta,A^-1(i,j)|<=g_inv.      (CD8)

The torus-distance sum is bounded by the Z^4 sum, with n0 scalar modes per
cell. The slightly weakened coth(m/4)^4 is a uniform upper bound. This is
also a sum-of-entrywise-suprema estimate; a pointwise matrix norm alone
would not justify it.

Zero-extend each principal inverse G_theta,A and define

    P_theta,A=chi_A G_theta,A chi_A, P_theta=sum_A P_theta,A,
    R_theta,A=-[K_theta,chi_A]G_theta,A chi_A,
    R_theta=sum_A R_theta,A.                             (CD9)

Because chi_A vanishes before the boundary, zero extension gives exactly
`chi_A K_theta G_theta,A chi_A=chi_A^2`. Expanding the commutator yields

    K_theta P_theta=I-R_theta,
    K_theta^-1=P_theta sum_(j>=0)R_theta^j.              (CD10)

This fixes both the sign and the order. Boundary entries are included.
Moreover `[K_theta,chi_A]=theta[K,chi_A]`; the constant diagonal adds no
commutator. Both displayed local components read only S_A.

For a residual row, at most 2J cutoffs meet a neighboring pair, the difference
of each cutoff is at most C_chi r0/R, the K endpoint sum costs b_abs and the
inverse endpoint sum costs g_inv. For a residual column restrict first to the
at most J final cutoffs, then sum the K and inverse columns in that order.
A marked sum has at most J patches and at most n_R rows per patch. Therefore

    M_beta(P_theta)<=p, B_beta(P_theta)<=n_R p,
    M_beta(R_theta)<=r, B_beta(R_theta)<=n_R r,
    M_beta(K_theta^-1)<=m_h:=p/(1-r),
    B_beta(K_theta^-1)<=b_h:=n_R p/(1-r)^2.               (CD11)

The last marked bound is the sum of
`n_R p r^j+j n_R p r^j`, from marking P or one of the j residual factors.
All constants are uniform in theta; all complete-reader path labels survive.
For the one-patch small torus R_theta=0. These formulas are holomorphic in
the original coarse data, agree on overlapping center charts, and have
uniformly convergent coefficient families. No critical-field-dependent patch
inverse is used: K_theta is built from the **local lift** matrix K.

## 4. Full lift determinant and its extensive budget

For a scalar family l_S define

    ||l||_beta=sup_x sum_(S containing x)exp(beta|S|)sup|l_S|.

A diagonal trace is a subsum of B_beta, since it sums all scalar i with their
actual labels. It costs no additional volume or colour factor.

Here is an explicit local family for L=K-cI. Assign each ordered nonzero
K_ij the connected label
`S_ij=N_3(X_i) union N_3(X_j)`. Its two neighborhoods meet because K's range
is at most two. The label contains the actual radius-three entry readers,
is contained in N_5(X_i), and has size at most s_K=11^4. Assign each -c
scalar diagonal to its singleton owner. These safe endpoint/read collars
retain any unused local variables without changing the coefficient. Thus

    M_beta(L)<=a_K:=exp(beta s_K)(b_abs+c),
    B_beta(L)<=b_K:=n0*11^4*a_K.                         (CD12)

Indeed a marked label forces its row owner within five cells of the mark;
there are at most n0*11^4 such scalar rows. This proof uses actual support
cardinality and local incidence, not a diameter-to-cardinality conversion.

Define LogDet K to mean Tr log K on the accretive matrix branch, real at
positive real data. It is not the principal scalar logarithm of det K, which
can wrap when d is large. Jacobi's finite determinant identity gives

    LogDet K=d log c+integral_0^1 Tr[K_theta^-1 L]dtheta.
                                                                  (CD13)

For completeness, differentiate the finite determinant by multilinearity
in its columns to obtain `(det A)'=det A Tr(A^-1 A')`. Starting at cI
and integrating gives CD13; exponentiating yields det K. Since the entire
path is accretive, its continuous logarithm agrees with Tr log K: triangularize
K and apply the scalar logarithm to each diagonal entry of K_theta, whose
segment stays in the right half-plane. This also fixes the square-root
determinant branch without a volume-dependent disc.

Insert the complete CD10 families and the local CD12 entries into CD13.
For every nonzero trace word the endpoint indices close; adjacent reader
labels intersect. Integrate each coefficient over theta, retaining its
whole union label. CD6/CD11 allow absolute uniform integration. Assign the
constant n0 log c to each singleton coarse cell. This constructs

    LogDet K=sum_(connected S) l_S^lift(V_S),
    ||l^lift||_beta<=C_lift:=n0 exp(beta)|log c|
                                      +b_h a_K+m_h b_K.  (CD14)

All coefficients depend only on the stated original coarse data and are
holomorphic on their projected CD3 domain. This is a uniform per-block
bound, independent of u,T, and generally large. It does not assert a small
total determinant or a small determinant density.

The finite homotopy is the already used SA/IC mechanism. The alternative
improper integral for Tr log K would require subtracting its diagonal
1/(1+s) contribution before absolute values; bounding the resolvent alone
would integrate 1/s and fail. No such divergent bound or unproved uniform
resolvent integral is used here. This is a rejected estimate, not a failed
experiment and not an obstruction to the present finite homotopy.

## 5. Recomputed FU domain and the complete critical correction

The field and source radii must pay the fixed R just chosen. To make that
requirement explicit, use FU's positive-core inverse family at this R. Put

    d_core=p+w J c0, e_lift=p r/(1-r),
    b_lift=n_R p[r/(1-r)+r/(1-r)^2],
    m_G=c0 exp(beta)+d_core+e_lift,
    b_G=n0 c0 exp(beta)+n_R d_core+b_lift, A_G=m_G+b_G.
                                                                  (CD15)

These are FU10--FU11's actual M_beta(G), B_beta(G), Q_beta(G) bounds for
G=K^-1. They need not equal the homotopy family's bounds m_h,b_h; both are
valid families for the same matrix at theta=1. A_G is finite and may be very
large. It is not an uncharged constant in the critical-field construction.

For reference, the complete local majorants to be paid are

    q=(8L^4+8)D, s0=9^4, d0=(9L^4+5)9^4, d1=q d0, d2=q^2 d0,
    f(t)=H(1-t/a)^(-q), S(t)=f'(t)-f'(0)-t f''(0),
    N(t)=d1 exp(beta s0)[S(t)+t S'(t)],
    B_src=2d2 exp(beta s0)f''(0),
    D_H(t,rho)=2d2 exp(beta s0){f''(t)-f''(0)+t f'''(t)
                                    +rho[f''(t)+t f'''(t)]},
    g_*=4sqrt(N)d1 exp(beta s0),
    d_*=min(gamma/4,1/(4m_G),c0/(32m_G^2)).               (CD16)

Choose tau and then rho positive so tau<min(a/8,r_CB/(4sqrt(D))),
`A_G[rho B_src+(1+rho)N'(tau)]<=1/4` and D_H(tau,rho)<=d_*.
Retain rho below FU's admitted source radii. Choose positive
`delta_*<=min(delta0,delta_CB,delta_A)` and eta last, inside all FU/CB
preliminary bounds and eta_PC, so
`delta_hat<=min(delta_CB/2,delta_A)` and
`A_G g_*(1+rho)delta_hat<=tau/4`. These are nonempty choices because
N'(0)=D_H(0,0)=0. They are fixed before u and T. For NRR composition retain
also NR6's stricter d_H cap and all of its later chart restrictions; shrinking
the final domain preserves every bound here. No fixed-radius claim is made
before the R-dependent marked constants are paid.

FU20's actual map is
`a -> -G[g+H_epsilon a+N_0(a)+N_epsilon(a)]`, including the source-linear
Hessian H_epsilon a. It contracts by at most 1/4 under CD16, gives the actual
b in CD1, and its local Taylor composition gives

    Q_beta(Delta)<=d_H:=D_H(tau,rho)<=d_*,
    Delta=F_epsilon''(b)-K.                              (CD17)

This is FU's proved actual finite-t/Haar/source perturbation, not a new
critical point construction. Each Delta atom includes its two field
endpoints, the original local vertex and source, and every substituted
critical-field reader. In particular K_* is local in its field indices
but generally nonlocal in original data. Replacing K_A by a principal
compression of K_* in section 3 would lose the proved patch locality.

Let X=G Delta, h=m_G d_H<=1/4 and b_X=(m_G+b_G)d_H. CD6 gives M_beta(X)<=h
and B_beta(X)<=b_X. Its ordered trace series yields

    LogDet K_*-LogDet K
       =Tr log(I+G Delta)
       =sum_(j>=1)(-1)^(j+1)Tr[(G Delta)^j]/j
       =sum_(connected S) l_S^crit(V_S,epsilon_S),
    ||l^crit||_beta<=C_crit:=b_X/(1-h).                 (CD18)

Indeed B_beta(X^j)<=j b_X h^(j-1); the trace's 1/j cancels that marking
count, and its geometric sum gives CD18. Both the G marks and the Delta
marks have been paid. Every closed path and every scalar colour remains.
Absolute convergence proves joint holomorphy and original-reader locality.

There is no unproved noncommuting logarithm identity in CD18. Along
K+tDelta, 0<=t<=1, accretivity is at least gamma/2, since the lift bound is
3gamma/4 and d_H<=gamma/4. Its logarithmic derivative is
`Tr[(I+tG Delta)^-1 G Delta]`. Expanding this inverse and integrating t
proves the displayed trace series. It starts at the CD13 branch, so its
exponential is exactly det K_*/det K. The accretive matrices form a convex
set: the path through K and the direct cI-to-K_* path are homotopic there,
with no determinant zero. Their lifted logarithms agree, so no branch
constant is suppressed.

Combining CD14 and CD18 proves the bounded conclusion

    LogDet K_*=sum_(connected S) l_S,
    ||l||_beta<=C_lift+C_crit,
    det K_*^(-1/2)=exp[-(1/2)sum_S l_S],                 (CD19)

with C_crit explicitly small when the already paid Hessian budget is made
small. That is a domain-dependent relative correction to the full lift
determinant. Neither term is claimed O(1/u). At flat real coarse data the
critical field is zero, but complex original Wilson sources can still
change its Hessian. On curved zero-source data the critical shift can
also change the Hessian. No vacuum/source cancellation follows.

## 6. Literal consumer placement and limits

For the centered contour of NRR, with the same fixed R and any common
restricted domain just described, the exact normalization remains

    Z_cent=h_N^n(2pi sigma^2)^(d/2)
       exp[-F_epsilon(b)/sigma^2-(1/2)sum_S l_S]
       exp[sum_Y H_Y].                                  (CD20)

This is NRR37 with its full determinant localized. The determinant's
rooted budget is (C_lift+C_crit)/2 at beta. NRR's small nonlinear log has
its own beta/2 rate and O(sigma^2)+exp(-c/sigma^2) bound; restricting CD19
to that smaller rate costs nothing. The critical action, scalar Gaussian
scale and h_N constants are separate. In particular log sigma has its
actual u dependence, the compact normalizer remains in F, and all d modes
remain in the determinant. No action/one-loop/normalizer cancellation is
asserted by this organization.

CD19 supplies the determinant row of RD3's accounting only when its Q is
this precise actual bare-step K_* on the matching chart and joint domain.
It supplies no determinant theorem for a history-dependent inherited
precision. It does not match RD's existing two-unit support expenditure,
prove a beta-function coefficient, identify effective-level dynamics,
transport hard histories, price original-cut complements, sum shifted
contour sides, or provide a multiscale induction. The full continuum
existence and physical mass-gap objectives remain open.

Bałaban's constructions and Dimock's expositions are the architectural
antecedents; SA/IC's finite homotopy is credited and reused. Every additional
norm/domain match needed here is displayed above. No new external theorem
is imported by citation, and no numerical experiment is needed. The source
is frozen before its compact identity/read packet. That packet checks
provenance, not mathematics. The coordinator owns PR #10114, Git, fronts,
review dispatch, preservation and audit gates; this author assigns neither
an independent LAND nor a retained grade. Requested Astra/max is dispatch
metadata, not independent backend attestation.
