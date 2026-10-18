# Independent full-dimer mapping and four-site trial check

## Exact Clifford change of variables
Define U|t,r>=|t,t xor r>, with the first physical bit on the first x-dimer site. Direct 4x4 matrix multiplication independently gives zero residual for all six relations:

X1=tau_x rho_x, Y1=tau_y rho_x, Z1=tau_z;
X2=rho_x, Y2=tau_z rho_y, Z2=tau_z rho_z.

For native ferromagnetic H=−J sum sigma_x^a sigma_(x+ea)^a, the full transformed Hamiltonian is therefore exactly

H/(−J)=sum_d [tau_x(d)
 +rho_x(d) tau_x(d+x) rho_x(d+x)
 +tau_y(d)tau_y(d+y)rho_x(d)rho_x(d+y)
 +tau_z(d)tau_z(d+y)rho_y(d)rho_y(d+y)
 +tau_z(d)tau_z(d+z)(1+rho_z(d)rho_z(d+z))].

Here d+x is the neighboring x dimer (two original lattice spacings), while d+y and d+z are one original lattice spacing. No projection or Hamiltonian modification is involved; both logical qubits are retained. Periodic x length must be even, with small-size duplicate-bond conventions handled consistently.

## Conditional partial expectation
Put all tau spins in the same product state with Bloch vector (s,0,m), m²=1−s². The operator partial expectation is

< H >_tau=−J [N_d(s+m²)+sum_d(s rho_x(d)rho_x(d+x)+m² rho_y(d)rho_y(d+y)+m² rho_z(d)rho_z(d+z))].

It is an exact variational energy functional on rho states. It is not the autonomous rho Hamiltonian for native time evolution: tau-rho correlations generally develop, and no invariant manifold, spectral separation, or adiabatic reduction has been supplied.

## Four-site trial and optimization
Pair neighboring rho sites along y and use cos(eta)|00>−sin(eta)|11> on each pair. Set t=sin(2eta); then YY=t, XX=−t and single-site Z=cos(2eta). Physical four-site blocks consist of two x dimers joined along y. With even y size and no coincident endpoints, rho x bonds have zero mean, half the rho y bonds have YY=t and the rest zero, and all rho z bonds have ZZ=1−t². Thus, per original site,

E/N=−(J/2)[s+(1−s²)(2−t²+t/2)].

For −1<=t<=1, B(t)=2−t²+t/2 is maximized at t=1/4 with B=33/16. Because 1−s²>=0, this maximizes the bracket at any fixed s. Then s+B(1−s²) has its global maximum on −1<=s<=1 at s=1/(2B)=8/33. The maximum bracket is B+1/(4B)=1153/528, giving

E_trial/N=−1153J/1056.

Exact rational arithmetic independently checked this value. It improves the previous −17J/16 by 31J/1056 per site and lies below the fully site-separable bound −J. This is a new variational upper bound on the ground energy for compatible periodic volumes; it does not establish a lower bound or equality for the true ground energy.

## Scope
The construction uses the existing Hamiltonian and an explicit entangled trial state; the full Clifford map has no discarded parity degrees of freedom. The four-site state is a product across blocks but is not fully separable across physical sites. No stationarity follows from optimizing this restricted family. The trial picks x and y pairing directions and translation periods, so it is not a derived symmetry-selected vacuum. Symmetry averaging can preserve the energy but does not supply stationary dynamics. No scalar excitation, cosmological field identification, or measurement coupling is established by the energy improvement.
