# Fixed two-pair compactness derivation before controls

Author checkpoint, September30,2026. No new computation has run. The new
contract remains frozen. The proposed result is V S_(2,L)->T0 on all fifteen
channels for fixed mu,tau>0, fixed guard R>=14 and odd L tending to infinity.
This is not a uniform-n expansion or a physical boundary comparison.

Use the actual zero-total-momentum four-particle orbit Hilbert space. Odd L
makes every four-site translation orbit free: the order of a stabilizing
translation divides both4 and odd L. Let psi be an orbit-amplitude vector.
For the nine forward graph bonds d,e define

 f_de(r)=psi({0,e,r,r+d}) if those sites are distinct, else0,
 F_de(r)=f_de(r)/sqrt2.

These fields obey exchange F_de(r)=F_ed(-r), including their actual compact
matching multiplicities. For r=0 every entry vanishes because the two bonds
share their anchor. Outside the finite collision core, the map to this
exchange-symmetric ordered pair space is an isometry. Inside the core it is
only a redundant removal map; no isometry is asserted there.

Restricting actual positive rows to graph-edge residuals gives

 E>=2a sum_(r,d,e,j)|F_de(r+e_j)-F_de(r)|^2,
 E>=2 sum_e S_onepair(F_.e),
 E>=mu ||Q_nonmatching psi||^2.

The last bound is the actual N4 no-perfect-matching D>=1 classification.
The factor two in the first two formulas comes from f=sqrt2 F, not from a
bosonic commutator. Periodic Fourier projection onto the mean M=V^-1sum F
and S_onepair(0)=2mu P_high imply

 E>=4mu V ||P_high M||_HS^2.

Exchange makes M symmetric, so all components outside Sym^2 U tend to zero
for uniformly bounded raw energy.

A needed uniform discrete torus Sobolev inequality is

 ||F-M||_ell6 <=C ||gradient F||_ell2,

with C independent of L. A self-contained proof uses the translation-
invariant piecewise-affine interpolant on unit cubes. Its mean is the
lattice mean, its L6 norm is equivalent to the lattice ell6 norm and its
Dirichlet norm is bounded by the lattice edge form. Extend periodically,
cut off on a fixed number of periods at scale L, and apply the Euclidean
Sobolev inequality; the cutoff term L^-1||v||2 is controlled by the
mean-zero periodic Fourier Poincare inequality. Euclidean Sobolev itself
follows from the elementary three-direction W11 inequality obtained by
Fubini and Cauchy, applied to |v|^4. Thus no dilute-gas theorem is imported.
The common pin then bounds ||M|| and every fixed F(r) by C sqrt(E).

Let chi_R,L be the physical raw guarded incoming map, with exterior
amplitudes sqrt2 U A U^T, zero in the fixed guard collision region. The
actual normalized polar frame is chi_R,L G_L^-1/2/sqrt(V), where
G_L=chi_R,L^dagger chi_R,L/V=I+O(V^-1). The exact finite Schur minimizer with
polar frame coordinate A, rescaled by sqrt(V), minimizes raw energy
V<A,S_(2,L) A> subject to

 chi_R,L^dagger psi_L /V =G_L^1/2 A.

The minimizer is translation invariant by the frame and uniqueness in its
gapped complement. Its raw energy is uniformly bounded by the checked trial
frame estimate. The constraint equals the U-U component of mean F_L, up to
O(V^-1) from a fixed number of bounded core entries. Therefore

 mean F_L -> U A U^T.

Local diagonal compactness gives a physical infinite orbit profile psi_inf.
Its Q_nonmatching component is in ell2; in the separated two-pair exterior,
F_inf-U A U^T belongs to ell6 by Fatou. The actual positive finite rows and
D term give lower semicontinuity of the physical energy. No free reference
operator is substituted in the collision core.

To compare the limit with T0, its difference from the true incoming profile
Phi_A must be approximable by compact responses in the physical energy
seminorm. The core difference is finite and the Q difference is ell2.
In the separated exterior the difference u is ell6 and has finite actual
free-pair row energy. With a cutoff eta_m equal to one on the m-ball,
finite-range row commutators are bounded by

 C m^-2 sum_(annulus)|u|^2
 <=C (sum_(annulus)|u|^6)^(1/3) ->0.

The existing tail row energy also tends to zero. Cut Q in its ell2 norm;
its operator is bounded and its couplings to the core have finite support.
This gives genuine compact physical response vectors whose energies tend
to the limiting energy. The variational definition of T0 consequently gives

 <A,T0 A> <=liminf V<A,S_(2,L) A>.

For the reverse bound, choose one common finite-support response map for
all15 incoming columns whose actual infinite energy form is at most
T0+epsilon I. Such maps follow from the checked compact/l2 variational
threshold definition and density in finitely many columns. Embed
Phi_A+chi_A on large odd tori. All nonzero square rows lie in a fixed
collision neighborhood, so their energies agree exactly with the infinite
ones. The frame-coordinate matrix differs from I by O(V^-1); invert that
15x15 matrix to impose the exact polar-frame constraint. The trial energy
then gives the limsup bound. Polarization in finite dimension gives operator-
norm convergence, without a claimed rate.

Combining this with the checked finite Schur/band theorem should imply
V lambda_j(H_N=4,L)->lambda_j(T0), j=1,...,15, along odd L. Every other
level is bounded below by Delta~c/L^2, so its V-rescaled energy diverges.
The Schur versus true eigenvalue error is O(L^-1) after V rescaling; this
does not imply an O(L^-1) rate for the new threshold convergence itself.

Why the naive inverse shortcut fails: for scalar Delta on a three-dimensional
torus with the origin deleted, the exact zero-energy Dirichlet inverse is
G_L^+(x-y)-G_L^+(x)-G_L^+(y)+G_L^+(0). Its infinite limit differs from the
infinite transient Dirichlet inverse by
 g[1-G_inf(x)/g][1-G_inf(y)/g], a nonzero rank-one harmonic term.
The mean constraint is therefore load-bearing.

Remaining risks to check are literal orbit/removal multiplicities, the
complete uniform Sobolev argument, energy closure across Q/core/exterior,
and exact finite trial normalization. Growing n has collision tubes with
unbounded spectator coordinates and is not covered by this N4 compactness
argument. A lower physical cell boundary law remains entirely separate.
