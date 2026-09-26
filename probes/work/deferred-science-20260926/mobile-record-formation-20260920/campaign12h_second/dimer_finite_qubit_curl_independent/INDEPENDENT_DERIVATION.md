# Independent reconstruction before author controls

Boundary: the complete supplied finite-qubit note at SHA-256
2448a007eb36de39c3b71db88190af5eec858b6c21a65d005f4229f4ff477010
has been read. The author checker, results and analytic-vector source receipt
have not. This is a selective proof check, not an audit or a microscopic
implementation claim. No actionable defect has been found in this reconstruction.

## 1. Actual qubits, occupation order and the cutoff

A singlet and the three vectors (sigma_i tensor I)|singlet> form an orthonormal
basis of two actual qubits. In the symmetric subspace of K such pairs, normalize
the sum of words with counts (n_0,n_1,n_2,n_3) by the square root of
K!/(n_0! n_1! n_2! n_3!). Counting preimages of a word under the collective
matrix unit E_{0i}/sqrt(K) gives exactly

    a_iK |n> = sqrt(n_i (1-(n-1)/K)) |n-e_i>,
    a_iK^* |n> = sqrt((n_i+1)(1-n/K)) |n+e_i>.

Thus, on the common three-mode Fock space, the order is f_K(N_x)a_i,
with adjoint a_i^* f_K(N_x), where f_K(n)=sqrt(max(1-n/K,0)). At n=K
raising vanishes; at n=K+1 lowering also vanishes. The entire sector n>K
is annihilated. The physical sector n<=K is reducing, not merely compressed.
The operator norm is finite: ||a_iK|| <= (K+1)/(2 sqrt(K)). For a fixed finite
number of cells this makes the extended H_K bounded and self-adjoint.

The exact finite-K commutator is

    [a_iK,a_jK^*] = (delta_ij E_00 - E_ji)/K.

For i=j it is 1-(N_x+n_i)/K. There is no exact finite-dimensional canonical
commutation relation. The original tensor-product Hamiltonian is a sum of
Hermitian squares, is positive, and preserves the symmetric block subspaces.
These are statements about the newly supplied collective Hamiltonian, not
about immutable projector conservation under the original record process.

## 2. Weighted operator error on the common space

Write N for total occupation over the fixed finite lattice. The scalar inequality
0 <= 1-sqrt(max(1-u,0)) <= u, u>=0, proves separately

    ||(a_iK-a_i)psi|| <= K^-1 ||(N+1)^(3/2)psi||,
    ||(a_iK^*-a_i^*)psi|| <= K^-1 ||(N+1)^(3/2)psi||.

It remains valid above the physical cutoff; there the canonical coefficient is
bounded by the right side because N>=K. Consequently C_1=2 is sufficient for
the sum in the source's equation (5).

For X equal to either Q or P, and also for X_K, a useful explicit weighted bound is

    ||(N+1)^s X_K psi|| <= b_s ||(N+1)^(s+1/2)psi||,
    ||(N+1)^s (X_K-X)psi|| <= b_s/K ||(N+1)^(s+3/2)psi||,
    b_s=(1+2^s)/sqrt(2), s>=0.

Annihilation does not increase the output number weight; creation increases
N+1 by at most a factor two. Linear combinations gain their coefficient l1 norm.
For two quadratures use

    A_K B_K - A B = (A_K-A)B_K + A(B_K-B).

The two constants are b_0 b_(3/2)=1+2sqrt(2) and b_(1/2)b_0=1+sqrt(2).
Hence 2+3sqrt(2) suffices for a quadratic product, times the two l1 norms.
For M=3|Lambda| modes, one sufficient constant in equation (6) is

    C_Lambda=(2+3sqrt(2))/2 [M + sum_rows ||C_row||_1^2].

For the supplied centered cubic curl with side >=3, each row has l1 norm two,
so C_Lambda=(5M/2)(2+3sqrt(2)). No optimization or volume uniformity is claimed.
This proves the displayed weighted estimate on the finite-particle core.
Fock cutoffs converge in the weighted norm, extending it to D((N+1)^2).

## 3. Self-adjointness, moment propagation and Duhamel

The symmetric quadratic H changes particle number by at most two and has norm
at most C(m+1) on the sector N<=m. Iteration bounds ||H^n psi|| by
C_psi^n (n+m)! for a finite-particle vector psi supported below m. Dividing by
n! gives a convergent analytic-vector series for sufficiently small positive
time. The dense invariant finite-particle domain therefore satisfies the
analytic-vector criterion for essential self-adjointness. Positivity passes
to the closure.

There is also a concrete finite-mode way to check the moment step. Diagonalize
the real symmetric matrix C orthogonally; the same orthogonal transformation
on Q and P preserves N. The Hamiltonian becomes a finite sum of independent
oscillators, including free coordinates for the zero eigenvalues. For
omega=|lambda|>0,

    Q(t)=cos(omega t)Q + sin(omega t)/omega P,
    P(t)=-omega sin(omega t)Q + cos(omega t)P;

for omega=0 these formulas are Q(t)=Q+tP and P(t)=P. The finite-dimensional
quadratic propagator preserves Schwartz vectors in the Schrödinger
representation; equivalently these formulas bound each finite polynomial
in Q,P applied to the evolved vector. Finite-particle vectors are Schwartz.
Therefore M_psi,T=sup_|t|<=T ||(N+1)^2 exp(-itH)psi|| is finite, including
zero-frequency coordinates. The occupation vacuum need not be an H-ground
state, and no normalizable free-particle ground state is assumed.

For fixed finite-particle psi, H_K is bounded, H is self-adjoint and the
canonical orbit is continuous in the necessary weighted domain. Differentiating
exp[-i(t-s)H_K] exp(-isH)psi and integrating gives

    sup_|t|<=T ||(exp(-itH_K)-exp(-itH))psi||
      <= C_Lambda T M_psi,T/K.

For K large enough psi belongs to the physical sector and its H_K trajectory
remains there. For normalized states, a bounded observable's expectation error
is at most twice its operator norm times this vector error. Strong convergence
alone does not give convergence of unbounded observables.

The same argument for a fixed linear combination F of Q,P proves the asserted
Weyl convergence, using a (N+1)^(3/2) bound. Fixed finite products of Weyl
operators and propagators can be telescoped with canonical intermediate
vectors on the right. Canonical Weyl and quadratic transformations preserve
Schwartz space and have finite number moments uniformly on compact parameter
sets. This supplies the required weighted bounds without assuming uniform
H_K-evolved number moments. The result stays at fixed volume, time horizon,
initial vector and finite list of smearing vectors.

## 4. Curl signs, zero modes and physical scope

The centered differences are real skew-symmetric and commute. The two
antisymmetries of epsilon_ijk and D_j make C real symmetric; div C=0. In the
canonical limit E=-P, B=CQ, giving [E_alpha,B_beta]=i C_beta,alpha and bracket
matrix [[0,C],[-C,0]]. Hamilton's equations are

    E_dot=C B, B_dot=-C E.

Thus magnetic divergence vanishes identically; electric divergence is conserved
but not selected by this construction. For a Fourier wave vector k, C(k) is
i[sin(k) cross], with eigenvalues 0,+|sin(k)|,-|sin(k)|. The E/B bracket has
rank four when sin(k) is nonzero. B has no longitudinal component because it
is a curl. At zero symbol, all associated free coordinates must be kept.
There is one zero momentum on odd side length, eight on even side length.

Expanding H_K gives coarse range at most two and at most two pair factors per
term. Its collective intra-block terms do not establish fine-lattice uniform
locality as K increases. The canonical gauge direction is a limiting statement;
finite-K quadratures have deformed commutators. No formation coupling, immutable
original-projector dynamics, electric-Gauss preparation, continuum uniqueness,
or microscopic photon identification follows.

## 5. Decisive controls and boundaries

`independent_check.py` constructs normalized symmetric occupation vectors
inside the full 4^K pair tensor product for K=1,2,3, checks all lowering/raising
intertwiners and all nine finite commutators exactly, and tests the weighted
coefficient inequalities at and above cutoffs K=1,2,5,11. It constructs actual
periodic spatial curl and divergence matrices for side 3 and 4; their exact
ranks are (52,26) and (112,56), with one and eight zero momenta respectively.

The numerical evolution control deliberately uses a one-cell diagonal positive
quadratic C=diag(1,0,1), not a simulation of the spatial cubic curl. It keeps the
actual shared-total-occupation cutoff and includes a free coordinate. For
K=2,4,8,16,32,64 the entire finite physical sector is included exactly. Canonical
cutoffs 80 and 100 disagree by at most 3.89e-15 on the selected vectors/times.
The observed scaled errors are bounded (largest K*error 6.122); this corroborates
the proved fixed-time bound but is not a proof of its rate or a uniform-time
claim. All 36 finite evolutions have zero measured leakage outside the physical
sector. The run completed with empty stderr and no failed attempt.

The source's analytic-vector receipt and author computations remain unopened
when this document is sealed. The argument above is an independent reconstruction
of the supplied claim, not a new candidate theorem replacing it.
