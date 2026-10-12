# Independent QUMOND solar Hessian derivation

This root derivation precedes inspection of the gravity worker's solar code,
derivation or numerical output. It is a conditional calculation for the newly
supplied QUMOND field equation, not a new fit to a Solar-system observation.
The shared galaxy-calibrated acceleration scale still depends on an algebraic
circular-response approximation; a full QUMOND disk calibration is separate.

Define the gravitational potential Phi by acceleration=-grad(Phi). With
r_M=sqrt(GM/a0), x=r/r_M and a Newtonian uniform external acceleration
a0 eta e_z, let u=grad(Phi_N)/a0=x/x^3-eta e_z. The supplied equation is
laplacian(Phi)=div[nu(|grad Phi_N|/a0) grad Phi_N], with
nu(q)=1/[1-exp(-sqrt(q))]. Write phi=Phi-Phi_N. Away from the point source,
laplacian(phi)=(a0/r_M) div_x[(nu(q)-1)u]. Since nu->1 exponentially near
the source, the anomalous field is harmonic there. Its Hessian is

`H_ij=-a0/(4pi r_M) integral div_x[(nu-1)u] (3n_i n_j-delta_ij)/x^3 d^3x`.

Set c=cos(theta), radial inverse coordinate v=1/x, and
q=sqrt(v^4+eta^2-2eta v^2 c). Direct differentiation gives

`div_x[(nu-1)u] = nu'(q) v^3/q
 [-2v^4+4eta c v^2+eta^2(1-3c^2)]`.

Thus h=H_zz r_M/a0 equals

`h_direct=-1/2 integral_0^infinity dv integral_-1^1 dc
 nu'(q) v^2/q [-2v^4+4eta c v^2+eta^2(1-3c^2)] (3c^2-1)`.

Independently integrate the Poisson Hessian by parts. With
T_zz=(3c^2-1)/x^3,
`u dot grad_x T_zz=-3(3c^2-1)/x^6+3eta c(5c^2-3)/x^4`.
The origin surface vanishes exponentially; the infinity surface vanishes as
1/x even for the nonzero constant external response. Therefore

`h_parts=3/2 integral_0^infinity dv integral_-1^1 dc
 [nu(q)-1] [-v^2(3c^2-1)+eta c(5c^2-3)]`.

Axisymmetry and harmonicity give H_xx=H_yy=-H_zz/2. If the anomalous potential
is written `phi=Q_Phi/2 [z^2-r^2/3]`, then Q_Phi=3H_zz/2. A publication
using positive Newtonian potential U=-Phi has the opposite quadrupole sign;
its precise convention must be read before comparison. The present h values
are not labeled with a paper's Q2 convention in advance.

The zero of q at v=sqrt(eta),c=1 is integrable. The numerical method uses
c=1-2t^2, dc=4t dt, and splits the v interval at sqrt(eta). Both direct and
parts forms are evaluated with distinct integrands at increasing orders.
Finite-order agreement is a convergence check, not interval quadrature.
For the parts form, the absolute tail above V>sqrt(eta) is bounded by

`6 exp(sqrt(eta)-V) [V^2+2V+2+eta]/[1-exp(-(V-sqrt(eta)))]`.

Indeed q>=v^2-eta, sqrt(q)>=v-sqrt(eta), |3c^2-1|<=2 and
|c(5c^2-3)|<=2. Integrating the exponential polynomial yields the bound.
It is a rigorous truncation bound distinct from numerical angular/radial
error. Freeze eta in {.5,1,2,3,4}, cutoff40, and Gauss orders64,128,256,512
before execution. No quadrupole datum calibrates the model or quadrature.

After independent results are sealed, compare to the other worker's raw
forms, then read the primary physical external acceleration, its inference
assumptions, and the new ephemeris fitted quadrupole. The conversion
g_external=a0 eta nu(eta) is itself a declared collinear/algebraic Galactic
background hypothesis, not a consequence of imposing uniform local boundary
data. Preserve its uncertainty or return a prediction region.
