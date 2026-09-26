# The operational moment map of the fourteen classical pair colors

2026-09-21. Root conditional calculation; independent check pending.

This note tests one precise quantum readout interpretation of the routed
color construction. Suppose a record carrying P_n is physically a single
qubit in that pure state, an antipodal pair is prepared in the product
P_n tensor P_-n, and ordinary quantum measurements read those qubits with
Born probabilities. These are added interpretation premises, not claims
derived from the repository axioms. The routed theorem itself assumes
exact classical access to the projector label and explicitly does not
provide such a finite-qubit measurement.

Under these premises the relevant quantum ensemble has a simple moment
map. For the specified even cubic color classes, opposite classical
colors have exactly the same pair density operator at a fixed birth-edge
direction. The six vector fields used in the color-wave theorem are odd
under those opposite-color exchanges. Their population signal is therefore
absent from this quantum encoding. The statements below concern that
encoding and its stated ensemble, not every possible record readout.

## 1. Pair density in a singlet/triplet basis

Let |s>=(|up,down>-|down,up>)/sqrt(2), and
|t_i>=(sigma_i tensor I)|s>, i=x,y,z. These four vectors are an orthonormal
complex basis. Up to an irrelevant phase the antipodal product state is

    |n,+> tensor |n,-> = (|s>+sum_i n_i |t_i>)/sqrt(2).

This follows directly by expanding its projector with the Pauli matrices.
For any probability distribution of the unit vector n, write
mu=E n and M=E nn^T. Its pair density in this basis is consequently

    rho(mu,M) = (1/2) [[1, mu^T], [mu, M]],              (1)

with tr M=1. The distribution's higher moments are not readable from this
single pair density. If the distribution has positive density on an open
spherical patch, its covariance M-mu mu^T is positive definite: a nonzero
linear function of n cannot be constant on an open sphere patch. The
Schur complement then shows that rho is positive definite.

## 2. The actual color-conditioned birth ensemble

Use exactly the color code of DIMER_ROUTED_RECORD_TRANSPORT.md:

    f(n)=(n_y n_z(n_y^2-n_z^2),
          n_z n_x(n_z^2-n_x^2),
          n_x n_y(n_x^2-n_y^2)).

It is even in n and covariant under the twenty-four proper cubic rotations.
The six A colors are the sign and axis of a unique component exceeding
0.9|f|. Otherwise the eight B colors are the component signs of f, with
the source's zero-measure exceptional convention. The reference g0 is
even and proper-cubic invariant, constant separately on the A and B unions.
Every color class has positive measure and contains an open patch.

For a color a, let M_a be the second moment of n conditioned on that class
under g0. At an ordered birth edge with unit direction delta the density is
g0(n)(1+epsilon n.delta), where 0<|epsilon|<1. Evenness of each class gives
the unchanged class probability, zero even-reference first and third
moments, and hence exactly

    mu_(a,delta)=epsilon M_a delta,
    M_(a,delta)=M_a,
    rho_(a,delta)=rho(epsilon M_a delta,M_a).             (2)

This is the two-qubit product-state interpretation of the actual supplied
birth law, including its nonzero neighbor-dependent tilt. It does not
replace that law by a direction-independent birth distribution.

## 3. Opposite colors have the same quantum density

Consider the A color +e_x. Its class is invariant under a quarter turn
around x, so its real symmetric second moment must have form

    M_(A,+x)=diag(a,b,b),   a+2b=1.

A proper half turn about y sends the color +e_x to -e_x and leaves this
matrix unchanged. Therefore M_(A,-x)=M_(A,+x). Rotating gives the same
equality for the other two A pairs.

For B_(1,1,1), the cyclic permutation of the coordinates fixes the color,
so its second moment has equal diagonals and equal off-diagonals:

    M_(B,111)=(1/3-c)I+c 11^T.

The proper rotation (x,y,z)->(-y,-x,-z) sends that color to its opposite
and leaves this matrix unchanged. Covariance under proper cubic rotations
then gives M_(B,b)=M_(B,-b) for every corner b. Thus, at every fixed delta,

    rho_(a,delta)=rho_(-a,delta)                         (3)

for all seven opposite-color pairs. The equality includes the first moment
in (2), not only the antipodally symmetrized reference ensemble.

For any quantum effect E on those two physical qubits, (3) gives identical
outcome probabilities tr(E rho). No measurement on this pair distinguishes
the opposite class labels in that ensemble. Repeating preparation of
independent pairs with the same conditional ensemble does not help:
their density-operator tensor powers are also equal. This differs from
receiving many copies of the same unknown pure projector n, which is a
changed preparation and is not excluded.

## 4. The wave population directions are in the kernel

For a mixture with arbitrary color probabilities p_a, keeping the
within-class birth ensemble and delta fixed, its density is determined
by M(p)=sum_a p_a M_a via (2). The matrix M(p) is symmetric with trace one,
so this operational population map has at most five independent tangent
directions. In particular, every probability perturbation satisfying

    v_-a=-v_a

leaves M(p), mu(p) and the entire pair density unchanged. There are seven
independent such tangent directions among the fourteen colors.

The routed vector moments X=sum_a p_a e_a and Y=sum_a p_a b_a receive
their linear population signal from this odd subspace: e_-a=-e_a and
b_-a=-b_a. Three A-pair imbalances independently change X, and three
independent B-pair imbalances change Y. Thus all six vector population
directions, including the four propagating transverse modes under the
isotropic law, can change without changing the encoded pair density.

For independent preparations at different fixed matched pairs, choose
small spatially varying probability perturbations in those directions.
Each physical pair density is unchanged, so the full product density is
unchanged. Any collective quantum measurement has the same statistics,
and any common completely positive quantum evolution preserves that
indistinguishability. This is an exact comparison of these preparation
ensembles. The classical routed dynamics need not define such a quantum
channel, since it reads the additional exact labels by assumption.

The conclusion is not that every higher-moment property of an individual
projector is meaningless. It is that the chosen population wave cannot
be identified with an operational quantum signal through this particular
single-pair encoding. A different encoding or additional accessible record
degrees of freedom would require a separate analysis.

## 5. A separate finite discrimination bound

At epsilon=0, (1) is block diagonal with a singlet eigenvalue 1/2 and
triplet block M_a/2. Since M_a is positive semidefinite with trace one,
rho_a<=I_4/2. For equal priors on the fourteen classes and any fourteen-
outcome POVM {E_a}, the probability of guessing the entire class correctly
therefore obeys

    p_guess=(1/14)sum_a tr(E_a rho_a)
              <= (1/28)tr I_4 = 1/7.                   (4)

For the actual tilted ensemble, the density weight is at most 1+|epsilon|
times its even-reference weight. The same positive-operator integral gives
rho_(a,delta)<=(1+|epsilon|)rho_a and hence

    p_guess <= (1+|epsilon|)/7.                          (5)

These bounds apply to equal class priors; the orbit-isotropic choice
rho_A=3/7, rho_B=4/7 makes all fourteen probabilities 1/14. They are upper
bounds and are not claimed tight. Equation (3), unlike (4)-(5), is an exact
indistinguishability statement for each opposite pair and any allowed tilt.

## 6. Physics implications and alternatives kept open

The classical conditional wave theorem remains intact. Its label readout
is an explicit supplied premise. This calculation identifies an additional
obligation for using that construction as quantum physics: the field must
be connected to an operationally accessible degree of freedom, and its
dynamics must act consistently on whichever quantum encoding is proposed.

An accessible classical marker, a larger orthogonal encoding, multiple
copies of a fixed n, a different color code, another preparation ensemble,
or a different microscopic interpretation can change the problem. No
theorem excluding those alternatives is claimed. In particular, ordinary
Born readout is an assumption of this test, not a result or an axiom that
has been silently inserted into the original research lane. This note
does not settle whether the intended primitive records are such qubit
states, ontic labels with extra readout, or something else.
