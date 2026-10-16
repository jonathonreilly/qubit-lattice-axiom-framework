# Count-derived scalar energy requirements along inertial references

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_count_kernel_energy_check.py](../scripts/scalar_count_kernel_energy_check.py)

**Exact target:** derive the vector time weights imposed by finite calibrated counts, characterize the least free-field energy compatible with their residual contrasts, and bound that requirement uniformly over nonnegative scalar masses and constant subluminal reference velocities. No initial field is selected by this construction.

The count operator is the starting point. Unknown constant velocity and supplied nuisance shapes are removed by exact contrasts. The real energy Hilbert-space construction then turns those contrasts into a resource requirement. Under an explicit conformal test-body model, a momentum-space change of variables proves that the stationary massless matrix remains a conservative enclosure for inertial moving references. Choosing a mass or a minimum-energy initial state is unnecessary for that inequality. Actual calibration, accelerated trajectories, source forcing, nonlinear errors and an independently supported energy upper budget remain application work.

## Observational target and surviving physical identification

The input problem is a finite list of count intervals and compressed readouts. Derive the weights that those intervals impose, then find the least field energy compatible with a calibrated residual. Do not choose an averaging shape or an initial field to manufacture agreement. Already exposed Cassini day169 archive values may be used only under .claude/science/physics-loops/observations-backward-24h-20261014/residual_energy/DEVELOPMENT_TIMING_PROTOCOL_v1.json. They are receiver/reference products, not physical scalar-force residuals. All later raw tracks remain unopened.

The mathematical model below explicitly supplies a calibrated velocity response, a C1 clock map with derivative positive and bounded away from zero on every finite interval, a known observation direction and a stationary reference point for the closed free-field Gram formula. Actual spacecraft motion, retarded rays, electronics, plasma, planetary forces and nonlinear/source errors are not supplied by the raw count reconstruction. A physical energy budget or constraint is not claimed until those bridges and error budgets are established.

## 1. Derive the kernel from compressed measurements

Let the relevant coordinate be s=ct and let v(s) be an absolutely continuous vector perturbation with a=v'. Each scalar compressed measurement has the conditional form

    y_i = integral k_i(s) n_i(s).v(s) ds + (X beta)_i + e_i,

where k_i is a known compact integrable weight, n_i is a known bounded direction, each f_i=k_i n_i is square-integrable, X a known nuisance design, beta arbitrary coefficients and e a measurement error. Define the vector functions f_i=k_i n_i and the three-column matrix N_i=integral f_i(s) ds. For a real contrast c satisfying N^T c=0, set

    F_c(s)=sum_i c_i f_i(s),
    W_c(s)=-integral_{-infinity}^s F_c(u) du.

The cancellation makes W_c vanish after the final interval as well as before the first. If F_c is square-integrable and compactly supported, W_c belongs to H1, is compact and has derivative -F_c. Integration by parts gives the exact identity

    c^T(y-X beta-e) = integral W_c(s).a(s) ds.

This removes an arbitrary constant initial velocity vector. A scalar condition sum c_i integral k_i=0 is insufficient when n varies. If using a scalar w times a direction n instead, differentiating n.v produces n.a+n'.v; the vector primitive above incorporates that geometry exactly rather than dropping it. Nuisance cancellation also requires X^T c=0. If these columns exhaust the measurement space, no nonzero such contrast exists; do not assume an extra channel.

For instrument time tau and a known C1 map s(tau) with s'(tau)>=epsilon>0 on the finite observation intervals, the inverse is absolutely continuous and the ordinary change of variables applies. A readout

    y_i=(1/Tau_i) integral_{a_i}^{b_i} kappa(tau) n(tau).v(s(tau)) d tau

gives k_i(s)=kappa(tau(s))*tau'(s)/Tau_i on its transformed interval. The required moments are integrals of k_i n_i, not nominal durations. Unknown clock/calibration functions remain imports. Under varying calibration, two means generally cannot cancel both an arbitrary additive baseline and arbitrary constant velocity; all columns must be included explicitly.

For two constant-calibration, fixed-direction adjacent velocity averages with lengths T_i,T_{i+1}, define H_i=(T_i+T_{i+1})/2. Their difference divided by H_i gives a normalized hat: it rises with slope1/(H_i T_i), falls with slope-1/(H_i T_{i+1}), and reaches1/H_i at the common endpoint. For a gap g, H_i=g+(T_i+T_{i+1})/2 and the hat has a plateau1/H_i in the gap. It integrates acceleration in that gap; it does not assume the gap dynamics vanish.

## 2. Exact stationary free-field Gram and mass enclosure

For real free KG data with mathematical norm ||h||_H^2=2E, let A_W=integral W(s).grad h(s,x0) ds at one fixed spatial point. The unitary spatial Fourier solution h(s)=cos(s Omega)q+sin(s Omega)p/Omega, Omega=sqrt(-Delta+mu^2), and real data give the following Riesz inner product. The real plus/minus frequency contributions pair without another factor two:

    <g_W,g_V>_H = (1/(6 pi^2)) integral_mu^infinity
       ((omega^2-mu^2)^(3/2)/omega)
       Re[Wtilde(omega).conjugate(Vtilde(omega))] d omega.

For smooth real data, write alpha=(2pi)^(-3/2), omega=sqrt(k^2+mu^2), and C=Re Wtilde, S=Im Wtilde. The Riesz initial data are qhat_W=-i alpha exp(-i k.x0)(k.C(omega))/omega^2 and phat_W=-i alpha exp(-i k.x0)(k.S(omega))/omega. They obey real-data conjugate symmetry. Their energy inner product is the displayed Gram; smooth spectral cutoffs provide the energy-completion limit. Angular isotropy uses integral_{S2} khat_a khat_b dOmega=(4pi/3)delta_ab; it is not an assumption of isotropic initial data. For mu=0,

    G0(W,V) = (1/(6 pi)) integral W'(s).V'(s) ds.

The L2 premise on every f_i makes every entry of the following auxiliary raw matrix finite. This matrix describes bounded contrasts; it does not assert boundedness of uncontrasted velocity observations. Consequently B_ij=(1/(6pi)) integral f_i.f_j gives the contrast Gram C B C^T when rows of C satisfy C N=0. For mu>=0 the spectral coefficient is bounded above by omega^2. Applying this to every contrast establishes the matrix inequality Gmu <= G0 as positive quadratic forms. No mass is fitted or set to zero in this enclosure.

For common-normalization independent modes and scalar acceleration a=-sum alpha_j grad h_j at the stationary reference point, write q=sum alpha_j^2 and E_tot=sum E_j. The exact response Gram is sum alpha_j^2 Gmu_j and is bounded by q G0. For q>0 it follows that every consistent residual obeys all energy inequalities from q G0, even when the actual masses differ. Equality/minimum-energy attainment using G0 is asserted only for the massless supplied model with an active coupling, not for arbitrary massive modes. If q=0 the scalar response is zero and the observed contrast must be explained entirely by errors; division by q is unavailable.

The stationary-reference linear response is essential. The full conformal force on a moving reference contains both the spatial gradient and v*partial_s h. The inertial section below derives an exact tensor and proves this same upper enclosure for the full force along a constant subluminal reference. Arbitrary accelerated tracking observations still require the actual operator or a controlled enclosure and modeling error.

## 3. Infer the required energy without selecting a state

For any finite real Hilbert-space observation map A, with G=AA^*, exact data r are consistent iff r belongs to range(G). In that case

    E_min(r)=(1/2)r^T G^+ r,
    h_min=A^*G^+r.

Indeed A h_min=GG^+r=r; any other consistent h=h_min+z has Az=0, and h_min is orthogonal to z. Thus E=E_min+(1/2)||z||^2. Energy-class attainment is distinct from attainment by smooth Schwartz data. When finite observations have full rank, smooth approximants of the representers have an invertible observation matrix for sufficiently close approximation; recombining them enforces the exact constraints with energies approaching E_min.

This characterizes compatible fields; it is not a physical principle selecting h_min. Finite data in this specified infinite-dimensional linear space retain invisible directions. The code tests explicit nonzero invisible fields and finite amplitude changes; this is not an exclusion of all possible observational or nonlinear theories.

If G is positive definite and a finite nuisance design X has unknown coefficients, let U have independent columns spanning ker(X^T). Then

    min_beta (1/2)(r-X beta)^T G^-1(r-X beta)
      = (1/2)(U^T r)^T (U^T G U)^-1(U^T r).

One proof treats U^T A as the observation map: U^T A h=U^T r exactly means r-Ah is in range(X). It is therefore the same constrained least-energy problem. In singular cases retain the range condition for the quotient; unrestricted minimization of an expression with G^+ can incorrectly assign zero cost to an impossible residual. The independent checker identified this useful boundary before implementation.

For the mass enclosure above, choose C with full row rank spanning contrasts annihilating both N and X. If H0=C B C^T is positive definite, every consistent model satisfies

    E_tot >= (1/(2q)) (C y)^T H0^-1 (C y),

with errors subtracted if present. Indeed |b^T C y|^2<=2 q E_tot b^T H0 b for every real b; taking b=H0^-1 C y gives the inequality without inverting a possibly singular actual massive Gram. This is a lower bound on required energy. It is not an observed upper energy limit and does not by itself exclude the scalar candidate.

The singular nuisance extension also has a direct solution. Choose C with ker(C)=range(X), set H=C G C^T, and require C r in range(H). Applying the same Hilbert theorem to C A gives the constrained minimum (C r)^T H^+ (C r)/2, because C A h=C r is exactly equivalent to r-A h in range(X). Empty contrast spaces give zero cost. This characterizes feasibility, not a nuisance prior.

## 4. Unequal-window identity and joint information

For nonoverlapping intervals and unit directions, constant unit calibration gives B_ii=1/(6pi T_i), B_ij=0 for i!=j. Direction averages enter N even though B is diagonal. Joint minimization removes the actual supplied initial-velocity and nuisance columns:

    E_tot >= (3pi/q) min_beta sum_i T_i (y_i-(Z beta)_i)^2,
    Z=[N,X],

where redundant columns are interpreted through their span. This is a derived quotient, not a decision to set beta or the initial field to a convenient value. Equality as a least-energy value holds for the massless stationary model under the stated full-rank quotient conditions.

For fixed direction and no additional nuisance, the only initial-velocity column is1. Therefore

    E_tot,min = (3pi/q) sum_i T_i (bar_v_i-weighted_mean(bar_v))^2.

For adjacent intervals, integrated-velocity counts Q_i=T_i bar_v_i give r=DQ, where D_i,i=-1/(H_i T_i), D_i,i+1=1/(H_i T_{i+1}). The acceleration Gram is

    G0=(1/(6pi)) D diag(T_i) D^T.

Writing K=D diag(sqrt(T_i)) shows ker(K)=span(sqrt(T_i)); hence r^T G0^-1r equals6pi times the duration-weighted velocity variance. This also proves the unequal-window relation without guessing independent per-window energy budgets. For equal T, G0=L/(6pi T^3), L has diagonal2 and neighboring entries-1, and (L^-1)_ij=min(i,j)*(n+1-max(i,j))/(n+1). Treating windows as independent loses their negative cross terms.

## 5. Physical normalization and honest error budget

Under the supplied quadratic normalization Q_J>0, nonzero coupling q>0, and constant frame conversion derived below, E_phi=2Q_J E_tot and G_bare=1/(8pi Q_J). Thus

    E_phi >= (Q_J/q) z^T H0^-1 z
           = [1/(8pi G_bare q)] z^T H0^-1 z,
    z=C y.

If additionally the candidate's derived q<1/3 and the same-environment positive-geometry relation G_meas>=G_bare>0 apply, then

    E_phi >= [3/(8pi G_meas)] z^T H0^-1 z.

For nonoverlapping unit-calibration means this becomes

    E_phi >= [9/(4 G_meas)] min_beta sum_i T_i(y_i-(Z beta)_i)^2.

All quantities here use the same specified natural units and stationary linear response. No SI number is assigned, and no actual measured gravity, scalar energy or force residual has been imported. The candidate action and same-environment identification remain conditional; the result merely removes the need to choose individual masses/couplings within their stated ceiling.

For positive-definite B and deterministic errors in a declared weighted ball ||B^-1/2 e||<=rho with rho>=0, whiten y and Z: yhat=B^-1/2 y, Zhat=B^-1/2 Z, P the orthogonal projector off range(Zhat). The exact minimum whitened residual norm over that ball is max(0,||P yhat||-rho). The corresponding rigorous lower bound is this square divided by2q in mathematical energy, or multiplied byQ_J/q in physical energy. The actual rho, correlations and calibration must come from evidence, not from the archive's storage quantum. Componentwise error budgets |e_i|<=eta_i with eta_i>=0 instead give the valid contrast bound

    E_tot >= max(0,|c^T y|-sum_i |c_i| eta_i)^2 / (2q c^T B c)

for every contrast c annihilating Z with q>0 and c^T B c>0. If c^T B c=0, the response in that contrast vanishes; compatibility instead requires |c^T y|<=sum_i |c_i| eta_i. The same compatibility condition applies to every contrast when q=0. Singular B does not admit the displayed full-space inverse square root; retain a supported error set, the contrast range condition, or the general quotient formulation rather than silently projecting away inconsistent data. No stochastic confidence level is inferred from this deterministic statement.

## Inertial force tensor and all-mass enclosure

### Supplied model and target

Use the real free KG equation in one fixed Minkowski coordinate frame, mathematical lab-frame energy E=(1/2) integral(p^2+|grad h|^2+mu^2 h^2), mu>=0, and a prescribed inertial reference x(s)=x0+u s with beta=|u|<1. The linear scalar contribution to the conformal test-body acceleration is

    a_h(s)=-(1-beta^2)[grad h+u partial_s h](s,x0+u s).

The full time-derivative term is retained. A constant reference trajectory is the zeroth-order path in the linear response, not an exact accelerated body path in a nonzero field. The conformal matter model, free operator, constant background/coupling, coordinate clocks and finite-energy hypothesis remain supplied.

For real compact vector weights W,V in H1, define L_W=integral W.a_h ds. Rough energy-class fields use the continuous extension proved below; classical pointwise values are not presumed. The real time transform is Wtilde(lambda)=integral W(s) exp(i lambda s) ds. Spatial Fourier is unitary, alpha=(2pi)^(-3/2). Once the H1 bound is proved for compact weights, density extends it to H1 weights; the rapidly decreasing Gaussian windows in the controls are covered by that limit. No compactly supported Gaussian is asserted.

### Real Fourier norm and boost variables

After combining the two real Fourier signs, the energy dual Gram is

    G_mu,u(W,V)=alpha^2(1-beta^2)^2 integral d^3k / omega^2
      Re{[(k-omega u).Wtilde(lambda)]
           conjugate[(k-omega u).Vtilde(lambda)]},
    omega=sqrt(k^2+mu^2), lambda=omega-k.u>0.

Using h=exp(i omega s)(q+p/(i omega))/2+exp(-i omega s)(q-p/(i omega))/2, the joint real q,p norm produces the average of the two signed force-branch squared amplitudes. The plus/minus contributions give the same integrated result by k -> -k and reality. The spatial phase exp(i k.x0) cancels in the Gram. This is the norm relative to the original lab-frame energy, not a Lorentz-invariant energy assertion.

Choose z parallel to u, gamma=(1-beta^2)^(-1/2). A change of integration variables to primed on-shell momentum gives

    omega=gamma(omega'+beta k'_z),
    k_z=gamma(k'_z+beta omega'),  k_perp=k'_perp,
    lambda=omega'/gamma,
    k_z-beta omega=k'_z/gamma,
    d^3k/omega=d^3k'/omega'.

These identities only transform the integral; E itself is not relabeled rest-frame energy. Put p=sqrt(lambda^2-(mu/gamma)^2), r=p/lambda in [0,1], and S=diag(1,1,1/gamma). For n on S2,

    k'=gamma p n,
    k-omega u=gamma p S n,
    omega=gamma^2 lambda(1+beta r n_z),
    k'^2 dk'=gamma^3 p lambda d lambda.

Thus, with A(t)=integral_{S2} n n^T/(1+t n_z) dOmega,

    G_mu,u(W,V)=(1-beta^2)/(2pi)^3
      integral_{mu/gamma}^infinity lambda^2 r^3
        Re[Wtilde^* S A(beta r) S Vtilde] d lambda.       (1)

The integral of the imaginary antisymmetric part is irrelevant to the real Gram. Axial symmetry makes A diagonal: equal transverse entries and a longitudinal entry.

### Exact massless time-local tensor

Let L(beta)=atanh(beta)/beta, with its continuous value L(0)=1. Direct angular integration gives

    A_parallel(beta)=4pi [L(beta)-1]/beta^2,
    A_perp(beta)=2pi [L(beta)-(L(beta)-1)/beta^2].

At beta=0, both are 4pi/3. Parseval in (1), for mu=0, yields

    G_0,u(W,V)=integral W'(s)^T M(u) V'(s) ds,
    M(u)=m_perp(I-u_hat u_hat^T)+m_parallel u_hat u_hat^T,

    m_perp=(1-beta^2)/(4pi beta^2)
                  [1-(1-beta^2)L(beta)],
    m_parallel=(1-beta^2)^2/(2pi beta^2)[L(beta)-1].       (2)

At zero velocity M=I/(6pi); the direction u_hat is then immaterial. For W=e w_T with a triangular unit-area weight, integral |w_T'|^2=2/T^3. Multiplying (2) by this reproduces the explicit triangular parallel/perpendicular constants. Here (2) holds for arbitrary vector H1 windows, so changing directions and cross-window correlations are retained without supplying an isotropic initial field.

For numerical evaluation near beta=0 use the convergent series, not subtract nearly equal numbers. If x=beta^2,

    m_parallel=(1-x)^2/(2pi) sum_{n>=0} x^n/(2n+3),
    m_perp=(1-x)/(2pi) sum_{n>=0} x^n/[(2n+1)(2n+3)].

These show m_parallel,m_perp>0 for beta<1. They also show
m_parallel<=(1-x)/(6pi)<=1/(6pi) and m_perp<=1/(6pi), because each series coefficient is at most1/3 and sum x^n=1/(1-x). Consequently

    0 < M(u) <= I/(6pi), beta<1.                         (3)

The beta->1 limit is not a lightlike theorem: both coefficients tend to zero in this coordinate-force/lab-energy norm but the allowed reference is strictly subluminal. The zero-velocity limit is continuous.

### Nonnegative masses: a true moving enclosure

Pair n_z=z and -z inside A(t). The denominator pair is 2/(1-t^2 z^2), increasing with t^2 for |t|<1. The transverse and longitudinal diagonal integrals are therefore nondecreasing for t>=0. For fixed beta and 0<=r<=1,

    0 <= r^3 S A(beta r) S <= S A(beta) S.

Extending the massive integrand by zero below mu/gamma in (1) proves the positive-quadratic-form enclosure for every real vector kernel and every finite Gram family:

    0 <= G_mu,u <= G_0,u <= G_0,stationary.              (4)

The final inequality follows from (3) and Parseval. Thus the same stationary matrix is a valid conservative upper enclosure for the full conformal force along any prescribed constant subluminal reference. It is not generally the exact moving Gram. Equality is not asserted for positive masses or nonzero velocity.

This conclusion would not follow by omitting u partial_s h: that omission changes the Fourier force vector k-omega u and its tensor. The runner includes a direct control distinguishing that omitted term. Neither arbitrary accelerated trajectories nor arbitrary retarded radio endpoint mixtures are covered by (4); those require their own operator.

### Count-derived consequences and limits

Under the reduced calibrated velocity model from the count-kernel model above, F_c=sum c_i k_i n_i, W_c'=-F_c and the exact cancellation N^T c=0 eliminate unknown constant initial velocity. For a single inertial reference, the massless auxiliary metric becomes

    B_u,ij=integral f_i(s)^T M(u) f_j(s) ds,
    G_contrast=C B_u C^T.

It is not generally diagonal in scalar direction space, though disjoint count intervals still eliminate cross-integrals before contrasts. Its stationary enclosure is B_0,ij=(1/(6pi))integral f_i.f_j. If finitely many modes share that prescribed reference and normalization, sum alpha_j^2 G_mu_j,u<=q C B_0 C^T. Therefore every nonzero-coupling lower-energy inequality already derived using the stationary enclosure remains valid for these inertial full-force responses. The exact massless minimum uses B_u, not B_0.

No new field-state selector, individual mass, decomposition age or support radius has been introduced. The calibrated physical operator, same-environment gravity relation if used, actual error budget, free-field energy budget, forcing/nonlinear effects and the discrepancy between a real accelerated spacecraft and this inertial reference all remain quantitative obligations. No observational values enter this derivation.

## Force and physical-energy premises made explicit

The full-force expression used above follows from the supplied test-body action S_p=-m integral A(phi) sqrt(1-v^2) ds in a frozen Minkowski Einstein metric. With ell=log A and gamma=(1-v^2)^(-1/2), its Euler-Lagrange equation is d_s(A gamma v)=-A gamma^(-1)grad ell. The total derivative of ell is partial_s ell+v.grad ell. Inverting I+gamma^2 v v^T yields a=-(1-v^2)[grad ell+v partial_s ell]. Linearizing about a constant background gives ell=ell_b+sum alpha_j h_j and the force used in the inertial proof. Finite-body sensitivity, self-gravity, tensor perturbations and higher orders are not included in this supplied matter model.

A kinetic term -Q sum(partial h_j)^2 gives E_phi,E=2Q E_tot,E. At a constant background A_b, physical coordinates satisfy x_J=A_b x_E and s_J=A_b s_E; E_tot,J=A_b E_tot,E while E_phi,J=E_phi,E/A_b. Thus Q_J=Q/A_b^2 and E_phi,J=2Q_J E_tot,J. The conditional weak tensor normalization G_bare=A_b^2/(8pi Q)=1/(8pi Q_J) gives the physical factors in section5. These are positive quadratic perturbation energies, not an absolute cosmological vacuum energy.

For the supplied scalar candidate, 0<k<1/3, a=(1-k)(1+3k)/4, sigma=(1+k)/(k(1-3k)), Z=exp(2 sqrt(a)u), F=1+sigma Z, J=1+(1-3a)sigma Z, K_uu=J/F^2, and A^2=(1+sigma)Z/F. The remaining kinetic entries are positive and A has no dependence on the other fields. Therefore partial_u log A=sqrt(a)/F and q=alpha_A K^{AB}alpha_B=a/J. Since 1/3-a=(1-3k)^2/12>0 and J>1 at finite background, 0<q<1/3. This derives the ceiling within the supplied sector; it does not derive the action, potential, background or actual masses. The optional relation G_meas=G_bare(1+q_geom), q_geom>=0, still requires the same environment and a justified measurement geometry. No laboratory value or error budget is silently substituted.

The candidate formulas originate in EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md and EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md at main92574ffe95192cc0724a27e1acad28e42d325115. The antecedent finite-window calculation is SCALAR_FINITE_WINDOW_INITIAL_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-15.md at444fddc785280eb01898986edfc301bda9e8d9df. They identify provenance; all formulas needed for this argument are supplied and rederived here, without reading an ancestor result or treating it as retained authority.

## Exposed count-window inventory

The already-exposed Cassini day169 ODF and its label are pinned by SHA-256 in scripts/cassini_count_window_inputs.json. Before this transform, the campaign registered DEVELOPMENT_TIMING_PROTOCOL_v1.json. The earlier source/processed-count reconstruction is context, not independent gravity evidence. Only those same-day ODF bytes and label enter the timing inventory; later calibration and validation tracks remain unopened.

For a record with nominal center t seconds plus milliseconds and compression d centiseconds, both edges are computed exactly in doubled milliseconds: 2*(1000*t+milliseconds) plus or minus10*d. Doppler types11,12,13 are partitioned by every other static decoded configuration field, including validity, station, bands and reference-frequency fields; time, observable, compression and station-delay values are excluded from the static key. Every interval is retained, sorted by both endpoints and record number, then a new chain starts at each gap, overlap or duplicate. Changing delays remain counted. This is a declared nominal-timing grouping, not a derived physical station/retarded clock map.

All91863 orbit records are accounted:91664 Doppler and199 type37. The Doppler records form8static strata and36contiguous chains, with91628adjacent pairs and28gaps, no overlaps or interval duplicates. All durations are nominal100centiseconds. The raw integer-nanohertz means and duration-weighted centered second moments are computed with exact rational arithmetic. They are descriptive Hz and Hz^2 seconds, not physical velocity residuals or field energies. Distinct streams/chains are not summed as independent energy constraints. The derived weighted-variance identity avoids inversion of a large tridiagonal count matrix when its conditional physical model is justified; the raw inventory does not establish that model.

The source URLs are https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/sce1_169/odf/c32easc2002_169_0000xmmmv0.odf and its paired c32easc2002_169_0000xmmmv0.lbl. SHA-256 values are39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f and37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e respectively. The archive label describes the fixed36byte record fields; no new physical precision is inferred from their storage quantum.

## Proof obligations and empirical separation

| Input or step | Provenance and role | Present scope |
| --- | --- | --- |
| Known count kernels, clock map, direction and nuisance shapes | Explicit reduced measurement model | Contrasts and vector primitive derived; actual radio identification remains open |
| Compact L2 kernels, positive durations and contrast rank | Mathematical domain | Raw auxiliary metric finite; singular/zero response requires feasibility |
| Stable free KG fields and finite joint energy | Supplied local field model | Exact energy-space minimum and nonnegative-mass enclosure proved |
| Constant subluminal reference and full conformal test-body force | Supplied linear response and derived coordinate-force law | Anisotropic tensor and stationary enclosure proved; accelerated paths remain outside this exact formula |
| Positive Q and candidate K,A formulas | Explicit sector and unit normalization | q ceiling and conditional physical conversion derived; action/potential selection remains open |
| Same-environment positive gravity response | Optional measurement premise | No actual environmental calibration supplied |
| Error set and upper field-energy/resource budget | Required quantitative application inputs | Neither inferred from raw frequency spread nor selected for agreement |
| Day169 archive and labels | Exposed development data | Exact nominal timing inventory, no independent scalar test |

The proof chain is count integration by parts to bounded vector contrasts; real Fourier energy to the Gram; Hilbert projection to minimum energy and nuisance/error quotients; on-shell momentum substitution to the inertial matrix; positive spectral weights to the all-mass enclosure; and the displayed normalization to physical energy. The finite-data kernel examples are explicit controls within that linear map. They do not assert theory-wide impossibility, unbounded physically admissible energy or exhaustion of alternative reconstruction routes.

## Execution and review record

The primary runner executes150 count/Gram/error/field controls and81 inertial controls, then reconstructs nominal timing from the two pinned public inputs. The count-energy author controls include separate smooth Fourier fields and direct time observations; individual-mass finite quadratures are supplemented by a mixed-mode sum in the inertial suite. Numerical integration and optimizers are ordinary floating-point controls, not interval-certified continuum proofs. The analytic statements rest on the arguments above.

Independent Gram/count/mass-error implementations were run before access to the corresponding author code. Preserved findings include the vector cancellation condition, L2 kernel domain, positive-definite whitening, zero-coupling/zero-Gram compatibility and the ambiguous subscript repair. The first timing script failed at import because its repository path was wrong; the preserved successor corrects only that setup before any data transform. One deliberately doubled hat-Gram normalization survived the first mutation run because field constructions only bounded energy from below. The repaired control directly compares that Gram to the independently assembled finite-count overlap matrix; the original survivor is preserved. Complete source correspondence, inertial confirmation and publication artifacts are recorded in the campaign pack. These checks are distinct from formal audit and combined landing validation.

The executable source closure consists of the primary, two mathematical helpers, the timing helper, the existing reviewed ODF decoder, and a two-input public manifest. All output is under the requested directory; public data can be downloaded to the specified input cache and must match their byte counts and SHA-256. Package-local integrity reads hash the note, manifest, primary and helpers. Python, NumPy and SciPy are required. The declared timeout is240seconds. The cache is logs/runner-cache/scalar_count_kernel_energy_check.txt. No empirical fit, physical energy estimate or measured-gravity test is emitted.

## Claim-status record

```yaml
target_claim_id: scalar_count_kernel_energy
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: "Count-derived energy requirements for specified free fields and inertial conformal-force responses"
hypothetical_axiom_status: null
admitted_observation_status: "Previously exposed day169 nominal count geometry; no scalar fit or independent observational test"
claim_type_reason: "Positive Gram, minimum-energy and mass/velocity enclosure theorems under explicit operator and measurement hypotheses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: upstream_support
target_blocker_text: "Derive or eliminate the revised scalar theory's remaining initial-state and measurement assumptions"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive the accelerated retarded radio-to-force map and an evidence-based error/resource budget before applying a scalar constraint"
```
