# Native pair stabilization, ground-space packing, and controlled deformations

**Status:** conditional discovery with exact operator proofs and one bounded
author check. Independent checking is pending. This is not a formal audit,
premise adoption, PR proposal, or proof of a gravity phase.

A cubic-symmetric **three-body density interaction** stabilizes the specified
collective-pair law on the entire physical-qubit carrier at its simultaneous
pair closing, while vanishing identically on all zero-, one-, and two-particle
states. The proof is an exact sum of squares plus a nonnegative polynomial
of integer occupation numbers. It needs no harmonic replacement.

The stabilized model has an extensive family of compact-pair ground states.
A natural chemical-potential scan has an exact discontinuous density-onset
bound. Positive pair hopping removes the flat two-particle bands but gives
five quadratic branches. A uniform on-site rotation gives a finite-density,
number-nonconserving description with the same spectrum. These discriminate
several concrete routes without assuming a tensor phase.

## 1. Source and premise boundary

The complete `independent-native-route/REPORT.md` and
`independent-native-check/REPORT.md` were read before constructing the
stabilizer. Their exact pair operators and unrestricted hard-core carrier
are retained. Main remains `e75578f7136401d4bd750131671aed9212c06291`; selected
campaign procedure is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Relevant
path identities and coverage are in [SOURCES.json](SOURCES.json). Actual
read-only PR checks returned unchanged heads for PR9363
`fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`, PR9285
`146e33463ea70c3b802bc5be8084f38de9078e13`, and PR9287
`b484be7728741fe37efa1af4eee2e01a723337d5`.

The current axiom memo, primitive registry, and all three primitive notes
were refreshed. They supply no chosen basis, tensor-product quantum state,
Hamiltonian, coupling, ground-state selection, Born readout, or record
instrument for this construction. One ordinary `C²` per physical vertex,
the common number axis, Hamiltonian time, and the following law remain
explicitly supplied. No oscillator, link-role qubit, additional local slot,
or continuous field is introduced.

The actual native virtual-pair ring source was read in full. Its supplied
edge carrier, incident anticommutation and perturbative Schur construction
are different from this commuting physical-site hard-core carrier; its
ring coefficient and spectral bound are not imported. PR9363's actual
finite-slot harmonic tensor argument was read with its carrier/analytic
quadratic-form hypotheses; it expressly leaves strongly correlated and
one-qubit-per-site models open. It is not an exclusion premise here.
Searches for local stabilizers, three-body terms, localized pairs and
sum-of-squares mechanisms found no matching construction in the inspected
main/proposal sources. The actual three-neighbor normalizer note concerns
conditional formation probabilities, not this Hamiltonian stabilization.
This is a bounded prior-source search, not an exhaustive novelty claim.

## 2. Fixed physical-site law

Use a cubic periodic torus of side `L>=5`, with volume `V=L³`, or finite
particle forms on `Z³`. At each physical vertex,

\[
 b_x=|0\rangle\langle1|_x,\qquad n_x=b_x^\dagger b_x,\qquad
 n_x^2=n_x,\quad b_x^2=0,
\]

with different-site factors commuting. Put

\[
 d_i(x)=b_{x+e_i}b_{x-e_i},\quad a_i(x)=b_{x+e_i}-b_{x-e_i},
\]
\[
 Q_{E1}=(d_1-d_2)/\sqrt2,\quad
 Q_{E2}=(d_1+d_2-2d_3)/\sqrt6,\quad
 Q_{Tij}=a_i a_j/2.
\]

Write `P_E(x)=sum_(A in E) Q_A(x)†Q_A(x)` and similarly `P_T`.
The supplied original law is

\[
 H(\mu,g_E,g_T)=\mu N-g_E\sum_xP_E(x)-g_T\sum_xP_T(x),\quad
 N=\sum_xn_x,
\]

with positive `mu` and nonnegative attractive couplings. The simultaneous
closing is `g_E=2mu,g_T=mu`. The local five-component cubic representation
and exact two-particle Gram/bands have focused independent coverage in the
preceding native check. Their key identities are re-used explicitly below.

## 3. An unrestricted operator completion of squares

Define a graph on the *same physical vertices* by its eighteen displacements

\[
 \mathcal D=\{\pm2e_i\}\cup\{\pm e_i\pm e_j:i<j\},\qquad
 m_x=\sum_{d\in\mathcal D}n_{x+d}.                                  \tag{1}
\]

This graph records the possible endpoints of the original pair words; it is
not an extra carrier or a newly adopted adjacency axiom. It is translation-
and proper-cubic-covariant. Each axial opposite pair has one shell center,
and each orthogonal-axis pair has two shell centers, for every stated torus.
No displacement or neighbor in (1) aliases another when `L>=5`.

Let `D(x)=d_1(x)+d_2(x)+d_3(x)`. For a plane `ij`, enumerate its four signed
pair words as

\[
 v_{ij}^{st}(x)=st\,b_{x+s e_i}b_{x+t e_j},\qquad s,t=\pm1,
 \qquad Q_{Tij}(x)=\tfrac12\sum_{s,t}v_{ij}^{st}(x).
\]

Define the full-carrier positive operator

\[
 \mathcal A=\frac{2\mu}{3}\sum_xD(x)^\dagger D(x)
 +\frac\mu4\sum_{x,i<j}\sum_{a<b}
       (v_{ij}^a-v_{ij}^b)^\dagger(v_{ij}^a-v_{ij}^b).                \tag{2}
\]

There are six differences for each four-word plane and nineteen squares
per center in total. The following identities require no commutation
between overlapping pair operators:

\[
 P_E=\sum_i d_i^\dagger d_i-\tfrac13D^\dagger D,
\]
\[
 \sum_{a<b}(v_a-v_b)^\dagger(v_a-v_b)
       =4\sum_a v_a^\dagger v_a-(\sum_a v_a)^\dagger(\sum_a v_a).
\]

Normal ordering is exact: `d_i†d_i=n_(x+ei)n_(x-ei)` and
`v_a†v_a` is the corresponding pair of distinct number projectors.
Counting the one or two centers gives

\[
 \mathcal A=2\mu\sum_{\{x,y\}\in G}n_xn_y
                  -2\mu\sum_xP_E(x)-\mu\sum_xP_T(x).
\]

Thus at the closing, on the entire finite tensor-product Hilbert space,

\[
                   H=\mathcal A+\mu\sum_xn_x(1-m_x).                \tag{3}
\]

Equation (3) preserves all interference and hard-core exclusions. It is not
a two-particle identity extrapolated to higher number.

## 4. Two explicit stabilizers, with an all-volume proof

The low-degree choice is

\[
 V_3=\mu\sum_x n_x\binom{m_x}{2}
     =\mu\sum_x\sum_{\{y,z\}\subset x+\mathcal D}n_xn_yn_z.        \tag{4}
\]

The equality follows from `n_y²=n_y`. Every triple has three distinct
physical sites. There are 153 unordered neighbor pairs per center, each
with positive coefficient. Consequently `V3>=0`, it is exactly zero as an
operator on the complete `N<=2` sectors, and it is finite range: radius two
from its center and maximum interaction diameter four in lattice units.
It is invariant under translations and every proper cubic rotation.

Since `n_x` commutes with `m_x` and the latter has integer spectrum
`0,1,...,18`, (3) becomes

\[
 H+V_3=\mathcal A+
        \frac\mu2\sum_x n_x(m_x-1)(m_x-2)\ \ge\ 0.                \tag{5}
\]

The diagonal polynomial has values `1,0,0,1,3,...` after division by two.
It is nonnegative on the exact occupation spectrum. Replacing `m_x` by a
continuous mean-field variable would lose this proof. Equation (5) proves
positivity on every finite torus `L>=5`, without a thermodynamic
approximation or a fixed-number restriction.

A second, pointwise smaller choice is

\[
 V_{\rm cap}=\mu\sum_xn_x(m_x-1)_+,
 \qquad H+V_{\rm cap}=\mathcal A+
              \mu\sum_xn_x\mathbf1_{m_x=0}\ge0.                   \tag{6}
\]

Here the function is the exact finite-spectrum functional calculus of the
19-site star. It can equivalently be written as a finite polynomial of
number projectors. It is still local, cubic, positive, and zero on `N<=2`;
its expansion can contain terms beyond three-body order. For every integer
`m`, `binom(m,2)>=(m-1)_+`. It is smaller only in this explicit diagonal
comparison; no globally minimal stabilizer is claimed.

For the positive-coupling family, an `N<=2`-preserving stabilizer making the
vacuum a full-carrier ground state exists **if and only if**

\[
                         g_E\le2\mu,\qquad g_T\le\mu.              \tag{7}
\]

Sufficiency follows by using the same (4) and adding the positive differences
`(2mu-gE) sum PE+(mu-gT) sum PT` to (5). Necessity follows from the actual
two-particle eigenvectors: their energies include `2mu-gE` and
`2mu-2gT` at zero momentum, where the Gram vectors are nonzero. An interaction
which is identically zero on that sector cannot lift a negative energy
there. This is a complete existence statement for this specified
sector-preserving stabilization problem, not a classification of all native
Hamiltonians or their phases.

## 5. Exact ground states and a density-onset bound

At the closing, every compact vector `Q_EA(x)†Omega` has zero energy: its
two-particle pair center is unique and its opposite-pair coefficients sum
to zero. Put centers on `5Z³` in a torus with side divisible by five. Shells
from distinct centers are disjoint, and no endpoint of one is a graph-G
neighbor of an endpoint of another: their minimum possible separating
coordinate is three, whereas (1) has maximum coordinate two.

At each chosen center independently take local vacuum, `E1`, or `E2`. Every
product is an exact zero vector of `H`, `V3`, and `Vcap`. In every occupation
word of such a product, each occupied site has exactly one graph-G neighbor;
the other two-particle annihilators cannot use endpoints from different
clusters. The two normalized local E states and local vacuum are orthogonal.
Therefore

\[
                 \dim\ker(H+V_3)\ \ge\ 3^{V/125}.                 \tag{8}
\]

Every even particle number from zero through `2V/125` occurs among these
ground states. The density `2/125` is a conservative packing bound, not a
maximum ground-state density or a ground-space classification.

This degeneracy is robust for a broader reason. Suppose any finite-range
Hamiltonian `H'` is positive, agrees with `H` on the complete `N<=2` sectors,
and is supplied uniformly on the lattice. Separate the compact pair clusters
by more than its interaction diameter. Each local term sees at most one
cluster. Its expectation in a packed product therefore sums the single-pair
expectations, with the repeated vacuum expectation subtracted. Each total
is zero because the isolated pair and vacuum energies are zero. Positivity
then forces the packed product itself into `ker H'`. This argument does
not require every term of `H'` to be positive or require number conservation.
For any fixed finite interaction range it again gives exponentially many
ground states at a positive, possibly smaller packing density.

Thus a finite-range stabilizer preserving all two-particle data cannot
remove the compact zero-pair ground states. This limits the proposed
empty-reference interpretation; it does not rule out a different dense
ground-state component or every possible tensor phase of another law.

The following one-parameter family sharpens the phase information without
guessing a phase. Define the dimensionless positive closing operator `F` by
`F=(H+V3)/mu` at `gE=2mu,gT=mu`. For `g>0`, take the actual law

\[
 H_{\mu,g}=\mu N-2g\sum P_E-g\sum P_T
                +g\sum_xn_x\binom{m_x}{2}
           =gF+(\mu-g)N.                                          \tag{9}
\]

If `mu>g`, its unique ground state is vacuum and its exact spectral gap is
`min(mu,2(mu-g))`, uniformly in volume. The one-particle sector has energy
`mu`; every `N>=2` sector lies above `N(mu-g)`; a compact E pair realizes
`2(mu-g)`. For `g>0` the two-particle minimum has multiplicity `2V+3L` on
odd sides and `2V+6L` on even sides: the two E channels give `2V`, and each
T channel has `Sij=2` at `qi=qj=0` (also `qi=qj=pi` for even sides), with
free third momentum. The one-particle energy has multiplicity `V`; the
two gaps coincide when `g=mu/2`. If `mu=g`, (8) applies. If `0<mu<g`, a
maximally packed trial product gives

\[
 E_0\le-(g-\mu)\frac{2V}{125},\qquad
 H_{\mu,g}\ge-(g-\mu)N.
\]

Hence every ground state satisfies `〈N〉/V>=2/125` on this volume subsequence.
The onset across `mu=g` has a discontinuous lower bound on ground-state
density; it is not an inferred dilute continuous condensation. No value
for the actual dense ground energy, broken symmetry, order parameter,
excitation dispersion, or universality class follows from these bounds.

For another exact discriminator, a spatially uniform spin-coherent product
with site occupation `rho` has, at the closing,

\[
 \langle2P_E+P_T\rangle=8\rho^3-\rho^4,\qquad
 \langle H+V_3\rangle/V=\mu(\rho+145\rho^3+\rho^4).                \tag{10}
\]

It has positive energy for every `rho>0`. The explicitly packed zero-energy
states are correlated pairs, not such a uniform product condensate. This
variational comparison does not classify entangled finite-density states.
On the infinite lattice and even tori, the original stabilized law also
factorizes between the two parity sublattices, conserving their numbers
separately. No associated Goldstone theorem or mode count is assumed.

## 6. A native deformation which changes the flat sector

Supply positive pair-hopping squares on the same physical carrier,

\[
 W_\tau=\tau\sum_{x,i,A}
 [Q_A(x+e_i)-Q_A(x)]^\dagger[Q_A(x+e_i)-Q_A(x)],\qquad\tau>0.       \tag{11}
\]

The channel sum is invariant under cubic rotations; the three positive
directions give the undirected translation-invariant gradient form. This
term is number conserving, quartic, has interaction diameter at most three,
and is positive on the full hard-core carrier. It breaks the separate
parity-sublattice number conservation by allowing pair transfer, while
preserving total number. It changes the two-particle sector, so it is a
declared change of law beyond the stabilization target (4).

Let `ell(q)=2 sum_i(1-cos q_i)` and
`S_ij(q)=1+cos q_i cos q_j`. The exact, non-null pair bands of
`H+V3+Wtau` at the closing are

\[
 \epsilon_{E1,E2}=\tau\ell(q),\qquad
 \epsilon_{Tij}=\mu(2-S_{ij}(q))+\tau\ell(q)S_{ij}(q).              \tag{12}
\]

This follows by applying the same exact pair-frame outer products as the
original two-particle derivation, with the additional multiplier `ell`.
The orthogonal complement still has energy `2mu`. A vanishing Gram vector
is still a zero vector, not a band state. Near zero momentum all five
branches are quadratic:

\[
 \epsilon_E=\tau|q|^2+O(q^4),\qquad
 \epsilon_{Tij}=\tfrac\mu2(q_i^2+q_j^2)+2\tau|q|^2+O(q^4).         \tag{13}
\]

Thus a genuine finite-carrier deformation makes the flat pairs mobile and
keeps global positivity, but does not produce two linear tensor modes.
Adding an on-site mass for all three T channels could leave two E channels
gapless, but on the z axis the formal TT pair is `E1,T12`, not `E1,E2`.
That would not establish the desired tensor polarizations either.

There is also a full-carrier zero-state statement, stronger than the band
calculation. On the infinite-lattice vacuum Hilbert space, any zero-energy
vector with bounded particle number must be killed by every square in
(11). Hence `Q_A(x)psi` is independent of `x`. The sum of its squared norms
over `x,A` is finite: Cauchy–Schwarz bounds each by a finite sum of occupied
pair projectors, and each site enters finitely many words. The constant
vector must therefore be zero. All attractive terms then annihilate `psi`,
and zero energy requires `〈mu N+V3〉=0`, forcing vacuum. This removes the
compact ground-state degeneracy in the finite-particle representation.
It is not a finite-volume uniqueness assertion: the q=0 two-particle waves
are normalizable zero states on each finite torus. It is also not a theorem
about finite-density infinite-volume states.

## 7. Non-number conservation and the record boundary

A uniform on-site rotation is a useful exact control. With
`Utheta=product_x exp(-i theta Y_x/2)`, define
`Htheta=Utheta(H+V3)Utheta†`. It is local, cubic-symmetric, positive, and
uses exactly the same qubits. Its rotated vacuum has physical occupation
`sin²(theta/2)`. For a generic rotation it does not conserve the original
`N`, although it conserves `Utheta N Utheta†`. Its spectrum, compact
degeneracy and flat/quadratic branches are unchanged. Finite density and
nonconservation of the original number label alone do not supply linear
tensor propagation. This is a unitarily equivalent control, not a claim
about all non-number-conserving interactions.

The fixed instantaneous occupation-readout obstruction from the two native
reports remains: the two states `(d1†±d2†)Omega/sqrt2` have identical
occupation distributions and different `P_E` expectations. The stabilizer
is zero throughout their sector and does not change this fact.

A concrete temporal protocol illustrates the boundary without claiming a
framework record law. In the supplied Hamiltonian/Born measurement model,
the opposite-pair singlet `u=(d1†+d2†+d3†)Omega/sqrt3` has energy `2mu`, while
the E doublet has energy zero. Evolve the two states under `H+V3` for
`t=pi/(2mu)` and then perform the supplied occupation measurement. The minus
state stays in the first two pair words. For the plus state the final
probabilities on `(d1,d2,d3)` are `(1/18,1/18,8/9)`. Thus the third pair
occurs with probability zero versus `8/9`: the known native dynamics can
convert this relative phase into distinguishable occupation data.

This does not identify occupation measurement with the framework's
permanent readable records, derive its instrument or probabilities, select
the waiting time, or close a gravitational observable bridge. It shows
exactly why the single-time fixed-readout witness must not be promoted to
an exclusion of all temporal protocols. No original record-birth instrument
is replaced or claimed reproduced here.

## 8. Checks, exact scope, and next discriminating lemma

[check_stability.py](check_stability.py) is the single priced sparse job for
this route. It imports no prior implementation. It checks the full 64-state
six-qubit matrix identity behind (2)–(3), all 24 rotations, all nineteen
degree values, graph multiplicities on `L=5,6,7`, and the literal global
action on a coherent eight-particle state with 54 occupation words on
1,000 physical qubits. That state has exactly zero residual under both
the original closing Hamiltonian and `V3`. It also checks (10) using exact
rational-amplitude product vectors. All assertions completed; actual
runtime was 0.867s and peak RSS 24,444,928 bytes, below the priced 100MB/30s.
Only integers and `Fraction` arithmetic are used.

The deadline and absent stop sentinel were checked before the script. BLAS
and OpenMP thread counts were set to one. No dense many-body diagonalization,
unmanaged worker, source mutation, PR, or audit was run. The all-volume
conclusions come from the operator identities and geometric incidence proof,
not extrapolation from these three tori. [results.json](results.json) and
[results.log](results.log) preserve the actual checks. Equations (8)–(13),
the general packing argument, the on-site rotation control, and the temporal
readout probabilities have analytic proofs here; they were not separate
large numerical experiments.

Family tuple: **(full physical-qubit collective-pair Hamiltonian;
pair-word sum of squares and integer occupation positivity;
all-volume stabilization followed by ground-space and phase discrimination)**.
The all-volume stability lemma requested by the parent report is closed
conditionally, with no axiom change. Its strength is **strictly weaker**
than the desired finite-density two-linear-tensor phase and readable-record
bridge. The existence of a gravity phase has not been deduced.

An attainable next lemma is the finite-density coercivity question for the
explicit mobile model (11): for fixed positive `mu,tau`, does there exist
volume-independent `c>0` such that

\[
 H+V_3+W_\tau\ \ge\ c\,\frac{N(N-2)}{V}
 \quad\hbox{on every sufficiently large torus}?                    \tag{14}
\]

The two-particle zero modes are explicitly respected by `N(N-2)`. A proof
would separate all fixed positive densities from the vacuum ground energy
and rule out the packed zero-energy coexistence of (8) in this deformed
law. An exact higher-number zero state would refute it. Neither possibility
is assumed. This is a concrete full-carrier operator question, smaller than
the target and amenable first to carefully priced sparse fixed-number
tests. Classifying the common kernel of (2),(5),(11) is a second precise
route to it; the current finite-particle argument is not a uniform-density
bound.

The stronger terminal requirement remains a separately specified native
law and state with exactly two linear tensor excitations, controlled extra
gapless content, a genuine record instrument and common source/action
identification. Supplying that conclusion as an “emergent tensor phase”
would be target-equivalent. The present construction instead retires one
specific full-carrier stability gap and exposes exact degeneracy and
dispersion tests for further work. Independent checking is required before
substantial downstream reuse.
