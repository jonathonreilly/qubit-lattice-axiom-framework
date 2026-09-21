# A positive curl Hamiltonian as a controlled finite-qubit block limit

**Status:** proposed conditional construction; author controls and independent
check pending. **Date:** 2026-09-21.

This is an explicit alternative to the onsite energy identification tested in
`DIMER_COVARIANT_QUANTUM_FLUCTUATION_ENCODING.md`. It starts from actual finite
qubit Hilbert spaces, constructs a positive Hamiltonian, and proves a fixed
finite-volume, fixed-time limit to canonical Gaussian fields. Electric and
magnetic observables then have a derivative commutator and curl dynamics.

The construction supplies a block architecture and a new Hamiltonian. It does
not preserve each original classical record projector, implement the earlier
label-dependent stochastic exchanges, couple to record formation, or satisfy
a uniform nearest-neighbor rule on the original fine lattice. These are
explicit outstanding realization questions. The result is a controlled model
construction, not a derivation from the record axioms or a photon/TOE claim.

## 1. Finite qubit blocks and the exact occupation representation

Fix a finite periodic coarse cubic lattice Lambda with L>=3 sites per side.
At every coarse cell x put K independent pairs of qubits. In each pair use
the singlet |0> and the three Cartesian triplets |i>,i=1,2,3, as an orthonormal
basis of C^2 tensor C^2. Retain the permutation-symmetric subspace of the K
pairs at each cell; the Hamiltonian below preserves that subspace exactly.
Its normalized occupation basis is

    |n_1,n_2,n_3>_K,  n_i>=0, n=n_1+n_2+n_3<=K.

This is a finite subspace of the actual 2K-qubit Hilbert space, of dimension
binomial(K+3,3). Identify it isometrically with the same occupation vectors
in a three-mode bosonic Fock space. Let

    a_{i,x,K}=K^-1/2 sum_{ell=1}^K |0><i|_(x,ell).

Counting the identical terms between normalized occupation sums gives

    a_{i,x,K}|n> = sqrt[n_i (1-(n-1)/K)] |n-e_i>,
    a_{i,x,K}^dagger|n> = sqrt[(n_i+1)(1-n/K)] |n+e_i>. (1)

The second line vanishes when n=K. Thus, on Fock space, the exact extension is

    a_{i,x,K}=f_K(N_x) a_{i,x},
    a_{i,x,K}^dagger=a_{i,x}^dagger f_K(N_x),
    f_K(n)=sqrt(max(1-n/K,0)).                          (2)

The physical sector N_x<=K is reducing; outside it the operators for that
cell vanish. Define Q_{i,x,K}=(a_K+a_K^dagger)/sqrt(2) and
P_{i,x,K}=i(a_K^dagger-a_K)/sqrt(2). These are bounded Hermitian operators
on finitely many qubits. The vacuum of the occupation representation is the
actual product of K singlets per cell, not a postselected classical dimer law.

Simultaneous spin rotations preserve the singlet and rotate the three
triplets as a Cartesian vector. Spatial proper cubic rotations, accompanied
by this physical spin rotation, therefore rotate Q_K and P_K as vectors.
No spin-3/2 or enlarged single-pair representation is used.

## 2. A specified discrete curl and positive microscopic Hamiltonian

Set the coarse spacing to one, as a chosen unit. Let

    D_j f(x)=[f(x+e_j)-f(x-e_j)]/2,
    (C f)_i=sum_{j,k} epsilon_ijk D_j f_k.

The finite periodic difference matrices commute and satisfy D_j^T=-D_j.
Because epsilon is antisymmetric in its vector indices, the full real
matrix C is symmetric: C^T=C. Discrete divergence D dot annihilates C
exactly. Define on the finite qubit blocks

    H_K=(1/2) sum_{x,i} P_{i,x,K}^2
        +(1/2) sum_{x,i} (C Q_K)_{i,x}^2.              (3)

This is positive semidefinite, self-adjoint, and permutation-invariant inside
each cell. Expanded in qubit operators it has at most two pair factors in
any term. A pair factor itself may act on both qubits of that pair. Within
and between the finitely many neighboring coarse cells, its couplings are
collective sums with 1/K weights. Squaring C gives a finite coarse-cell
range of at most two steps.

The architecture has an honest locality cost: embedding K distinct pairs in
a fine lattice makes the block diameter grow with K, and (3) directly couples
many pairs throughout those blocks. No constant-range fine-lattice
implementation or uniform interaction-strength bound is claimed. The limit
below keeps Lambda fixed while K grows. It is not a simultaneous infinite
spatial-volume limit.

## 3. A quantitative finite-time Fock-space limit

Let Q,P be the canonical Fock quadratures at the same finite set of cells,
and set

    H=(1/2) sum P^2+(1/2) sum (C Q)^2.                 (4)

Let N be the total Fock number over all 3|Lambda| modes. On the finite-particle
core, the elementary inequality

    0<=1-sqrt(max(1-u,0))<=u,  u>=0

and (2) give, with constants independent of K,

    ||(a_{i,x,K}-a_{i,x})psi||
       +||(a_{i,x,K}^dagger-a_{i,x}^dagger)psi||
       <= C_1 K^-1 ||(N+1)^(3/2) psi||.              (5)

The estimate includes occupations above K; there the left coefficient is at
most sqrt(n+1), while (n+1)/K>=1. A quadrature changes total number by at most
one, and its coefficient is bounded by C sqrt(N+1). Expanding a difference
of quadratic products, for example A_K B_K-AB=(A_K-A)B_K+A(B_K-B), therefore
proves

    ||(H_K-H)psi|| <= C_Lambda K^-1 ||(N+1)^2 psi||.  (6)

The same inequality extends to the indicated weighted-number domain by
truncation. Here H_K is extended through (2) to the common Fock space. It is
bounded for each fixed K and finite Lambda; its restriction to the physical
sector is exactly the finite-qubit Hamiltonian (3).

The real positive quadratic H is essentially self-adjoint on finite-particle
vectors. One direct justification expands its n-fold action: each factor
changes number by at most two and has norm at most C(N+1). A fixed finite
particle vector then satisfies ||H^n psi||<=C_psi^n (n+m)!, making it analytic
for sufficiently small parameter; the analytic-vector criterion applies.
The positive closure generates a unitary group.

For any finite-particle initial vector psi and fixed T, the quadratic
Heisenberg evolution is a finite linear transformation of Q,P. Consequently
all fourth number moments remain bounded on [-T,T]:

    sup_{|t|<=T} ||(N+1)^2 exp(-itH)psi|| = M_{psi,T}<infinity. (7)

This also follows by bounding the commutator of H with (N+1)^4 as a quadratic
form by C(N+1)^4 and applying Gronwall after number truncation. Equation (7)
does not claim a bound uniform in Lambda,T,or high-energy initial states.

Duhamel's formula, unitarity, and (6)-(7) now give the strong estimate

    sup_{|t|<=T} ||[exp(-itH_K)-exp(-itH)]psi||
       <= C_Lambda T M_{psi,T}/K.                    (8)

For sufficiently large K the fixed finite-particle vector lies in the
physical sector at every cell. Thus (8) compares the exact finite-qubit
unitary evolution with the Gaussian limit. Expectations of any fixed bounded
Fock observable differ by at most twice its norm times the right side of (8).
No claim about unbounded-observable convergence follows from that last
sentence alone; those require weighted moment control.

Physical bounded Weyl observables can also be compared. Replacing canonical
quadratures by Q_K,P_K in an exponential of a fixed finite linear combination,
Duhamel's formula for that exponential and (5) give O(1/K) on vectors with
bounded required number moments. Combining this with (8) transfers fixed
finite products of such Weyl observables on finite time intervals. The
constants depend on the fixed smearings, time and finite coarse lattice.

## 4. The limiting observable algebra and curl equations

In the canonical limit define

    E=-P,    B=C Q.

Then [Q_alpha,P_beta]=i delta_alpha,beta gives exactly

    [E_alpha,B_beta]=i C_beta,alpha,
    [E_alpha,E_beta]=[B_alpha,B_beta]=0.              (9)

The block commutator matrix is [0,C;-C,0], because C is symmetric. From (4),

    d_t Q=P,       d_t P=-C^2 Q,
    d_t E=C B,     d_t B=-C E.                       (10)

Thus the same positive H generates curl dynamics with a derivative
commutator. The onsite-canonical energy test of the previous note does not
apply to these E,B observables: one has explicitly changed their bracket.
The magnetic divergence vanishes as an operator identity, D dot B=0.
Electric divergence D dot E is conserved but generally nonzero in the
product-singlet fluctuation state. A zero-charge sector or suitable initial
constraint is an additional step, not supplied by (8).

For lattice Fourier momentum k, C(k)=i[sin(k) cross]. Let s(k) be the vector
of its three sines. At s(k)!=0 the curl eigenvalues are +|s|,-|s|,0; the
transverse canonical oscillators have frequency |s| and positive quadratic
energy. The E,B bracket has rank four at that momentum and its two
longitudinal components are central in the E,B observable algebra. B's
longitudinal component is identically zero. The potential's longitudinal
coordinate is a gauge direction only in the limiting canonical description;
no exact finite-K gauge symmetry is inferred.

The centered discretization also has s(k)=0 at every available combination
of k_j in {0,pi}. For even L this includes eight lattice momentum zeros.
These extra zeros and longitudinal free-coordinate directions are preserved
as limitations, not silently dropped. The small-k branch has linear frequency
|k|+O(|k|^3) in the chosen units. No absence of lattice species doubling or
emergent Lorentz theorem is claimed.

## 5. Scope of the positive construction

Equations (1)-(10) provide a finite-qubit, positive-Hamiltonian route to
Gaussian curl fields with a derivative commutator. The load-bearing small
parameter is inverse block size at fixed coarse volume and time. The route
uses a supplied Hamiltonian and initially singlet blocks; it does not transfer
the earlier classical filling law, wave theorem, or immutable-content dynamics.

To use this inside the permanent-record research program, one would have to
supply an admissible physical meaning for these evolving qubit states,
realize the collective couplings with the permitted local moves and clock,
control a joint spatial limit, and specify the electric constraint/physical
state sector. Those are constructive questions, not assertions that a new
axiom is required. They are why this note is a conditional model construction
rather than a completed derivation of quantum electromagnetism.
