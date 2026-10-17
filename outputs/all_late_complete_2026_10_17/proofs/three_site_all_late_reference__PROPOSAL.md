# Exact three-site scalar reference: all-late physical-halfline concentration

Status: new conditional analytical author interface, requiring distinct checking. Direct nonstationary-phase integration of the exact hard-band coefficient proves explicit outgoing and conjugate-incoming halfline bounds for every t>=T. No linear-dispersion comparator, actual-source analyticity, new operating point or finite permanent-storage claim is used.

## 1. Exact scalar packet and domain

Retain the nominal physical calibration, the same coefficient F_s3 as the checked weighted-reference source, and

    0<lambda<=1e-8, eta=lambda/j<=1/16,
    .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6,
    d=2j sin h, d/g<=1/2.

Here j is the original calibrated j=J(1-C0), with old J=.030021107107032. It is not independently retuned. Define

    alpha=asin(d/(2g)), k_-=pi/2-alpha, k_+=pi/2+alpha,
    delta(k)=-2g cos k, q(k)=pi/2+asin(delta(k)/(2j)),
    k_old(q)=2asin(sqrt(j/J)sin(q/2)),
    phi(k)=61.5q(k)+.5k+172k_old(q(k)),
    C=sqrt(8lambda^5/(3pi)), s=sqrt(1-3eta),
    m_j(delta+i0)=delta/(2j^2)-i sqrt(1-delta^2/(4j^2))/j,
    P2(delta)=delta^2-lambda^2/3,
    q3(delta)=P2(delta)[delta-3jlambda m_j(delta+i0)]
                                      -(8lambda^2/3)delta.

The flux transmission is

    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2).

On I_k=[k_-,k_+] the EXACT raw Fourier coefficient is

    F(k)=zeta exp[i phi(k)] sqrt(2g) C N(k)/q3(delta(k)),
    N(k)=sqrt(sin q sin k)|t_f|
        =sin q sin k/sin((q+k)/2).

Set it to zero elsewhere in one length-2pi Fourier cell. Here zeta is the fixed unit phase from the reference, not a fitted phase. The exact transmitted mass p=int_I_k |F(k)|^2 dk satisfies 0<p<=1 by the checked scalar spectral identity and flux contraction. The first physical slow site remains m=0, distinct from the old gate port.

Define RAW sequences

    beta_m(t)=(2pi)^(-1/2) int_I_k F(k) exp[imk-it delta(k)] dk,
    iota_m(t)=(2pi)^(-1/2) int_I_k conjugate(F(k))
                                           exp[-imk-it delta(k)] dk.

Their full integer-lattice norms are sqrt(p). The normalized scalar sequences are beta/sqrt(p) and iota/sqrt(p). The common physical carrier exp[-it(c_att+2j)], literal old aging exp(-itK), outgoing W and incoming W-star remain as specified in the traveling interface. The incoming formula conjugates the coefficient and reverses spatial phase, but DOES NOT reverse physical time or conjugate an arbitrary input state. These fixed unitary factors do not change the scalar norm estimates.

## 2. Explicit constants and result

All constants below depend only on the fixed supplied scalar parameters. Put

    v_*=2g cos alpha>0, Q1=g/(j cos h),
    P_phi=.5+102.78 Q1,
    P_N=tan(h)Q1+tan(alpha)
                    +.5 tan((h+alpha)/2)(Q1+1),
    A=3+9eta/(2 cos h), K0=sqrt(2g) C,
    I0=2K0/(s v_* lambda^2),
    I1=(P_phi+P_N)I0+K0 A pi/(2s^2 lambda^3),
    E_edge=2K0/[s(d^2+lambda^2)^(3/2)],
    B=E_edge+I1+(d/v_*)I0.

These are finite for every fixed positive admissible g,h,lambda. For t>0 set z_t=v_* t and

    J_in(t)=B/sqrt(2pi)*sqrt(z_t^(-2)+z_t^(-1)),
    J_left(t)=B/sqrt(2pi z_t).

Then the exact raw sequences satisfy

    ||1_{m>=0} iota(t)|| <= min{sqrt(p),J_in(t)},       (1)
    ||1_{m<0} beta(t)|| <= min{sqrt(p),J_left(t)}.      (2)

If an estimate also charging outgoing m=0 is preferred, its bound is min{sqrt(p),J_in(t)}. No identification of m<0 with m<=0 is made.

Every right side is decreasing in positive t. Consequently its value at T bounds ALL t>=T. A simple explicit sufficient onset for any prescribed scalar norm allowance 0<e<1 is

    T >= max{1/v_*, B^2/(pi p v_* e^2)}.              (3)

For all t>=T, both normalized wrong-halfline norms are then <=e (and the outgoing m<=0 estimate is also <=e). This is a sufficient onset, not a sharp or optimized time. No parameter point is evaluated here. The estimate has algebraic decay and need not improve a previously checked finite-window bound at a particular early time.

## 3. Proved exact coefficient derivative

The derivative bounds concern the actual scalar coefficient, not a bound inferred from its small value. The hard cutoff will be handled separately by its endpoint values.

On I_k, sin q>=cos h, sin k>=cos alpha, and

    delta'(k)=2g sin k>=v_*, |delta''(k)|=|2g cos k|<=d,
    0<q'(k)=g sin k/(j sin q)<=Q1.

The original energy-margin argument first places this entire q band inside the original calibrated k_old band; its checked k_old'(q)<.24 is therefore available throughout. Hence |phi'(k)|<=.5+(61.5+172*.24)Q1=P_phi. The exact phase is retained; only its derivative is bounded.

The positive numerator obeys 0<N<=1, since sqrt(sin q sin k)<=1 and |t_f|<=1. Differentiating its exact expression gives

    N'/N=cot(q)q'+cot(k)
                         -.5 cot((q+k)/2)(q'+1).

Using |q-pi/2|<=h and |k-pi/2|<=alpha bounds its absolute logarithmic derivative by P_N. Thus |N'|<=P_N N<=P_N. There are no numerator zeros or half-angle poles in this band.

For the denominator, the checked exact scalar identity gives

    |q3(delta)|>=s(delta^2+lambda^2)^(3/2).            (4)

A direct derivative bound is also available without importing any actual matrix inverse. The Weyl expression above has

    |m_j'(delta+i0)|=1/[2j^2 sqrt(1-delta^2/(4j^2))]
                                      <=1/(2j^2 cos h),
    |m_j(delta+i0)+i/j|<=|delta|/(2j^2 cos h).

The second inequality follows by integrating the first from zero along the real interval. Exact algebra gives

    q3(delta)=(delta+i lambda)^3
                     -3jlambda P2(delta)[m_j(delta+i0)+i/j].

Differentiating this identity, using |P2|<=delta^2+lambda^2 and 2delta^2<=2(delta^2+lambda^2), proves

    |dq3/d delta| <= A(delta^2+lambda^2).              (5)

This is a deliberately general scalar ceiling; it does not rely on the narrower numerical derivative constant from a separate cancellation note.

Let r_delta=sqrt(delta^2+lambda^2). Differentiating F on the CLOSED band from its smooth one-sided continuation, using (4)-(5), gives

    |F'(k)| <= (P_phi+P_N) K0/(s r_delta^3)
                         +K0 A delta'(k)/(s^2 r_delta^4).

The change of variables dk=d delta/delta'(k), followed only by extending positive integrals to the real line, yields

    int_I_k |F| dk <= K0/(s v_*) int_R (delta^2+lambda^2)^(-3/2)d delta
                   =I0,
    int_I_k |F'| dk <=(P_phi+P_N)I0
                       +K0 A/s^2 int_R (delta^2+lambda^2)^(-2)d delta
                   =I1.

The two rational integrals are 2/lambda^2 and pi/(2lambda^3). Both endpoint energies have |delta|=d, so

    |F(k_-)|+|F(k_+)|<=E_edge.

Thus every needed variation and endpoint quantity has an explicit analytical bound, including the determinant's complex phase. The conjugate coefficient has the same value and variation bounds.

## 4. Nonstationary phase and the exact integer sum

For incoming m=n>=0, the oscillatory phase is -nk-t delta(k). Its derivative has absolute value n+t delta'(k)>=n+v_*t. For outgoing m=-n, n>=1, it is the SAME phase with coefficient F rather than conjugate(F). Thus the two cases admit the same integration-by-parts estimate. For either coefficient f and either allowed n,

    |int_I_k f exp[-ink-it delta(k)]dk|
      <= [|f(k_-)|+|f(k_+)|+int|f'|]/(n+v_*t)
                         + t int |f| |delta''|/(n+v_*t)^2
      <= B/(n+v_*t).                                (6)

The first line follows by differentiating f divided by the phase derivative. The last inequality uses t/(n+v_*t)<=1/v_*. Both hard-edge boundary terms are retained. The extension of F by zero is discontinuous at those edges; it is not incorrectly treated as a globally smooth periodic function with vanishing boundary terms.

For z>0, monotonicity of (z+x)^(-2) gives

    sum_{n=0}^infty (z+n)^(-2) <= z^(-2)+1/z,
    sum_{n=1}^infty (z+n)^(-2) <= 1/z.

Squaring (6), inserting the Fourier factor 1/(2pi), and summing proves (1)-(2). In particular the incoming m=0 summand is explicitly paid. Taking z>=1 bounds z^-2+z^-1 by 2/z and proves (3).

This uses the exact Fourier coefficients on one cell and the exact integer sum. Parseval gives total mass p on that cell, including its hard cutoff. There is no real-line sampling approximation or periodized rational comparator; consequently no separate alias error is introduced or omitted. The integer lattice and hard edges have already been treated exactly. No complex strip or pole continuation is asserted.

## 5. Physical-halfline normalization and reuse boundary

Let r(t)=||1_{m>=0} beta(t)||. The exact scalar total norm gives

    r(t)^2=p-||1_{m<0} beta(t)||^2
             >=p-min{p,J_left(t)^2}.

Whenever J_left(t)<sqrt(p), the physical normalized outgoing reference beta_+(t)/r(t) is well-defined. Its distance from the RAW halfline vector beta_+(t) is exactly 1-r(t), with the upper bound

    1-r(t) <= 1-sqrt(p-J_left(t)^2).                  (7)

Alternatively, after first normalizing the full-lattice scalar vector by sqrt(p), the additional halfline normalization cost is

    1-r(t)/sqrt(p)
      <=1-sqrt(1-J_left(t)^2/p).

These are two accounting conventions, not two charges to add indiscriminately. A later raw actual traveling synthesis should use (7) once. It must separately pay its actual omitted spectral vector once and its actual coefficient errors; this scalar transmitted mass is not actual seed mass. The incoming bound in raw synthesis is J_in(t), capped by sqrt(p), with the common physical time and incoming W-star factors retained.

For each fixed admissible family member, the bounds tend to zero as t tends to positive infinity and r(t) tends to sqrt(p). Thus the limiting raw-to-normalized halfline cost is 1-sqrt(p), not zero unless p=1. This is a quantitative infinite-ray scalar reference statement. It supplies no finite receiver's all-future storage, permanent halt, repeated-measurement protocol or actual apparatus escape by itself. Existing finite-window performance remains unchanged; no old time or operator-valued source analyticity is imported.

## 6. Sources, exposure and verification limits

The exact packet, scalar lower bound and phase domain are reused from the complete refreshed weighted-reference source `three_site_weighted_reference_time/PROPOSAL.md`, SHA256 d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36, and its complete refreshed distinct check `three_site_weighted_reference_time_check/REVIEW.md`, SHA256 809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac. Their exact coefficient identification, scalar determinant and calibrated map premises are reused within scope. Their finite-time dispersion comparison, residue and alias estimates are not used to prove the present all-late bound.

Relevant unchanged identities are the scalar source a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 with check c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b; exact outgoing source af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac with check 721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02; calibrated bandwidth map d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2; and scalar inverse source 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 with check 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2. No full actual-source matrix conclusion is inferred from the scalar bound.

I authored the weighted refinement and related traveling interfaces, and reviewed other scalar/inverse ancestors. Root requested an all-late exact-dispersion route without a target constant. This is new exposed author work, not its own independent validation. A distinct check is needed for the coefficient variation, endpoint terms, halfline indexing and normalization. No scientific runner, numerical integration, dynamics, parameter sweep, new hardware point, source/canonical/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.
