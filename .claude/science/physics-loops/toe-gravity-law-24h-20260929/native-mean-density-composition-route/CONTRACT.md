# Native mean-density/grand-potential composition contract

New author composition, September30. Prior files remain immutable. The
supplied full-qubit H0, positive mu,tau, physical N4 threshold T0 and its
normalization remain unchanged. Main refreshed tofb5da8dd; selected procedures
7146fe17. No computation, git/source mutation, PR or formal review is planned.
Original deadline22:41UTC and runtime STOP guard remain binding.

Define e_L(rho) as the minimum energy per site over ALL density matrices
with mean particle number rho L^3, not the exact-N sector energy. Define
g_L(nu)=L^-3 min spec(H0-nu N). Put t=min_(||z||=1)<z^2,T0 z^2>, c=t/8.
Use the checked full-carrier lower composition and freshly reread actual
normalized compact-correction unitary upper. Derive exact prescribed-mean
density trials (continuity suffices; do not assume monotonicity of the pulse).
Seek matching e(rho)=c rho^2+o(rho^2), g(nu)=-nu^2/(4c)+o(nu^2), and every
thermodynamic grand-ground density rho(nu)=nu/(2c)+o(nu).

First prove any thermodynamic limits actually used. A bounded finite-range
seam comparison may prove the GRAND limit uniformly on bounded nu intervals;
finite-volume convex duality can then give the mean-constrained limit near
rho=0. No canonical fixed-N limit or exact-N upper may be inferred from this.
All-density coercivity c0 N(N-2)/V must confine minimizing densities to O(nu)
before a dilute lower is used in the grand minimization. Density slope must
follow from concave secants, including degenerate ground states; no
assumption of g differentiability, second derivative or phase order is allowed.

All compact-correction, volume, density and approximation limits must remain
ordered. No ODLRO, condensate, polarization selection, record law, Hamiltonian
selection or canonical EOS is targeted. Root's separate canonical block
candidate must not be opened until this composition is frozen; its known
method brief is not an input here. After this freeze a separate independent
PRE/check will address that candidate in another directory.
