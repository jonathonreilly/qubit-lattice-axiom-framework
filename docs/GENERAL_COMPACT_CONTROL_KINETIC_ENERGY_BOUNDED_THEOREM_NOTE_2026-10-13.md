---
title: "General Compact Control Kinetic Energy Bounded Theorem Note"
claim_id: general_compact_control_kinetic_energy_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
runner: scripts/general_kinetic_identity_2026_10_13.py
assembly_status: publication_prepared_root_review_and_runtime_pending
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied massive free CAR model, specified vacuum, exact fixed control and time hypotheses, conditional actual-cell premises
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: unchanged reviewed conditional cores with exact source and exposure history
next_trace_action: root publication review and source integration; cumulative current-main review and retained audit remain separate
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - two_zero_kinetic_energy_bounded_theorem_note_2026-10-13
  - kinetic_correlation_limits_bounded_theorem_note_2026-10-13
  - energy_adapted_calibration_bounded_theorem_note_2026-10-13
  - calibrated_energy_transfer_bounded_theorem_note_2026-10-13
---

Claim type: bounded_theorem

Publication source wrapper: all five historical cores and the accepted assembly retain their precise hypotheses and exposure history. This note adds canonical metadata and recovery links only. Mean, marginal energy law, fixed correlation tests and finite-mode bounds retain their different control classes, time windows and resources. No joint stochastic process, physical selector or retained status is asserted.

# General compact-control kinetic energy: mean and full law

**Type:** bounded_theorem

Status: conditional-support; bounded theorem source assembly. Two unchanged
cores appear in chronological order: the 301-line mean derivation, followed
by the separately checked 470-line full-law extension. Their historical
pending-review statements remain verbatim. The later exact acceptances are
recorded here; this wrapper supplies no new mathematics.

    actual_current_surface_status: conditional-support
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    conditional_surface_status: supplied massive free CAR model; fixed periodic drive
    hypothetical_axiom_status: null
    admitted_observation_status: null
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

## Theorems and distinct scopes

Both slots are fixed arbitrary real compact smooth functions. The supplied
model has fixed m,v>0, the free vacuum, and drive lambda cos(omega t) with
fixed omega>2m. Limits use T=tau/lambda^2 on bounded kinetic windows.
The 301-line mean core proves only mean-energy convergence. It does not itself
prove the full law, a small operator norm of Z-I, or actual-cell transfer.

The 470-line full-law core adds the full signed-input weighted Born remainder,
the small operator norm of Z-I, and the pair-coordinate/continuous trace-log
argument. Together with the separately proved mean, it gives the marginal
Poisson energy law and W1 convergence. Mean and fixed-characteristic-function
errors have the stated square-root/logarithm bound. No W1 rate is claimed.
The finite-mode and correlation consequences in G25--G27 have their own
kinetic-window norm scale. They do not inherit the two-zero correlation
core's all-time arbitrary-envelope estimate or its stronger rank scale.
The rank lower bound is necessary, nonoptimal and not a detector construction.

The causal-square gain retains matrix order and nonzero internal frequencies.
The strict gap omega-2m, fixed controls and fixed frequency are hypotheses.
The larger control class has a generally nonzero threshold derivative in
its pair density. The full-law core therefore uses a logarithmic secular remainder;
the earlier finite first absolute time moment is not imported. No threshold,
massless, varying-frequency/control, modulated-drive, optimal-rate or finite-
volume conclusion is added. A failed estimate is not a no-go theorem.

Only the full-law core's final actual-cell paragraph supplies a conditional application.
It requires the exact common energy embedding/vacuum, real fixed-support
finite-order weighted input calibration and finite-first-energy work bound.
State/law transfer uses the stated epsilon_a=o(|lambda|) condition; mean/W1
transfer uses epsilon_a=o(lambda^2). N and all required seminorm resources
are fixed. Images need not satisfy a zero-integral condition. No calibration,
Fock-domain or unbounded-energy premise is discharged by a status label.

## Review, dependency and exposure history

The mean core is KINETIC_MEAN_RELAXED_CONTROLS_DERIVATION.md, SHA-256
0991b928e681892c5c3d3d514cd781c8fd0bf779f4cca07a2d525dd69bad4498.
Its author read corrected 859 and the 244/73 reviews while excluding root
kinetic/correlation proofs before freeze. The later one-zero comparison
was by this same mean-proof author and cannot independently certify the mean core.
Fresh 164/a20a5d24 is the subsequent non-author, same-family exposed check;
GENERAL_KINETIC_MEAN_ROOT_ACCEPTANCE.json binds it and its finite diagnostic
evidence. That evidence is archived, not rerun or treated as continuum proof.

The full-law core is GENERAL_KINETIC_LAW_ROOT_PROBE.md, SHA-256
6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b.
It was derived after exposure to 301, corrected 859 and prior correlation
machinery. Fresh 140/750f1502 and its 133-line analytic evidence check its
new arguments after exposure, at unchanged model/effort. The root acceptance
of 2026-10-13T10:43:47Z, SHA-256
a55573418998e6b496f985f3066835326ea8e74ef1fbb27c54a42bbc37ce422e,
binds exact 470 and the 14-file review freeze. No numeric or Lean diagnostic
was run for 470. Distinct analytic checks by one reviewer are not separate
independent reviewers, model diversity, retained status or formal proof.

Corrected 859 owns the common CAR/picture/pair-normalization machinery.
Correlation 335 supplies the cited finite-mode and compact-Fock proof steps;
470 separately proves the norm estimates needed for general controls.
Canonical calibration/transfer parents and archived historical inputs are
mapped in DEPENDENCIES.json and CANONICAL_CORE_MAP.json. The source assembly
is exposed to all listed arguments and does not claim new independence.
Original 847's picture defect and the root missed check remain archived.
No future publication base or physical selector is selected here.

## Unchanged general-control mean core


# Kinetic mean for general compact smooth controls in the supplied free CAR model

Status: conditional-support; author analytic derivation, awaiting independent review. This note supplies a bounded theorem in the stated free model. It supplies no formal retained status, physical model selection or empirical prediction.

    actual_current_surface_status: conditional-support
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    conditional_surface_status: supplied gapped free CAR dynamics and periodic drive
    hypothetical_axiom_status: null
    admitted_observation_status: null
    claim_type_reason: exact mean limit from explicit supplied model data
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

## 1. Statement and fixed premises

Use exactly the corrected picture conventions of the supplied V2 source. On K=L2(R;C^2), with the unitary momentum Fourier transform, let

    D(p)=-vp sigma_x-m sigma_y,
    E(p)=sqrt(m^2+v^2p^2),
    P=(I+D/E)/2, P_-=I-P,

where m,v>0 are fixed. Real conjugation is Gamma hhat(p)=overline(hhat(-p)). The positive one-particle space is P K and the free Fock energy is H0=dGamma(E|_(P K)), with its free vacuum Omega.

Let f,g be any fixed real C_c^infinity(R;R^2) smearings. Set

    F(z1,z2)=z1 f+z2 g,
    k=2i [[0,1],[-1,0]],
    K_V=F k F*,
    Q=(i/2)[gamma(f),gamma(g)],
    V=Q-<Omega,Q Omega>I.

The Fock Hamiltonian is H0+lambda cos(omega t)V. Write W_lambda for its full propagator, Y_lambda=exp(itH0)W_lambda for the interaction propagator, S_lambda for the one-particle propagator of D+lambda cos(omega t)K_V, and Z_lambda=exp(itD)S_lambda. The exact identities supplied and checked in V2 are

    Y_lambda(t)* gamma(h)Y_lambda(t)=gamma(Z_lambda(t)*h),
    i Z_lambda'(t)=lambda c(t)F_t k F_t*Z_lambda(t),
    F_t=exp(itD)F, c(t)=cos(omega t),
    E_lambda(T)=||H0^(1/2)Y_lambda(T)Omega||^2
              =||E^(1/2)P Z_lambda(T)P_-||_HS^2.          (1)

Both sides are nonnegative energy forms; the finite-time weighted estimates below show that they are finite. The full and interaction states have the same H0 law and mean.

In the scalar positive-band frame of V2, put u=sqrt(2)Pf, w=sqrt(2)Pg and

    Delta(p,q)=u(p)w(q)-w(p)u(q),
    r(s)=(1/2) integral |Delta(p,q)|^2
                         delta(s-E(p)-E(q)) dp dq.       (2)

Here r is the ordinary pushforward density proved in V2, extended by zero below 2m. For arbitrary compact smooth f,g it is continuous, nonnegative, rapidly decreasing, and r(2m+x)=O(x). No zero-integral premise is needed for these properties.

**Theorem (mean only).** For every fixed omega>2m and every finite tau_star>=0, as real lambda tends to zero through nonzero values,

    sup_(0<=tau<=tau_star)
      |E_lambda(tau/lambda^2)
                -tau (pi/2)omega r(omega)| ->0.         (3)

In fact, for sufficiently small h=|lambda|, the left side is at most

    C_tau_star h^(1/2) sqrt(log(2+h^(-2))).              (4)

The constants may depend on the fixed m,v,omega,f,g and tau_star. No uniformity as omega approaches 2m, as m approaches zero, or as the controls or frequency vary is asserted. Componentwise zero integrals of either smearing are unnecessary for (3). In particular, the requested case with one zero-integral smearing and the other arbitrary is included.

This is an exact mean theorem. No extension of the full Poisson energy law, Wasserstein convergence, finite-volume dynamics, or lattice calibration is claimed here. Those conclusions require their own additional argument.

## 2. Exact causal equation and norm spaces

For T<infinity let

    X(t)=F_t* Z_lambda(t)P_-,
    X0(t)=F_t*P_-,
    G(t)=F*exp(-itD)F, t>=0.

These are two-channel row operators from K to C^2. They belong to L2([0,T];HS(K,C^2)); for example ||X(t)||_HS<=||F||_HS by unitarity. The exact integral equation is

    X=X0+lambda L_T X,
    (L_T x)(t)=-i integral_0^t G(t-s)c(s)k x(s)ds.       (5)

The same operator L_T acts on L2([0,T];C^2) and on Hilbert--Schmidt-valued columns, with identical norm bounds. All following bounds are on these spaces, unless a different space is stated.

There are fixed constants C0,C2 for which

    ||L_T|| <= C0 sqrt(1+T),
    ||L_T^2|| <= C2 sqrt(1+T).                          (6)

The second inequality is a bound on the operator square, not the square of the first bound. Section 4 proves the oscillatory gain that distinguishes them. This is the main replacement for the absolute L1 correlation bound used in V2.

When h^2 C2 sqrt(1+T)<1, the algebraic factorization gives the genuine bounded inverse

    (I-lambda L_T)^(-1)
       =(I+lambda L_T)(I-lambda^2 L_T^2)^(-1),

    ||(I-lambda L_T)^(-1)||
       <=[1+h C0 sqrt(1+T)]/[1-h^2 C2 sqrt(1+T)].        (7)

Every factor here is a polynomial or norm-convergent series in the same L_T, so both left and right inverse identities hold. For 0<=T<=tau_star/h^2 and sufficiently small h, the denominator is at least 1/2 and the right side is bounded by a constant depending on tau_star. No expansion small in hT is used.

## 3. Threshold expansion and synthesis estimate

For t>=0 define q(t)=(1+t)^(-1/2). The channel correlation has the decomposition

    G(t)=q(t)[exp(-imt)A_+ +exp(imt)A_-]+R(t),
    ||R(t)||<=C(1+t)^(-3/2),                           (8)

where A_+,A_- are fixed two-by-two matrices. In particular ||G(t)||<=C q(t), giving the first inequality in (6) by Young's inequality.

Here is a proof of the remainder in (8), not merely a leading asymptotic assertion. Split D into its positive and negative projections and make the smooth odd change

    p(y)=y sqrt(2m+y^2)/v, E(p(y))=m+y^2.

Each matrix entry becomes exp(+-imt) integral exp(+-it y^2)a(y)dy with a Schwartz function. For t>=1, Fourier inversion and the damped Gaussian integral give

    integral exp(+-it y^2)a(y)dy
       =exp(+-i pi/4)sqrt(pi/t)
          (1/(2pi)) integral ahat(xi)exp(-+i xi^2/(4t))dxi.

The Fourier transform in this display is the nonunitary transform of the amplitude a. Since integral ahat(xi)dxi/(2pi)=a(0) and
|exp(-+i xi^2/(4t))-1|<=xi^2/(4t), the error after the leading term is at most C t^(-3/2) integral xi^2|ahat(xi)|dxi. Gaussian damping justifies the oscillatory identity: its Fourier kernel has modulus at most sqrt(pi/t), uniformly as the damping tends to zero, so the Schwartz Fourier transform supplies domination. Replacing t^(-1/2) by q(t) changes the remainder by O(t^(-3/2)). Boundedness on 0<=t<=1 completes (8).

The transformed amplitudes are Schwartz because p(y) and its derivatives have polynomial growth, P_+(p),P_-(p) are smooth for m>0, and fhat,ghat are Schwartz. The same proof permits any fixed nonnegative energy power and either fixed band projection.

Define the positive-band energy synthesis map on [0,T] by

    S_E,T z=integral_0^T E^(1/2)P F_t z(t)dt.

Its Gram kernel is F_t*P E F_s. The preceding weighted correlation estimate bounds its matrix norm by C(1+|t-s|)^(-1/2). Schur's test therefore gives

    ||S_E,T||^2 <= C sqrt(1+T),
    ||S_E,T|| <= C(1+T)^(1/4).                          (9)

The same estimate holds for Hilbert--Schmidt-valued z, by applying it to each input basis vector and summing. At finite T the integral exists in the weighted graph norm, since its two fixed smearing vectors lie in every fixed energy graph domain and L2([0,T]) is contained in L1([0,T]). Thus (9) identifies actual energy-weighted vectors, not a formal unbounded trace manipulation.

## 4. Oscillatory estimate for the causal square

For sigma in {+1,-1}, define

    H_sigma(r)=integral_0^r
          G(r-v)exp(i sigma omega v)k G(v)dv.            (10)

The kernels are bounded on each finite interval and L2 is contained in L1 there, so Fubini applies on the finite causal triangle. Changing the order in L_T^2 gives exactly

    (L_T^2 x)(t)=-(1/2) sum_sigma integral_0^t
       H_sigma(t-s)exp(i sigma omega s)c(s)k x(s)ds.    (11)

The ordering of k and G is retained. The multiplication factors after H_sigma have uniformly bounded norm.

For any alpha,beta in {-m,+m}, the product of two leading terms of (8) in (10) has scalar integral

    exp(i alpha r) integral_0^r
       q(r-v)q(v)exp(i delta v)dv,
    delta=beta+sigma omega-alpha.

Since omega>2m,

    |delta|>=omega-2m>0.                               (12)

To obtain a uniform decay estimate, put a_r(v)=q(r-v)q(v). This positive function decreases on [0,r/2] and increases on [r/2,r], with a_r(0)=a_r(r)=q(r). Its total variation is at most 2q(r). Integration by parts against exp(i delta v) therefore proves

    |integral_0^r a_r(v)exp(i delta v)dv|
       <=4 q(r)/|delta|.                              (13)

Terms with one remainder are bounded absolutely by convolutions of q with (1+t)^(-3/2); splitting at r/2 gives

    integral_0^r q(r-v)(1+v)^(-3/2)dv <=C q(r),

and the reversed convolution obeys the same bound. Two remainders are no larger at the required order. Combining the finitely many matrix terms yields

    ||H_sigma(r)||<=C_omega q(r), all r>=0.             (14)

Young's inequality in (11), followed by integral_0^T q(r)dr<=2sqrt(1+T), proves the second inequality in (6). This argument does not assume commutativity of the channel matrices, an infinite-time convolution inverse, or interchange of finite volume and infinite time.

## 5. The first causal correction has only a logarithmic threshold cost

The second ingredient is the Hilbert--Schmidt forcing estimate

    ||L_T X0||_(L2 HS)
          <=C sqrt(T log(2+T)).                        (15)

The remainder R in (8) contributes a uniformly bounded Hilbert--Schmidt row at each time, since R is integrable and ||X0(t)||_HS=||F*P_-||_HS.

Write C_(-m)=A_+ and C_(+m)=A_- for the two coefficients in (8). For a leading term exp(i alpha r)q(r)C_alpha, alpha in {-m,+m}, use r=t-s and expand c(s) into its two exponentials. In momentum space the row kernel of its contribution, up to fixed matrix factors and the factor 1/2, is

    exp(i(E(p)+sigma omega)t)
       J_t(E(p)+sigma omega-alpha) C_alpha k Fhat(p)*P_-(p),
    J_t(z)=integral_0^t q(r)exp(-izr)dr.                (16)

Here Fhat(p) is the matrix with columns fhat(p),ghat(p). Direct splitting at |z|^(-1), followed by one integration by parts on the remaining monotone tail, proves

    |J_t(z)|^2 <= C min(1+t,|z|^(-1)), z!=0;           (17)

at z=0 use the first bound. For |z|>=1 integration by parts gives the stronger bound |J_t(z)|<=C/|z|. No claim of absolute time integrability of q is made.

Change the input momentum to its positive energy epsilon=E(p). The nonnegative matrix-weight majorant is

    w_-(epsilon)=sum_(p=+-sqrt(epsilon^2-m^2)/v)
           ||Fhat(p)*P_-(p)||_HS^2/|E'(p)|,
    integral_m^infinity w_-(epsilon)d epsilon
                                 =||F*P_-||_HS^2.

It is bounded on each compact interval strictly inside (m,infinity), is at most C(epsilon-m)^(-1/2) near m, and decreases rapidly at infinity. The possible roots in (16) are epsilon_0=alpha-sigma omega. For sigma=+1 they lie below the input spectrum. For sigma=-1 they are omega-m and omega+m, both strictly above m because omega>2m. Thus any root is either separated from the input spectrum or lies in an interval where w_- is bounded. In particular no root coincides with the input threshold.

Around an interior root choose a fixed small interval disjoint from m. On that interval (17) gives

    integral w_-(epsilon)|J_t(epsilon-epsilon_0)|^2d epsilon
       <=C integral_(-a)^a min(1+t,|x|^(-1))dx
       <=C log(2+t).

Outside it, the argument of J_t is separated from zero and the integrability of w_- gives a uniform bound. The same uniform bound covers roots outside the spectrum. The finite sum of these estimates and the R contribution show

    ||(L_T X0)(t)||_HS <=C sqrt(log(2+t)).

Integrating its square over [0,T] proves (15). This bound uses the continuum input spectral measure explicitly; replacing it by the crude operator norm of X0 would lose the needed gain.

## 6. Exact-to-Born estimate on the kinetic interval

Let B(T)=PZ_lambda(T)P_-, and let

    B1(T)=-i lambda integral_0^T c(t)P F_t k F_t*P_-dt.

From (5), (7), and (15), for 0<=T<=tau_star/h^2 and sufficiently small h,

    ||X-X0||_(L2 HS)
      <=C_tau_star h sqrt(T log(2+T)).                 (18)

The exact output integral, (9), and bounded multiplication by c(t)k give

    ||E^(1/2)[B(T)-B1(T)]||_HS
      <=C_tau_star h^2 (1+T)^(1/4)
                                  sqrt(T log(2+T)).   (19)

Hence uniformly on those intervals,

    ||E^(1/2)[B(T)-B1(T)]||_HS
      <=C_tau_star h^(1/2)sqrt(log(2+h^(-2))) ->0.      (20)

This proves the exact sufficient obligation (41) from V2 for all the compact smooth smearings under consideration and fixed omega>2m. It does not infer that obligation merely from equality of scalar norms.

For clarity about the powers, h^2 sqrt(T)(1+T)^(1/4) is bounded by h^(1/2)sqrt(tau_star)(h^2+tau_star)^(1/4). The inverse in (7) stays bounded because h^2 sqrt(1+T)<=h sqrt(h^2+tau_star), while its numerator is bounded by 1+C sqrt(h^2+tau_star).

Every finite-time weighted block is well-defined independently of these estimates: the output integral contains only E^(1/2)P f_t and E^(1/2)P g_t multiplying bounded Hilbert--Schmidt rows. Finite-time integration in the graph norm and closedness of E^(1/2) identify it with the weighted block. Thus no domain conclusion has been inferred from an unproved asymptotic limit.

## 7. The mean and its coefficient

The exact Born identity from the supplied normalization is

    ||E^(1/2)B1(T)||_HS^2
       =lambda^2 integral b(s)|I_T(s)|^2ds,
    b(s)=s r(s),
    I_T(s)=integral_0^T cos(omega t)exp(ist)dt.          (21)

Since b is bounded, temporal Plancherel immediately gives

    ||E^(1/2)B1(T)||_HS^2
       <=2pi ||b||_infinity h^2 T.                     (22)

Thus the Born weighted norm is uniformly bounded on bounded kinetic intervals. Equations (20), (22), and the difference-of-squared-norms inequality give an exact-minus-Born mean error bounded by the right side of (4).

For the secular coefficient write I_T=(Q_T(s-omega)+Q_T(s+omega))/2, with Q_T(x)=integral_0^T exp(ixt)dt. The kernels |Q_T(x)|^2/T are nonnegative approximate identities of total integral 2pi. Since b is continuous at the fixed omega,

    (1/T) integral b(s)|Q_T(s-omega)|^2ds ->2pi b(omega).

The counterrotating square is bounded uniformly by 4 integral b(s)/(s+omega)^2ds, because b is supported in [2m,infinity). Its cross term with the resonant square is O(sqrt(T)). Consequently

    integral b(s)|I_T(s)|^2ds
                         =(pi/2)T b(omega)+o(T).       (23)

One may keep an explicit uniform error: b is smooth in a neighborhood of omega>2m, so |b(omega+x)-b(omega)|<=C|x| for small x. Splitting the resonant kernel at |x|=1/T and a fixed neighborhood, and using |Q_T(x)|<=min(T,2/|x|), bounds its remainder by C log(2+T). The counterrotating and cross terms therefore give an O(log(2+T)+sqrt(T)+1) remainder in (23). Multiplication by h^2 makes this O_tau_star(h) uniformly for 0<=T<=tau_star/h^2, after harmless enlargement for small T. This is smaller than (4).

Combining (1), (20)--(23) proves (3)--(4), with the same coefficient (pi/2)omega r(omega) as the supplied theorem. The factors pi/2 and the exterior 1/2 in r are inherited from the checked exact normalization and reappear from the positive-frequency half of the cosine; no rate was fitted.

At tau=0 the energy is exactly zero. If either smearing vanishes, or g is a real scalar multiple of f, the control and density vanish and the conclusion is consistent. No strict positivity is asserted for arbitrary nonzero controls. Negative lambda is covered by h=|lambda|. The theorem is for fixed positive frequency strictly above 2m only.

## 8. The requested one-zero case and search record

The main argument includes the requested one-zero-integral case. An initial mixed-channel attempt is preserved in kinetic_mean_relaxed_controls/proof/ONE_ZERO_WORKING.md as a working recovery artifact. It suggested separating the large threshold correlation from the feedback estimate. The complete argument above supersedes that attempt; no conclusion in this final note depends on its additional claims or on a second review of that working file.

The crude unrestricted absolute-value estimate ||L_T||=O(sqrt(T)) alone cannot be inverted by a Neumann series on the entire kinetic interval at arbitrary fixed tau. This is a failed estimate, not a counterexample. The useful new step is to retain the periodic phase through two causal interactions, proving ||L_T^2||=O(sqrt(T)) rather than O(T), and then use the exact polynomial factorization. The distinct logarithmic forcing estimate uses separation of the input threshold from the shifted internal thresholds. Both gains are proved for the continuum before taking the long-time limit.

No counterexample or broad impossibility result was sought as a required outcome. The exact mean for frequencies at the threshold, the massless limit, full energy-law extension and optimal rates are not resolved by this note. The failure of estimate (12) at omega=2m identifies the limit of this proof, not the truth or falsity of the mean theorem there.

## 9. Sources, exposure and verification boundaries

The only scientific source bodies read were the following exact files under the assigned run directory:

| Source | Lines | SHA-256 |
|---|---:|---|
| WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md | 859 | c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b |
| KINETIC_POISSON_LAW_FRESH_REVIEW.md | 244 | 39a689492e3710536a4ad7707887fb81124485ba268666cbedaef0868dff7fd0 |
| KINETIC_POISSON_PICTURE_V2_CONFIRMATION.md | 73 | c2aa65ec0dcb1150e28c9a17afd0b48e14a458083503d558f9df5069d3b8b8ae |

All three hashes and line counts matched the dispatch. The primary source was read completely in the ranges 1--300, 301--600 and 601--859. The review and confirmation were read completely; an initially truncated aggregate review display was supplemented with an untruncated read of the missing central argument. Referenced upstream sources and author numerical scripts were not opened and are not newly certified. Section 8 of V2 and its transfer premises are outside the new conclusion.

The neutral plan was frozen before reading any scientific source body, SHA-256 c4be1fa6db1de124f72119ebcf75680c62ffb9a01d534653f73e697070871dfe. Instructions were read by read-only Git from main 516cb69d8487ff04f8a48e065d3dcbe71d7dd237 and ai/execution 3a4b2c66a1ead7a1c48b4359627e968f681e3c39. Procedure snapshots are retained under evidence/instructions. No fetch was permitted, so these are dispatch-pinned identities, not a newly observed remote state. Broader source/registry/PR sweeps were excluded by the bounded scientific-source contract; no primitive or formal status judgment is inferred from those unperformed reads.

An initial overbroad instruction-filename inventory exposed filenames only and was truncated; it establishes no scientific source coverage. No excluded root kinetic/correlation probes, other worker mathematics, pair notes, checkpoints or source assemblies were read. No external literature was used. The analysis uses the inherited selected model and effort, without substitution or additional agents.

This proof is source-exposed to the original causal formulation and supplied free model. Its threshold decomposition, operator-square bound, polynomial inverse and forcing estimate are new author reasoning within this context, not an independent review of themselves. No finite diagnostic is used as proof of an infinite-time limit. No Lean/formal checker, numerical continuum simulation, finite-volume approximation, or limit interchange was performed. Independent review of the new load-bearing argument remains necessary before substantial downstream reuse.

Only this derivation and the assigned kinetic_mean_relaxed_controls subtree were written. No Git, correlation-worktree, prompt, cache, graph, PR, audit or external-message mutation occurred. No editable prompt file changed.

Final cold-read checks, input refresh, exact source identity and seal are recorded in the evidence/checkpoint/freeze directories. The next decision is a focused independent analytic check of (8)--(20), especially the noncommuting causal square, the shifted-threshold forcing measure, and the uniform kinetic scaling. The mean extension does not by itself supply a full probability-law extension.

## Unchanged general-control full-law core

The following 470 was frozen while 301's fresh review and its own review were
pending. Those historical statements remain unchanged inside the core.
The two later exact acceptances and complete 140/133 check are recorded in
the wrapper above. This is a separate full-law proof; it does not retroactively
expand the mean-only theorem 301 or erase earlier exposure exclusions.


# Kinetic energy law for arbitrary compact smooth control slots

Status: conditional-support, new source-exposed root construction awaiting
independent check. The supplied gapped free CAR model is a premise. No physical
selector, empirical prediction, formal Lean verification or retained audit is
claimed. The general mean301 argument is provisional until its fresh review.

## 1. Exact scope and statement

Use the corrected full/interaction conventions of kinetic V2,859 lines,
SHA c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b.
Its earlier picture defect and repair remain preserved. The new input is
KINETIC_MEAN_RELAXED_CONTROLS_DERIVATION.md,301 lines,
SHA 0991b928e681892c5c3d3d514cd781c8fd0bf779f4cca07a2d525dd69bad4498.
Root read it after sealing the separate one-zero proof. The present argument
is an extension after exposure, not an independent derivation of that mean.

Let K=L2(R;C^2), with unitary momentum transform, and fixed m,v>0. Set

    D(p)=-vp sigma_x-m sigma_y,
    E(p)=sqrt(m^2+v^2p^2), P=(I+D/E)/2, P_-=I-P.

Real conjugation is Gamma hhat(p)=overline(hhat(-p)); Gamma D Gamma=-D.
The physical Fock carrier here is Fock(h), h=PK, with H0=dGamma(E|h)
and vacuum Omega. The inner product is linear in its second slot and a is
antilinear. For a real slot f, gamma(f)=a*(sqrt(2)Pf)+a(sqrt(2)Pf).

Fix arbitrary real f,g in C_c^infinity(R;R^2). There is no zero-integral
restriction on either slot. Put F=(f,g), M=2i[[0,1],[-1,0]], B=FMF* and
V=(i/2)[gamma(f),gamma(g)] minus its vacuum expectation. Fix omega>2m.
The drive is exactly c(t)=cos(omega t). Let W be the full propagator of
H0+lambda c(t)V, Y=exp(itH0)W, S the full propagator of D+lambda c(t)B,
and Z=exp(itD)S. Every propagator has initial value I. The exact identities are

    W*gamma(h)W=gamma(S*h), Y*gamma(h)Y=gamma(Z*h),
    N(T)=P Z(T)P_- Z(T)* P,
    E_lambda(T)=||E^(1/2)P Z(T)P_-||_HS^2.              (G1)

The full and interaction states have the same H0 law. The positive energy
identity follows from finite-rank and bounded energy cutoffs and monotone
convergence; the finite weighted bounds below establish its finiteness.

Write h_lambda=|lambda| and, for 0<h_lambda<=1, define

    eta_lambda=sqrt(h_lambda log(2+h_lambda^(-2))).

For every fixed tau_star<infinity and fixed q>=0 there are finite constants
and h0>0 such that, on 0<h_lambda<=h0 and 0<=T<=tau_star/lambda^2,

    ||Z(T)-I||<=C eta_lambda,
    ||E^(q/2)[Z(T)-I-K1(T)]||_HS<=C_q eta_lambda,       (G2)
    K1(T)=-i lambda integral_0^T c(t)F_t M F_t*dt,
    F_t=exp(itD)F.

Thus the second assertion is for the full one-particle map, not only its
off-diagonal block. Let r be the exact exterior-pair density defined below.
For T=tau/lambda^2 the claimed complete energy law is

    mu_lambda,T -> Law(omega N_tau),
    N_tau~Poisson(tau nu_omega), nu_omega=(pi/2)r(omega),
    E_lambda(T) -> tau omega nu_omega.                 (G3)

The law convergence is weak and in W1. Mean and each fixed characteristic
function have error O(eta_lambda), uniformly for bounded tau intervals.
Constants depend on the fixed data and, for characteristic functions, the
fixed Fourier variable. No uniform omega->2m, m->0, arbitrary-envelope,
fixed-lambda all-time, moving-control or interacting-spectrum claim is made.

## 2. Causal square and its bounded inverse

This section reconstructs the new mean argument and changes its input space
to the whole K. On H_T=L2([0,T];C^2), define

    X(t)=F_t*Z(t):K->C^2, X0(t)=F_t*,
    G(t)=F*exp(-itD)F,
    (L_T x)(t)=-i integral_0^t G(t-s)c(s)M x(s)ds.

Unitarity gives ||X(t)||_HS=||F||_HS, so these are actual finite-time
Hilbert--Schmidt-valued L2 functions. Bounded Dyson integration gives exactly

    X=X0+lambda L_T X.                                (G4)

All matrix orders are fixed as written. L_T acts on time-channel space and
on its Hilbert--Schmidt amplification with the same bounds.

There are fixed matrices A_+,A_- such that, with q0(t)=(1+t)^(-1/2),

    G(t)=q0(t)[exp(-imt)A_+ +exp(imt)A_-]+R(t),
    ||R(t)||<=C(1+t)^(-3/2), t>=0.                    (G5)

To justify the error, split both massive bands and use the smooth odd
coordinate p(y)=y sqrt(2m+y^2)/v, E=m+y^2. Each entry becomes a phase
exp(+-imt) times integral exp(+-ity^2)a(y)dy with a Schwartz amplitude.
The damped Gaussian Fourier identity gives, for t>=1, the leading value
exp(+-i pi/4)sqrt(pi/t)a(0) with an error at most
C t^(-3/2) integral xi^2 |ahat(xi)|dxi. The Fourier transform of a here
is nonunitary. The inequality |exp(ix)-1|<=|x| supplies this remainder;
Gaussian damping and Schwartz domination justify the identity and limit.
Replacing t^(-1/2) by q0(t) adds O(t^(-3/2)). Bounded small times complete
(G5). The same argument holds with any fixed energy power and band inserted.

Consequently ||L_T||<=C0 sqrt(1+T). The crucial stronger square bound is

    ||L_T^2||<=C2 sqrt(1+T),                           (G6)

not C(1+T). Indeed, for sigma=+-1 let

    H_sigma(r)=integral_0^r G(r-s)exp(i sigma omega s)M G(s)ds.

Finite-time Fubini gives the noncommuting identity

    (L_T^2 x)(t)=-(1/2)sum_sigma integral_0^t
       H_sigma(t-s)exp(i sigma omega s)c(s)M x(s)ds.   (G7)

The leading-leading pieces of H_sigma have scalar factor

    exp(i alpha r) integral_0^r q0(r-s)q0(s)
                      exp(i(beta+sigma omega-alpha)s)ds,
    alpha,beta in {-m,m}.

Every internal frequency has modulus at least omega-2m. The positive
amplitude q0(r-s)q0(s) decreases then increases, has both endpoint values
q0(r), and total variation at most2q0(r). Integration by parts bounds
the integral by4q0(r)/(omega-2m). A piece containing a remainder is bounded
by q0*(1+t)^(-3/2)<=C q0, by splitting at r/2. Thus
||H_sigma(r)||<=C q0(r). Young's inequality proves (G6) without reordering
any matrix. The proof uses the periodic phase essentially.

The exact polynomial identity therefore gives

    (I-lambda L_T)^(-1)
       =(I+lambda L_T)(I-lambda^2 L_T^2)^(-1),
    ||(I-lambda L_T)^(-1)||
       <=[1+h_lambda C0 sqrt(1+T)]/
                         [1-h_lambda^2 C2 sqrt(1+T)]. (G8)

For T<=tau_star/h_lambda^2 the denominator is at least1/2 after choosing
h0 small, while the numerator is bounded by a constant depending on
tau_star. Both inverse identities hold because all factors are series or
polynomials in L_T. This controls arbitrarily large fixed tau_star; it
does not require h_lambda sqrt(T) small.

## 3. Full input forcing and the weighted remainder

The new point relative to the mean-only input is to check both initial
spectral signs. Let P_epsilon=(I+epsilon D/E)/2 for epsilon=+-1.
On this band the free row is Fhat(p)*P_epsilon(p)exp(-i epsilon E(p)t).
A leading term exp(i alpha r)q0(r)A_alpha of G contributes to L_T X0 a
finite sum of rows, with scalar factor

    exp(i(-epsilon E(p)+sigma omega)t)
         J_t(-epsilon E(p)+sigma omega-alpha),
    J_t(z)=integral_0^t q0(s)exp(-izs)ds.              (G9)

The fixed matrix order is A_alpha M Fhat(p)*P_epsilon(p). A sign reversal
in the phase of J_t is immaterial for its absolute bound, but (G9) follows
directly from r=t-s, rather than swapping input/output bands implicitly.

Splitting the defining integral at1/|z| and integrating its monotone tail
by parts gives

    |J_t(z)|^2<=C min(1+t,1/|z|), z!=0.               (G10)

For |z|>=1 one also has |J_t(z)|<=C/|z|. At z=0 use the first bound.
The spectral majorant of each input row is

    w_epsilon(e)=sum_(p=+-sqrt(e^2-m^2)/v)
       ||Fhat(p)*P_epsilon(p)||_HS^2/|E'(p)|, e>m.

It is integrable, at most C(e-m)^(-1/2) near m, bounded on compact
interior intervals, and rapidly decreasing at infinity. A root of the
argument in (G9) has e=epsilon(sigma omega-alpha). Its possible values
are +(omega-m), +(omega+m), -(omega-m), -(omega+m). Positive roots are
strictly above m; negative roots are separated from [m,infinity). Thus
no input band has a resonance at its threshold. This is the full-input
check that cannot be inferred just from the negative-band mean theorem.

Near each interior root use bounded w_epsilon and (G10):

    integral_(-a)^a min(1+t,1/|z|)dz<=C log(2+t).

Outside the chosen root intervals the integrability of w_epsilon gives
a uniform bound. The integrable remainder in (G5) gives a uniformly bounded
HS row, since ||X0(t)||_HS=||F||_HS. Summing the finite bands and phases,

    ||(L_T X0)(t)||_HS<=C sqrt(log(2+t)),
    ||L_T X0||_(L2 HS)<=C sqrt(T log(2+T)).             (G11)

Combining (G4),(G8),(G11) proves

    ||X-X0||_(L2 HS)<=C_tau_star h_lambda
                                         sqrt(T log(2+T)). (G12)

For fixed q>=0 the full weighted synthesis map

    S_q z=integral_0^T E^(q/2)F_t z(t)dt

has norm at most C_q(1+T)^(1/4). Its Gram kernel is the weighted form of
(G5), bounded by C_q(1+|t-s|)^(-1/2), so Schur's inequality proves the
claim. All finite-time integrals exist in the graph norm because f,g are
in every fixed energy domain. Closedness identifies the weighted output;
no energy trace is justified by unweighted convergence alone.

The exact Dyson output gives

    E^(q/2)[Z(T)-I-K1(T)]=-i lambda S_q cM(X-X0),
    ||E^(q/2)[Z(T)-I-K1(T)]||_HS
       <=C_q,tau_star h_lambda^2(1+T)^(1/4)
                                        sqrt(T log(2+T))
       <=C_q,tau_star eta_lambda.                     (G13)

This establishes the second part of (G2). In particular the full remainder
has small operator norm at q=0. It remains necessary to control the full
Born operator norm; its HS norm need not vanish on this time scale.

## 4. Threshold-separated Born operator estimate

Choose a fixed a>0 with2a<omega-2m. Let chi be a real smooth function on
[0,infinity), equal to1 near0, zero for x>=a, and between0 and1. Define

    F_near=chi(E-m)F, F_far=(I-chi(E-m))F.

These columns are smooth in momentum, are Schwartz and retain the real
structure. They need not retain compact spatial support; here they are only
an auxiliary decomposition of the exact Born operator, not new controls.
The full synthesis maps for these columns satisfy

    ||S_near||<=C(1+T)^(1/4), ||S_far||<=C.            (G14)

For the second bound, the Gram amplitudes vanish in a neighborhood of the
only stationary point p=0. Repeated nonstationary integration by parts gives
an integrable time kernel; Schwartz decay controls infinity. The first bound
is the unweighted version of the previous Schur estimate.

Expand K1 into its four near/far terms. Every term with at least one far
slot is -i lambda S_j cM S_k*, and hence has norm at most
C h_lambda(1+T)^(1/4) by (G14). For the remaining near-near term, write its
momentum matrix kernel as a sum over epsilon,epsilon',sigma in {+1,-1}:

    (-i lambda/2) P_epsilon(p)F_near(p)M F_near(q)*
       P_epsilon'(q) Q_T(epsilon E(p)-epsilon'E(q)+sigma omega),
    Q_T(z)=integral_0^T exp(izt)dt.                    (G15)

On the support of this kernel E(p),E(q)<=m+a. Therefore

    |epsilon E(p)-epsilon'E(q)+sigma omega|
                                  >=omega-2(m+a)>0.

Using |Q_T(z)|<=2/|z| and the L2 column norms bounds the entire near-near
kernel in HS norm by C h_lambda, uniformly in T. No oscillatory operator
norm is replaced by its pointwise value without this square-integrable
kernel majorant. The finite band sum and finite channel matrix cause only
fixed constants. Thus

    ||K1(T)||<=C h_lambda(1+T)^(1/4).                  (G16)

On the kinetic interval this is O(sqrt(h_lambda)). Equations (G13),(G16)
give ||Z-I||<=C eta_lambda and complete (G2). The threshold window depends
on the fixed frequency gap; no uniform threshold assertion follows.

## 5. Pair density regularity and secular normalization

In the scalar positive-band frame set

    e_+(p)=(exp(i theta(p)/2),-i exp(-i theta(p)/2))/sqrt(2),
    theta(p)=arctan(vp/m),
    u(p)=sqrt(2)e_+(p)*fhat(p), w(p)=sqrt(2)e_+(p)*ghat(p),
    Delta(p,q)=u(p)w(q)-w(p)u(q).

The pair vector is u wedge w, with scalar wavefunction Delta/sqrt(2), and
V Omega=i(u wedge w). Its exact energy density is

    r(e)=(1/2)integral |Delta(p,q)|^2
                              delta(e-E(p)-E(q))dpdq. (G17)

For completeness, this density has more regularity than mere continuity.
Apply p(x)=x sqrt(2m+x^2)/v separately to each momentum. The function

    A(x,y)=|Delta(p(x),p(y))|^2 p'(x)p'(y)

is smooth and Schwartz on R^2. Antisymmetry gives A(0,0)=0 and its gradient
is zero. Polar coordinates give, for s>=0,

    r(2m+s)=(1/4)integral_0^(2pi)
                    A(sqrt(s)cos(theta),sqrt(s)sin(theta))d theta.

The angular average is smooth in s down to0: Taylor expand to any desired
finite order, note that every odd homogeneous polynomial averages to zero,
and use the smooth remainder at the correspondingly higher even order.
This argument applied to derivatives proves the claimed C^infinity
one-sided regularity, not just a formal power series. Since the value at0
vanishes, r(2m+s)=s rho(s) with rho smooth on [0,infinity). The density
and all derivatives decrease rapidly as s tends to infinity; radial
derivatives are polynomially bounded factors times Schwartz derivatives
away from s=0. Thus r is continuous when extended by zero below2m.

For j=0,1, b(e)=e^j r(e) has b(2m)=0 and integrable first two derivatives
on [2m,infinity). Two integrations by parts, including the finite boundary
term b'(2m), yield

    |C_j(t)|<=C(1+|t|)^(-2),
    C_j(t)=integral e^j r(e)exp(iet)de.                (G18)

The same holds for b_s(e)=r(e)(exp(ise)-1) at each fixed real s. This
uses antisymmetry of the pair, not absolute integrability of each single
channel correlation. The individual channel threshold terms need not cancel.

Let beta=PZP_- and B1=PK1P_-. The exact CAR normalization gives

    ||B1||_HS^2=2lambda^2 integral r(e)|I_T(e)|^2de,
    ||E^(1/2)B1||_HS^2=lambda^2 integral e r(e)|I_T(e)|^2de,
    I_T(e)=integral_0^T cos(omega t)exp(iet)dt.         (G19)

Each squared norm is bounded by C lambda^2 T, either by (G18) in the
double time integral or temporal Plancherel and bounded e^j r(e).
The output energy factor in the second identity uses antisymmetry to
symmetrize E(p); the exterior factor1/2 must not be lost.

For any of the densities b above, the double time cosine product yields

    integral b(e)|I_T(e)|^2de
        =(pi/2)T[b(omega)+b(-omega)]+O(log(2+T)).       (G20)

The cos(t-s) piece has triangular factor T-|t-s|. Replacing it by T on
the whole line costs a truncated first absolute moment O(log(2+T)) plus
T times an O(T^-1) tail. Fourier inversion applies since C_b is in L1
and b is continuous. The cos(t+s) piece is uniformly bounded by a fixed
multiple of ||C_b||_1/omega after its other time integral. This proves
(G20) also for complex b_s. It does not assume a finite full first time
moment, which need not hold for this control class.

By (G13) at q=1 and (G19), the exact-minus-Born energy mean is bounded by
C eta_lambda on bounded kinetic intervals, using the difference of squared
norms. Taking b(e)=e r(e) in (G20) proves the mean in (G3), since b(-omega)=0.

## 6. Graph coordinate and full law

Set A0=PZP:h->h. By (G2), A0 is invertible for small h_lambda and
||A0^-1-I||<=C eta_lambda. The exact CAR annihilator of Y(T)Omega is
a(A0 xi)+a*(beta Gamma xi). With scalar conjugation C on h, its graph
coordinate is L=beta Gamma A0^-1 C, and CAR gives L^T=-L.
Let J=Gamma C. Equations (G13),(G16),(G19) imply

    ||L||<=C eta_lambda, ||L||_HS<=C,
    ||L-B1 J||_HS<=C eta_lambda.                      (G21)

For example the last bound follows by separating beta-B1 and
beta Gamma(A0^-1-I)C. The HS factor is beta, bounded by (G13),(G19);
an identity on the infinite one-particle carrier is never assigned an HS norm.

The corrected kinetic theorem's reviewed finite-exterior/overlap-ODE
identity and its HS limit require precisely this graph condition. They
do not require zero-integral smearings. For L_s=exp(isE)L exp(isE^T),
they give the exact characteristic function of the H0 law through the
continuous trace-log lift

    log chi_lambda,T(s)
       =(1/2)Tr log(I+L*L_s)-(1/2)Tr log(I+L*L).       (G22)

The lift is defined by the norm-small operator series, not an arbitrary
principal scalar logarithm at large tau. The series remainder is bounded
by C||L||^2||L||_HS^2=O(eta_lambda^2). Replacing L by B1 J in its quadratic
part costs O(eta_lambda). The exact exterior normalization then gives

    log chi_lambda,T(s)
       =lambda^2 integral r(e)(exp(ise)-1)|I_T(e)|^2de
                                                   +O(eta_lambda). (G23)

Apply (G20) to b_s and T=tau/lambda^2. For fixed s,

    log chi_lambda,T(s)
       ->tau (pi/2)r(omega)(exp(is omega)-1),           (G24)

uniformly for bounded tau. The secular error lambda^2 log(2+tau_star/lambda^2)
is smaller than eta_lambda. The limit is continuous at s=0 and is the
characteristic function of the asserted Poisson energy law, proving weak
convergence. The mean was proved separately; weak convergence alone would
not exclude rare energy tails. For nonnegative laws weak convergence plus
convergence of means gives W1: use E[(X-R)_+]=E[X]-E[min(X,R)], then
x1_(x>2R)<=2(x-R)_+ and truncate Lipschitz tests. This completes (G3).

## 7. Correlations, finite-mode resources and conditional transfer

Let d_lambda=C eta_lambda be the bound in (G2). The exact CAR identity and
telescoping imply, for every degree-r word in real slots,

    |omega_lambda,T(product_j gamma(h_j))
                         -omega_vac(product_j gamma(h_j))|
        <=r d_lambda product_j ||h_j||.               (G25)

This holds for full and interaction states, uniformly on the kinetic window
and for bounded degree and slot norms, even if slots vary with lambda or T.
For W compare with simultaneously free-rotated slots and use vacuum free
invariance. Fixed polynomial approximation gives convergence for each fixed
CAR observable. No uniform bound on its whole unit ball is asserted.

The occupation in (G1) obeys 0<=N<=d_lambda^2 I. For any finite-rank
one-particle projection Q of rank d, the exact reduced state satisfies

    Tr(rho N_Q)<=d d_lambda^2,
    ||rho_Q-P_vac,Q||_1<=2 min(1,sqrt(d)d_lambda).      (G26)

The first inequality is a finite orthonormal sum. The integer finite-mode
number spectrum bounds nonvacuum probability by its mean; the pure-vacuum
trace bound then follows by spectral mixture or purification. Thus a detector
with excitation probability at least p0>0 necessarily has d>=p0/d_lambda^2
when d_lambda>0. In particular d is bounded below by a positive constant
times 1/[h_lambda log(2+h_lambda^-2)]. This is a necessary rank bound from
the stated sufficient error estimate, not an optimal detector claim.
A bounded continuum energy band is infinite rank.

The gap gives 1_[0,a0](H0)=P_Omega for0<a0<m. Weak energy-law convergence
therefore gives vacuum weight exp(-tau nu_omega). Since the global states
are pure, their trace distance to vacuum tends to

    2 sqrt(1-exp(-tau nu_omega)).                      (G27)

The finite-mode occupation bound and finite Fock projections also imply
Tr(rho Kcompact)->exp(-tau nu_omega)<Omega,Kcompact Omega> for each compact
Fock operator, exactly by the reviewed finite-section argument. A normalized
vacuum CAR functional and a possibly subnormalized compact-test limit refer
to different test algebras. No physical escape velocity, current law or
spatial local-algebra norm convergence follows from this statement.

Under the separately supplied real energy-adapted actual-cell embedding,
common H0/vacuum and weighted calibration/work estimates, an error
epsilon_a=O(a^(N+1)) transfers state laws if epsilon_a=o(h_lambda) and
means if epsilon_a=o(lambda^2), as in corrected V2 section8. The latter
suffices for the law, mean and W1 together. The unweighted one-particle
Duhamel comparison adds C tau_star epsilon_a/h_lambda to d_lambda;
epsilon_a=o(lambda^2) makes this o(h_lambda), smaller than eta_lambda.
Actual image slots need not have zero integrals. This is conditional
composition with those exact upstream premises, not a new proof of their
alias, frame, inverse, graph-domain or embedding estimates.

## 8. A strictly positive-rate example with both means nonzero

Fix k0=sqrt((omega/2)^2-m^2)/v>0. Choose nonzero nonnegative even
b in C_c^infinity(-L,L), with k0 L<pi/2, and set f=(b,0), g=(0,b).
Both vector integrals are nonzero. Write Bhat=bhat in the unitary convention.
The scalar slots give exactly

    Delta(p,q)=2 sin((theta(p)-theta(q))/2)Bhat(p)Bhat(q).

Thus Delta(k0,-k0)=2 sin(theta(k0))Bhat(k0)^2>0, since Bhat(k0) is its
strictly positive cosine integral. The regular energy curve contains an
angular neighborhood on which the pair amplitude is nonzero, hence
r(omega)>0. This example is excluded by both earlier zero-integral classes
and has a strictly positive limiting energy and vacuum depletion for tau>0.

## 9. Exposure, failures and audit boundary

Root plan43/b44108ca was sealed before any fresh general-mean review or
one-zero crosscheck finding. The independent mean301 supplied the causal
square and spectral-forcing route. The new full-input, threshold-separated
Born and complete-law arguments were developed after that exposure. This
is a conditional composition, not blinded validation or model diversity.

The failed absolute-value route gives ||L_T||=O(sqrt(T)), insufficient for
a simple Neumann inverse at arbitrary fixed kinetic tau. It is a failed
estimate, not a counterexample. The successful proposed proof keeps the
phase in L_T^2 and separately controls the full Born operator; a bounded
mean by itself would not supply the small graph norm or the Poisson law.

No numeric or Lean checker has run for this extension. Its new continuum
and limit claims require focused independent analytic review. Useful scoped
formal obligations include the noncommuting polynomial inverse and the
operator/HS composition steps; no existing Lean result is presented as
verification of these analytic estimates. General drives, threshold omega=2m,
massless limits, optimal rates and physical model selection remain open here.

## Assembly trace and verification limits

The exact core bytes, line/byte offsets, literal wrapper pieces and complete
wrapper-only unified diff are supplied with this note. The single diff
convention is three context lines (`difflib.unified_diff`, n=3), against the
verbatim concatenation of its included cores. Empty core diffs and exact
extraction record zero core edits. SOURCE_CHECKER.py checks reconstruction
and identity only; it does not certify any theorem.

The selected immediate source freezes and every directly bound byte object
are archived with explicit one-hop maps. Nested receipts are preserved
opaque, not recursively audited. Historical diagnostic programs/results
are provenance, not new execution or newly certified mathematics. The
review, exposure, limitation and dependency records remain part of the
packet. No CW, Git, cache, graph, PR, audit, axiom or prompt mutation is
authorized by this source assembly; the parent owns any later publication.


## Publication imports and recovery

- [two_zero_kinetic_energy_bounded_theorem_note_2026-10-13](TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [kinetic_correlation_limits_bounded_theorem_note_2026-10-13](KINETIC_CORRELATION_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [energy_adapted_calibration_bounded_theorem_note_2026-10-13](ENERGY_ADAPTED_CALIBRATION_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [calibrated_energy_transfer_bounded_theorem_note_2026-10-13](CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md)

These are the direct mathematical or conditional parents. The accompanying packet at `.claude/science/physics-loops/toe-kinetic-energy-20261013` binds canonical bytes, consumed same-packet cores and archived inputs to their actual consumers in `PARENT_BINDINGS.json` and `CLAIM_REGISTRY_ADDITIONS.json`. Five historical exposure/provenance relations are separate from the fourteen direct edges. Pair PR9515 supplies the actual Git parent; its ancestry and root484 exposure do not create a new mathematical edge. Historical pair792 has an exact canonical map; the separate root286 remains an archived provisional input.

The complete405-file accepted assembly, original847 picture defect, missed root check, exact V2 repair, all source reviews and the scoped one-hop closure are recoverable from content-addressed objects. Historical pending and exposure text remains unchanged. General301 remains mean-only; the separate470 core supplies the full-law extension with its own bounds. The published identity tools check byte reconstruction and declared inputs with zero mathematical predicates. They do not perform a fresh proof, independent review, retained audit or source-status promotion. Unaccepted modulated-drive work is excluded.


Review-loop integration note: current main 82fdc12d51e3e47bf8ac1f74601c9600115942d6 plus this kinetic-energy batch supplies the reviewed live dependencies. Original proof bodies and archives are unchanged. Live parent hashes and consumed-core coordinates are refreshed, with original bindings preserved. Historical pending and review labels remain provenance, not audit authority.
