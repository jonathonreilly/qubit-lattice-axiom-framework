# Fixed finite-link ground-state control at weak coupling

Working theorem. The construction is supplied mathematical physics, not a
selection of matter, geometry or couplings from the framework axioms. It
controls a bounded plaquette observable and a specified monopole POVM; it
does not establish the photon or the charged Weyl phase.

## Declared family and target

Take a periodic cubic graph with L_i>=3, V cells, 3V oriented links and 3V
positively oriented plaquettes. Each link belongs to four plaquettes and
each plaquette to two cubes. Let a,g>0, r>=0, w_i>0 be fixed supplied
coefficients. Put a hard integer link |n>, -S<=n<=S, with
U_S|n>=|n+1> for n<S and U_S|S>=0. Use four CAR orbitals per cell and

```text
H_S = (r/a) sum_x c_x^dag h_on c_x
    + (r/a) sum_(x,i) [c_x^dag T_i U_(x,i) c_(x+i) + h.c.]
    + (g^2/(2a)) sum_(links i) w_i E_l^2
    + (1/(g^2 a)) sum_(plaquettes normal i) w_i [1-Re W_p,S],
G_x = div(E)_x-(N_x-2),                  Re W=(W+W^dag)/2.
```

The magnetic constant is explicitly chosen so its term is positive. The
claim below concerns the deficit observable itself, so an additive vacuum
energy convention cannot remove it. The onsite Hermitian matrix h_on has
exactly two negative eigenvalues. The T_i have nuclear norms q_i; define
q_sum=sum_i q_i and w_sum=sum_i w_i, w_min=min_i w_i.
The physical space G_x=0 is finite and nonempty.

The concrete mixed carrier has 0<b<pi/2, 1/2<zeta<1 and
0<mu^2<1-zeta^2, with sigma acting on orbital and tau on flavor:

```text
h_on=(2+zeta)sigma3+mu tau_x(sin b sigma1+cos b sigma3),
T_i=(C_i-i S_i)/2,
C_x=-sin b sigma1-cos b sigma3, S_x=tau_z(cos b sigma1-sin b sigma3),
C_y=C_z=-sigma3,                 S_y=sigma2, S_z=0.
```

Here q_i=2 and q_sum=6. In the tau_x basis the onsite eigenvalues are
+/-epsilon_eta, epsilon_eta=sqrt[(eta mu sin b)^2+(2+zeta+eta mu cos b)^2].
Thus two negative onsite orbitals can be filled at each cell. Their product
has exactly N_x=2, even fermion parity per cell and onsite energy E_on,min,
the minimum of the unconstrained onsite many-body Hamiltonian. This local
product is only an auxiliary variational state, not the proposed physical
Weyl ground state. Its hopping expectations vanish.

Define the weighted plaquette deficit in any state rho by

```text
D(rho)=(1/V) sum_(plaquettes normal i) w_i <1-Re W_p,S>_rho.
```

The first target is D=O(g^2), uniformly in V, as g tends to zero with fixed
w_i,r,q_i and a. This is a precise weak-fluctuation target in this specified
integer-link family. It does not define an entire Coulomb phase.

## Exact local cutoff lower bound

For one plaquette write b_p for its oriented integer boundary vector. In
electric-flux space W_p,S shifts E to E+b_p whenever the result stays inside
the box. Its shift orbits are finite disjoint open chains. Any participating
link changes by one per step, so no chain has more than 2S+1 states. The
Hermitian half-adjacency matrix on a chain of n states has eigenvalues
cos(j pi/(n+1)), j=1,...,n. It follows that

```text
lambda_max(Re W_p,S)=cos(pi/(2S+2)),
1-Re W_p,S >= [1-cos(pi/(2S+2))] I.
```

The maximum is attained on the length-2S+1 chain E=m b_p, -S<=m<=S, with all
other fluxes zero. Since div b_p=0, this chain is available even with neutral
matter N_x=2 and exact Gauss law. Simultaneous saturation for all plaquettes
is not asserted. Summing positive operator inequalities gives, for every state,

```text
D(rho)>=w_sum[1-cos(pi/(2S+2))]>=w_sum/[2(S+1)^2].            (1)
```

The last inequality is 1-cos x>=2x^2/pi^2 for |x|<=pi. Consequently, if a
family of states satisfies D<=K g^2 with a fixed finite K>0, then

```text
S+1 >= sqrt[w_sum/(2K)] / g.                                 (2)
```

This necessary cutoff scaling is independent of the matter dynamics and
volume. It applies to the hard unit-amplitude shift family just defined,
not to every finite-spin gauge encoding or every possible infrared phase.

## A positive closed-flow trial state at fixed cutoff

Let B be the link-by-plaquette boundary incidence matrix and D_vertex the
vertex-by-link incidence matrix. Then D_vertex B=0. Introduce auxiliary
integers n_p in [-M,M], M>=0, and the nonnegative path weights

```text
kappa=pi/(2M+2),
f_M(n)=cos(kappa n) for |n|<=M, and 0 otherwise,
F(n)=product_p f_M(n_p).
```

Define the linear push-forward on finitely supported amplitudes by
L|n>=|Bn>, and set psi=L F. This is a finite sum at any finite graph and M.
It is not an isometry, and no bounded-operator assertion about L on an entire
infinite Hilbert space is needed. Redundant plaquette flows add their positive
amplitudes. In particular psi(0)>0, so psi is nonzero; its norm must be taken
after the push-forward, not assumed equal to the product norm of F.

Every supported electric vector obeys div E=0 and |E_l|<=4M, since each link
meets four plaquettes. Thus psi belongs to one finite link cutoff S>=4M,
independently of V. It occupies the zero winding sector, which is sufficient
for a variational upper bound on the full physical ground energy.

On one auxiliary integer line, let t shift n to n+1. The elementary cosine
recurrence and the two outside endpoints give the componentwise identity

```text
(t+t^dag) f_M = 2cos(kappa) f_M + r_M,
r_M>=0, supported at n=+/- (M+1).
```

The map L preserves componentwise positivity and intertwines t_p with the
untruncated rotor plaquette W_p. Therefore, on the finite support involved,

```text
(W_p+W_p^dag) psi >= 2cos(kappa) psi      componentwise.
```

Pairing with the nonnegative psi and normalizing yields

```text
<Re W_p>_psi >= cos(kappa).                                  (3)
```

Compression to S>=4M leaves this expectation unchanged, since psi is already
inside its range. This step handles all linear dependencies among plaquette
boundaries; it does not replace three-dimensional plaquettes by independent
physical rotors. The lower bound can be strict because of redundant flows.

For the normalized trial state, the electric support bound and (3) give

```text
<H_E> <= (V/a) w_sum 8g^2 M^2,
<H_B> <= (V/a) w_sum [1-cos(kappa)]/g^2.                      (4)
```

Tensor psi with the onsite two-particle product described above. This is an
exact physical state of the coupled model, since its electric divergence and
N_x-2 both vanish. It achieves E_on,min in the onsite term and zero hopping
expectation. Neither a free filled Bloch sea nor a gauge-noninvariant product
of charged states is assumed to be physical.

## Matter norm and physical ground-state deficit

The Hermitian bond operator has a sharper bound than twice the norm of its
raising half. On the full rotor, the number-controlled unitary

```text
V_x=sum_n P_(N_x=n) tensor U^n
```

conjugates F+F^dag to F U+F^dag U^dag, where F=c_x^dag T_i c_y.
The one-particle Hermitian off-diagonal block has eigenvalues +/-s_j(T_i).
Its CAR second quantization therefore has norm sum_j s_j(T_i)=q_i.
Compression cannot increase this norm. The comparison unitary is used only
for an ambient operator-norm proof; it is not a proposed physical gate or
state preparation. Hence

```text
H_matter >= E_on,min I -(r/a) V q_sum I.                     (5)
```

Let rho_0 be any physical ground state, including a mixture in a degenerate
ground eigenspace. Variational comparison with (4) and positivity of H_E imply

```text
D(rho_0) <= g^2 B(g,M),
B(g,M)=w_sum[8g^2 M^2+(1-cos(pi/(2M+2)))/g^2]+r q_sum,
S>=4M.                                                       (6)
```

No fermion determinant or assumed gap enters (5)-(6). For 0<g<=1 take
M=ceil(1/g). Since gM<=2 and g(M+1)>=1,

```text
B(g,M)<=B_*=w_sum(32+pi^2/8)+r q_sum.                         (7)
```

Equations (1)-(7) prove matching necessary and sufficient order S=1/g for
the declared O(g^2) plaquette-deficit target: (2) is necessary for any state;
S>=4ceil(1/g) is sufficient for all physical ground states of this family,
uniformly in spatial volume. The coefficient bound is deliberately loose.
The exact expression (6) is stronger. Binary encoding of 2S+1 link states
then uses log2(1/g)+O(1) qubits at this optimal order, within this encoding.
The result is not a lower bound on the payload of every possible theory.

For a Gibbs state on the physical space at inverse temperature beta>0,
U_beta-E_0 <=log(dim H_phys)/beta and
log(dim H_phys)<=V[log16+3log(2S+1)]. The same argument gives

```text
D(rho_beta) <= g^2[B(g,M)+(a/beta)(log16+3log(2S+1))].         (8)
```

This finite-temperature extension remains an energy/deficit estimate. It does
not establish a thermal phase transition or a real-time photon pole.

## A local monopole POVM and its energy inequality

Use the full rotor angle representation with normalized Haar measure. Let
vartheta_p be the principal representative in [-pi,pi) of the oriented
plaquette angle. For each cube c define the integer

```text
Q_c=(1/(2pi)) sum_(outward cube faces) vartheta_p.
```

It is integer almost everywhere because the unwrapped cube curl sums to zero;
principal wrapping changes it by integer multiples of 2pi. Branch surfaces
have Haar measure zero and do not affect the multiplication operators. The
definition is the familiar compact-lattice monopole convention, redeclared
here; it is not an emergent monopole excitation gap.

For finite S define the local positive operators

```text
M_c,S=P_S Q_c^2 P_S,       I_c,S=P_S 1_(Q_c!=0) P_S.
```

These are compressions of functions of the twelve cube-link angles. They
are local and gauge invariant. More explicitly, a finite link has angle POVM
|theta;S><theta;S| dtheta/(2pi), where
|theta;S>=sum_(n=-S)^S exp(-in theta)|n>; its integral is identity. The cube
charge event is a gauge-invariant coarse graining of the product POVM.
Thus M_c,S is its mean square charge statistic, and 0<=I_c,S<=M_c,S.
It is generally false that M_c,S=(P_S Q_c P_S)^2. No sharp conserved
finite-dimensional magnetic charge is silently introduced.

Since 1-cos theta>=2theta^2/pi^2, Cauchy-Schwarz on six faces gives

```text
sum_(faces c) [1-cos vartheta_p] >= (4/3) Q_c^2.
```

Summing over cubes counts each plaquette twice. Multiplication inequalities
remain positive after compression, and P_S W_p P_S=W_p,S. Therefore

```text
sum_c M_c,S <= (3/2) sum_p [1-Re W_p,S]
             <= (3V/(2w_min)) D_operator.                   (9)
```

Here D_operator is the weighted operator whose expectation defines D(rho).
For every physical ground state of (6), the volume-averaged defect statistics
obey

```text
(1/V)sum_c <I_c,S> <= (1/V)sum_c <M_c,S>
                  <= [3g^2/(2w_min)] B(g,M)
                  <= [3g^2/(2w_min)] B_*.                    (10)
```

The last line uses (7). All volumes and all S>=4ceil(1/g) satisfy it. No
translation-invariant ground state is required: the statement is an average.
For a translation-invariant state it bounds the expectation on each cube.
A union bound also controls the probability of any nonzero cube charge in a
fixed finite region when that joint angle POVM is used. Equation (8) gives
the analogous finite-temperature bound with its explicit entropy term.

## Exact-zero defect exclusion has a narrow meaning

At any fixed finite S, the one-cube operator I_c,S is positive definite.
To see this, take a nonzero finite Fourier polynomial on the twelve cube-link
angles. A charge-one event has nonempty open interior: outward raw face
angles (-5pi/3,pi/3,pi/3,pi/3,pi/3,pi/3) sum to zero and lie in the cube
curl range, whose rank is five. Their principal representatives all equal
pi/3. Small variations of the link angles preserve the nonzero charge.
A nonzero finite Fourier polynomial cannot vanish on that open set. Its
integrated squared modulus there is strictly positive. Compactness of the
unit sphere in the finite link space therefore gives

```text
I_c,S >= epsilon_S I,       epsilon_S>0.                     (11)
```

At S=0 even the trivial one-state link has a Haar-distributed angle POVM;
this illustrates why the statistic cannot be identified with a count of
emergent monopole particles without an additional physical argument. The
qualitative constant is local and volume independent; no numerical value
or asymptotic rate for epsilon_S is claimed. Tensoring with other links or
matter and restricting to the physical space preserves the inequality. Thus
this particular finite-bandwidth angle POVM has a nonzero floor for its
unsharp charge statistic at fixed S. Finite-spin Coulomb phases can contain short-distance
virtual defects, so (11) is not a photon or deconfinement no-go. An exactly
restricted classical angle measure, a different encoding or a different
emergent defect observable is outside this statement.

## What remains unproved

The small-deficit and small-defect-density bounds concern actual physical
ground states of the supplied Hamiltonian, which improves on a finite-time
or classical-symbol comparison. They do not give the connected correlations,
helicity response, disorder-operator spectrum or monopole worldline estimates
needed to establish the charged Coulomb phase. They also do not show that
the matter spectrum remains Weyl-like, exclude a Mott or ordered matter
state, protect the common metric, or select these couplings from the axioms.

A density bound alone cannot exclude long-range order. For a simple logical
counterexample, a product of sqrt(1-rho)|0>+sqrt(rho)|1> has arbitrarily small
occupation rho but <b_x^dag b_y>=rho(1-rho) for all distinct sites. Averaging
over the common global phase makes the state number-symmetric while leaving
that correlation unchanged. This is a counterexample to an inference from
density to absence of order, not a proposed model of the monopoles here.
The next phase task must control the relevant correlations or excitations,
not relabel (10) as a photon theorem.
