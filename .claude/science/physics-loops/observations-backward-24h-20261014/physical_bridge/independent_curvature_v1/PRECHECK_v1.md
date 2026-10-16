# Independent de Sitter scalar/count bridge precheck

Reviewer /root/inertial_response_check; root remains author. Frozen before any
new physical_bridge author draft or code is opened. The complete supplied
curved-action note was read at SHA-256
1eb49b6a111c0532e9ed6540e3a11ce8970cc1b9dd8cb0cd026e23bb0becd874,
and unchanged M6 conventions at note SHA-256
4d4bb8843d43e24c4184f4f99347766a26805df9a9021e647cb89a6a7fa5fb76.
Base c6b3c14760d0d2efb5f7eacf3b9ff7ae25cbf0ee. No raw observations,
network, canonical mutation, new initial-state prescription or formal audit.

## Domain and normalization

Set c=1, signature -+++, H>0, a(t)=(1-Ht)^(-1), a(0)=1 and
0<=t<=T<1/H. This t is conformal time, not comoving-observer proper time.
Einstein proper time obeys d tau_E=a dt; the proper clock of a body with
comoving-coordinate velocity u=dx/dt obeys d tau_J=A a sqrt(1-|u|^2)dt.
Here |u| is peculiar speed measured by the Einstein comoving tetrad, k is
comoving momentum, and k/a is physical momentum. No fixed physical areal
radius or static-patch Killing time is being identified with x or t.

The action's coupled perturbation is h=delta varphi=sqrt(K_u0)delta u_field,
with S_h^(2)=-Q integral sqrt(-g_E)[g_E^(mu nu)partial_mu h partial_nu h
+m^2 h^2], Q=Q0(1+k_parameter)>0 and m^2=B H^2, B>12. This convention
has no 1/2 in front of Q's scalar kinetic term. Equivalently sqrt(2Q)h is
a conventionally normalized canonical scalar. log A=alpha_m h+O(h^2),
alpha_m^2=k_parameter. Couplings in the supplied c,W can be absorbed there;
rescaling h without rescaling energy and readout weights is not permitted.
The other field directions and free linear metric excitations are outside this
scalar response channel. Holding the Einstein de Sitter background fixed is
part of this linear scalar problem, not a proof that all metric data vanish.

## Field equation and two distinct energies

The source-free equation is
 h''+2 mathcalH h'-Delta h+a^2 m^2 h=0,
 mathcalH=a'/a=H a.
With chi=a h it becomes
 chi''-Delta chi+V(t)chi=0,
 V=a^2 m^2-a''/a=(B-2)H^2 a^2=M^2 a^2,
 M^2=(B-2)H^2>0.
Thus the frozen equation has mass-squared V(0)=M^2, not m^2. No perturbation
stationarity was assumed, and its time-dependent potential is retained.

The positive computational energy is
 E_chi(t)=1/2 integral[|chi'|^2+|grad chi|^2+V(t)|chi|^2]d^3x,
 E_chi'=V'/2 integral|chi|^2.
It is not conserved. The physical quadratic Einstein-frame energy measured by
comoving unit observers n=a^(-1)partial_t, integrated over their proper slice,
is instead
 E_com(t)=Q a integral[|h'|^2+|grad h|^2+a^2 m^2|h|^2]d^3x.
The conformal-time Hamiltonian is a E_com, not E_com. Neither is a static
Killing energy. At t=0 their lapse difference happens to vanish. The vacuum
stress is excluded. In chi variables,
 E_com=Q/a integral[|chi'-mathcalH chi|^2+|grad chi|^2+a^2 m^2|chi|^2].
Its derivative is Q a mathcalH integral[-3|h'|^2+|grad h|^2+3a^2m^2|h|^2],
so it is not generally monotone.

Write f=chi(0)=h(0), p=chi'(0)=h'(0)+Hh(0). Then
 2E_chi(0)=integral[p^2+|grad f|^2+M^2 f^2],
 E_com(0)/Q=integral[(p-Hf)^2+|grad f|^2+B H^2 f^2],
 2E_chi(0)=E_com(0)/Q+2H integral h(0)h'(0)-H^2 integral h(0)^2.
The energies cannot be identified. Nonetheless exact uniform equivalence is
 lambda_- E_com(0)/Q <= 2E_chi(0) <= lambda_+ E_com(0)/Q,
 lambda_+/-=1-1/(2B) +/- sqrt(4B+1)/(2B).
This follows from the two-by-two matrix on (h'(0),m h(0)); spatial gradients
add an identity term. For B>12, 2/3<lambda_-<1<lambda_+<5/4. The constants
are sharp in a long-wavelength limit, not attained by a nonzero spatially
constant finite-energy datum. Arbitrary finite-energy initial data remain.

## Exact observation-weight transformation

For the supplied coordinate-time scalar functional
 O[h]=sum_paths integral {c h-(1-|u|^2)W dot(grad h+u h')}dt,
put sigma=1-|u|^2. The exact transformed functional on chi has the same
force syntax with
 W_tilde=W/a,
 C=c_tilde=[c+sigma mathcalH(W dot u)]/a.
In particular mathcalH/a=H. The additional direct-field term has a PLUS sign;
it comes from h'=(chi'-mathcalH chi)/a. It is absent only for special weights.

This transformation does not say that the flat-reference M6 weights apply
unchanged in this chart. Null curves remain conformally Minkowski but the
reference lapse is a sqrt(1-|u|^2), and the background coordinate force of a
freely falling massive body is -sigma mathcalH u. The actual trajectory-clock
adjoint must include that drift and its velocity derivative. The M6 retarded
endpoint algebra still applies with the appropriate reference lapse and
trajectory, not with a frozen proper-time Jacobian. A supplied external force
and its scalar variation remain additional inputs. No coordinate acceleration
is silently equated to a proper accelerometer readout.

For each path define P=sigma W_tilde, J=-P dot u and vector
 Bvec=P-u(P dot u). With W continuous, compactly supported and zero at the
outer endpoints, integrating the J chi' term by parts gives the mode readout
 O_k=sum_paths integral exp(i k dot x(t))[A(t)-i k dot Bvec(t)]v_k(t)dt,
 A=C-J'=C+(P dot u)'.
No boundary term remains. If c has compact BV zero extension, W is continuous
with W' BV and compact support, and the path is smooth with bounded derivatives
on the finite interval, A is BV, Bvec is continuous, Bvec' is BV. Distributional
endpoint/jump variations must be included in BV norms; values at isolated
clock jumps do not change the integral. These conditions are stronger than
needed for the comparison bound but also make the frozen readout bounded.

## Controlled comparison to the frozen potential

Use the SAME arbitrary initial chi data for the true solution v and frozen
solution v0 at each q=|k|, with omega=sqrt(q^2+M^2):
 v''+(omega^2+R(t))v=0, R=M^2(a^2-1)>=0,
 v0''+omega^2 v0=0,
 e=v-v0=-integral_0^t sin(omega(t-s))R(s)v(s)ds/omega.
Set N_k^2=|p_k|^2+omega^2|f_k|^2. Since R'>=0, the mode energy obeys
 E_k(t)<=((q^2+V(t))/omega^2) E_k(0), hence
 |v(t)|<=N_k/omega, |v'(t)|<=sqrt(q^2+V(t))N_k/omega.
Consequently |e(t)|<=D N_k/omega^2 and |e'(t)|<=D N_k/omega, where
 D=integral_0^T R(s)ds=M^2 H T^2/(1-HT).
These are uniform over initial phase; no chosen vacuum/state is used.

For one path let delta=1-sup|u|>0, J1=integral|u'|dt and
 A1=integral|A|dt, B1=integral|Bvec|dt. Define
 S_A=(2||A||infty+TV A)/delta+||A||infty J1/delta^2,
 S_B=(2||Bvec||infty+TV Bvec)/delta+||Bvec||infty J1/delta^2.
For multiple paths sum their A1,B1,S_A,S_B, each using its own delta,J1.
All fields use common initial data: summing constants is a triangle bound,
not independent energies or an assertion that cross terms vanish.

Low momentum has the direct bound for the normalized mode response row
 |Delta O_k|/N_k <= D(A1+q B1)/omega^2
                    <= D(A1/M^2+B1/(2M)) =: L.
For high momentum, swap t and s in Duhamel and integrate each outer phase
exp(i[q n dot x(t) +/- omega t]) once. Its derivative has modulus at least
delta omega. BV integration by parts gives, on every [s,T],
 |integral g exp(i phase)dt| <= (S_A+q S_B)/omega
for g=A-iq n dot Bvec. Therefore
 |Delta O_k|/N_k <= D(S_A+q S_B)/omega^3.
The inner sine supplies one factor 1/omega and |v(s)| another; both must be
kept. The difference is a bounded energy functional despite point-trace force
being unbounded without time averaging.

With unitary spatial Fourier transform, the exact real-data dual squared norm
of a functional is (2pi)^(-3) integral (|ell_f|^2/omega^2+|ell_p|^2)d^3k,
where ell are response coefficients before the (2pi)^(-3/2) Fourier prefactor.
Reality pairs k and -k, not two independent copies; there is no extra factor2.
For ANY K>0 the conservative explicit bound is
 ||O_V-O_0||_H0^2 <= (2pi^2)^(-1) {
   K^3 L^2/3
   +D^2[S_B^2/K+S_A S_B/K^2+S_A^2/(3K^3)] } =: epsilon_K^2,
 ||data||_H0^2=2E_chi(0).
The tail follows by omega>=q and integrating q^(-2),q^(-3),q^(-4). K may be
optimized without changing the theorem. This is a one-sided bound, not an
exact Gram nor a claim that it is small near t=1/H. Multiplying by
sqrt(lambda_+/Q) converts it into an E_com(0)^(1/2) bound. If an energy budget
is absent, only the conditional inequality follows. At fixed B,T, bounded
weights/path norms and fixed K, the displayed bound tends to zero as H tends
to zero (D=O(H^3), M=O(H)); the H=0 equation agrees identically. This limit
cannot be taken while allowing windows/paths to violate the uniform hypotheses.

## The frozen response is itself bounded

For completeness, let U1=||u'||infty and J2=TV(u') on [0,T]. Uniformly in
p_phase=+/-1+(q/omega)n dot u, |p_phase|>=delta. For scalar B_n=n dot Bvec,
Z=(B_n/p_phase)' obeys
 Zinf<=||Bvec'||infty/delta+||Bvec||infty U1/delta^2,
 TVZ<=TV(Bvec')/delta+2||Bvec'||infty J1/delta^2
       +||Bvec||infty J2/delta^2+2||Bvec||infty U1 J1/delta^3.
Set S_Z=(2Zinf+TVZ)/delta+Zinf J1/delta^2. A first integration by parts of
B_n has no endpoint term because Bvec vanishes there; a second BV integration
then gives |integral B_n exp(i phase)dt|<=S_Z/omega^2. The clock term has
one BV integration, <=S_A/omega. The normalized two-initial-component row for
O_0 is thus at most (S_A+S_Z)/omega^2 (sum these constants across paths).
Since integral_0^infty q^2/(q^2+M^2)^2dq=pi/(4M),
 ||O_0||_H0 <= (sum_paths(S_A+S_Z))/sqrt(8pi M).
This controls O_V by adding epsilon_K. Smooth finite-energy data first justify
all rearrangements; the bounds extend by density to the massive H1 x L2 energy
space. It is a finite-time variable-potential result, not a static-horizon or
retarded-source decay theorem. The ultraviolet/infrared split is necessary for
this stated elementary bound; dropping oscillatory cancellation and integrating
the pointwise derivative estimate over all momentum would diverge.

## Independent concrete control plan

Use H=1/10,B=16,T=1, x(t)=(t/10+t^2/40)e1, u=1/10+t/20,
W=16t^2(1-t)^2 e1 and c=(2/5)16t^2(1-t)^2. These are synthetic compact
windows, not data fits. Their transformed A and Bvec are rational polynomials;
absolute polynomial coefficient sums give conservative exact BV/sup/L1 bounds.
Check symbolic field/energy/weight identities independently, solve both h and
chi mode equations from consistently transformed initial data, compare original
and transformed readouts by quadrature, compare the direct difference with its
Duhamel integral, and check every computed normalized response row against both
proved bounds over low/high momentum and angular samples. Record numerical
error, versions, all failed attempts and no claim of certified quadrature.
