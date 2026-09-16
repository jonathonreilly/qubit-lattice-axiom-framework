# Working route: a simultaneous weak-coupling and large-volume ground limit

2026-09-16 UTC. ACTIVE DERIVATION, NOT A COMPLETED THEOREM.
Personal work only. Deadline13:45:03 UTC. Block01 is pushed at
69fcacc8e754e0bf1baba6b56ce4e09e0673dd8e.

02:20 UTC update: the energy proof is now written separately in
BLOCK02_UNIFORM_GROUND_ENERGY_AND_OSCILLATOR_DEFECT.md. Both selective
author runners completed without an assertion failure. The new theorem
explicitly excludes the optional unscaled onsite charge penalty permitted
by Block01: that interaction would survive and invalidate a free-matter
claim. Sections E--F here remain proposed obligations, not consequences
already certified by the energy estimate.

The new mechanism is an exact positive-square identity plus a dressed Slater
trial. If all steps survive review, they may remove the order-of-limits
restriction of the preceding campaign's equal-time field/state result.
They do NOT make a fixed-positive-g infrared theorem. Real-time dynamics is
also separate until proved. No finite cyclic payload or selected law is implied.

## A. Exact oscillator-defect decomposition

First take unit weights. Let C be the periodic cubic curl,
Omega=(C^*C)^(1/2), Omega_p=(CC^*)^(1/2),
M=C^*(CC^*)^(+1/2), i.e. the partial isometry from plaquettes to links.
Here (+1/2) means inverse square root on the positive range, zero on kernel.
Put P=gE, Z=sin(Ctheta)/g, Q=P-i M Z. Then on the smooth physical core,

 H_gauge=(1/2)sum_l Q_l^* Q_l +(1/2)sum_p (Omega_p)_pp cos theta_p
       +(1/(2g^2))sum_p(1-cos theta_p)^2
       +(1/2)||[I-M^*M]Z||^2.                         [dimensionless aH]

Check the commutator sign: Q^*Q=P^2+Z.M^*M.Z-div(M sin theta), and
that divergence is sum_p (Omega_p)_pp cos theta_p. This identity is exact;
the nonlocal partial isometry is only a proof operator, not a new physical law.
All three residual terms after the cosine trace are positive.

Block01 gives <1-cos theta_p><=C g^2 uniformly in L. Therefore
<H_gauge> >= E_gamma,L - C g^2 V,
E_gamma,L=(1/2)tr Omega. The missing upper bound must include the actual
free matter energy, rather than the onsite product energy.

Positive diagonal weights can be included with
S=W_B^(1/2) C W_E^(1/2), Omega=(S^*S)^(1/2), Omega_p=(SS^*)^(1/2),
M=S^*(SS^*)^(+1/2), P=g W_E^(1/2) E, Z=W_B^(1/2)sin(theta)/g.
The quartic defect acquires b_p and the same exact square identity holds.

## B. Optimized integer Gaussian trial, without harmonic flux

Let S0=range(C^*) and Lambda0=S0 intersect Z^E. On the periodic cubic
cell complex this is the integer plaquette-boundary lattice: zero divergence
and zero winding flux. It is primitive. This integer statement must be checked,
not confused with the larger cycle lattice of Block01.

In the unit-weight case use coefficients exp[-g^2 n.Omega^+.n/2] on Lambda0.
For positive weights define
A=W_E^(-1/2) Omega W_E^(-1/2), range A=S0,
K=(A|S0)^(-1) on S0, and use exp[-g^2 n.K.n/2].
Centered theta domination bounds the electric covariance by A/(2g^2), giving
trial electric energy <=(1/4)tr Omega.

Primitivity gives Lambda0^*=P_S0 Z^E. Map its dual vector eta=P_S0 z to
q=Cz; this is a bijection onto C Z^E because C is injective on S0.
The dual weight is exp[-beta Q(q)], beta=pi^2/g^2,
Q(q)=eta.A.eta. In unit weights Q=q.(CC^*)^(+1/2).q >= ||q||^2/sqrt(12).
Generally A >= C^*W_B C/||Omega||, hence Q>=c||q||^2 with
c=b_min/sqrt(12 e_max b_max), uniform in L.

For a plaquette boundary d_p, the exact overlap is

 I_p=exp[-g^2 d_p.K.d_p/4] E_dual (-1)^(q_p).

Thus sum b_p(1-I_p)/g^2 <=(1/4)tr Omega
                         +(2 b_max/g^2)E_dual||q||^2.
The trace identity uses A W_E A=C^*W_B C and inversion on S0.
Since Z(beta/2)<=theta_1(beta c/2)^(3V),
E_beta Q <=(2/beta)log Z(beta/2),
the last energy error is exponentially small in1/g^2 per volume.
No convergent interacting cluster expansion is needed for this pressure bound:
it simply enlarges the integer-curl set to all integer plaquette arrays.

The trial's individual plaquette mean defect also has the elementary Jensen
bound <=g^2 d_p.K.d_p/2. Translation invariance and bounded symbol give a
uniform O(g^2) bound, even without the sharper dual estimate.

## C. Restore the free Slater energy by finite-block gauge dressing

Partition the torus into blocks of side of order R (allow controlled boundary
remainders if L is not divisible by R). In each block take a free plus Slater
ground state and its conjugate minus state with equal particle numbers.
For the Wilson symbol at half filling, the open-block one-particle spectrum
has a particle-hole symmetry: at flat b=0, sigma1 K anticommutes with the
real-space matrix; flat b is removed on an open block by a site phase.
Choose half of any zero eigenspace. This gives N_+=N_-=block volume.

Fix the coordinate axial spanning tree in each block. For a matter charge
configuration Q of zero block total charge let E_T(Q) be its integer tree flow,
D E_T(Q)=Q. Define the matter-valued wavefunction

 Phi(theta)=exp[i sum_l theta_l E_T(Q)_l] phi_free_blocks,
 Psi(theta)=psi_Gaussian(theta) Phi(theta).

This obeys exact Gauss law. It is normalized because the dressing is unitary.
The mean of every Q_x in phi_free_blocks is zero (conjugate species have equal
local densities), so the electric cross term with psi_Gaussian is zero.

For each subtree A, the Slater formula gives Var N_A=tr C_A(1-C_A)<=m|A|.
The two species are independent, hence <Q_A^2><=2m|A|. Summing subtree sizes
counts distances to the root, at most3R times the block volume. Therefore
the extra electric energy density is O(g^2 R), NOT an extensive norm squared.

After dressing, each internal hopping phase is its fundamental tree loop.
For a coordinate axial tree that loop is a product of at most2R elementary
plaquettes (verify orientation and count). The telescoping bound
|product U_p-1|<=sum |U_p-1| and <|U_p-1|><=sqrt(2 rho_p) imply a hopping
energy-density error O(Rg). Cross-block hopping has zero expectation in the
trial. Comparing cut free blocks with the full free Hamiltonian costs O(1/R).

Candidate total upper bound:

 a E_ground <= E_gamma,L + E_m,free,L
                 +C V [R^-1+gR+g^2R+exp(-c/g^2)].

## D. Matter lower bound in the actual ground state

At each fixed theta gauge-fix within each block by the SAME tree. Compare
the resulting block one-particle matrices with their zero-field matrices.
The paired Fock hopping difference is bounded by2||T||_* times the loop
phase difference. The actual state's Block01 plaquette concentration controls
its expectation. Cutting boundary hopping costs O(V/R), as does comparing
free block ground energies with E_m,free,L.

Candidate lower bound on the actual matter expectation:

 <H_m> >= E_m,free,L-C V [R^-1+gR].

Combine this, the trial upper bound, and the positive-square identity to get

 (1/V)<sum Q_l^*Q_l + g^-2 sum b_p(1-cos theta_p)^2
                       +||[I-M^*M]Z||^2>
    <= C [R^-1+gR+g^2R+g^2+exp(-c/g^2)].

Choose R of order min(g^-1/2,L), with a precise block tiling, to obtain an
error tending to zero along ANY joint g->0,L->infinity. Expected coarse rate
is C(sqrt(g)+L^-1). This would be a new uniform argument, not a corollary of
the earlier fixed-box oscillator theorem.

## E. Candidate equal-time Gaussian characteristic proof

Ground-trace translation invariance is essential. If the positive-square
error density is delta, then for ANY smear u with bounded discrete Fourier
amplitude,

 <Q(u)^*Q(u)> <=delta sup_k ||u_hat(k)||^2.

This follows from the positive Fourier covariance matrix and its trace sum.
It avoids a false l1 estimate for the nonlocal polar multiplier M. The same
bound holds for the projected residual Z_perp. Since ||M(k)||<=1, smears Mv
have the same Fourier bound as finite-support v.

For real local u,v put A0=P(u)+Z(v), xi=u+i Mv. Up to Z_perp(v),
A0=(Q(xi)+Q(xi)^*)/2. The latter annihilation error is O(sqrt(delta)).
The exact commutator [Q(xi),A0] is a cosine-weighted expression whose limit is

 kappa_L=u.Omega.u+v.Omega_p.v.

The error is O(g) in ground-vector norm for fixed smears by Cauchy--Schwarz
on the products of their l2 coefficients and <(cos-1)^2><=2rho=O(g^2).
For e^(it A0), the angle flow is a translation by t g W_E^(1/2)u, regardless
of its multiplication phase. This preserves the needed defect estimates
uniformly for bounded t. The derivative of chi(t)=<exp(it A0)> should obey

 chi'(t)=-(kappa_L/2)t chi(t)+O(sqrt(delta)+g(1+|t|)).

Then chi(1) approaches exp[-kappa_L/4] uniformly in L. The kernels Omega_L,
Omega_p,L have ordinary continuous symbols and local Riemann limits. This
would establish the simultaneous equal-time Gaussian gauge-field limit.
Prove every norm/domain/translation step explicitly before claiming it.

## F. Matter and joint factorization: still an obligation

Small fixed-loop plaquette defects make gauge-dressed finite-path neutral CAR
observables asymptotically path independent. A local gauge fixing on the
infinite cubic lattice can identify their limiting algebra with the invariant
part of the ordinary CAR algebra. The energy-density bounds would force its
translation-invariant state to minimize the free Wilson energy. Since the
one-particle zero set is finitely many Weyl nodes, a free energy-minimizing
translation-invariant state should be the filled-negative-band Slater state.
Prove this with positive excitation occupations and the measure-zero nodes.

The full Slater state is pure on CAR. A conditional expectation onto charge-
invariant CAR can extend a joint gauge-field/neutral-CAR limit positively;
purity would then force factorization. Need to check the gauge-invariant
algebra, fixed paths, positivity of the extension and all fillings carefully.

## G. Explicit limits

Even if A--F succeed, this is g->0 jointly with volume, not fixed g>0 followed
by arbitrary long distance. It does not itself establish real-time evolution.
Ground-state form convergence alone is insufficient for dynamics; do not
silently invoke strong-resolvent convergence from core matrix elements.
Finite-clock payload, native-law selection and a TOE remain separate.

## Next decisive work

1. Verify the integer-dual lattice bijection and exact positive-square identity
   on literal small cubic complexes with an independent representation.
2. Derive the dressed Slater Gauss/electric identities and axial-tree loop
   length bound, including torus block boundaries and fixed filling.
3. Write the complete uniform energy proof before testing characteristic limits.
4. Keep failures and rates; no broad no-go if any step fails.


## Further algebra details fixed before the new finite challenges

- Weighted optimized metric: A=W_E^-1/2 Omega W_E^-1/2 satisfies
  A W_E A=C^* W_B C. Its inverse K on S0 also obeys
  C K C^*=W_B^-1/2 Omega_p W_B^-1/2. To see the latter, use
  B=W_E^1/2 Omega^+ W_E^1/2: A B d=d for d in S0, so Kd=P_S0 B d;
  curl kills the discarded kernel component. This identifies each trial
  plaquette metric and keeps its bound independent of volume.
- In the unit case beta=pi^2/g^2 and c=1/sqrt(12). The excess trial gauge
  energy per volume is at most (12 sqrt(12)/pi^2) log theta_1(beta c/2),
  with log theta_1(t)<=2 exp(-t)/(1-exp(-3t)). No claimed smallness of the
  total dual partition function is needed; its logarithm is extensive.
- For D=tail-minus-head, the rooted tree path p_x satisfies
  D p_x=delta_root-delta_x. Therefore E_T(Q)=-sum_x Q_x p_x on a
  block-neutral configuration. A hop tail->head changes E_T by
  p_head-p_tail. Its dressed phase is the loop e_l+p_tail-p_head.
- The coordinate tree sets all z links, y links at z=0, and x links at
  y=z=0. For an x link the loop is the negative sum of xy plaquettes
  from0 to y at z=0 and xz plaquettes from0 to z at its y. For a y link
  it is a negative yz strip of length z. For a z link it is zero.
  Thus the bound2R concerns strips, not an R-by-R surface.
- The Gaussian characteristic should be proved for exp(i[P(u)+Z(v)]),
  with a self-adjoint first-order transport generator plus bounded phase.
  For xi=u+i Mv, [Q(xi),P(u)+Z(v)] approaches the REAL scalar
  u.Omega.u+v.Omega_p.v: the two imaginary cross terms cancel.
  Fourier trace positivity, rather than absolute spatial summability of M,
  controls Q(xi) in the ground state. Replacing this step by an l1 bound
  would lose uniformity because Riesz kernels need not be l1.
- Real-time convergence is NOT obtained merely from the proposed equal-time
  characteristic proof or convergence of quadratic forms on a core. It is
  an explicit later obligation.
