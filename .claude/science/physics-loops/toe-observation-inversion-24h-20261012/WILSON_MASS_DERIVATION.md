# One-loop spatial Wilson mass: frozen author derivation

2026-10-12. Conditional perturbative calculation for TARGET.md. Supply continuous Euclidean time as the continuation of the canonical Hamiltonian, a noncompact U(1) Maxwell field with its Gauss/Coulomb sector, the literal unitary minimal links exp(i e A), and the ordinary quantum path-integral expansion. Link operators are not replaced by normal-ordered exponentials. Bare a=w=1 and bare mu=0. No mass counterterm is inserted in the following coefficient. This is not a nonperturbative mass theorem or a value derived from the framework's primitives.

Let X_i=1-cos k_i, W=sum X_i, s_i=sin k_i, omega^2=2W, and E^2=sum s_i^2+W^2. Gamma matrices are Hermitian Euclidean matrices. The free inverse propagator is
 D(p)=i gamma_0 p_0+i sum gamma_i sin p_i+W(p),
 S(-k)=[i gamma_0 k_0+i sum gamma_i sin k_i+W]/(k_0^2+E^2).
The photon covariant-gauge propagator is
 D^gamma_mn(k)=delta_mn/K^2+(xi-1)K_m K_n/(K^2)^2,
 K=(k_0,2sin(k_i/2)), K^2=k_0^2+omega^2.
Midpoint spatial link fields remove extra endpoint phases from these vertices.

At external fermion p=0 and internal q=-k, define the charge-stripped one-photon vertices
 V_0=i gamma_0,
 V_i=i gamma_i cos(k_i/2)-sin(k_i/2) I.
The scalar minus sine term is essential; it is the Wilson hopping derivative. The second spatial derivative at external p=0 is +I, so the seagull in the inverse propagator is +(e^2/2) sum_i integral D^gamma_ii. The temporal derivative is linear and has no seagull.

To fix the overall sign directly, expand the inverse of D0+eV+e^2T in a fixed photon background and then average:
 <(D0+eV+e^2T)^(-1)>=S0-S0<e^2T>S0+S0<eV S0 eV>S0+... .
Thus the effective inverse propagator is D0+e^2<T>-e^2<V S0 V>+O(e^4). Define delta m as its scalar coefficient (one quarter of the Dirac trace), not as a self-energy with an unspecified sign convention.

In Feynman gauge the temporal exchange contributes +W/[(k_0^2+E^2)(k_0^2+omega^2)]. The ith spatial exchange contributes [W cos k_i-sin^2 k_i] with the same denominator. Summing gives numerator
 W[1+sum cos k_i]-sum sin^2 k_i=4W-E^2.
Therefore
 delta m/e^2 = integral_BZ d^3k/(2pi)^3 integral_R dk_0/(2pi)
  {3/[2(k_0^2+omega^2)] +(4W-E^2)/[(k_0^2+E^2)(k_0^2+omega^2)]}.

Integrating the continuous frequency exactly,
 C_W:=delta m/e^2
 = integral_BZ d^3k/(2pi)^3 {3/(4omega)+(4W-E^2)/[2E omega(E+omega)]}
 = integral_BZ d^3k/(2pi)^3 [E^2+3E omega+8W]/[4E omega(E+omega)] >0.
Near the origin the integrand is 1/|k|+O(1), so this three-dimensional integral is infrared integrable. Away from k=0, E and omega are strictly positive. This positivity establishes the sign of the one-loop coefficient without a finite numerical search. It does not fix the sign of the exact interacting mass at arbitrary coupling.

Gauge-parameter cancellation is pointwise before frequency integration. The lattice Ward identity gives sum K_m V_m=-D(-k). Hence the longitudinal exchange correction to the inverse propagator is -(xi-1)D(-k)/(K^2)^2; its scalar trace is -(xi-1)W/(K^2)^2. The spatial seagull gives +(xi-1)omega^2/[2(K^2)^2]=+(xi-1)W/(K^2)^2. They cancel exactly. The remaining gamma-vector numerator integrates to zero by oddness. No separate claim that each diagram is gauge independent is made.

For the naive w=0 control at zero bare mass, the scalar seagull vanishes and the scalar trace of every one-loop exchange numerator vanishes. Its extra fermion cones remain; it is not the same light-species model. This is a check of the mechanism, not evidence that naive fermions solve the physical problem.

At small e, the zero of the renormalized inverse-propagator mass requires the formal perturbative critical bare parameter mu_c=-e^2 C_W+O(e^4). For a small nonzero calibrated mass the bare parameter is measured relative to that critical surface, with multiplicative and higher-order corrections also required. The previously used tree label mu=m_e/Lambda is not automatically preserved by the literal interacting Hamiltonian. One must not insert a very small physical mu into the free formulas and silently omit this subtraction. Conversely a tuned renormalized model remains possible; this does not exclude Wilson QED or all discrete microscopic laws.

Needed controls before reuse: independently derive the sign and seagull, verify the 4x4 scalar numerator and Ward cancellation, integrate the continuous frequency independently, compare convergent deterministic cubatures and an independently implemented regulator/domain treatment, and inspect primary Hamiltonian-limit prior art. Numerical quadrature and focused verification are not a formal audit.
