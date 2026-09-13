# Next derivation: fixed finite-link monopole-energy control

Formulated personally while block12 is being packaged. Not yet reviewed or
checked. Target actual physical finite-link ground-state information rather
than another supplied continuum beta coefficient.

For rotor angles, define principal oriented plaquette angles theta_p in
[-pi,pi), integer cube monopole Q_c=sum_oriented_faces theta_p/(2pi).
The lattice Bianchi identity makes Q_c integer almost everywhere. Because
1-cos(theta)>=2theta^2/pi^2 and a cube has six faces,
 sum_faces(1-cos theta_p)>=4 Q_c^2/3.
Each plaquette belongs to two cubes on a periodic cubic graph, hence
 H_B^positive >= [2 w_min/(3 g^2 a)] sum_c Q_c^2.
This is an exact multiplication-operator inequality in the full rotor space.
Compression preserves it at any finite cutoff: H_B,S^positive >= const
P_S(sum Q_c^2)P_S. The compressed Q^2 is a positive local angle-POVM statistic,
not an integer-valued conserved monopole sector or a spectral gap theorem.

Key constructive trial idea for a *volume-independent* finite cutoff:
Give every oriented plaquette p an auxiliary integer n_p in [-M,M], with
positive path-ground-state weights f(n)=cos(pi n/(2M+2)) on that interval,
zero outside. Map its product amplitudes to divergence-free electric flux
E=B n, where B is the oriented plaquette-boundary incidence matrix. The map
L|n>=|Bn> is not isometric; redundant plaquette flows are deliberately summed
with positive amplitudes. psi=L tensor_p f is nonzero and has divE=0.
In cubic 3D each link meets four plaquettes, so |E_l|<=4M. Thus this is an
exact state of ONE fixed finite cutoff S>=4M, independent of total volume.

On the integer n_p line, (shift+shift^dagger) f =2 cos(kappa) f + positive
outside-boundary remainder, kappa=pi/(2M+2). The positive map L intertwines
the auxiliary shift with the physical rotor plaquette W_p. Consequently
(W_p+W_p^dagger) psi >= entrywise 2 cos(kappa) psi. Pair with the nonnegative
psi to get <(W_p+W_p^dagger)/2> >= cos(kappa), despite the non-isometric map
and all redundancies. Compression to S does not change this expectation
because psi is supported there. This is the crucial proof to challenge.

Electric trial energy <= [g^2/(2a)] S_trial^2 sum_links w_i with S_trial=4M.
Magnetic trial energy <= [(1-cos kappa)/(g^2 a)] sum_plaquettes w_i.
Choose M=ceil(c/g), with g<=1 and fixed c>0, to make both energy densities
O(1/a) while one fixed S=4M is sufficient for every spatial volume. This is
less sharp than Gaussian oscillator constants but entirely finite and exact.

Tensor with a number-two matter product at every cell. It is in exact G=0,
and hopping expectations vanish while the finite onsite expectation is
bounded. Bound the full matter operator from below by -C_m V/a using the
onsite norm and nuclear hopping bound 2r. Thus for any finite-volume ground
state in the physical subspace,
 <sum_c P_S Q_c^2 P_S>/V <= C(g,M,w,r) g^2,
with C uniform in volume for M~1/g. Translation-averaged local monopole
probability is bounded by the same expectation (Q^2>=1 on nonzero charge).
No assumption of free Slater/rotor-product Gauss compatibility is made.

This is a low-monopole-density ground-state bound, not a monopole excitation
gap, no-condensation proof, photon pole, fermion persistence, or common-cone
selection. Low density alone can coexist with other orders, and no inference
about those should ship. It materially controls an actual finite-link
physical ground-state quantity at weak g, with an explicit volume-independent
finite payload. Next: check the positive-map trial algebra on small periodic
cell complexes and exact finite examples; derive all constants and POVM
normalization; review whether monopole indicators are genuinely local and
principal-angle branch surfaces are measure-zero.

Sharper matter constant: each Hermitian bond F U+F^dag U^dag is unitarily
equivalent on the full rotor to F+F^dag, using the number-controlled rotor
shift sum_n P_(N_x=n) U^n. Its norm is the nuclear norm of T_i, namely 2,
because the one-particle off-diagonal block has eigenvalues +/- singular(T_i)
and the many-body maximal positive sum is sum singular(T_i). Compression
cannot increase the norm. Thus H_m>=E_on,min-6r V/a, not merely -12r V/a.
Choose the onsite product that fills its two negative orbitals; it achieves
E_on,min with N_x=2 and zero hopping expectation. For w_sum=sum_i w_i,

rho_Q2 <= (3 g^2/(2 w_min))
 [w_sum (8g^2 M^2+(1-cos(pi/(2M+2)))/g^2)+6r].

For 0<g<=1, M=ceil(1/g), S>=4M, this is at most
(3 g^2/(2 w_min))[w_sum(32+pi^2/8)+6r], uniformly in volume.
The loose constant is explicit; the exact M formula is sharper. The bound
also holds for translation-averaged density of the positive monopole-indicator
POVM since 1_(Q!=0)<=Q^2. Ground-state degeneracy causes no problem: each
physical ground state has the same variational energy upper bound.

Important proof details: L acts on finitely supported auxiliary amplitudes,
not as a bounded map between whole infinite Hilbert spaces. All sums are
finite at each finite graph/M. Redundant flow fibers only add positive
amplitudes, and no product normalization is assumed after the map. The finite
angle POVM has effects |theta;S><theta;S| dtheta/(2pi), with unnormalized
|theta;S>=sum_n=-S^S exp(-in theta)|n>; integrating gives identity. Its Q^2
statistic is local to the twelve cube edges and is not a sharp conserved
magnetic charge. Branch-cut surfaces are Haar-null and do not change the
operator inequality. Low density by itself permits long-range order: a
product of sqrt(1-rho)|0>+sqrt(rho)|1> has density rho and nonzero constant
creation-annihilation correlation at separated sites; its global phase
average retains that correlation. This logical counterexample must prevent
an unwarranted no-condensation/photon claim.
