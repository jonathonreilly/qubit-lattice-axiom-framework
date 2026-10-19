<!-- Original PR9814 source SHA256 a5b4764617eb80a7a94158c4b830fc461a6f8887a77dbf15ba2da9d1c7696152. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native energy current and collective-pole continuity

Status: bounded-support; upstream consistency support. No new interaction, observational fit or gravity identification.

## Exact local current

Write the supplied Hamiltonian as H=sum_a h_a, with native directional bond centers r_a, and E_q=V^-1/2 sum_a exp(-iq.r_a)h_a. For an overlapping pair use consistent local lifts of the two centers around their shared site on a torus. Their displacement d_ab=r_b-r_a stays bounded. At allowed torus momenta this agrees with the periodic Fourier density. Define sinc(x)=sin(x)/x including sinc(0)=1 and

 J_q=i/(2sqrt(V)) sum_(a,b) d_ab sinc(q.d_ab/2)
       exp[-iq.(r_a+r_b)/2] [h_a,h_b].

The sum is over ordered pairs; disjoint bonds commute. Antisymmetry gives

 [H,E_q]=(2sqrt(V))^-1 sum_(a,b)(exp(-iq.r_b)-exp(-iq.r_a))[h_a,h_b]
        =-q.J_q,
 J_q^dagger=J_-q.

Thus dE_q/dt=-i q.J_q exactly. No scalar field, additional interaction or transport coefficient was supplied. For two different native axes alpha,beta sharing site i,

 [h_(ij,alpha),h_(ik,beta)]
 =2i J_alpha J_beta epsilon_(alpha beta gamma)
   sigma_i^gamma sigma_j^alpha sigma_k^beta.

Only these three-spin local products contribute. Equal-axis overlapping bonds commute. The current depends on the stated bond-center density convention; adding a divergence to the density or a transverse term to the current changes the representative. Its longitudinal continuity relation is fixed once the density is fixed.

Constructing lattice energy currents from continuity is established methodology, not a new conservation principle; see [Heat flux operator, current conservation and the formal Fourier's law](https://arxiv.org/abs/0804.3371). The present calculation applies it to the native bond operators and the already derived pole coefficient.

## Coupling to the actual neutral pole

For an actual excited eigenstate n and ground g, with omega_n=E_n-E_g, exact continuity yields

 q.<n|J_q|g>=-omega_n <n|E_q|g>.

Use the checked Q4 lower pole, L=10, and q_z=0 with |q|<<lambda. Its energy-density amplitude is

 A_E=-Jgamma(L+2)/(8sqrt(2L)) lambdaL |q|²
       +O(Jlambda^(L+2)|q|²+Jlambda^(L-2)|q|4+JR³lambda^(M-14)).

Its longitudinal current amplitude is exactly -omega_p A_E/|q| for q nonzero. With omega_p=JDelta lambda4[1+O(lambda²)], Delta=L/16, the leading result is

 A_J,long=J²Delta gamma(L+2)/(8sqrt(2L)) lambda^(L+4)|q|.

The inherited relative error is O(lambda²+|q|²/lambda²+R³lambda^(M-L-14)/|q|²). Keeping this explicit avoids extending the source result to arbitrarily shrinking q at a fixed remainder order. The established p>1,M>24+5p condition controls first-grid q~lambda^p for L10. Exact continuity needs no independently truncated current expansion. In a reflection-symmetric transverse A1 branch, C4 and the axial mirrors allow only a vector proportional to q at linear order; higher transverse terms are not determined by this longitudinal identity.

## Static response, precisely scoped

For the normalized Hermitian real mode (E_q+E_-q)/sqrt(2) at generic q, or equivalently the matching conjugate Fourier response, define the positive static susceptibility to H-fE by the Lehmann convention chi=2sum_n |<n|E|g>|²/omega_n. The isolated pole contribution is

 chi_p(q)=Jgamma²(L+2)²/(64LDelta)
          lambda^(2L-4)|q|4 [1+o(1)]

in the same controlled joint limit. This is the pole contribution, not a bound on every other spectral channel. Uniform E_0=H/sqrt(V) has exactly zero inelastic response. This isolated pole contribution has no 1/q² infrared singularity; it cannot by itself be equated with a Newtonian potential. Energy conservation also constrains energy-density form factors in ordinary field theory, so q² suppression is not a general no-gravity theorem.

No momentum-density identification, symmetric stress tensor, Einstein equation, universal source coupling, relativistic common metric or empirical scalar follows from continuity alone. Those are separate remaining obligations. Geometry, Hamiltonian parameters and the readout convention remain explicit premises.

## Exact finite control

An eight-qubit open cube at native couplings (.37,.37,1) independently evaluates the three-spin commutator identity, Fourier continuity, every ground-to-eigenstate longitudinal relation, and a Hermitian-source Lehmann susceptibility against a finite-field ground-energy curvature. These are algebra/response controls, not a finite-size test of the L10 collective pole. No measured data enter them.
