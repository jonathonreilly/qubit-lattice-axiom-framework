# Next campaign: Gauss reduction and actual finite-volume weak-coupling spectrum

Formulated personally after the block13 ground-state deficit proof. Still
provisional; do not claim a thermodynamic phase or import this as retained.

Use a fixed finite contractible open cubic box, all elementary plaquettes,
connected graph incidence D (outgoing positive) and plaquette boundaries B.
The integer cycle lattice ker D intersect Z^E has a fundamental-cycle basis
C with identity on spanning-tree chord rows. Contractibility/H1=0 ensures
B=C Z, with columns of Z generating the full integer cycle lattice, not just
its real span. This matters: otherwise a finite-difference continuum limit
could contain disconnected sublattice copies. Check Smith invariants.

For each finite matter occupation basis f in total N=2V, rho_f=N_x-2 is
integer with zero sum. Choose a spanning-tree integer solution E0(f) of
D E0=rho_f. Every physical electric field is E0(f)+C n, n in Z^c.
This is an exact isometry of the Gauss physical space to a direct sum of
affine flux lattices indexed by matter states. Onsite orbital mixing keeps
rho unchanged. A hopping f->f' across link l shifts n by integer t with
C t=e_l+E0(f)-E0(f'). Plaquette p shifts n by z_p.

Scale x=g n. The magnetic positive term becomes a finite-difference form
sum_p w_p ||psi(x+g z_p)-psi(x)||^2/(2g^2 a), while electric energy is
(Cx+gE0(f))^T W_E(Cx+gE0(f))/(2a). Bounded matter translations by g t tend
to identity, giving the free finite-box CAR Hamiltonian in the limit.
If gS->infinity, the cutoff domains exhaust R^c. Expected limit:
H_osc tensor I + I tensor H_free,matter, with
H_osc=[-partial^T A partial+x^T K x]/(2a),
A=sum_p w_p z_p z_p^T, K=C^T W_E C, both positive definite.
Frequencies are sqrt(eig(A^(1/2) K A^(1/2)))/a, equal to the nonzero
weighted lattice curl spectrum. Prove form convergence, compactness and
fixed-index spectral convergence at this fixed graph; do not exchange
thermodynamic and weak-coupling limits. Integer generation lets telescoping
shift paths control nearest-coordinate differences, ruling out hidden copies.

If gS->s in (0,infinity), expect the same matrix oscillator with DIRICHLET
boundary on the polytope |Cx|_infty<s, because hard compression retains the
1-ReW diagonal at flux endpoints. This differs from a full Gaussian vacuum.
For one isolated plaquette, C=b has |b|^2=4, A=1, K=4; the limit is
-1/2 d^2/dx^2+2x^2 on [-s,s], ground energy strictly above 1 for finite s.
The full-line ground energy is 1. Thus the order S~1/g sufficient for an
O(g^2) plaquette deficit is not a proof of arbitrarily accurate Gaussian
weak-coupling convergence: for that, gS must diverge. Quantify this in a
finite one-plaquette check, not as a universal encoding no-go.

Additional exact Gauss identity, potentially stronger and simpler:
W_E diagonal positive, L=D W_E^-1 D^T. On neutral charge configurations,
E_L=W_E^-1 D^T L^+ rho, E_T=E-E_L. Then
D E_T=0, E_T^T W_E E_L=0, and
E^T W_E E=E_T^T W_E E_T+rho^T L^+rho exactly on physical space.
The term g^2 rho^T L^+rho/(2a) is an exact Coulomb-kernel contribution, but
it does not prove the full static potential is Coulombic: transverse/gauge
energy can still confine. In a charge-dependent shifted continuum coordinate,
the electric cross term vanishes and hopping translates transverse flux by
e_l-W_E^-1 D^T L^+(D e_l). This is the Coulomb-gauge Peierls coupling obtained
from the exact physical Hilbert space. The integer-affine cutoff and finite
S boundary remain explicit.

Periodic boxes have harmonic flux/flat holonomy modes and do NOT satisfy
the positive-definite oscillator argument unchanged. Open contractible boxes
are a declared change of boundary domain, not an unnoticed simplification of
the preceding periodic result. No volume-uniform phase conclusion follows
without controlling the soft modes, charged correlations and monopole sector.
