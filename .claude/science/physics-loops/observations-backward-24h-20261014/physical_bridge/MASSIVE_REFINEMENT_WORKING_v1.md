# Sharper mass bound and a spatial-interference ordering test

Date: 2026-10-15. Status: open working calculation; focused independent checks
in progress. Root authored the original low/high comparison and the count
implementation in MASSIVE_RESPONSE_WORKING_v1.md. During its independent
derivation, the focused checker suggested separating the clock term globally
and using the exact zero-offset response. Root rederives those integrals and
the consequence below. This provenance is distinct from a fully independent
final-source review.

## Sharper bound with the original L2 clock domain

Keep the exact observation, common energy-amplitude isometry, force and all
physical qualifications of the first working note. Write F=F_clock+F_force.
Only the force part now needs the stronger time regularity. Define

    V_F=sum_A sup_(v,n) TV{[(b_v,A.W_A)']/d_v,A},
    d_v=1-v n.u, b_v=(1-|u|^2)(v n-u)/d_v.

This is a nonnegative number computed from supplied trajectories/weights,
not an initial-field restriction. With delta=1-beta and B0,B1,B2 as derived
in the first note, a valid individual supplier is

    V_F,A <= [B2 ||W||1+2 B1 ||W'||1+B0 TV(W')]/delta
              +a[B1 ||W||1+B0 ||W'||1]/delta^2.

Thus no BV(c) premise is needed: compact L2 clocks have all the finite L1
moments used here. Use one common translated spacetime origin, write t and x
relative to it, and define

    C=sum_A integral |c_A|,
    D=sum_A integral [|t c_A|+(1-|u_A|^2)|W_A|],
    E=sum_A integral |t|(1-|u_A|^2)(1+|u_A|)|W_A|.

Let Delta=omega-k. Direct splitting at fixed k,n gives

    |F_clock,mu-F_clock,0|
       <= C Delta/(k omega)+D_clock Delta/omega,
    |F_force,mu-F_force,0|
       <= D_force Delta/omega+E Delta.

The last term is used only below K. Above K, compare force responses by the
BV bound 2V_F/k^2. The triangle inequality in the actual L2(d^3k)/(2pi)^(3/2)
norm, extending the first two radial integrals to infinity, gives

    epsilon_mu(K) <= 1/(sqrt(2) pi) [
       C sqrt((2-pi/2)mu)
       +D sqrt((pi/2-4/3)mu^3)
       +(E mu^2/2)sqrt(K)+2V_F/sqrt(K)].

For E,V_F>0 choose K=4V_F/(E mu^2), giving the particularly simple

    epsilon_mu <= 1/(sqrt(2) pi) [
       C sqrt((2-pi/2)mu)
       +D sqrt((pi/2-4/3)mu^3)+2mu sqrt(E V_F)].       (R1)

If E=0 or V_F=0, take the corresponding limiting cutoff; the optimized term
is zero. These are legitimate infima of the all-K bound, not assertions that
a finite cutoff achieves them. At mu=0 the comparison is exactly zero.

The two exact radial constants can be checked without an imported estimate:
put k=mu sinh y, then z=exp(-y). One obtains

    integral_0^infinity (1-k/omega)^2 dk
       =2mu integral_0^1 z^2/(1+z^2) dz=(2-pi/2)mu,
    integral_0^infinity k^2(Delta/omega)^2 dk
       =(mu^3/2) integral_0^1 (1-z^2)^2/(1+z^2) dz
       =(pi/2-4/3)mu^3.

Also k^2 Delta^2<=mu^4/4, which supplies the low-frequency force-phase term.
All three constants in R1 have explicit proof suppliers; no mass-shell
monotonicity claim is needed.

## A useful effect of the derived constant-offset contrast

Let C0=|sum_A integral c_A| and

    M=sum_A integral |c_A| (|t|+|x_A(t)|).

At the massless temporal/spatial phase,

    |sum_A integral c_A exp(ik[t-n.x_A])| <= C0+k M.

Therefore (R1) also holds with C replaced by C0 and D replaced by D+M.
An exact constant-offset contrast derived in M6 has C0=0. Its mass correction
then has an explicit O(mu) bound; a pure-clock contrast has O(mu^(3/2)).
This is a bound on the finite response operator after the common-amplitude
identification, not a claim about a physical mass, the actual state or data
calibration. A small floating C0 is not zero: retain its sqrt(mu) term.
The spatial first moment M is finite for prescribed compact path segments.

For the exact two-body count fixture, choose time origin1.8 for its first
contrast, with support [.2,3.4]. Conservative exact suppliers are

    C0=0, C<=4, D<=4*1.6+4=10.4,
    M<=4*1.6=6.4, E<=4*1.6=6.4, V_F<=16.

The direct clock is only on the station at the chosen spatial origin. The
force BV bound uses TV(W_s')<=8 and TV(W_b')<=8 at stationary paths. Hence

    epsilon_mu <= [(16.8)sqrt((pi/2-4/3)mu^3)
                           +2mu sqrt(102.4)]/(sqrt(2)pi).               (R2)

The second channel is a time translation, with the same per-channel bound if
its energy-space isometry is translated as well. For a simultaneous vector
comparison use a SINGLE common time origin and compute all its moments there;
do not combine unrelated per-channel isometries as one operator bound.
For example the common origin2.3 bounds both channels by T=2.1, giving
D+M<=20.8,E<=8.4,V_F<=16 and the same zero C0. The vector norm is at most
sqrt(2) times that scalar bound. No reference geometry or readout has changed.

## Why a general massless upper-Gram substitution needs a proof

For fixed points and identical real clock weight c(t), angular integration
of the exact massive energy response gives

    G_mu=(1/(2pi^2)) integral_mu^infinity |c_hat(omega)|^2
          v sum_AB sinc(v omega r_AB) d omega,
    v=sqrt(1-mu^2/omega^2), sinc(z)=sin(z)/z.

Take THREE stationary points at the vertices of an equilateral triangle of
side r, and add their clock readouts. At a frequency omega0 with omega0*r=pi,
the spatial factor is S_mu=3v+6sin(pi v)/pi, whereas S_0=3.
At v=2/3, mu=sqrt(5)omega0/3,

    S_mu/S_0=2/3+sqrt(3)/pi >1.

This shows a strict spectral reversal. It can be realized with compact smooth
zero-integral weights, not only an infinite-duration monochromatic function:
choose any nonzero smooth real bump psi of compact support and
c_T(t)=partial_t[psi(t/T)sin(omega0 t)]. Its integral is exactly zero. As T
grows, its positive-frequency power normalized by T concentrates at omega0;
negative-frequency power gives the conjugate and the same real energy norm.
Integration by parts makes its Fourier transform decay arbitrarily fast away
from that peak, so dominated localization gives the displayed strict ratio.
For sufficiently large FINITE T it exceeds one. The normalization cancels in
the ratio. This supplies existence of compact smooth counterexamples.

The statement concerns this general three-clock multipath functional. It
does not assert that the specific two-body coherent-count fixture violates
mass ordering. A single stationary clock has an order-preserving density v;
discarding interference between locations would miss this counterexample.
The correction bound R1/R2 is still applicable and does not rely on ordering.

Independent checking and explicit finite-window computations remain pending.
No claim of observational falsification or framework-wide no-go follows.
