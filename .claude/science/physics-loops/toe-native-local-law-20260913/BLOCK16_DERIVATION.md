# Free-carrier holonomy finite-size energy and local bulk limit

Provisional continuation after the flat-holonomy milestone. This is a free
matter calculation in supplied flat backgrounds, not a theorem about the
interacting charged gauge phase. No independent review or audit status.
The four-node/matched-metric algebra from the explicitly supplied carrier
is a provisional upstream input, preserved in PR8099 at
387cffa600b3dfb319b2975a2b1ec8f6b87ddf22 and redeclared below where used.

## A coarse finite-range estimate

For any fixed finite-range free CAR model on an L^3 torus, move a uniform
flat twist to one boundary cut in each direction by an onsite phase unitary.
Only L^2 bonds per direction change. If q_i is the nuclear norm of T_i,
the Fock-space norm of a single Hermitian changed bond is
|exp(i phi_i)-1| q_i, in units r/a. This follows from the paired singular
values of its two-site one-particle off-diagonal block. At fixed total number
the norm cannot increase. Variational comparison therefore gives

```text
|E_L(phi)-E_L(0)| <= (r/a)L^2 sum_i q_i |exp(i phi_i)-1|.
```

For the specified quartet q_i=2. The energy-density difference vanishes at
least as O(1/L). This requires no Weyl expansion, but is too coarse to
identify the slow holonomy potential. It does not control local states in
an arbitrary interacting model.

## Nodal Fourier coefficient

Now use exactly the free mixed quartet at half filling. Let
f(k)=-E_+(k)-E_-(k), with no energy-unit prefactor, so
E_L(phi)=(r/a) sum_(n in Z_L^3) f((2pi n+phi)/L).
The supplied parameter range has only four isolated simple nodes, and its
positive and negative eigenvalues pair at every k. At each node k_alpha,

```text
E_-(k_alpha+q)=sqrt(q^T G_alpha q)+R_alpha(q),
|partial^beta R_alpha(q)|<=C_beta |q|^(2-|beta|)
```

for sufficiently small nonzero q and all derivatives needed below. The
low squared energy is analytic with positive-definite quadratic term;
expanding its square root radially gives these bounds. The other occupied
energy is smooth at the node. Away from all zero energies, trace of the
positive matrix square root is smooth even at positive-band degeneracies.

With Fourier convention
f_hat(r)=integral_BZ f(k)exp(-ir dot k)d^3k/(2pi)^3, the homogeneous
distribution has, for r!=0,

```text
Fourier[sqrt(q^T G q)](r)
  =-1/[pi^2 sqrt(det G) (r^T G^(-1) r)^2].
```

For G=I, radial integration with Abel factor exp(-epsilon |q|) gives
(1/(2pi^2 |r|)) integral_0^infinity q^2 exp(-epsilon q) sin(|r|q)dq,
whose epsilon->0 limit is -1/(pi^2 |r|^4). A linear variable change gives
the anisotropic expression. The sign reverses for the occupied energy
-E_-. A smooth cutoff about the node changes this nonzero-frequency
asymptotic only by rapidly decaying terms.

The remainder has uniform coefficient O(|r|^-5). To see the power without
assuming analyticity at q=0, decompose it into smooth dyadic annuli of
radius h. Its L1 size is O(h^5), and N integrations by parts give
O(h^5 min(1,(|r|h)^-N)). Summing the annuli with N>5 gives O(|r|^-5).
Cutoff derivatives are supported away from zero and decay faster. Thus

```text
f_hat(r)=sum_alpha exp(-ir dot k_alpha)
 /[pi^2 sqrt(det G_alpha)(r^T G_alpha^(-1)r)^2]
 +O(|r|^-5),     r in Z^3, |r|->infinity.                 (1)
```

The constants depend on the fixed carrier and its nonzero separation/gaps.
This is a proposed analytic asymptotic with a dyadic proof; it still needs
focused independent checking of its remainder estimates and assumptions.

## Poisson sum and oscillating holonomy energy

The O(|r|^-4) coefficients are absolutely summable in three dimensions.
Uniform Fourier convergence therefore permits exact finite-grid sampling:

```text
E_L(phi)=(r/a)L^3 sum_(m in Z^3) f_hat(Lm) exp(i m dot phi).
```

Subtracting the zero twist and using (1) gives

```text
E_L(phi)-E_L(0)
 = (r/(a pi^2 L)) sum_(m!=0) [exp(i m dot phi)-1]
       sum_alpha exp(-iL m dot k_alpha)
       /[sqrt(det G_alpha)(m^T G_alpha^(-1)m)^2]
   +O((r/a)L^-2).                                         (2)
```

The remainder is uniform in phi because |exp(i m dot phi)-1|<=2 and
sum_(m!=0)|m|^-5 converges. The leading series also converges absolutely.
This determines a parameter-dependent oscillating coefficient of 1/L,
not a constant universal Casimir coefficient or a guaranteed fixed twist
minimum across all L.

For the aligned quartet, R=sqrt(1-mu^2),
x_*=acos(R cos b), z_*=acos(1+zeta-R), and the nodes are
(+/-x_*,0,+/-z_*). Their common metric is

```text
G=diag(R^2,1,R^2 sin^2 b sin^2 z_*/sin^2 x_*).
sum_alpha exp(-iL m dot k_alpha)
 =4cos(L m_x x_*)cos(L m_z z_*).
```

The changing commensurability of these cosines allows the preferred twist
to change with size. For the chosen numerical parameters, a conservative analytic tail bound is
available. The metric obeys lambda_max(G)<=1 and sqrt(det G)>0.74. For a
reciprocal cube |m|_infinity<=M, count 24k^2+2 points on its kth shell and
use |m|>=k. In the units r/a=1 the omitted leading energy is bounded by

```text
8/[pi^2 sqrt(det G)L] [24/M+2/(3M^3)]
 < 1.202 [24/M+2/(3M^3)]/L.                                (3)
```

The metric bound follows using R^2=24/25, R>979/1000 and
G_z=(384/409)[(16/5)R-63/25]; all comparisons are rational after bounding R.
The bound is deliberately conservative and does not certify the finite
floating-point sum itself. The much smaller difference between M=12 and
M=24 observed numerically is not a rigorous replacement for (3).

## Fixed local free observables lose the global twist

Choose holonomy representatives phi in [0,2pi)^3. Let P_-(k) be the occupied one-particle projector. It is bounded and smooth
away from the finite nodal set. For each fixed site displacement d, the
finite-volume covariance in the uniform-link-phase convention is
exp(-i phi dot d/L) times a shifted Riemann sum of
exp(i k dot d)P_-(k). In a local gauge with that flat comparator removed,
the prefactor is absent. It tends to one for fixed d in either case. Exclude balls of radius delta around the nodes. On the
complement, uniform continuity gives convergence uniformly in grid shifts
phi. Inside the balls, boundedness and elementary lattice-point counting
bound the normalized sum by C delta^3+o_L(1), again uniformly in phi.
Taking L->infinity then delta->0 gives the same covariance limit for every
choice of phi, including a size-dependent energy-minimizing sequence.

Wick's rule gives convergence of every fixed local polynomial in the free
CAR operators. If a finite grid hits a node exactly, changing occupation in
that finite-dimensional zero space changes fixed local covariances by
O(L^-3), so this does not invalidate the limit. Boundary phase conventions
must be compared in the same local gauge; the uniform phases phi/L vanish
on every fixed local region.

This proves a route by which a nontrivial finite-volume holonomy preference
is compatible with the same local bulk free state. It does not identify the
interacting physical state after gauge averaging and does not prove a
charged-particle pole or the coupled Maxwell phase.

## Slow holonomy scale: conditional estimate only

For a real divergence-free electric field on an isotropic cubic torus,
the harmonic projection in direction i is its winding flux n_i divided by
L^2. Its squared norm is n_i^2/L, so the electric energy contains the
harmonic contribution g^2 w_i n_i^2/(2aL). An integer link field may have
integer n_i but a fractional harmonic projection; that projection is not
an independent integer-link assignment. The residual affine flux lattice
remains. Replacing n_i by -i partial_(phi_i), with any charge-dependent
connection retained, is part of the effective-sector construction still
needed below.
If an effective slow Hamiltonian is justified, if (2) supplies its matter
potential, and if its scaled twist minimum has a positive Hessian along a
chosen size sequence, a harmonic expansion suggests frequencies of order
g sqrt(r)/(aL). This is below transverse finite-box frequencies of order
1/(aL) at small g. The effective reduction, Hessian nondegeneracy, Berry
terms and interacting corrections have not been controlled. This is a
next-campaign scale estimate, not an additional theorem or a universal gap.

## Prior art and next action

Node-induced oscillating Casimir energies are established literature, not
a new general effect claimed here. The primary comparison found is
Nakayama/Suzuki, arXiv:2207.14078, which studies finite-thickness Dirac/Weyl
systems. Sections 1-3 and the relevant boundary-condition footnotes were read.
The paper uses a finite-thickness sum-minus-integral energy per area; its
L^-3 scale and its periodic node-commensurability discussion concern that
geometry. The current work derives a three-torus total twist difference in
its own convention; no coefficient or phase theorem is imported.

Next independently challenge the Abel normalization, Poisson sign and four-node
multiplicity against the exact full-lattice free energy, then quantify the
Fourier tail. The interacting phase, local physical observables, metric
attraction and native state formation remain the higher-level open tasks.
