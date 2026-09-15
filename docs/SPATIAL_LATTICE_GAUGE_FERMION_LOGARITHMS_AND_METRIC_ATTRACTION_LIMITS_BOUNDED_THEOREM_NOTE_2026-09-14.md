# Spatial-lattice gauge–fermion logarithms and metric-attraction limits

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author proposal; actual source status is conditional-support. Independent
scientific review is pending. This note proves statements about specified
one-loop integrals and their displayed truncated flow equations. It does not
prove a nonperturbative gauge phase or an independently retained TOE result.

For a supplied continuous-time, nearest-neighbor spatial carrier, the actual
Peierls vertices and gauge tensor give a logarithmic fermion/photon response
with an integrable lattice remainder. A full tensor calculation identifies
relative metric and photon polarization modes that a shared-speed ansatz
misses. Running charge makes their contraction logarithmic, while a supplied
massive comparator has only a finite remaining polarization flow below its
charged threshold. The finite matching constants remain undetermined.

**Runner:** [self-contained primary](../scripts/spatial_lattice_gauge_fermion_logarithms_and_metric_attraction_limits_2026_09_14.py).
**Receipt:** [canonical execution cache](../logs/runner-cache/spatial_lattice_gauge_fermion_logarithms_and_metric_attraction_limits_2026_09_14.txt).
**Review:** [historical author review packet](work_history/repo/review_feedback/pr8111-lattice-metric-evidence/pr8111-REVIEW_HISTORY.md); the [preserved evidence](work_history/repo/review_feedback/pr8111-lattice-metric-evidence/README.md) records its original execution and reading limits.

## Precise claim and premises

| Supplied input | Proved implication | Limit |
|---|---|---|
| Noncompact quadratic gauge action and normal Peierls fermions below | Exact vertices, Ward cancellation, leading one-loop two-point logarithms | No compact or finite-payload phase follows |
| Fixed positive speeds and four separated simple Weyl nodes | Continuum-cone coefficient with a bounded infrared remainder | Constants need not remain uniform at node merger |
| Small parity-even marginal frame and photon-tensor deformations | Linearized tensor response and weighted multi-cone flow | General perturbations are an effective-sector probe; their microscopic realization is separate |
| Positive running charge and nonzero charges on the active species | Contraction of relative metric modes in the displayed massless ODE | Common metric is free; neutral disconnected sectors do not align by this mechanism |
| Separately supplied massive Dirac comparator | Low-momentum polarization and finite threshold integral | No mass generation in the normal carrier is inferred |

All premises, derivations and live code are in this pair. Earlier campaign
PRs and current-main velocity notes are context only. The approved kinetic-
isotropy primitive supplies its stated OS0 normalization; it does not select
this Hamiltonian or supply cross-sector dynamical metric protection. No axiom,
primitive, observed coupling, physical mass or empirical scale is added.

The characteristic speeds used below are the spatial/temporal coefficients
of the renormalized local one-loop two-point action. They are not exact
charged-particle pole speeds, microscopic signal-front speeds or a proved
interacting spectral threshold. This distinction is part of the claim.

## Supplied lattice action and actual gauge inverse

Set lattice spacing one, c>0 and e>=0. The noncompact quadratic gauge action is
S_g = 1/2 integral [sum_i E_i^2 + c^2 sum_{i<j} F_ij^2],
E_i=partial_tau A_i - nabla_i A_0, F_ij=nabla_i A_j-nabla_j A_i.
Link-midpoint Fourier variables give qhat_i=2 sin(q_i/2),
Q=omega^2+c^2 qhat^2. In the gauge-fixing term
(partial_tau A_0+c^2 div A)^2/(2 c^2 xi), the true inverse is

D_mn(xi)=diag(c^2,1,1,1)_mn/Q
         +(xi-1)c^2 k_m k_n/Q^2, k=(omega,qhat).

At xi=1 it is diagonal. For positive xi and nonzero k it inverts the
positive gauge-fixed quadratic matrix; it is not a scalar denominator
inserted into an unrelated tensor ansatz. The quadratic matrix and its
verification are given below.

A convenient two-component finite-range symbol is
h_0(k)=v[sin k_x sigma_1+sin k_y sigma_2
 +(2+zeta-cos k_x-cos k_y-cos k_z)/sqrt(1-zeta^2) sigma_3],
0<zeta<1, v>0. Define h_+(k)=h_0(k-b xhat),
h_-(k)=h_+(-k)^*, 0<b<pi; charges +e,-e, separately conserved
normal particle numbers, half filling. This is supplied model data.
All four nodes are (plus/minus b,0,plus/minus arccos zeta),
with local metric v^2 I, and each charge sector has two opposite chiralities.
Thus the parity-even long-wavelength polarization has four Weyl cones, or
N_D=2 four-component Dirac species, not four Dirac species. Opposite charge
signs square in the vacuum polarization. The anisotropic sigma_3 multiplier
is explicitly chosen to equalize the free cone speeds; it is not derived.

Peierls coupling every hopping gives the exact midpoint Ward identity:
qhat_j partial_j h(k) summed over j = h(k+q/2)-h(k-q/2),
with the temporal i omega identity added for D=i omega+h.
The action vertex is -e W, W_0=i I and W_j=partial_j h; thus
q.W=D(k+q/2)-D(k-q/2). This convention is used by the lattice checks.
The same expansion supplies the two-photon single-link vertex. Its omission
would invalidate the full lattice polarization Ward identity.

The sites are Z^3; A_0 is a site field, A_i is an oriented-link field, and time
is continuous. With the stated two charge sectors, the fermion action is

    S_f=sum_s integral bar(psi_s) [partial_tau-i q_s e A_0
                                  +h_s[exp(-i q_s e A)]] psi_s,
    q_+=1, q_-=-1.

This specifies the coupling as well as the free denominators. The reference
fermion state is the half-filled free sea. The gauge covariance is expanded
about the supplied noncompact Gaussian action, with fixed xi>0 and the
measure-zero constant gauge mode omitted. There is no state-selection theorem.

At a midpoint mode write k=(omega,qhat), Q=omega^2+c^2 qhat^2. The ungauged
quadratic matrix has blocks

    M00=qhat^2, M0i=-omega qhat_i,
    Mij=Q delta_ij-c^2 qhat_i qhat_j.

Adding rr^T/(c^2 xi), r=(omega,c^2 qhat), gives the positive gauge-fixed
matrix. Multiplication by the displayed D(xi) gives the identity. This also
checks the temporal numerator c^2 and the longitudinal tensor normalization.

A zero of h_+ requires shifted k_x and k_y each to be 0 or pi. The required
cos k_z is then zeta, 2+zeta or 4+zeta. Only the first lies in [-1,1], giving
the two stated plus nodes. Conjugation gives the two minus nodes. At each
node the Jacobian is v times an orthogonal matrix, with opposite determinant
signs at the two z nodes. The two-component parity-even loop trace is half
of the four-component Dirac trace; this fixes N_D=2 for the four cones.
The occupied-band Berry curvatures obey F_-(k)=-F_+(-k), so their equal-filling
charge-squared Hall contributions cancel. This free cancellation is separate
from a theorem excluding all relevant perturbations or spontaneous pairing.

## Complete one-loop objects and exact lattice Ward cancellation

Let S(k)=[i omega+h(k)]^(-1), W_0=i I and W_j(k)=partial_j h(k).
For one species, the correction R_f to the inverse fermion propagator is

    R_f(p)=-q_s^2 e^2 integral W_mu(p-q/2) S(p-q)
                                 W_nu(p-q/2) D_mu,nu(q)
           +(q_s^2 e^2/2) sum_j integral partial_j^2 h(p) D_jj(q).

Temporal vertices are constant; the displayed midpoint argument on W refers
to spatial momentum. The integration is over continuous frequency and one
spatial Brillouin zone with measure d omega d^3 k/(2 pi)^4. The second term
is the fermion contact contribution from the same Peierls exponential.

The photon bubble and contact tensor are

    Pi_mu,nu(p)=sum_s q_s^2 e^2 integral tr[W_mu(k+p/2) S(k+p)
                                          W_nu(k+p/2) S(k)]
       -delta_mu,nu 1_(mu spatial) sum_s q_s^2 e^2
                                    integral tr[S(k) partial_mu^2 h(k)].

Contract the bubble with (p_0,phat), use p.W=D(k+p)-D(k), and shift its
periodic spatial/continuous frequency integration variables. The remaining
spatial vertex difference is

    W_nu(k+p/2)-W_nu(k-p/2)=phat_nu partial_nu^2 h(k).

It is precisely canceled by the contact term. The temporal difference is
zero because W_0 is constant. Thus (p_0,phat)_mu Pi_mu,nu(p)=0. The traces
needed here are integrable at large frequency; the possible leading contact
trace vanishes because the hopping symbol is traceless. A finite cutoff shell
alone need not preserve the finite part of this identity; the complete tensor
does. The runner checks static torus modes and nonzero temporal transfer.

## Fermion and photon logarithmic coefficients

For one Dirac cone pair, use D_f(p)=i gamma_0 p_0+i v gamma_i p_i,
vertices gamma_0 and v gamma_i. The xi=1 gauge contractions weight the
temporal vertex by c^2 and the three spatial ones by one.
Feynman parameter x on the fermion denominator yields
V_x^2=x v^2+(1-x)c^2. The shifted numerator has temporal weight
(1-x)p_0 and spatial weight v c^2(1-x)p_i/V_x^2.
A four-dimensional radial logarithm is 1/(8 pi^2) log(Lambda/mu).

I_3 = integral_0^1 (1-x)/V_x^3 dx = 2/[c(c+v)^2],
I_5 = integral_0^1 (1-x)/V_x^5 dx
    = 2(2c+v)/[3 c^3 v(c+v)^2].

Clifford contraction gives temporal numerator c^2-3v^2 and spatial
numerator -(c^2+v^2). Expansion of the inverse averaged propagator fixes
the sign: delta D=e^2 integral Gamma S Gamma D_g, with S=-i slash p/p^2.
Consequently the coefficients in the inverse fermion propagator are

A_t=e^2(3v^2-c^2) I_3/(8 pi^2),
A_s=e^2(c^2+v^2)c^2 I_5/(8 pi^2).

The speed is the spatial/temporal coefficient ratio, so for
ell=log(Lambda/mu),

 dv/dell = v(A_s-A_t)
 = e^2(c-v)(4v^2+3vc+c^2)/[6 pi^2 c(v+c)^2].

The individual wavefunction factors are gauge dependent. For the longitudinal
part use i q.Gamma=D_f(p)-D_f(p-q). The linear logarithm from
[D_p-D_{p-q}] S_{p-q} [D_p-D_{p-q}]
is proportional to D_p itself, since its linear part is -D_p after angular
integration; the quadratic external-D term gives no linear UV logarithm.
Thus it cancels from A_s-A_t. The exact lattice reduction below supplies the
sign and regulator check.

For the photon, rescale spatial loop momentum by v and spatial gauge fields
by v. In the rescaled field-index basis, the transverse Dirac trace and
Feynman-parameter integral derived below give the parity-even logarithm
N_D e^2/(6 pi^2 v^3) times (P^2 delta_ab-P_a P_b), P=(p_0,v p).
The original-field tensor includes external factors V_mu,a V_nu,b, where
V=diag(1,v,v,v); these factors are required in extracting the coefficients.
Thus the electric coefficient changes by
 B_E=N_D e^2/(6 pi^2 v),
and the absolute magnetic coefficient c^2 changes by
 B_B=N_D e^2 v/(6 pi^2).
After electric normalization,

 dc/dell=N_D e^2(v^2-c^2)/(12 pi^2 v c),
 de/dell=-N_D e^3/(12 pi^2 v).

The charge Ward identity matches the temporal vertex and fermion field
normalization, leaving e_eff=e/sqrt(Z_E). Thus the displayed charge equation
follows from B_E. These are one-loop residues, not an all-orders phase proof.

For completeness, substitute u=sqrt(c^2+x(v^2-c^2)) into I_3 and I_5 when
v differs from c. Their primitives are respectively

    [-2u-2v^2/u]/(v^2-c^2)^2,
    [2/u-2v^2/(3u^3)]/(v^2-c^2)^2.

Evaluation from u=c to u=v gives the stated rational expressions. At v=c
the direct integrals give 1/(2c^3) and 1/(2c^5), agreeing continuously.
A separate spatial-radial shell integration has frequency integrals

    integral_R (v^2-t^2)/[(t^2+v^2)^2(t^2+c^2)] dt
        =pi/[c(c+v)^2],
    integral_R (t^2+v^2/3)/[(t^2+v^2)^2(t^2+c^2)] dt
        =pi(2c+v)/[3cv(c+v)^2].

These supply an independent normalization check on both fermion residues.

For the photon, the four-gamma trace, a Feynman parameter and a shift of the
loop variable give the transverse scalar factor before radial integration

    8 N_D e^2 integral_0^1 x(1-x) dx
       integral d^4 l/(2 pi)^4 [l^2+x(1-x)P^2]^(-2).

The coefficient of log(Lambda/|P|) is N_D e^2/(6 pi^2), since
integral x(1-x) dx=1/6 and the radial logarithm is 1/(8 pi^2).
The momentum/field rescaling by v contributes the Jacobian v^-3 and the
external vertex factors diag(1,v,v,v). Equivalently F'_0i=v F_0i and
F'_ij=v^2 F_ij; hence the electric and magnetic coefficients are B_E and B_B
above. This derivation fixes the factor of two between a Weyl and Dirac cone.

## Longitudinal reduction and gauge independence of the logarithm

Use lattice D=i omega+h, with internal momentum (omega,K-q), external
frequency zero and bare cone h(K)=0. The exchanged photon has frequency
-omega. Its contracted vertex is
 X=-i omega I+sum_j qhat_j partial_j h(K-q/2)
  =D_external-D_internal=-D_internal.

For external derivative a, let d0=partial_a D_external and
di=partial_a D_internal. Then X'=d0-di, S'=-S di S. Direct multiplication
therefore gives

 -partial_a(X S X)=2 d0-di.

The longitudinal inverse-propagator correction is this matrix times
(xi-1)e^2 c^2/Q^2. At the cone its leading part is d0, giving the same
wavefunction logarithm (xi-1)e^2/(8 pi^2 c) in time and every spatial
coefficient. Thus the characteristic-speed logarithm cancels for arbitrary
fixed xi. Finite lattice off-shell coefficient ratios can still depend on
xi; they are not promoted to physical velocities. This exact reduction is
checked against the unreduced matrix derivative in the primary runner.

## Integrable lattice remainder

Near a simple cone write D=D_0+R with R=O(|k|^2), uniformly in the
continuous frequency. For rho=sqrt(omega^2+|k|^2), small enough spatial k
gives ||S||+||S_0|| <= C/rho, ||S-S_0||<=C,
||partial S-partial S_0||<=C/rho, and
||partial^2 S-partial^2 S_0||<=C/rho^2 by the resolvent identity.
Peierls vertices differ from their cone values by O(rho), vertex derivatives
are bounded, and the true lattice gauge covariance differs from its cone
covariance by O(1). Derivatives with respect to external fermion momentum
therefore have remainder O(rho^-3) relative to the homogeneous degree -4
self-energy logarithm. Second external derivatives of the photon bubble have
the same integrable O(rho^-3) remainder. Four-dimensional radial measure
is rho^3 d rho, so each remainder integrates to a finite O(rho_0) value.

The fermion tadpole from the two-photon hopping vertex has no infrared
logarithm: its derivative multiplies only D_g=O(rho^-2). The photon seagull
is independent of its external momentum for single-link Peierls coupling;
it cancels the zero-momentum bubble term but has no q^2 logarithm. At large
frequency all needed differentiated integrands are absolutely integrable.
Away from every cone the fermion line is regular. In the fermion self-energy,
other cone singularities have a nonsingular gauge line and are integrable.
In the photon bubble all four cones contribute and each weighs one half of
a Dirac species. These estimates concern fixed microscopic parameters with
separated simple nodes, not a limit in which nodes merge.

The exact full lattice polarization identity can be proved without a grid:
contract its bubble with (q_0,qhat), use q.W=D_+-D_-, and shift the periodic
BZ/continuous-frequency variables. For a spatial index nu the remaining
vertex difference is
W_nu(k+q/2)-W_nu(k-q/2)=qhat_nu partial_nu^2 h(k).
It cancels the seagull -delta_mn integral tr[S partial_nu^2 h]. For the
constant temporal vertex the difference is zero. This identity relies on
both diagrams, not just a transversality check at selected momenta.
A shell cutoff by itself need not preserve the exact finite remainder Ward
identity; its logarithmic residue is the covariant cone result.

The primary uses actual-matrix checks: direct derivatives of the lattice fermion
self-energy (including momentum-dependent vertices) approach both analytic
wavefunction residues. Analytic second external derivatives of the actual
Peierls photon bubble approach the per-Weyl electric and magnetic residues;
longitudinal logarithmic residue vanishes. The finite shell remainders are
nonzero and are not discarded as numerical error.

Here is an explicit choice establishing the cone bounds. Put
s=sqrt(1-zeta^2), C_0=v[1/6+1/(2s)], and choose a cone radius rho_0 no larger
than 1, v/(2C_0), and one quarter of the minimum periodic separation of nodes.
Taylor's theorem gives ||h(K+k)-v R sigma.k||<=C_0 |k|^2 and therefore
|h(K+k)|>=v|k|/2 on this neighborhood. Thus

    ||S|| <= 1/[min(1,v/2) sqrt(omega^2+|k|^2)].

First through third derivatives of h are bounded by constants depending only
on v and zeta. Inserting the Taylor remainder and its derivatives into the
resolvent identity gives the displayed derivative-difference bounds.
Also |qhat_j-q_j|<=|q_j|^3/24 and
|qhat^2-q^2|<=|q|^4/12. The true gauge covariance therefore differs from its
cone covariance by O(1), including its fixed-xi longitudinal part. These
bounds justify the integrable remainder; a finite-grid trend is not its proof.

## Actual one-loop two-point asymptotics

The perturbative object is the infinite-spatial-volume Brillouin-zone
integral and continuous-frequency integral of the displayed supplied action.
Take that volume limit at the perturbative-integral level first. No limiting
interacting Gibbs state is inferred. For a small Euclidean external momentum
p at a fixed separated cone, write the integral as |q|>A|p| plus its complement,
with fixed A>2 and a fixed small outer cone radius rho_0.

For the fermion self-energy the homogeneous integrand has degree -3.
Its linear external Taylor term has degree -4 and integrates to the derived
matrix coefficient times p log(rho_0/|p|). The next Taylor remainder is
bounded by C |p|^2 |q|^-5; its outer integral is O(|p|).
In the inner region, rescaling q=|p|u bounds both the unexpanded integrand
and its zero-momentum subtraction by O(|p|): the singularities |u|^-2 and
|u-p_hat|^-1 are locally integrable in four dimensions, uniformly for unit
Euclidean p_hat. Other cones and the lattice remainder supply finite O(p)
matching terms. Therefore

 R_f(p)-R_f(0)=linear_log_matrix(p) log(rho_0/|p|)+O(|p|).

R_f is the inverse-propagator correction defined above. A finite R_f(0)
can shift the bare cone and is a matching/counterterm datum; changing that
location at order e^2 does not change the order-e^2 logarithmic residue.

For the photon bubble the homogeneous integrand has degree -2. Subtract its
constant and linear external Taylor terms. The quadratic term has degree -4
and gives the transverse tensor log. The cubic remainder is bounded by
C |p|^3 |q|^-5 and its outer integral is O(|p|^2). The inner region scales as
O(|p|^2); both translated simple fermion singularities are integrable. Hence

 Pi(p)-Pi(0)-p_a partial_a Pi(0)
   =quadratic_transverse_log_tensor(p) log(rho_0/|p|)+O(|p|^2).

The seagull cancels the constant term under the full Ward identity and has
no quadratic logarithm. Possible finite parity-odd linear response is a
separate lower-dimensional term; the supplied conjugate pair cancels its
free Hall response. No arbitrary parity-odd perturbation is silently excluded
from the general microscopic law by the parity-even tensor calculation.

These estimates provide a continuum logarithm from the actual lattice
vertices and propagators, with an integrable remainder. They do not evaluate
the finite O(p) or O(p^2) matching constants. They also do not continue the
error estimate uniformly onto Minkowski decay thresholds or prove an exact
massless charged pole. The proposed speed flow is the leading-log local
characteristic flow, with that precise observable boundary.

## Full tensor response from direct angular contraction

The full tensor response follows from an explicit contraction. Write a small
gauge kinetic deformation K_mnrs with Riemann
symmetries in the action (1/4) K_mnrs F_mn F_rs. Its gauge-invariant inverse
quadratic perturbation is M_ns(q)=2 K_mnrs q_m q_r, with M q=0.
At the reference Feynman gauge, delta D_g=-M/q^4. The coefficient of
i gamma_b p_a in the linear fermion correction is e^2/(8 pi^2) times

 T_ba = average_S3 [2 M_ba - delta_ba tr M + 2 q_b q_a tr M].

This follows from tr(gamma_b gamma_n gamma_a gamma_s)/4
=delta_bn delta_as-delta_ba delta_ns+delta_bs delta_na; the extra term
with M q vanishes by transversality. Unit-sphere moments are
<q_i q_j>=delta_ij/4 and
<q_i q_j q_k q_l>=(delta_ij delta_kl+delta_ik delta_jl
                  +delta_il delta_jk)/24.
With R_ns=sum_m K_mnms, substitution gives exactly

 T = (4/3) R -(1/3) tr(R) I.

Define (delta odot h)_mnrs=delta_mr h_ns+delta_ns h_mr
 -delta_ms h_nr-delta_nr h_ms. For K=delta odot h with tr h=0, R=2h, so
delta f=e^2 h/(3 pi^2). For a photon Weyl deformation R=0, delta f=0.
This derives the response for every traceless symmetric component without
assuming that a numerical scalar-speed test covers it. A simultaneous
f=h is a linear coordinate change; covariance of the leading cone residue
and the charge Ward identity then give the own-fermion term -e^2 f/(3 pi^2).

A finite exact check of the angular contraction can use the 24 unit vectors
consisting of the eight signed coordinate vectors and the sixteen vectors
(plus/minus 1/2,plus/minus 1/2,plus/minus 1/2,plus/minus 1/2), all with
weight 1/24. Their second and fourth moments agree exactly with the displayed
sphere moments; every polynomial entering T has degree at most four.
This is an exact cubature identity, not a sampled-sphere proof.

The metric/Weyl analysis concerns the parity-even marginal kinetic sector.
The supplied normal carrier's Hall cancellation and node separation must be
kept distinct from a theorem excluding every relevant perturbation or pairing
instability. Arbitrary independent cone frames are an effective-sector probe;
which ones a chosen microscopic hopping family realizes must be stated.

## Linearized multi-cone metric and photon-polarization flow

At the common Euclidean metric choose units c=v=1. Let f_a be each fermion's
symmetric traceless infinitesimal frame perturbation (nine components) and
h the photon metric frame perturbation. The metric is I+2f_a or I+2h.
Antisymmetric frame changes are spin-basis rotations; a trace is a field/unit
normalization. Common f_a=h is a change of coordinates, not a mismatch.

The parity-even quadratic Maxwell tensor has Riemann symmetries after the
constant axion term is set aside. Decompose it into scalar normalization,
traceless Ricci part delta odot h, and Weyl part C (ten components). Here
(delta odot h)_mnrs=delta_mr h_ns+delta_ns h_mr
                   -delta_ms h_nr-delta_nr h_ms.
Its Ricci contraction is 2h for traceless h. The tensor C has zero Ricci
contraction and represents the non-metric photon polarization part.

The direct contraction just proved gives the entire fermion frame response.
For the photon, a constant frame E gives the loop quadratic form
[1/(4 det E)] (E^T E)_mr (E^T E)_ns F_mn F_rs. For E=I+f with tr f=0,
its first variation is the metric tensor delta odot f, with no Weyl component.
This also proves the photon-frame and polarization normalization used below.

For species charge q_a e and multiplicity n_a in Dirac units (one Weyl has
n_a=1/2), define kappa=e^2/(6 pi^2), W=sum_a n_a q_a^2. The derived
linearized flow, after removing common isotropic normalization, is

 df_a/dell = 2 q_a^2 kappa (h-f_a),
 dh/dell = kappa sum_a n_a q_a^2(f_a-h),
 dC/dell = -W kappa C,
 dkappa/dell = -W kappa^2.

The photon formula follows independently because a fermion determinant in
its own frame adds a Maxwell quadratic form of that frame. Canonical field
normalization divides the existing photon tensor by 1+W kappa d ell;
its Weyl component therefore decays. It is not sourced at first order by a
fermion metric perturbation. The fermion response to a photon Weyl tensor
vanishes at this order by its Ricci contraction.

For every tensor component the metric equations form a weighted star graph.
The detailed-balance weights are n_a/2 on f_a and one on h. For E=(1/2) sum_i w_i (y_i-y_bar)^2, their weighted
quadratic energy has derivative
 E'= -kappa sum_a n_a q_a^2 (f_a-h)^2.
The conserved mean is (sum_a n_a f_a+2h)/(sum_a n_a+2).
The weighted matrix is symmetric positive semidefinite because its quadratic
form is sum_a n_a q_a^2(f_a-h)^2. If all charges are nonzero, vanishing of
that form forces every f_a=h, proving the stated one-dimensional kernel per
tensor component. Diagonalization in the weighted inner product and
integral_0^ell kappa(s) ds=log[1+W kappa_0 ell]/W give the solution powers.
If all charges are nonzero, the unique zero direction is a common metric.
All other eigenvalues lambda_j of the constant positive graph matrix give
powers [1+W kappa_0 ell]^(-lambda_j/W).

For four unit-charge Weyl cones, n_a=1/2 and W=2. The common matter average
versus photon mode has lambda=4 and exponent 2. The three independent
inter-cone metric differences have lambda=2 and exponent 1. The ten photon
Weyl-tensor components also have exponent 1. Thus an isotropic shared-fermion
ansatz misses slower linearized modes. This does not mean that every such
perturbation is independently realizable in the particular nearest-neighbor
symbol; that microscopic matching remains a condition to be stated.

These are componentwise Euclidean tensor identities. Their continuation to
real Hermitian physical perturbations carries the usual factors of i on
temporal indices; the note makes no stability claim for arbitrary large or
non-Hermitian tensor coefficients. For the actual displayed Hamiltonian the
spatial characteristic coefficients are unambiguous. General independent
cone-frame perturbations remain explicitly supplied effective-sector data.
If a species has q_a=0, its frame is a disconnected constant mode; no common
metric for that sector follows from charged interactions.

## Nonlinear isotropic truncated flow and its asymptotic rate

Let r=v/c and g=e^2/c. Algebra gives

 dr/dell = -g(r-1) H_N(r)/(12 pi^2),
 dg/dell = -N g^2(r+1/r)/(12 pi^2),
 d log c/dell = N g(r^2-1)/(12 pi^2 r),
 H_N(r)=2(4r^2+3r+1)/(r+1)^2+N(r+1), N=N_D.

H_N>0 for r>0. The speed ratio stays between its initial value and one.
Since r and 1/r stay bounded, g is comparable to 1/(1+ell), its integral
diverges and r tends to one. The individual speeds remain between the
initial two speeds because dv points toward c and dc toward v. They converge
to a positive common value. This is a theorem of the displayed truncated ODE,
not yet a theorem of the full quantum field theory.

Near equality, g~6 pi^2/(N ell) and
r-1 scales as ell^[-(N+2)/N]; for the four-Weyl carrier N=2, the exponent is 2.
The exact local linearized solution about fixed common c uses
r(ell)-1=[r(0)-1][1+N g(0)ell/(6 pi^2)]^[-(N+2)/N].
For a nonzero initial r-1, the exact asymptotic power follows without
assuming a constant charge. Divide the first two differential equations:
d log|r-1|/d log g=H_N(r)/[N(r+1/r)], whose limit is p=(N+2)/N.
More strongly, the derivative with respect to r of
log(|r-1|/g^p) is [1-p N(r+1/r)/H_N(r)]/(r-1), which extends continuously
to r=1. Its finite integral proves |r-1|/g^p tends to a finite nonzero
constant. Since r tends to one, Cesaro averaging in the equation for 1/g
gives g~6 pi^2/(N ell), as stated. If r starts at one it stays there.
These statements assume N>0 and g(0)>0. With zero coupling there is no
interaction-driven contraction. Higher-loop control remains open.

## Decaying lattice forcing and finite matching

If the exact local shell remainder produces a forcing bounded by
C kappa(ell) exp(-p ell), p>0, a mismatch mode solves
 y'=-lambda kappa y+f(ell).
Its integrating-factor expression is
 y(ell)=[1+W kappa_0 ell]^(-lambda/W)
        [y(0)+integral_0^ell [1+W kappa_0 s]^(lambda/W) f(s) ds].
The integral converges absolutely. The lattice correction changes the finite
matching constant but does not shift the massless truncated flow's asymptotic
fixed metric by a constant. This statement requires the decaying forcing;
a permanent marginal source or a new mass threshold is a different problem.
The full-BZ finite constant and physical finite-scale mismatch remain open.

## Massive threshold and finite available flow

This section is a separately supplied massive Dirac comparator at a common
reference metric, not a claim that the normal Weyl carrier dynamically gaps.
A gauge-invariant mass or pairing channel would require its own microscopic
matching. Below the masses the charged fields leave the active massless EFT.

The Dirac trace and Feynman parameter shift give the scalar photon quadratic
coefficient (up to a momentum-independent UV subtraction)

 Pi(Q^2)=N e^2/(2 pi^2) integral_0^1 x(1-x)
          log[Lambda^2/(m^2+x(1-x)Q^2)] dx.

One way to check the factor is the transverse form before radial integration:
8 N e^2 integral_0^1 x(1-x) dx integral d^4 l/(2 pi)^4
 (l^2+m^2+x(1-x)Q^2)^(-2) times (Q^2 delta_mn-Q_m Q_n).
The momentum-subtracted screening loss is positive and bounded by

 0 <= Pi(0)-Pi(Q^2) <= N e^2 Q^2/(60 pi^2 m^2),

using log(1+t)<=t and integral x^2(1-x)^2 dx=1/30.
Its logarithmic derivative relative to the massless charge coefficient is

 F(z)=6 integral_0^1 [x^2(1-x)^2 z/(1+x(1-x)z)] dx,
 z=Q^2/m^2.

Thus 0<F(z)<1, F(z)<=z/5, F is increasing, and F tends to one as z tends
to infinity by dominated convergence. The small-z derivative is 1/5.
In a momentum-subtraction charge convention the one-loop common-metric
charge equation is kappa'=-N F(exp(-2s)) kappa^2 below Q=m,
s=log(m/Q). Its total remaining polarization flow is finite:

 integral_0^infinity F(exp(-2s)) ds
 =3 integral_0^1 x(1-x) log[1+x(1-x)] dx <=1/10.

Consequently 1/kappa(infinity)-1/kappa(Q=m)<=N/10 in this comparator.
A mass-independent subtraction scheme can keep a formal running parameter,
but physical low-momentum polarization has the displayed decoupling. There
is no continuing charged massless logarithm below all charged thresholds.
This does not assign a massless speed to an integrated-out massive fermion.

For a mode with massless exponent p, the available interval L above a
threshold gives attenuation [1+W kappa_0 L]^(-p) within the displayed
linearized flow. To reduce a nonzero mismatch by a factor R<1 requires
L >= [R^(-1/p)-1]/(W kappa_0). This is a conditional scale requirement,
not a numerical empirical prediction. Neither the initial mismatch, matching
constant nor the charged thresholds are derived from the framework axioms.

The main lesson is two separate facts: bounded irrelevant lattice remainders
do not create a constant shift of the massless asymptotic fixed metric; a
finite charged interval does not force exact metric equality at its endpoint.
All-orders stability, finite matching and physical-observable identification
remain open. None of these conditions is a proven axiom contradiction.

## Payload, phase and native identification remain open

The gauge action used for this one-loop calculation is a supplied noncompact
quadratic action with Peierls-coupled fermions. Its continuous link variables
are not an already-derived finite-payload gauge phase. A formal weak-field
expansion of a compact model may share these perturbative coefficients only
after its action and normalization are matched; perturbative equality alone
cannot establish its infrared phase. None of the preceding campaign's
unmerged compact or finite-time approximation theorems is needed as a premise
for this block's one-loop integral calculation.

## Checks and falsifiers

The primary contains four substantial check families: the complete lattice
action/vertices and Ward cancellation; independent continuum residues and
actual lattice shell derivatives; full Clifford/tensor response and weighted
flow; and massive-threshold/nonlinear-flow comparisons. The spherical moments
are checked with exact rational arithmetic, while tensor examples and loop
quadratures have explicit numerical tolerances. The analytic remainder proof
and exact identities carry the general claims.

The runner reads no scientific data files or helper runners at runtime. Its cache pins this proof note and the [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) as proof and premise identities. Mutation receipts
in the review packet record which consequential errors the checks reject.
No count of passing examples or mutation failures constitutes independent
scientific review, a nonperturbative phase proof or empirical validation.

## Negative-claim discipline

### N1 — Examined alternatives

| Route | Work in this block | Disposition |
|---|---|---|
| Scalar denominator or static proxy as the physical RG coefficient | Read current-main velocity proxy boundaries and compare to the actual tensor action | Insufficient inference; replaced here for this supplied carrier |
| Full lattice Peierls response | Derive both vertices, complete Ward identity, residues and remainder | Supplies one-loop logarithmic matching |
| Shared fermion speed ansatz | Derive nonlinear isotropic flow, then full linearized cone metrics | Useful restriction that omits slower permitted effective-sector modes |
| Constant coupling for unlimited infrared contraction | Solve coupled charge and tensor flows | Constant-coupling power is not the derived QED4 flow |
| Massive charged interval | Derive momentum-subtracted polarization and threshold integral | No continuing massless charged logarithm below all charged thresholds |
| Direct Hamiltonian phase or nonperturbative compact expansion | Not attempted by this one-loop block; preceding campaign leaves the phase open | Live routes, not excluded alternatives |

### N2 — Wall relationships

The full interacting phase/stability and the physical spectral interpretation
are related obligations: a phase theorem would provide part of the setting
for an observable theorem. Finite matching constants and charged thresholds
control the available amount of contraction. Native law selection and the
finite-payload bridge are upstream identification obligations. They are not
five independently proved no-go walls. The only negative implications here
reject specified inference shortcuts or follow from the displayed comparator.

### N3 — Hidden premises

The continuous gauge variable, half-filled sea, normal number conservation,
chosen cone normalization, fixed separated nodes and microscopic couplings
are supplied. General frame perturbations and the massive Dirac comparator
have their own declared scopes. A common free metric, a positive gauge tensor
or a gauge Ward identity does not establish the original framework carrier,
absence of pairing, observed masses, physical spectral poles or empirical
Lorentz accuracy. The approved primitive is not demoted to a missing axiom.

### N4 — Source and residual matching

The current-main July 17 gauge-tensor/WTI velocity note explicitly confines
its result to static proxies and leaves true inverse, physical speed, carrier
and RG extraction open. This note supplies a new action-specific extraction;
it does not close that note's distinct blocked-staggered carrier bridge.
Anber–Donoghue section 4 and Roy–Juricic–Herbut section 3 are continuum
comparators, not lattice or phase premises. Kostelecky–Lane–Pickering equation
(28) is the prior tensor-beta comparator; the differential coefficients are
rederived here. Reading limits and a printed integrated-formula discrepancy
are recorded in the packet; that integrated expression is not imported.
No source's one-loop result is promoted into all-orders control.

### N5 — Resolution and rhetoric

All five per_element, per_site, per_mode, per_block and lattice_wide scope
lines appear in the primary. Lattice-wide refers to the stated analytic
one-loop Brillouin-zone matching, not an interacting thermodynamic phase.
The finite-radial tests challenge the analytic coefficients; they do not fit
an exponent and present that fit as a continuum theorem.

### N6 — Partial closure and live routes

The supplied model's logarithmic coefficient, tensor-mode spectrum and
threshold comparison are the partial closure. Finite renormalization matching,
nonperturbative infrared stability, physical source/spectral identification,
and a native finite-payload construction remain live work. Strongly coupled
fixed points, additional interacting sectors or a derived protecting symmetry
could change contraction rates; none is ruled out or added as a primitive.

### N7 — Hostile reading

A reviewer should reject interpreting the one-loop characteristic coefficients
as exact charged poles, or reading logarithmic asymptotic attraction as a
finite-scale empirical match. The source explicitly makes neither inference.
A reviewer should also reject treating the massive comparator as proof that
the normal lattice carrier gaps, or treating a finite matching term as a
permanent marginal drive without deriving such a drive.

### N8 — Cross-cycle distinction

The prior finite-clock history, massive covariance and compact-current
milestones did not provide this massless Peierls tensor calculation. This
pair supplies its own model, Ward proof, logarithmic matching and multi-cone
flow. The compact phase and native model-selection obligations remain the
same open obligations; they are not newly discovered axiom contradictions.
The standard continuum beta functions are credited as prior art. The repo
contribution is the checked lattice derivation and its precise limits.

Gate disposition: narrowly stated author-proposed conditional mathematics
and inference boundaries. Independent scientific review remains pending.

## Sources and review boundary

- [Anber and Donoghue, emergence of a universal limiting speed](https://arxiv.org/abs/1102.0789): continuum speed-flow comparator.
- [Roy, Juricic and Herbut, emergent Lorentz symmetry](https://arxiv.org/abs/1510.07650): independent continuum normalization and running comparator.
- [Kostelecky, Lane and Pickering, one-loop Lorentz-violating electrodynamics](https://arxiv.org/abs/hep-th/0111123): prior tensor-beta equations, with source limits recorded in the reading ledger.

No editable prompt or workflow file changes. No audit verdict, effective
status, main merge, axiom edit or primitive edit is part of this proposal.

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Derive interacting metric protection or attraction with matched microscopic vertices, sources, running couplings and physical limits."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the supplied lattice one-loop derivation; compute finite matching or establish a nonperturbative phase and physical-observable bridge."
conditional_surface_status: "Specified noncompact Peierls carrier and perturbative order; exact logarithmic matching, linearized tensor flow and threshold comparator, with native/finite-payload phase and spectral identification open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Direct statements about explicit one-loop integrals, bounded remainders and displayed ODEs, with no all-orders or axiom-forcing conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
