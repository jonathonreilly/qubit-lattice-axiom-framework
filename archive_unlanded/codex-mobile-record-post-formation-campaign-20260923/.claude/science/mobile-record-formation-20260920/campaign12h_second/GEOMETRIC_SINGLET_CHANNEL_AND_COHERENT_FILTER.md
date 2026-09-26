# Quantum channels for a matching-to-singlet conversion

2026-09-21. Root conditional derivation; independent check pending.

The signed-fiber construction supplies a linear map from orthogonal matching
labels to physical singlet coverings. A linear map alone is not a normalized
quantum operation. This note identifies both a trace-preserving realization
on basis preparations and a coherent heralded realization, and distinguishes
their input requirements. It does not add either operation to the record
axioms or claim that classical birth dynamics prepares its coherent input.

## 1. Spaces and the checked overlap

Let Omega be the nearest-neighbor perfect matchings of a finite bipartite
graph with K vertices per part. Let H_M have orthonormal basis |M>, M in
Omega. This is an auxiliary matching-label Hilbert space, not one qubit at
each lattice site. On the 2K physical qubits, |D_M> is the normalized product
of singlets oriented from black to white along M. Define

    D |M> = |D_M>,       G=D^dagger D.

The previously calculated overlap is

    G_(M,P) = 2^(ell(M,P)-K),                             (1)

where ell counts transition-graph loops, including doubled common edges.
It is strictly positive for every pair M,P, and G_(M,M)=1. None of the
channel arguments below assumes that D is injective. They use only the
normalized pure outputs and the nonzero pairwise overlaps. The signed
microscopic-fiber map had an additional common sqrt(K!) factor; here that
factor has been removed explicitly so every D column has norm one.

## 2. The trace-preserving channel with these exact basis outputs

Suppose a finite-dimensional completely positive trace-preserving map E
has Kraus operators L_a and satisfies

    E(|M><M|)=|D_M><D_M|              for every M.         (2)

Because the output in (2) has rank one, each Kraus image must lie on that
same ray: L_a|M>=c_(a,M)|D_M>. Trace preservation gives

    delta_(M,P) = sum_a <M|L_a^dagger L_a|P>
                = G_(M,P) sum_a conjugate(c_(a,M)) c_(a,P).

For M!=P, (1) therefore forces the coefficient inner product to vanish.
Taking its conjugate in the off-diagonal channel action gives

    E(|M><P|)=0,   M!=P.

For M=P the coefficients have squared norm one. Thus the channel is unique
on this input space and is exactly

    E(rho)=sum_M rho_(M,M) |D_M><D_M|.                   (3)

It exists: the operators L_M=|D_M><M| satisfy sum L_M^dagger L_M=I.
Equation (3) discards coherence between matching labels. It does not say
that its physical outputs are separable across lattice sites: each covering
contains entangled singlets. As a map from the auxiliary matching input to
the physical output it is a measure-and-prepare channel and cannot transmit
entanglement with a reference attached to that input.

For two coverings with overlap g in (0,1), the uniform matching superposition
is sent to the equal incoherent mixture. The normalized coherent sum is

    |psi_+>=(|D_1>+|D_2>)/sqrt(2+2g).

The mixture has eigenvalues (1+g)/2 and (1-g)/2 in the normalized sum and
difference directions. Its trace distance from |psi_+><psi_+| is (1-g)/2.
On one square g=1/2, so the distance is exactly 1/4. This is a controlled
distinction between two specified preparations, not an obstruction to
preparing |psi_+> by another quantum operation.

## 3. The optimal scalar coherent success operation

A different supplied instrument can preserve the coefficients coherently
on a heralded successful outcome. Let its success Kraus operator be

    L_success = a D.

It is trace nonincreasing exactly when |a|^2 G<=I. Hence the largest allowed
coefficient is |a|^2=1/lambda_max(G), and for a normalized input |c> its
success probability is

    p_success(c)=<c|G|c>/lambda_max(G).                 (4)

Conditioned on success, the physical pure output is D|c>/||D|c>|| when
that vector is nonzero. A failure operator sqrt(I-G/lambda_max) completes
the instrument into a trace-preserving map with a distinct failure output
space. This is an explicit finite-dimensional construction. No local
implementation or efficient preparation of |c> is inferred from it.

Any collection of declared success Kraus operators a_r D has the same
bound with sum_r |a_r|^2 replacing |a|^2. Thus splitting the same coherent
map into several herald labels does not improve (4). The statement here
concerns this amplitude-preserving map; arbitrary success maps with changed
target coefficients are outside its premises.

Every basis input has success probability 1/lambda_max(G). However an input
in the top eigenspace of G succeeds with probability one. Since G has
strictly positive entries, its top eigenvector can be chosen strictly
positive. This explicitly preserves an alternative route: a specially
prepared coherent matching state need not pay the small basis-input
probability. Preparing that state and implementing the map remain separate
microscopic obligations.

For |+>=|Omega|^(-1/2)sum_M |M>, (4) is

    p_success(+) = [sum_(M,P) G_(M,P)]
                     /[|Omega| lambda_max(G)].          (5)

If all row sums of G coincide, |+> is a top eigenvector and the success
probability is one. This happens on an isolated square and on a product
of independent squares. Equations (2) and (5) do not conflict: the coherent
instrument is deterministic on that selected input, whereas (2) demands
deterministic exact pure-covering outputs on every basis input.

## 4. An exact tiled-square bound on a cubic torus

For even N, partition the cubic torus into P=N^3/4=K/2 disjoint elementary
xy plaquettes. Their z layers are separate. On each plaquette choose either
of its two internal dimer coverings and use no bond joining plaquettes.
All 2^P choices are valid full matchings of the original cubic graph.

The Gram principal submatrix for this subset is exactly

    [[1,1/2],[1/2,1]] tensor-power P.

Its largest eigenvalue is (3/2)^P. Extending its normalized top vector by
zero to the other full matchings and using the Rayleigh principle gives

    lambda_max(G_all) >= (3/2)^(K/2).

Therefore the coherent scalar conversion of Section 3 has, on each matching
basis state, success probability bounded by

    p_success(M) <= (2/3)^(K/2).                        (6)

The result uses a subset of actual cubic matchings and no asymptotic
matching-count estimate. It is a bound for the stated uniform coefficient
map on basis inputs. It is not a bound on (5), on its specially prepared
top-eigenvector input, on an arbitrary RVB preparation algorithm, or on an
effective low-energy theory.

The square-product example makes that restriction decisive: it saturates
the exponential basis-input probability (6), yet its uniform coherent input
succeeds with probability one. Reporting (6) as a universal exponential
cost of producing an RVB state would be incorrect.

## 5. Relation to the TOE lane and open alternatives

The concrete gain is a correctly normalized quantum-operation interface
for the earlier linear singlet map. Three objects remain different: the
classical probability law of geometric matchings, a coherent vector in the
auxiliary matching space, and a physical multi-qubit singlet state. A
classical mixture can be converted by (3); the desired coherent sum requires
additional coherent input or a different state-preparation mechanism.

Several alternatives remain open under explicitly changed premises:

* Directly prepare a particular physical coherent state. A channel promised
  only on one input is not constrained by (2) on every basis state.
* Use the coherent success operation with a top-eigenvector or other
  favorable coherent input. Its success probability is state dependent.
* Keep orthogonal physical marker degrees of freedom. If the intended
  outputs are orthogonal, the nonzero-overlap step in Section 2 fails and
  coherence can be transferred isometrically to the enlarged system.
* Change the output states, permit approximation, or derive a local
  Hamiltonian preparing a low-energy state directly. None is covered by
  the exact basis-output premise or the scalar map in Section 3.

Approximation has not been excluded; neither has a microscopic mechanism
for quantum entanglement. This note does not establish that the supplied
record dynamics implements any channel above. No Born rule, local spin
Hamiltonian, quantum photon, or theory of everything follows. The earlier
finite singlet/Klein calculations and the present channel result require
their own independent checks before a publication milestone is claimed.
