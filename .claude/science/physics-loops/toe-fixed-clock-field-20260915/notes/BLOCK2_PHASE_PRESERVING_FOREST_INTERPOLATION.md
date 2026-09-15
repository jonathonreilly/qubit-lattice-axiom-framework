# A phase-preserving stable forest interpolation

Personal derivation, 2026-09-15. This gives a finite connected-weight
identity and an undifferentiated stability bound. It does not yet bound
the complete differentiated tree sum over component positions and shapes.

## 1. Why interpolating the raw phase loses a useful identity

For integer fillings and fixed integer N, the two representatives
theta_P=2pi N<n,PS> and theta_Q=-2pi N<Qn,S> differ by an integer
multiple of 2pi. Their exponentials agree. In general exp(i s theta_P)
and exp(i s theta_Q) do not agree for 0<s<1. Thus ordinary linear
interpolation of the exponent cannot silently reuse both physical-energy
root bounds throughout its interpolation interval.

Instead interpolate the mixed pair factor itself:

    Phi_ij(s) = 1-s+s exp(i sigma_i sigma_j theta_ij)
              = 1+s(cos theta_ij-1)+i s sigma_i sigma_j sin theta_ij.

Here sigma_i is the orientation sign. This factor is periodic in theta
at every s in [0,1], has modulus at most one, equals one at s=0 and the
physical pair factor at s=1. Its derivative contains the full original
sine and cosine difference. No sine of a fraction of the phase occurs.

## 2. A stable extension through incompatible configurations

Let component i have current j_i (electric) or q_i (magnetic), with
x_e=g^2, x_m=b^2. The relevant cubic Hodge Laplacians have spectrum at
most 16, so their inverse on its range satisfies G_r>=I/16. Take
c0=1/32 and define within each species the Gram matrix

    J'_ij = x_e <j_i,(G_1-c0 I)j_j>,
    J'_ij = x_m <q_i,(G_3-c0 I)q_j>.

Equivalently its filling kernels are x_e(P-c0 DD*) and
x_m(Q-c0 B*B). These are positive semidefinite, with the unscaled
operator norms at most one. This formulation applies on a free
contractible finite complex and to finite currents on the infinite
cubic lattice, with the usual matched Hodge inverses. Harmonic sectors
in a periodic finite complex require separate treatment.

Distinct compatible components have disjoint current support. Hence their
off-diagonal current inner product vanishes and J'_ij equals the original
Coulomb pair coupling J_ij. For incompatible pairs the modified coupling
may differ; their physical weight at full coupling is zero. We can choose
this extension without changing the endpoint law.

The diagonal self-weight splits exactly as

    exp(-x_i E_i/2)
      = exp(-c0 x_i ||current_i||_2^2/2) exp(-J'_ii/2).

Interpolate the same-species incompatibility indicator chi_ij by the
factor 1-s_ij chi_ij, with chi=1 for incompatible components. It lies
in [0,1]. Retaining the original unmodified off-diagonal Gram coupling
while softening hard core would not retain this particular local reserve:
opposite overlapping currents can cancel. The modified extension is
what permits the following positive Gram argument even at overlaps.

## 3. The finite interpolation and its uniform mass reserve

For a fixed finite list of occupied components and their signs, set
s_ii=1 and

    W_sigma(s) = product_i exp(-c0 x_i ||current_i||_2^2/2)
       * exp[-(1/2) sum_same i,j s_ij sigma_i sigma_j J'_ij]
       * product_same i<j (1-s_ij chi_ij)
       * product_mixed i,j Phi_ij(s_ij).

At s_ij=1 it is exactly the original joint component weight, including
hard core. Setting cross-block s entries to zero factorizes it across
those blocks, including the orientation average.

For a forest F with edge parameters t in [0,1], put s^F_ij equal to the
minimum t along its unique path, or zero for disconnected vertices.
The diagonal is one. This matrix is positive semidefinite: it equals
the integral from zero to one of the partition matrix whose blocks
are the components of the forest restricted to edges with t>=u.
Each partition matrix is a Gram matrix of block indicators.

The Schur product s^F composed entrywise with each J' is therefore
positive semidefinite. Every real Gram exponential above is at most
one; so are the moduli of all the other pair factors. For every sign
assignment, including incompatible component lists,

    |W_sigma(s^F)| <= product_i exp(-x_i m_i/64),
    m_i=||current_i||_1.

We used integer currents: ||current_i||_2^2>=m_i. The bound is uniform
in all forest parameters and list length. With a physical complex source
|z|<=R, the component-source note supplies an extra factor at most
exp(C_f R a sqrt(x_i) m_i). For sufficiently small a at fixed R and
fixed x_i this consumes at most half the displayed mass reserve.
This is a bound on W, not its logarithm or its normalized response.

## 4. Exact connected-weight forest identity

Let W_A(s) be the uniform orientation average for any subset A of the
component labels, and W_empty=1. Define its connected weight by partitions,

    U_A = sum_partitions pi (-1)^(|pi|-1)(|pi|-1)!
                                  product_(B in pi) W_B(1).

The finite BKAR Taylor forest formula, followed by this partition
inversion and the cross-block factorization, gives

    U_A = sum_spanning_trees T on A
              integral_[0,1]^T (product_(ij in T) partial_sij)
                                            W_A(s^T) dt.

The imported identity's hypotheses are checked here: the label set is
finite; W is a smooth function on the whole pair-parameter cube; and
setting cross-block parameters to zero factorizes the integrand. Complex
values present no problem by applying the scalar formula to real and
imaginary parts. See [Lohmann, section 2.1.3, equation (16)]
(https://arxiv.org/html/1411.1107v1). This imports the finite forest
identity only, not that paper's mass-dependent convergence theorem.

For a same-species edge the differentiated pair factor is

    exp(-s sigma_i sigma_j J'_ij)
       [-chi_ij-sigma_i sigma_j J'_ij(1-s chi_ij)].

For a mixed edge it is cos(theta)-1+i sigma_i sigma_j sin(theta).
The remaining factors retain the stable interpolation above. Taking
absolute values of every odd linear edge at this point, however, would
discard the spatial cancellations needed for a massless problem.

## 5. A useful matrix fact with a limited scope

If S is positive semidefinite with diagonal one, its Schur multiplier
is an operator-norm contraction: ||S composed A||<=||A||. Write S_ij
as <u_i,u_j> with unit vectors and embed e_i as e_i tensor u_i; the
entrywise product is the compression of A tensor I. For a rectangular
mixed kernel use the corresponding off-diagonal block of this identity.

For a fixed finite universe of component types and a fixed forest
correlation matrix indexed by those types, this preserves the small
full-sine operator norm. A forest on particle labels is not automatically
such a single fixed multiplier after positions, repeats, and other
interactions are summed. The tree integrand also includes products of
other component-dependent factors. The contraction statement alone
does not control those products or their connected graph combinatorics.

The remaining substantive task is a source-sensitive, summable bound
on the orientation-averaged differentiated trees that preserves signed
long-range cancellations through hard core and branching. The finite
identity and stable mass reserve specify a candidate starting point;
they are not a proof that this last task can be completed.

## 6. Finite author challenge

The accompanying checker independently assembles floating cubical
incidences on a free chain of four four-cubes and cross-checks four
projection entries against the earlier rational calculation. With N=3
and beta=1/2, it compares the connected weight from all 15 partitions
with the sum over all 16 spanning trees. Integrals are split into the
six edge-order sectors before Gauss quadrature, avoiding nonsmooth
path minima inside a sector. The original endpoint and modified endpoint
agree for compatible lists and vanish identically at excluded overlaps.

For compatible, electric-overlapping and doubly overlapping lists,
order-16 quadrature differs from direct partition inversion by at most
2.33e-12 after the common self-weight is factored out. The corresponding
order-10 maximum error is 0.00330, so the coarse result alone would not
be adequate. Random forest parameters also pass sign-wise stability
and finite Schur-contraction checks. A valid integer filling change
alters the raw halfway phase factor by 2, while the affine factor is
unchanged to 8.55e-15. These are finite author checks; neither quadrature
is interval certified, and the proof of the finite identity is the
matched forest formula above. An initial traversal bug and its interrupted
source are preserved under review/block2_forest_initial_cycle.
