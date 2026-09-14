# Fixed finite-cyclic transfer scaling and the massive-fermion matching gap

Exploratory author derivation; independent review pending. The clock
Hamiltonian is supplied. These statements do not identify it with the
isotropic massive Wilson determinant model or prove a Coulomb phase.

## 1. Exact one-link temporal transfer

Fix N>=2 and X^N=I on C^N, with X the angle-translation operator. Write

    theta(x)=sum_{q in Z} x^(q^2),  0<x<1,
    Q_x=theta(x)^-1 sum_{q in Z} x^(q^2) X^q.

This is exactly the normalized convolution transfer of a Villain temporal
plaquette on Z_N when

    beta_tau=N^2/(2*pi^2) log(1/x).

Indeed the angle difference r has weight sum_n x^((r+nN)^2); summing over
r mod N gives theta(x). The normalization makes Q_x 1=1. Its eigenvalues
are strictly positive by the Fourier transform of a periodized Gaussian,
and are at most one because it is an average of unitary translations.
Thus Q_x is positive definite and a contraction for every fixed N and x.

Set x=delta*t with t>0 and delta*t<1. If H0=2-X-X^*, then

    Q_(delta*t)=I-delta*t H0+O(delta^2),
    -delta^-1 log Q_(delta*t) -> t H0

in operator norm, for fixed N. In fact the error estimates can be independent
of N. Let R(x)=2 sum_{q>=2} x^(q^2)<=2*x^4/(1-x^5). Since ||H0||<=4,

    ||Q_x-(I-x H0)|| <=8*x^2+(4*x+2)R(x).

This follows by writing Q_x-I=[-x H0+(R_op-R I)]/(1+2x+R), with
||R_op||<=R, then adding x H0. The scalar logarithm is uniformly Lipschitz
on a fixed interval containing the spectra for small x, and
||exp(-x H0)-(I-x H0)||<=8*x^2*exp(4x), giving the stated generator limit.

This is a logarithmic temporal coupling at fixed N:

    beta_tau=N^2/(2*pi^2) log[1/(delta*t)].

By contrast, beta_tau=b/delta with fixed b>0 gives
x=exp[-2*pi^2*b/(N^2*delta)]. Then ||Q_x-I||=O(x), x/delta->0, and
-delta^-1 log Q_x->0. That conventional rotor scaling freezes the electric
motion when N is fixed. It is not the same order of limits as first taking
N to infinity.

## 2. A spatial Villain factor that yields the Wilson plaquette potential

For any plaquette angle phi define the positive normalized multiplier

    B_y(phi)=[1+2 sum_{q>=1} y^(q^2) cos(q phi)]/theta(y),
    y=exp[-1/(2*beta_s)].

The numerator is the Villain Fourier series. It is positive by its real
Gaussian representation and at most theta(y), so 0<B_y<=1. Uniformly in phi,

    B_y(phi)=1-2*y*(1-cos phi)+O(y^2).

Choose y=delta*K/2, K>0. Then

    beta_s=1/[2 log(2/(delta*K))],
    -delta^-1 log B_(delta*K/2)(phi) -> K(1-cos phi)

uniformly in phi. The same remainder estimate as for Q applies after
replacing H0 by the scalar 2(1-cos phi). This is inverse-logarithmic spatial
coupling. beta_s proportional to delta would instead give a spatial
interaction that vanishes faster than delta.

For fixed N,t,K the two matched scalings satisfy

    beta_tau*beta_s -> N^2/(4*pi^2).

This limiting product is a scaling identity, not a critical-coupling relation.
The t/K ratio remains in the subleading logarithms and in the Hamiltonian.

## 3. Matched finite-box Hamiltonian and Gauss projection

On a fixed finite spatial cell complex, allow link-dependent t_l>0 and
plaquette-dependent K_p>0. Let Q_delta be the tensor product of the temporal
Q_(delta*t_l), and let B_delta multiply by the product over plaquettes of
B_(delta*K_p/2)(phi_p). Form the positive symmetric transfer

    T_delta=B_delta^(1/2) Q_delta B_delta^(1/2).

Each factor is gauge invariant for Z_N: the link translations commute with
vertex gauge translations, and plaquette angles are unchanged. For fixed
finite volume, multiplying the norm expansions gives

    T_delta=I-delta H_g+O(delta^2),
    H_g=sum_l t_l(2-X_l-X_l^*) + sum_p K_p(1-Re W_p).

Therefore T_delta^(floor(T/delta))->exp(-T H_g) in operator norm for fixed
T>=0, as does -delta^-1 log T_delta->H_g. The same limits hold after
restriction to any invariant Gauss sector. The O(delta^2) constant from this
simple product proof depends on the finite box; no uniform thermodynamic
statement is inferred from it.

A supplied finite-dimensional gauge-invariant Hermitian matter Hamiltonian
H_m can be included by the positive sandwich

    T_delta,m=exp(-delta H_m/2) T_delta exp(-delta H_m/2).

It has generator H_g+H_m on the fixed finite box. A harmless scalar energy
shift can make each matter exponential contractive if desired. This uses the
specified operator H_m; it does not show that its coherent-state determinant
is the nearest-neighbor Euclidean Wilson D of the other campaign block.

In particular exp(-delta h(theta)) for a spatial hopping matrix generally
has an infinite Fourier series in the link phases, even on a finite graph.
The finite-degree determinant-current bound from the nearest-neighbor D
cannot simply be transferred to that exact exponential. A bond-split transfer
can restore bounded phase degrees per factor, but its source map, multiplicity
and limiting error must be derived for that discretization.

## 4. Why the isotropic massive bound does not cover this limit automatically

Take the usual supplied r=1 free Wilson discretization with temporal spacing
delta and fixed spatial spacing a in three spatial dimensions. Its diagonal
M_delta=m0+1/delta+3/a and forward/backward hopping norms are 1/a_mu each.
The absolute rooted-walk majorant used in block2 has ratio

    q_count(delta)=(2/delta+6/a)/(m0+1/delta+3/a) ->2.

It therefore leaves its q_count<1 domain for every fixed physical m0. This
is a limitation of that particular absolute path estimate, not a proof of
singularity of the Wilson operator. For r=1 the orthogonal spin projectors
in opposite temporal directions can improve the operator norm: each axial
hopping operator has norm at most 1/a_mu, hence

    ||K||/M_delta <= (1/delta+3/a)/(m0+1/delta+3/a)<1, m0>0.

For open boundaries this follows by compression from unitary covariant shifts;
for periodic boundaries it follows directly from the orthogonal projectors.
The improved ratio still tends to one. It establishes invertibility/log-series
convergence at each delta, but does not supply the volume- and delta-uniform
curl-curvature majorant used by block2. Its proof counted individual paths
in absolute value, so inserting the smaller operator norm in that path count
would be invalid.

The operator also has a coercivity proof independent of the walk expansion.
Writing U_mu for the unitary covariant forward shift and P_mu,+/- for the
orthogonal spin projectors,

    Re D = m0 I + sum_mu [I-(U_mu+U_mu^*)/2]/a_mu >=m0 I.

The anti-Hermitian spin-derivative contribution cancels in Re D. Compression
preserves this inequality for open boundaries. Therefore the minimum singular
value is at least m0 and ||D^-1||<=1/m0, uniformly in delta, volume and gauge
field. This does not by itself provide the needed gauge-curl curvature bound:
trace multiplicities, gauge derivatives and physical spacetime weights still
have to be controlled.

A plausible next attack is to resum long temporal runs before expanding in
spatial hopping. It must preserve the physical field/source normalization,
fermion boundary conditions and finite-cyclic Gauss projection. No such
resummation or uniform interacting phase theorem is claimed here.

## 5. Prior art and what is actually new in this working block

After deriving the displayed Villain scaling, a targeted search located
Pásztor and Pesznyák, *Gauge field digitization in the Hamiltonian limit*,
arXiv:2609.07886v2 (9 September 2026). Their section II derives logarithmic
temporal scaling for the Wilson action; the spatial Wilson coupling scales
linearly in the time step. Their numerical work concerns pure gauge models
in 2+1 dimensions. It is not an interacting 3+1-dimensional phase theorem.
The logarithmic finite-group mechanism therefore has explicit prior art.
This working block's role is the direct Villain normalization, its pairing
with the campaign's specified clock Hamiltonian, and the checked separation
from the massive determinant/current proof domain. These are model-matching
steps, not a claim to discover the general finite-group scaling principle.

Primary source: https://arxiv.org/abs/2609.07886v2 . The fetched v2 PDF has
SHA256 5a64a9eec53ae6b24b0677ac6cc857e0d09023c9914c7fea02974840891ca835.
