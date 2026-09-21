# Uniformly local two-qubit cells with a dilute quantum curl limit

**Status:** proposed conditional model and direct proof; author controls and
independent check pending. **Date:** 2026-09-21.

This construction supplies a fixed Hamiltonian on two qubits per cell. It
has bounded interaction range and strength, a positive energy and a unique
gapped product ground state. After removal of a specified carrier frequency,
its finite-particle quantum dynamics converges on an Euler time scale to curl
waves. The limit is not a gapless electromagnetic vacuum: the laboratory
spectrum remains gapped and the carrier-subtracted Hamiltonian has both signs.

The Hamiltonian changes local singlet/triplet content. It does not preserve
the original permanent classical record projectors, derive a clock, implement
the label-dependent classical rates, or couple the previous formation theorem
to quantum evolution. The two-qubit cell architecture and Hamiltonian are
additional supplied structures. The purpose is to test what a local quantum
realization can accomplish and to identify the remaining physical questions.

## 1. A fixed local Hamiltonian

Let Lambda_N=(Z/NZ)^3, N>=3, V=N^3. At each cell use the actual two-qubit
singlet |0> and Cartesian triplets |i>,i=1,2,3, as an orthonormal basis.
Define

    t_i=|0><i|, n=sum_i |i><i|, N_exc=sum_x n_x.

The cell has either vacuum or one triplet; this exclusion is an exact local
Hilbert-space property, not a bosonic approximation. Set c>0 and let

    D_j f(x)=[f(x+e_j)-f(x-e_j)]/2,
    C_N f = D cross f.

The real matrix C_N is symmetric. On a Fourier vector exp(i k.x),
C_N(k)=i[sin(k) cross], with eigenvalues 0,+|sin k|,-|sin k|.
In particular ||C_N||<=sqrt(3), uniformly in N. Specify

    H_N = mu N_exc
          + c sum_(x,i),(y,j) (C_N)_(x,i),(y,j)
                                  t_(i,x)^dagger t_(j,y),       (1)
    mu > c sqrt(3).

Only adjacent cells interact and every matrix entry is bounded by 1/2.
Each pair-cell factor is an operator on two physical qubits. The two-cell
terms are therefore at most four-qubit operators. The model is covariant
under proper cubic rotations of the cell lattice together with the physical
spin rotation of each pair. All coefficients are independent of N.

This is uniform locality on the supplied cell lattice. For a concrete fine
qubit-lattice embedding, place the active pair at 2x and 2x+e_1 in each
2-by-2-by-2 cube, leaving the other six qubits inactive. Terms then have
bounded fine-lattice support diameter at most three Manhattan steps. That
chosen packing is not a proof of the original one-site nearest-neighbor law
or of its rotation covariance: the packing itself selects a direction and
the interactions can act jointly on four qubits. Those distinctions remain
explicit even though the support bound is uniform.

## 2. Exact relation to free bosons and positivity

For each excitation number n, embed the physical n-excitation space
isometrically into the n-boson space over l^2(Lambda_N;C^3). Its image is the
subspace with at most one boson, of any component, at each cell. Denote its
orthogonal projection by P_N and Q_N=1-P_N. The physical hopping amplitudes
are exactly one, so

    H_N|_n = mu n + P_N dGamma(c C_N) P_N|_Ran(P_N).  (2)

This formula follows directly on the occupation basis: hopping into an
occupied cell is removed by P_N, while an allowed hop has the same unit
amplitude as t_x^dagger t_y. There is no claim of a projection of the entire
unitary group; the error in that replacement is estimated below.

Since ||dGamma(c C_N)||<=n c sqrt(3) on the n-particle sector, (2) gives

    H_N >= (mu-c sqrt(3)) N_exc >=0.                  (3)

The product of singlets is the unique ground state, of energy zero, and the
gap is at least mu-c sqrt(3). These statements hold for every finite N,
including all momenta and all excitation densities. The lattice momentum
zeros of the sine curl, including the eight zeros available when N is even,
remain present as carrier-frequency degeneracies; they are not discarded.

Because N_exc commutes with H_N, removal of the carrier is exact:

    exp(i mu t N_exc) exp(-it H_N)
      = exp[-it P_N dGamma(c C_N)P_N]                (4)

on the physical space. The right-hand generator is not positive. In
particular (3)-(4) do not derive a positive gapless photon energy by a change
of notation: the physical gap and rotating-frame choice must be retained.

## 3. Uniform collision estimate for finitely many Fourier modes

Fix a finite set S of distinct integer wavevectors, s=|S|, and a fixed
particle number n. Take N large enough that the wavevectors remain distinct
modulo N. Let E_N be the one-particle space spanned by all three polarizations
of exp(2 pi i q.x/N)/sqrt(V), q in S. Let psi_N be any normalized vector in
the symmetric n-fold tensor power of E_N; its coefficients in that fixed
mode basis are independent of N.

For the position projector A_x onto all three components at cell x, the
compression to E_N has operator norm s/V: there are three orthogonal
rank-one blocks, one for each component. Consequently the probability of
at least one coincident pair of particles is bounded by

    ||Q_N psi_N||^2
      <= sum_(a<b) sum_x <psi_N,A_x^(a) A_x^(b) psi_N>
      <= binom(n,2) s^2/V =: epsilon_N^2.            (5)

The first inequality is the union bound in the commuting position
projectors. In the second, on E_N tensor E_N each A_x tensor A_x has norm
(s/V)^2, and there are V cells. This bound holds for arbitrary entanglement
among the fixed Fourier modes. It is zero for n=0,1.

The free Hamiltonian L_N=dGamma(c C_N) preserves E_N and its n-particle
space because it changes only the three polarizations at a given momentum.
Equation (5) therefore holds uniformly for exp(-it L_N)psi_N, for all real
t. Set alpha_N=||P_N psi_N|| and use the normalized physical initial state

    phi_N=P_N psi_N/alpha_N,                         (6)

when epsilon_N<1. This state is a product of collective triplet-creation
operators with their exact physical normalization, or a finite superposition
of such products. Specifying it is an initial-state assumption. No preparation
from the earlier irreversible birth law is inferred.

## 4. Duhamel control through Euler times

Let U_hc(t)=exp(-it P_N L_N P_N) on Ran(P_N), and U_0(t)=exp(-it L_N).
Differentiate P_N U_0(t)psi_N and apply variation of constants on Ran(P_N):

    ||U_hc(t)P_N psi_N-P_N U_0(t)psi_N||
       <= integral_0^|t| ||P_N L_N Q_N U_0(u)psi_N|| du
       <= |t| n c sqrt(3) epsilon_N.                (7)

All operators in a fixed n-particle sector are bounded, so this argument
needs no domain or thermodynamic-limit assumption. Adding the missing Q_N
component and normalizing the initial state gives

    ||U_hc(t)phi_N-U_0(t)psi_N||
       <= epsilon_N [1+n c sqrt(3)|t|]+epsilon_N^2. (8)

Here the physical vector is compared in its bosonic occupation embedding,
and 1-alpha_N<=epsilon_N^2 justifies the normalization term. For t=N tau,
|tau|<=T, n and S fixed, (8) is O(N^-1/2) in three dimensions. It is a
sufficient estimate, not a measured or asserted optimal exponent. It gives
exact equality for n=0,1. The proof does not cover a fixed positive particle
density, a growing number of occupied Fourier modes, or arbitrarily long
scaled times.

In the same fixed mode basis,

    N c C_N(2 pi q/N) -> c i[(2 pi q) cross]

with operator error at most c |2 pi q|^3/(6N^2), from the scalar sine
remainder. A second, finite-dimensional Duhamel estimate therefore replaces
U_0(N tau) in (8) by the continuum-mode evolution with additional error

    n c T max_(q in S) |2 pi q|^3/(6N^2).           (9)

Equations (8)-(9) are a strong finite-particle quantum wave limit for the
explicit local Hamiltonian, with the carrier removed as in (4).

## 5. The noncommuting limiting fields

Define b_i(q)=V^-1/2 sum_x exp(-2 pi i q.x/N)t_(i,x). Exact local matrix
algebra gives

    [t_i,t_j^dagger]=delta_ij |0><0|-|j><i|,
    [t_i,t_j]=0.

On the sector with at most m excitations this implies, for all q,q' in S,

    ||[b_i(q),b_j(q')^dagger]-delta_ij delta_(q,q')||
       <= 2m/V,                                    (10)

with the norm restricted to that sector. The identity follows by summing
the Fourier phase of |0><0|=I-n; the norm of a sum of phased operators
acting only on occupied cells is at most m. No independence or classical
probability approximation is used here. Thus the limiting mode algebra is
bosonic, with canonical quadratures Q=(a+a^dagger)/sqrt(2),
P=i(a^dagger-a)/sqrt(2) for real spatial smearings.

Under the carrier-subtracted continuum generator dGamma(c curl),

    d_t Q=c curl P,        d_t P=-c curl Q.          (11)

These are quantum curl waves with an onsite canonical commutator. Their
rotating-frame quadratic energy has both helicity signs, consistently with
the earlier onsite-bracket calculation. In the laboratory frame the carrier
term mu N_exc restores (3), the gap and the rapid phase. Equations (10)-(11)
are not the derivative electromagnetic bracket of the positive block model.

The fixed-particle strong estimate transfers matrix elements of bounded
observables under the stated embedding. Equation (10) gives the algebraic
CCR limit on a finite-particle core. A general finite-density interacting
quantum fluctuation theorem or a uniform bound for all unbounded field
moments is not being inferred from these two statements.

## 6. What this resolves and what remains

This supplies actual qubits, uniform finite-range interactions, a positive
microscopic Hamiltonian, noncommuting dilute fields and a controlled Euler
curl limit within one declared model. It shows that growing collective
blocks are not necessary for that particular combination of conclusions.

It leaves the permanent-record interpretation, admissible microscopic law,
state preparation, positive gapless vacuum energy, electric constraint,
extra lattice branches, and coupling to matter or geometry unproved. The
carrier is a specified parameter, not a derived physical frequency. These
open obligations distinguish a concrete quantum transport model from a
completed TOE or a derivation of quantum electromagnetism.
