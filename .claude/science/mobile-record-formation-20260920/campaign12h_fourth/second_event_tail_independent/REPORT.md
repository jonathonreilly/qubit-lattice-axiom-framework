# Independent long-time and moment analysis of the second ring clock

For the actual first-mark output on the eight-site unit-rotor ring, put
`a=eta-4 delta`, with kappa>0. For any single integer-circulation input and either the resolved or stipulated coherent first mark, the entire finite-a survival law is the same. When a!=0 its long-time behavior is

    Pr(T>t) ~ [32 |a| sqrt(2 pi kappa)]^-1 t^-3/2.       (1)

Thus completion has probability one and mean 3/(8 kappa), but every integer moment of order at least two is infinite. More precisely, positive moments exist exactly for orders p<3/2. At a=0 the law is instead Exp(4 kappa), with all moments p!/(4 kappa)^p for integer p. This exceptional cancellation cannot be covered by (1).

These conclusions concern the supplied effective unit-rotor clock. They are not a finite-spin, microscopic stopping-time, large-volume, or later-event theorem. The previous ring reconstruction and its author comparison were already known. This new calculation starts from my frozen exact clock; the new `second_event_tail_author` packet and every finite-spin folder, plan, checkpoint, and registry remain unopened. Its seal hash was supplied, but its contents were not accessed. This is an independent continuation, not a formal audit or publication decision.

## 1. Exact starting point and scalar resolvent

The prior independent report is pinned at `39e2b04f9140f10db8d8bbd178a086902d9b09f6854b0e317a663071bacf4582`, PRE at `e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734`, and final comparison seal at `44d2a76280ebbbc97d2a1f34d83c7ccac28647de54d3cceaf6212d17b7b32731`. The exact H4 correction is retained through a=eta-4 delta; its remaining commuting unitary does not affect survival.

For the reference first mark on (0,1), the six word angles, singular frequencies, and actual preparation weights are

    alpha_j=(4 theta+2 pi j)/6,  j=0,...,5,
    s_+/-^2=4+/-4 cos(alpha_j/2),
    b_j^resolved=1/6,
    b_j^coherent=[1+cos(theta-alpha_j)]/6.

The normalized coherent mark means the actual unnormalized sum of its two charge orientations, normalized after the mark. It is not a mixture of those outputs. For a pre-mark trace-class circulation state let g(theta)>=0 be its angle density, with integral g dtheta/(2pi)=1. The existing exact result is

    S_g(t)= (1/2)e^(-4 kappa t)
      +(1/4) integral g(theta) sum_j b_j(theta)
          [f_(a s_+)(t)+f_(a s_-)(t)] dtheta/(2pi),       (2)

where f_omega(t)=||exp(tK_omega)(1,0)||² and

    K_omega=[[-2 kappa, i omega],[i omega,0]].

Each scalar initial vector is the lossy adjacent coordinate. One cannot substitute an arbitrary opposite-coordinate state: its low-frequency behavior and moments differ. The field density in (2) is the initial density because the first ring mark has a scalar Gram and preserves the angle probability after normalization. For a single circulation |ell>, g=1, independent of ell. Rotational/reflection symmetries give the same single-circulation law for the other first marks covered by the previous reconstruction.

An independent two-coordinate calculation supplies the Laplace transform without a long-time ansatz. Write the amplitude as (A,iB), with A,B real, and set x=A², y=B², z=AB. Their equations are

    x'=-4 kappa x-2 omega z,
    y'=2 omega z,
    z'=omega x-omega y-2 kappa z,

starting at (1,0,0). Solving this three-variable resolvent gives, for Laplace variable u>0,

    F_omega(u)=integral_0^infinity e^(-u t) f_omega(t) dt
      = (u²+2 kappa u+4 omega²)
         /[(u+2 kappa)(u²+4 kappa u+4 omega²)].          (3)

At omega=0 it reduces to 1/(u+4 kappa). For omega!=0 its first four waiting moments are

    m1=1/(2 kappa),
    m2=1/(2 kappa²)+1/(2 omega²),
    m3=3/(4 kappa³)+3/(4 kappa omega²)+3 kappa/(2 omega^4),
    m4=3/(2 kappa^4)+3/(2 kappa² omega²)
                          +3/(2 omega^4)+6 kappa²/omega^6.   (4)

In general m_n=n(-1)^(n-1) F_omega^(n-1)(0). These are moments of the positive waiting law, not derivatives exchanged with a field integral. The angular integrations below use Tonelli with extended value infinity. At omega=0 the moment is n!/(4 kappa)^n instead; the pointwise survival limit omega->0 does not justify passing its moments.

## 2. A single circulation: complete Laplace law and algebraic tail

For g=1 the coherent cosine contribution in (2) vanishes exactly. Under theta->theta+pi/2 the word branches permute; summing over four such translates gives the four cosine phases with total zero. The same cancellation holds for any pi/2-periodic g. Uniformly averaging the resolved word branches and then the two singular signs gives

    S_1(t)=(1/2)e^(-4 kappa t)
       +(1/pi) integral_0^(pi/2) f_(Omega sin v)(t) dv,
    Omega=2 sqrt(2)|a|.                                (5)

The factor is fixed by S_1(0)=1. Equivalently, the bright half has the arcsine frequency density 2/[pi sqrt(Omega²-omega²)] on (0,Omega). This uses normalizable circulation states; it is not a fixed-angle preparation.

Using (3) and the elementary integral of 1/(A+B sin²v), the exact survival Laplace transform is

    L_a(u)=1/[2(u+4 kappa)]+1/[2(u+2 kappa)]
       - kappa u /{(u+2 kappa)
          sqrt[u(u+4 kappa){u(u+4 kappa)+32 a²}]}.       (6)

Formula (6) is valid for u>0 also at a=0, where it simplifies to 1/(u+4 kappa). It independently checks the rate and frequency normalizations. For a!=0, L_a(0)=3/(8 kappa), and its nonanalytic small-u term is

    L_a(u)=3/(8 kappa)
          -sqrt(u)/[16 |a| sqrt(2 kappa)]+O(u).         (7)

Here is a direct time-domain proof of (1), so no unverified Tauberian implication is needed. For 0<|omega|<kappa set w=sqrt(kappa²-omega²). The exact survival is

    f_omega(t)=A_s e^(-lambda_s t)+A_f e^(-lambda_f t)
                         -(omega²/w²)e^(-2 kappa t),
    lambda_s=2(kappa-w),  lambda_f=2(kappa+w),
    A_s=kappa(kappa-w)/(2w²),
    A_f=kappa(kappa+w)/(2w²).                            (8)

At small omega,

    A_s=omega²/(4 kappa²)+O(omega^4),
    lambda_s=omega²/kappa+O(omega^4).

On |omega|<=kappa/2 the slow contribution is bounded by a constant times omega² exp(-omega² t/kappa), and the other terms are exponentially small. On any compact frequency interval separated from zero the entire two-coordinate survival has a uniform exponential bound with a harmless polynomial prefactor, including the critical-damping point. These bounds justify splitting (5) near zero and rescaling omega by sqrt(kappa/t). Its nonzero leading contribution is

    [1/(pi Omega)] [1/(4 kappa²)]
         integral_0^infinity omega² e^(-omega² t/kappa) d omega
       = [1/(16 sqrt(pi) Omega sqrt(kappa))] t^-3/2,

which is (1). All constants here are for fixed finite a!=0 and fixed kappa>0; this is not an asymptotic uniform through a=0.

Since E[T^p]=p integral t^(p-1)S_1(t)dt, the positive coefficient in (1) proves finiteness exactly for p<3/2. The borderline p=3/2 diverges logarithmically. In particular E[T²]=infinity and the variance is infinite despite the finite mean. For positive fractional p<3/2 the value is fixed completely by (5) or (6). For 1<p<3/2 an especially useful positive integral is

    E[T^p]=M_infinity(p)
      + [p(p-1)/Gamma(2-p)] integral_0^infinity
            D_a(u) u^(-p) du,
    M_infinity(p)=Gamma(p+1)[(4 kappa)^(-p)+(2 kappa)^(-p)]/2,
    D_a(u)=kappa u/{(u+2 kappa)
              sqrt[u(u+4 kappa){u(u+4 kappa)+32a²}]}.     (9)

It follows by integrating the Laplace identity for E[e^(-uT)-1+uT]. The integral is finite at zero exactly in this range. At a=2, kappa=.7, p=5/4 it gives
`0.556327564855006256580048167967850261...`; an independent complex-root moment integration agrees. No finite value is assigned to divergent integer moments by analytic continuation.

## 3. Which field assumptions change the answer

The exact mean remains 3/(8 kappa) for every normalized L1 angle density when a!=0, by (2), the scalar m1, and the fact that zero frequencies occupy a null set. This statement by itself gives no universal moment of order greater than one.

For p>1, the slow term in (8) gives

    m_p(omega) ~ Gamma(p+1) kappa^(p-2)
                              /[4 |omega|^(2p-2)]       (10)

as omega->0 through nonzero values. Away from zero m_p is finite and continuous, including critical damping, and approaches Gamma(p+1)/(2 kappa)^p as |omega|->infinity. It follows that, for any fixed a!=0, the necessary and sufficient moment criterion is

    I_p(g)=integral g(theta) sum_j b_j(theta)
            [s_+(alpha_j)^(-2p+2)+s_-(alpha_j)^(-2p+2)]
                                        dtheta/(2pi) < infinity. (11)

The expression is interpreted almost everywhere; arbitrary values at the isolated zeros do not affect the criterion. Positivity prevents cancellation of divergent contributions. All p<=1 are finite for normalized g, because the mean is finite. A density integrably singular near a noncancelled exceptional angle can make any prescribed p>1 diverge. For example g proportional near zero to 1/[|theta| log²(1/|theta|)], with a compact local cutoff, is L1 but violates (11) for every p>1. Its square root is a legitimate L2 angle wavefunction. No electric-moment regularity was assumed in the bounded-rotor model; this rough example should not be imported into an electric-energy theorem with stronger premises.

For p=2 the exact extended-valued expression is particularly simple:

    E[T²]=5/(16 kappa²)
       +(1/(16a²)) integral g(theta) sum_j
                       b_j(theta)csc²(alpha_j/2) dtheta/(2pi).   (12)

For a resolved mark the sum is 6 csc²(2 theta), using the six-angle cotangent identity. Thus

    E[T²]_resolved=5/(16 kappa²)
        +(3/(8a²)) integral g(theta)csc²(2 theta)dtheta/(2pi).   (13)

For a coherent mark the nonnegative sum can be written

    6(1+cos theta)csc²(2 theta)-2 cos theta
                                  +2 sin theta cot(2 theta).  (14)

The unsimplified nonnegative sum is preferable at singular angles. Formula (14) has a finite limit 7/4 at theta=pi, where the coherent weight cancels that singularity. For the normalizable finite-flux superposition with g=2 sin²(2 theta), both instruments have

    E[T²]=5/(16 kappa²)+3/(4a²),
    Var(T)=11/(64 kappa²)+3/(4a²).                       (15)

Hence an all-normalizable-input assertion of infinite variance would be false. This particular density still has a t^-5/2 tail and an infinite third moment. Support separated from all four exceptional angles gives a uniform positive bright frequency and an exponential survival bound, hence all moments finite.

More precise tail qualifications follow from local density behavior. Let E={0,pi/2,pi,3pi/2}. Near theta_e in E there is one small singular frequency with

    s_min(theta_e+r)=(sqrt(2)/3)|r|+O(|r|³).

Let h_e(r)=g(theta_e+r)b_(small branch)(theta_e+r). If h_e(r) is asymptotic to c_(e,+)|r|^nu from the right and c_(e,-)|r|^nu from the left, with nu>-1, that angle contributes

    [(c_(e,+)+c_(e,-)) Gamma((nu+3)/2) kappa^((nu-1)/2)]
      /[64 pi (|a| sqrt(2)/3)^(nu+1)] * t^(-(nu+3)/2).  (16)

This follows by the same rescaling and domination as (8). If several powers occur, their positive contributions add and the smallest exponent controls the tail. Assuming g is continuous near all four angles, a convenient version is

    lim t^(3/2) S_g(t)
       = [3/(64 |a| sqrt(2 pi kappa))]
                              sum_(theta_e in E) g(theta_e)b_e, (17)

where b_e=1/6 for resolved formation and b_e=(1+cos theta_e)/6 for coherent formation. The formula permits a zero coefficient; it does not then specify the next power without additional vanishing information.

For example, let g=pi/w on |theta-pi|<w and zero elsewhere, 0<w<pi/4. This is a normalizable packet with no weight near the other exceptional angles. Resolved formation has a t^-3/2 tail, while the actual coherent weight is r²/108+O(r^4), giving

    S_coherent(t) ~ [3 g(pi) sqrt(kappa)
                   /(1024 sqrt(2pi)|a|³)] t^-5/2.       (18)

It has a finite second moment and an infinite third moment. The change is a property of the specified coherent instrument, not a change in its total loss operator. At a=2, kappa=.7, w=.3, the finite coherent second moment from (12) is approximately `0.6657970402856614`; the resolved second moment is infinite. These examples delineate the density and instrument hypotheses needed to extend the single-circulation claim.

## 4. Exceptional parameters, fibers, and the fast limit

At a=0, equivalently eta=4 delta, the commuting Q part is the only non-scalar Hamiltonian relevant here and stays within the initial adjacent subspace. Formula (2) reduces to exp(-4 kappa t) for every g and either mark. All positive moments are Gamma(p+1)/(4 kappa)^p. There is no residual polynomial tail. The sign of a elsewhere is immaterial for survival.

At scalar critical damping |omega|=kappa,

    f_omega(t)=e^(-2 kappa t)[1-2 kappa t+2 kappa²t²].

It introduces no new moment divergence. At a fixed exceptional angle one singular frequency is zero, but the actual output has no population in its dark opposite coordinate. That fixed-fiber clock is a finite sum of exponentially decaying matrix terms and has all moments. Such generalized angle vectors are not normalizable circulation states. Arbitrarily near them, weakly populated slow modes produce the physical tail; deleting only the measure-zero points does not eliminate it. For an arbitrary post-birth state, occupation of a dark fiber or a different low-frequency preparation would require a different analysis.

The fixed-normalizable-input fast survival limit from the preceding PRE is

    S_infinity(t)=[e^(-4 kappa t)+e^(-2 kappa t)]/2,

uniformly in t>=0. It does not permit unrestricted interchange with unbounded time moments. For a single circulation, every finite a!=0 has infinite moments p>=3/2, whereas this limiting mixture has the finite value M_infinity(p) at every p. Likewise its exponential decay rate is 2 kappa while -lim_(t->infinity) log(S_1(t))/t=0 at every finite nonzero a. The mean happens to pass through the fast limit because it was computed exactly, not because uniform convergence of survival curves suffices.

For 1<p<3/2 and a single circulation, the excess moment in (9) is positive and O(1/|a|). Indeed

    D_a(u) <= kappa sqrt(u)
                   /[4 sqrt(2)|a|(u+2 kappa)sqrt(u+4 kappa)],

whose product with u^-p is integrable in this range. For general fixed g, whenever criterion (11) holds, the bound m_p(omega)<=C_(p,kappa)[1+|omega|^(-2p+2)] and the scalar large-frequency limit give moment convergence by domination. If (11) fails, the finite-a moment stays infinite. For p<1, the uniformly bounded exact means give uniform integrability of T^p; p=1 uses its exact value. These are statements for fixed g, not arbitrarily eta-dependent spectral preparations.

Approaching a=0 is a separate singular limit. At each fixed time the law tends to Exp(4 kappa), but for every nonzero a its mean is 3/(8 kappa), rather than 1/(4 kappa). For the uniform input, finite moments 1<p<3/2 diverge as a->0: (10) and the integrable arcsine weight give order |a|^(2-2p). This is another explicit failure of moment interchange. kappa=0 is excluded throughout; without birth loss the stated completion clock does not exist.

## 5. Controls, provenance, and limits

`tail_check.py` was independently written without author imports. It derives (3) and the first four scalar moments symbolically, then checks a stable version of the exact survival against 48 direct two-coordinate matrix exponentials, including omega=0, critical damping, and a very small nonzero frequency. All discrepancies are below 4e-16.

It also compares the complete six-branch angular formula for both instruments with (5), checks (6) by independent angular quadrature, and tests the tail coefficient through t=100000 at a=2, kappa=.7. There t^(3/2)S is `0.007450526428765151`, versus predicted `0.007450425422014002`. The analytic rescaling proves the asymptotic; these finite values only corroborate it. The regularized-density second moment, the different resolved/coherent band tails, and the exact cutoff divergence of (13) are checked separately. A positive Laplace integral and a 55-digit complex-root moment integral independently agree on the quoted p=5/4 value. The complete numerical result, stdout/stderr and actual command receipt are preserved.

No attempted assertion or helper failed in this continuation. The older failures remain unchanged in the older packet; no failure has been removed or silently replaced. `provenance_check.py` authenticates five reused sources and the actual new run. `SOURCE_BINDINGS.json` records those identities and runtime versions. The old PRE/final seals are authenticated as dependencies; no claim of redoing their entire underlying mathematical review is made.

The new author-tail seal known only by hash is `0ffc4d68970054377f6b80c4b5cc0ec593d38380944d8e5d202a6aa0090648c7`. This report, control, all complete output and source bindings are frozen by `PRE_COMPARISON_SEAL.json` before any access to that packet. Readiness for comparison does not give this raw result formal retained status.
