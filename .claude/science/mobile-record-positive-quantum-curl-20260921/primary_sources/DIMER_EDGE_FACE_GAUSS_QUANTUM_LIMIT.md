# Positive qubit blocks, edge-face curl, and a controlled electric constraint

**Status:** proposed conditional construction and direct proof; author controls
and independent check pending. **Date:** 2026-09-21.

This replaces the centered cell-vector curl of
`DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md` by the incidence curl on oriented
edges and faces. The resulting positive Gaussian Hamiltonian has two
transverse oscillator polarizations at each nonzero momentum and no extra
Brillouin-zone frequency zeros. A simultaneous block-size and squeezing
limit prepares the zero-charge, zero-global-flux observable sector, with a
quantitative bound for finite words of bounded field Weyl operators.

The microscopic qubits, Hamiltonian, block architecture and correlated initial
states are supplied. Collective couplings still lack a uniform fine-lattice
range as block size grows; original permanent record projectors and the birth
law are not preserved or derived. The limit fixes the coarse spatial volume
and time interval. It is not a joint spatial continuum limit, an interacting
gauge theory, or a derivation from the record axioms.

## 1. Cubical incidence operators

On the periodic cubic cell complex Lambda_L, L>=3, V=L^3, let vertex, edge,
face and cube cochains have their ordinary Euclidean inner products. There
are V vertices, 3V positively oriented edges, 3V positively oriented faces,
and V cubes. Use the right-hand orientation for the three face types.

Write D_j^+ f(x)=f(x+e_j)-f(x). With the usual basepoint conventions,

    (d_0 f)_j=D_j^+ f,
    (C A)_i=sum_(j,k) epsilon_ijk D_j^+ A_k,
    d_2 B=sum_j D_j^+ B_j.                           (1)

These real incidence matrices satisfy

    C d_0=0,           d_2 C=0.                      (2)

They follow by commuting the forward differences, not by approximating a
continuum identity. C need not be symmetric. Its adjoint C^T is the correct
map from faces to edges in the electric equation. This distinction is
essential: replacing C^T by C would generally destroy energy conservation.

At k_j=2 pi n_j/L set d_j=exp(i k_j)-1 and lambda(k)=sum_j |d_j|^2. Then

    C(k)=[d cross],
    C(k)^dagger C(k)=lambda I-d d^dagger,
    lambda(k)=4 sum_j sin^2(k_j/2).                   (3)

For k!=0 modulo 2pi, C has rank two and its two nonzero singular values are
sqrt(lambda). The only zero of lambda in the Brillouin torus is k=0,
including for even L. Thus

    rank C=2V-2, dim ker C=V+2,
    ker C = im d_0 plus the three harmonic edge fields. (4)

The sum in (4) is orthogonal. Let T=(ker C)^perp=im C^T and Z=ker C.
This is a fixed finite-dimensional real orthogonal decomposition of the edge
space. The corresponding face image im C contains divergence-free faces
with zero harmonic flux; its dimension is 2V-2. Harmonic flux sectors are
not silently included in this image.

These incidence constructions are standard discrete differential-form
machinery. Stern, Tong, Desbrun and Marsden, arXiv:0707.4470, is contextual
literature for that machinery; only its abstract was consulted for this note.
All identities and bounds used here are derived explicitly rather than
importing a theorem from that paper or asserting this discretization is new.

## 2. Positive canonical dynamics and its physical observable sector

Put canonical real coordinates (Q_e,P_e) on edges and define

    H=(P^T P+Q^T C^T C Q)/2,
    E=-P on edges,        B=CQ on faces.             (5)

The finite-mode positive quadratic Hamiltonian has its usual self-adjoint
closure on Fock space. The analytic-vector argument and checked criterion
in the earlier block note apply with C^T C in place of C^2. Directly,

    E_dot=C^T B,         B_dot=-C E,
    [E_e,B_f]=i C_fe,    [E,E]=[B,B]=0.              (6)

The energy is conserved since the two terms cancel using the adjoint. The
magnetic constraint d_2 B=0 is an operator identity. Electric divergence
d_0^T E is conserved, because d_0^T C^T=0.

For the zero-charge and zero-harmonic-electric-flux sector, quantize only the
real canonical coordinates in T. On that reduced Hilbert space,

    E_T=-P_T, B_T=CQ_T, H_T=(P_T^2+Q_T^T C^T C Q_T)/2. (7)

The electric and magnetic constraints and the two zero harmonic fluxes then
hold as observable identities. The reduced Hamiltonian is a positive
oscillator Hamiltonian with 2V-2 canonical modes. At each nonzero momentum
there are two equal frequencies sqrt(lambda(k)). Its Gaussian ground state
exists at this fixed L; its additive zero-point energy can be subtracted
when identifying an energy reference. No nonnormalizable equation P_Z psi=0
has been imposed on a vector in the unreduced Hilbert space.

The unreduced E,B algebra has central electric directions in Z. Choosing
their zero value and zero magnetic harmonic flux is a sector choice. Other
fixed flux values can be treated separately, but are not derived by (7).

## 3. Actual finite-qubit link blocks

For each positive edge e place K pairs of qubits. In every pair retain the
two-dimensional subspace spanned by the singlet |0> and the Cartesian
triplet |t_e> polarized along the oriented edge. Retain the symmetric
subspace of the K pairs on that edge. Its basis is |n_e>,0<=n_e<=K.
The remaining pair states and nonsymmetric sectors are not used by the
declared initial state; the operators below preserve the specified sector.

Define

    a_(e,K)=K^-1/2 sum_(ell=1)^K |0><t_e|_(e,ell),
    a_(e,K)|n>=sqrt[n(1-(n-1)/K)] |n-1>.

On a common edge-boson Fock space the exact extension is

    a_(e,K)=f_K(N_e)a_e, f_K(n)=sqrt(max(1-n/K,0)),
    Q_(e,K)=(a_K+a_K^dagger)/sqrt(2),
    P_(e,K)=i(a_K^dagger-a_K)/sqrt(2).              (8)

The physical subspace Pi_K={N_e<=K for every edge} is reducing. Supply the
finite-qubit Hamiltonian and observables

    H_K=[sum_e P_(e,K)^2+sum_f (C Q_K)_f^2]/2 >=0,
    E_K=-P_K,             B_K=C Q_K.                (9)

This uses 6KV actual qubits. Its coarse-cell range is finite and its
fine-lattice collective-coupling cost remains explicit. Proper rotations
act on oriented edges and faces as signed permutation matrices R_E,R_F,
with C R_E=R_F C. Edge reversal changes |t_e> to -|t_e> while fixing the
singlet, so Q_K,P_K acquire the same edge sign. Thus the link-block model
and H_K respect those proper rotations, including edge basepoint shifts.
This is covariance of the supplied edge architecture, not identification
with the original one-qubit-per-site primitive.

Magnetic divergence d_2 B_K=0 is exact even at finite K. Electric divergence
does not in general commute with H_K at finite K: the local commutator has
the occupation-dependent factor 1-2N_e/K. The limiting electric constraint
below is therefore a controlled state/observable limit, not an assertion
of an exact microscopic gauge symmetry.

For total number N_tot, the same elementary coefficient estimate as in the
earlier block note gives

    ||(H_K-H)psi||<=A_L/K ||(N_tot+1)^2 psi||,        (10)

and a fixed linear field combination differs by at most
A_(L,test)/K times ||(N_tot+1)^(3/2)psi||. Both bounds hold on their weighted
number domains, including the portion above the physical occupation cap.
They use finite L and real C, not symmetry of C.

## 4. Normalized states approaching the electric constraint

Choose a normalized transverse vector psi_T with all required polynomial
number moments finite, for example a finite excitation of the ground state
of (7). On each of the dim Z unobserved coordinate modes choose a centered
pure Gaussian chi_epsilon with

    Var(Q_Z)=1/(2 epsilon^2), Var(P_Z)=epsilon^2/2,
    0<epsilon<=1.

Set psi_epsilon=psi_T tensor chi_epsilon. Its P_Z fluctuations tend to zero,
while the unobserved Q_Z fluctuations grow. This is an explicit preparation
of correlations between edge blocks, not a state produced by the classical
record birth process or by independent singlet blocks.

At fixed L and fixed |t|<=T, the quadratic flow and any fixed finite word
of canonical field Weyl operators are linear canonical transformations and
finite translations. Gaussian moment bounds therefore give

    ||(N_tot+1)^2 W_r U(t_r)...W_1 U(t_1)psi_epsilon||
        <= A_(L,T,word,psi_T) epsilon^-4.           (11)

The number is quadratic in Q,P, so its squared norm uses at most eighth
moments. The growing Q_Z standard deviation is O(epsilon^-1); all other
fixed transformations and translations have bounded coefficients. This
proves the epsilon^-4 power in (11); it is not a uniform bound as L or the
word length grows.

Project to the actual finite-qubit sector and normalize:

    phi_(K,epsilon)=Pi_K psi_epsilon/||Pi_K psi_epsilon||.

If any edge occupation exceeds K then N_tot>K. Markov's operator estimate
and (11) consequently give

    ||(1-Pi_K)psi_epsilon||<=A K^-2 epsilon^-4,
    ||phi_(K,epsilon)-psi_epsilon||<=2A K^-2 epsilon^-4 (12)

once the right side is small. Projection is a specification of the initial
vector, not a claimed efficient or postselection-free preparation protocol.

## 5. Joint block and squeezing limit for bounded observables

Let W_K(a,b)=exp(i[a.E_K+b.B_K]) and W(a,b) its canonical counterpart,
for fixed real edge and face tests. Duhamel's formula, (10)-(11), and the
linear-operator estimate compare a finite word of their Heisenberg
evolutions at fixed times. Telescope so each operator difference acts on
canonical evolutions and Weyl words, whose moments are bounded by (11).
Unitarity controls all remaining factors. Including (12), the difference
between the finite-qubit expectation in phi_(K,epsilon) and the canonical
expectation in psi_epsilon is bounded by

    A_word [K^-1 epsilon^-4+K^-2 epsilon^-4].        (13)

The Weyl differences alone cost K^-1 epsilon^-3 and are covered by (13)
for epsilon<=1. No estimate of unbounded H_K-evolved number moments is
silently used in this telescoping argument.

To compare the canonical state to the reduced theory, observe that B has no
Z coordinate, and E_Z=-P_Z is constant under H. Each field word therefore
factorizes into its transverse word and a commuting Gaussian phase. If
a_(j,Z) denotes the Z projection of the electric test in its j-th factor,
the extra factor is exactly

    exp[-epsilon^2 ||sum_j a_(j,Z)||^2/4].           (14)

Its difference from one is at most epsilon^2 ||sum_j a_(j,Z)||^2/4. Choose

    epsilon_K=K^-1/6.

Equations (13)-(14) yield, for every fixed such word and time interval,

    |<word_K>_phi - <word_T>_psi_T| <= A_word K^-1/3. (15)

The projection normalization contribution is O(K^-4/3). This proves a
bounded-observable convergence to the reduced zero-charge, zero-flux
quantum field sector. It does not assert convergence of all unbounded
electric-divergence moments or exact electric conservation at finite K.
In particular, taking a=d_0 f and b=0 shows that the characteristic function
of the finite-K electric Gauss observable tends to one at each fixed time.
Finite collections follow by the same word argument.

## 6. Scope and relation to the campaign

The positive limiting energy, derivative bracket, magnetic identity,
electric sector and two transverse frequencies occur together in this
declared finite-volume model. Equation (3) removes the additional centered-
difference zeros. Small momenta have sqrt(lambda)=|k|+O(|k|^3).

The remaining realization questions are substantial: the initial squeezed
state is supplied and correlated, the interactions are collective inside
growing link blocks, records change their local quantum content, and the
spatial continuum/thermodynamic limit is uncontrolled by (15). There is no
claim of matter, gravity, coupling constants, a Born-rule derivation, or a
TOE. This is a constructive conditional improvement over the earlier block
model, with a precise physical observable sector and an explicit small
parameter.
