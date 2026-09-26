# A covariant two-qubit encoding and its fluctuation-energy test

**Status:** proposed construction and conditional calculations; independent check pending.
**Date:** 2026-09-21. This changes the earlier physical encoding. No primitive is adopted.

The earlier classical fourteen-color process supplies two vector population
fields X and Y. The antipodal-product interpretation in
`DIMER_COLOR_OPERATIONAL_MOMENT_MAP.md` cannot operationally distinguish the
opposite classes used there. This note tests a specific alternative rather
than treating that result as a limit on every two-qubit encoding. It constructs
six observable components and noncommuting Gaussian fluctuations, then checks
the energy needed to give those fluctuations the same curl-wave drift.

The proposed states below are generally mixed and may be entangled. They are
not the original pair of individually pure antipodal record states. Quantum
states, the Born rule, product preparation between different pairs, and any
Hamiltonian interpretation are supplied premises. The classical label-dependent
Markov generator is not asserted to define a completely positive quantum map.

## 1. Explicit positive, rotation-covariant states

Use the normalized singlet s and orthonormal Cartesian triplets
`t_i=(sigma_i tensor I)s`. In this basis a simultaneous spin rotation acts as
`diag(1,R)` with R its proper three-dimensional rotation matrix. Let

    rho_0 = diag(q,r,r,r),    q+3r=1, q,r>0.

For the six axis colors take e=+/-e_i,b=0; for the eight corner colors take
e=0,b=(+/-1,+/-1,+/-1). Choose positive lambda_A,lambda_B with

    max(lambda_A^2, 3 lambda_B^2) < q r.                 (1)

For each color a define the three-vector
`w_a=lambda_A e(a)+i lambda_B b(a)` and the two-qubit density matrix

    rho_a = [ q      w_a^dagger ]
            [ w_a       r I_3   ].                     (2)

The Schur complement is `q-||w_a||^2/r>0`, so all fourteen states are strictly
positive and trace one. They are distinct but not mutually orthogonal. For
any proper cubic rotation R, `rho_{Ra}=diag(1,R) rho_a diag(1,R)^dagger`.
Exchange of the two endpoint qubits reverses the singlet-triplet off-diagonal
blocks, taking rho_a to rho_{-a}. This is an oriented-pair encoding.

Define the six Hermitian observables

    A_i = |s><t_i|+|t_i><s|,
    B_i = i(|t_i><s|-|s><t_i|).                       (3)

Their expressions in physical Pauli operators are

    A_i = (sigma_{1i}-sigma_{2i})/2,
    B_i = -(sigma_1 cross sigma_2)_i/2.               (4)

Consequently

    Tr(rho_a A_i)=2 lambda_A e_i(a),
    Tr(rho_a B_i)=2 lambda_B b_i(a).                  (5)

An independently mixed color population p therefore encodes
`X=sum p_a e(a)` and `Y=sum p_a b(a)` as six directly measurable expectation
values. These observables need not commute and are measured on separate
preparations as appropriate. Tomographic access to six moments does not
identify fourteen nonorthogonal labels in a single sample.

Every orbit-isotropic population has X=Y=0 and encodes rho_0. Different
isotropic orbit weights then share rho_0; no inference of those extra color
statistics is claimed. The map has exactly six independent population-tangent
directions: the axis differences span three e coordinates and corner
differences span three b coordinates. Remaining color statistics are lost.

For a rational example set q=1/2,r=1/6,lambda_A=1/8,lambda_B=1/16. The two
Schur complements are 13/32 and 55/128. These parameters are choices, not
measured constants or predictions.

## 2. Product-state quantum fluctuation limit

Order O=(A_1,A_2,A_3,B_1,B_2,B_3), and use independently prepared blocks in
rho_0. Their means vanish. Direct matrix multiplication gives the symmetrized
covariance V and commutator form Sigma:

    V_ab = Tr rho_0 {O_a,O_b}/2 = (q+r) I_6,
    Sigma_ab = -i Tr rho_0 [O_a,O_b]
             = 2(q-r) [ 0  I_3 ; -I_3  0 ].           (6)

The same-type commutator expectations vanish; cross expectations are
`Tr rho_0[A_i,B_j]=2i(q-r)delta_ij`. Positivity of the quantum covariance
`V+i Sigma/2` follows directly from the Gram matrix `Tr rho_0 O_a O_b`;
its eigenvalues are 2q and 2r, each threefold. For q!=r the limiting algebra
has three canonical pairs. At q=r=1/4 the commutator form vanishes and this
fluctuation limit is classical. Thus noncommutation depends on preparation.

Here is a direct finite-dimensional proof of the claimed limit, without
assuming a general interacting quantum central-limit theorem. For K blocks set

    F_K(O_a)=K^-1/2 sum_{x=1}^K O_a^(x),
    W_K(z)=exp(i sum_a z_a F_K(O_a)), z real.

For any fixed finite sequence z_1,...,z_m, operators on distinct blocks commute,
so the expectation of `W_K(z_1)...W_K(z_m)` is exactly

    [Tr rho_0 product_{j=1}^m exp(i z_j.O/sqrt(K))]^K. (7)

All matrices are bounded, m and the z_j are fixed, and the first-order term
vanishes. Expanding the single-block product through second order gives

    1 + K^-1[-(1/2) z_sum^T V z_sum
                -(i/2) sum_{j<l} z_j^T Sigma z_l]
        + O(K^-3/2).                                 (8)

The constant is finite for the specified sequence, by the matrix exponential
Taylor remainder and a finite product expansion. Taking the Kth power proves
convergence to

    exp[-(1/2) z_sum^T V z_sum
             -(i/2) sum_{j<l} z_j^T Sigma z_l].        (9)

This is the Gaussian Weyl characteristic function, including its ordering
phase. Equation (9), rather than only a single observable's Gaussian law,
identifies the noncommuting fluctuation algebra. It says nothing about a
microscopic quantum time evolution.

The spatially smeared version replaces z_j at block x by bounded real test
functions z_j(x). If their pairwise empirical inner products converge, the
same expansion holds with averages of the local quadratic terms. Its
commutator kernel is onsite: Sigma times the limiting spatial delta function.
One obtains this statement for each fixed finite family of test functions,
not a uniform limit over unbounded frequencies or shrinking supports.

The general subject is established in Goderis and Vets,
[Central limit theorem for mixing quantum systems and the CCR-algebra of
fluctuations](https://doi.org/10.1007/BF01257415) (1989). Only its publisher
abstract and metadata were inspected here. Equations (7)-(9) prove the
specific product-state assertion used in this note; no general mixing theorem
is imported from the unread paper.

## 3. Matching the classical wave normalization

Write the earlier orbit-isotropic wave equations as

    d_t X = a curl Y,    d_t Y = -b curl X, a,b>0.     (10)

For the supplied gamma>0 model, a=gamma rho_A/3 and b=gamma rho_B.
The physical expectation fields in (5) are U=2lambda_A X and Vfield=2lambda_B Y.
Choosing

    lambda_B/lambda_A=sqrt(a/b)                       (11)

makes their hypothetical drift

    d_t U = c curl Vfield,    d_t Vfield=-c curl U,
    c=sqrt(ab).                                      (12)

Both lambda values can be decreased together to meet (1), so this normalization
poses no positivity obstruction. Their product-state fluctuation covariance
is the same on the U and Vfield observables, and is preserved by (12).
The rational example in section 1 matches the equal-fourteen-color weights:
a=gamma/7,b=4gamma/7,c=2gamma/7.

Equation (12) is only a candidate fluctuation evolution. This note does not
construct a quantum generator that realizes it, derive it by applying the
old label-dependent rates to (2), or transfer the classical Euler theorem to
these new quantum states.

## 4. The Hamiltonian fixed by the onsite commutator

Assume q!=r and write s_0=2(q-r). For real fields Z=(U,Vfield), their candidate
onsite Poisson/CCR form is `Sigma=s_0 J`, with
`J=[0,I;-I,0]`. A quadratic Hamiltonian with self-adjoint Hessian H generates
`d_t Z=Sigma H Z`. Curl is self-adjoint on periodic real vector fields; at
Fourier wavevector Q it is the Hermitian matrix `C(Q)=i[Q cross]`.
The generator of (12) is

    L(Q) = c [ 0 C(Q); -C(Q) 0 ].

Since Sigma is invertible, its unique quadratic Hessian is

    H(Q)=Sigma^-1 L(Q)=(c/s_0) diag(C(Q),C(Q)).        (13)

For every Q!=0, C(Q) has eigenvalues +|Q|,-|Q|,0. Equation (13) therefore has
two positive, two negative and two zero eigenvalues. The real field uses
paired Q and -Q; the negative directions persist on real sine/cosine fields.
Restricting to transverse fields removes the zero modes and leaves both signs.
Changing the sign of s_0 reverses the signs without making the form positive.

This is an energy-compatibility test for the stated onsite bracket, full
transverse helicity space and exact drift. It excludes interpreting (13) as
a positive quadratic vacuum energy on that space. It does not exclude a
bounded microscopic spin Hamiltonian with this fluctuation linearization
around an excited state, a restricted helicity sector, a different bracket,
additional degrees of freedom, or a different encoding. Stable oscillation
frequencies alone do not make the generating quadratic form positive.

The positive classical conserved norm `(||U||^2+||Vfield||^2)/2` is indeed
preserved by (12). With the onsite Sigma it generates onsite rotations,
not (12). Confusing a conserved quadratic norm with the Hamiltonian generating
the flow would miss the curl in (13).

## 5. Explicit positive-energy escape with a derivative bracket

The following elementary canonical construction identifies a concrete change
that avoids section 4. It is supplied continuum Gaussian field theory, not
a result about the moving-record microscopic law. Let Qpot,P be canonical
vector fields on a periodic box, `{Qpot_i(x),P_j(y)}=delta_ij delta(x-y)`, and
choose the positive semidefinite Hamiltonian

    Hplus = (1/2) integral [|P|^2+|curl Qpot|^2].      (14)

Define E=-P and Bmag=curl Qpot. Hamilton's equations imply

    d_t E = curl Bmag,    d_t Bmag=-curl E.           (15)

The observable bracket has the derivative matrix
`J_EB=[0,curl;-curl,0]`, so the positive field energy generates (15).
The identity div Bmag=0 is automatic; div E=0 requires a separate initial
constraint, subsequently preserved. Longitudinal Qpot is a gauge direction.
At Q!=0 the derivative bracket on transverse E,Bmag has rank four; its null
directions on the full six-component space are the two longitudinal fields.

A discrete curl can play the same algebraic role if its adjoint, divergence
identity, and spectrum are checked. No such operator is identified with a
microscopic record observable here. The standard field-theory reference is
[Marsden and Weinstein, The Hamiltonian structure of the Maxwell-Vlasov
equations](https://www.cds.caltech.edu/~marsden/bib/1982/04-MaWe1982/)
(1982); the direct vacuum calculation (14)-(15) carries this note's claim.

## 6. What this changes and what remains to be built

There is a concrete rotation-covariant two-qubit encoding of both vector
moments, and its independently prepared fluctuations can have nonzero CCR.
These are kinematic constructions under changed encoding/preparation premises.
The old operational degeneracy is not a universal obstruction to six vector
observables. The positive-energy test points to a specific next obligation:
derive a derivative commutator/constraint structure and a compatible local
quantum generator from an admissible microscopic encoding.

The same exact label-dependent exchange law has not been implemented as a
quantum channel. The original pure-record interpretation has not been recovered.
No vacuum, photon, gauge constraint on actual record states, Lorentz symmetry,
Born rule, gravity, or TOE follows. The energy calculation is a narrow
conditional statement, not a no-go for those alternatives. Finite matrix
controls below supplement the complete arguments and are not an all-system
simulation or an independent audit.
