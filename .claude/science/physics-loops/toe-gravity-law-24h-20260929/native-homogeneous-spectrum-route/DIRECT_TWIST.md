# Direct homogeneous twist and the unresolved local spectral weight

This is a third, elementary construction on the actual pair law. It also
records why it does not replace the two-cut argument at positive density.
Let theta=2pi/L and U=exp(i theta sum_x x_1 n_x). Work in any homogeneous
canonical ground vector that is also a translation eigenvector. If N/L is
not an integer, Upsi and U*psi each have a different translation eigenvalue
from psi. If the canonical ground is unique, both are orthogonal to it.

The checked actual row expansion is

 H0=mu Ddiag+sum_(e,f)K_ef B_e* B_f,
 max_e sum_f |K_ef|<=b=3mu+24tau,
 sum_e B_e*B_e=sum_edges n_x n_y<=9N.

Edges are physical unordered axial/plane edges, with both plane centers
retained in K. For every nonzero row connection, unwrap the center locally.
The affine first-coordinate sums p_e of the two endpoints differ by at most6.
Torus wrapping changes their difference by a multiple of L and has no effect
on the phase exp(i theta(p_e-p_f)). The diagonal term commutes with U.
Averaging the two trial energies cancels the linear current exactly, without
assuming a real ground or zero persistent current:

 ( <Upsi,H0 Upsi>+<U*psi,H0 U*psi> )/2 -E_N
   =sum_(e,f)K_ef [cos(theta(p_e-p_f))-1]<B_e*B_f>.

Use |cos t-1|<=t^2/2, |p_e-p_f|<=6 and
|<B_e*B_f>|<=(<B_e*B_e>+<B_f*B_f>)/2. The symmetric absolute row bound gives

      average excess <=162 b theta^2 N.                  (D1)

Each trial excess is nonnegative by the sector variational principle, so
one of the two normalized, number-preserving trials has excess at most(D1).
For a unique sector ground this proves the same-sector gap upper bound
162b(2pi)^2 N/L^2, whenever N/L is noninteger. The result is useful for
N=o(L^2), but grows like rho L at fixed positive density in three dimensions.
A degenerate ground may absorb the trial entirely; then(D1) does not bound a
positive-frequency gap above the full ground projection.

The row bound is the already focused-checked actual density-response input,
not a bosonic-pair commutator. Its proof sums the axial S row(2mu), plane S
rows from two centers(3mu), and axial/plane gradient row bounds at most24tau.
The same calculation yielded the actual density f-sum m1<=162b rho s^2 for
s=2sin(pi/M). A lower bound on homogeneous m_(-1), or on the norm of the
FULL-ground-complement density trial, is still required to obtain a
homogeneous density-coupled soft mode. Neither the global twist state nor
exact parity partners supply that lower bound.

The already checked nearby-field result remains exactly a modulation jump
OR inelastic density response at some regular lambda* in(-alpha rho,alpha rho).
The scalar EOS cannot move lambda* to0. The actual N=1 example in
EXACT_PARITIES.md shows why zero-energy degeneracy alone must not be promoted
to positive-frequency weight; the response packet's finite diagonal-pencil
example separately shows why scalar energy convergence cannot establish
pointwise zero-field susceptibility. The latter is a logical discriminator,
not an assertion that H0 is diagonal at finite density.
