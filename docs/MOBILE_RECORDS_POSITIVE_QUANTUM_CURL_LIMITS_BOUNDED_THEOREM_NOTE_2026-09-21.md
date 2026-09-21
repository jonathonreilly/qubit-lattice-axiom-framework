---
claim_id: mobile_records_positive_quantum_curl_limits_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Supplied finite-qubit Hamiltonians admit two distinct controlled curl-field limits: collective edge blocks at fixed coarse volume approach a positive two-polarization zero-charge observable sector, while a uniformly local active-cell model has a fixed-particle carrier-subtracted Euler limit. Their hypotheses and conclusions are not combined into one microscopic theory. Neither model derives the permanent-record law, its state preparation, a joint continuum quantum limit, matter or gravity."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_positive_quantum_curl_limits_2026_09_21.py
---

# Positive quantum curl fields from specified finite-qubit models

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

A positive quantum energy, two transverse polarizations and a controlled
electric constraint coexist in the explicit sequence of finite-qubit models
below. This is not a derivation from the
[minimal record axioms](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonians, time
evolution, block architecture and initial quantum states are supplied.
Their changing singlet/triplet contents do not implement the earlier
permanent-color stochastic record law.

The four complete arguments establish two different limits:

| Construction | Fixed quantities and limit | Controlled conclusion | Remaining realization cost |
|---|---|---|---|
| Collective edge blocks, 6 K L^3 qubits | Fixed coarse L, time interval, tests and transverse state; K grows with epsilon=K^-1/6 | Positive limiting energy; two polarizations at each nonzero momentum; one frequency zero; bounded field-word error O(K^-1/3); electric Gauss mean square O(K^-1/6) | Growing collective interaction range, correlated projected preparation and no uniform spatial limit |
| Local active cells, two qubits per cell | Fixed particle number and Fourier-mode list; N grows at time N tau | Positive gapped laboratory Hamiltonian; carrier-subtracted vector error O(N^-1/2), plus O(N^-2) symbol error | Rotating-frame curl energy indefinite; extra sine zeros and longitudinal modes; no positive-density theorem or selected electric constraint |

The two rows have different microscopic models, brackets and energy
interpretations. Their favorable properties cannot be combined into one
derived theory. The local active-cell fine packing has range three and a
preferred pair direction. Its ground-state uniqueness concerns the active
cells; unused fine-lattice qubits must be excluded or fixed.

For edge blocks, C maps edges to faces. The positive Hamiltonian
H=(P^T P+Q^T C^T C Q)/2 gives E=-P, B=CQ and
E_dot=C^T B, B_dot=-C E. Exact chain identities give magnetic divergence zero.
A normalized finite-energy sequence of actual qubit states approaches a
transverse sector with zero electric charge and zero global flux.
Electric Gauss need not be exactly conserved at finite K. The mean-square
estimate needs Part III's energy argument; bounded characteristic
convergence alone would not suffice.

Part I supplies the elementary weighted operator estimate. Part II changes
the spatial discretization and preparation. Part III proves the Gauss-moment
bound. Part IV develops the separate local dilute route. Every source
argument is reproduced completely, with its title removed and headings
shifted. Original pending-review sentences are historical; the source-bound
reports define completed selective check coverage. Formal retention remains
unaudited.

## I. Finite blocks and the weighted operator estimate

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

### 1. Finite qubit blocks and the exact occupation representation

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

### 2. A specified discrete curl and positive microscopic Hamiltonian

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

### 3. A quantitative finite-time Fock-space limit

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

### 4. The limiting observable algebra and curl equations

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

### 5. Scope of the positive construction

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

## II. Edge-face incidence and quantum field words

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

### 1. Cubical incidence operators

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

### 2. Positive canonical dynamics and its physical observable sector

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

### 3. Actual finite-qubit link blocks

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

### 4. Normalized states approaching the electric constraint

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

### 5. Joint block and squeezing limit for bounded observables

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

### 6. Scope and relation to the campaign

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

## III. Conserved energy and electric Gauss mean square

**Status:** proposed conditional extension, pending controls and independent
check. **Date:** 2026-09-21. **Dependency:**
`DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md`, SHA-256
`a6759908ef27e5f2990c7f20d4615aa4166d9a33bec66ea4b4e8143c22f01824`.

The primary note proves convergence of bounded field words. The extra energy
argument here, rather than bounded convergence alone, also controls the
electric constraint in mean square. All volume, state, architecture and
microscopic-interpretation limitations of that note remain in force.

### Initial and conserved energy

On a link block, ||Q_K|| and ||P_K|| are at most sqrt(K/2): these are the
spin-K/2 components multiplied by sqrt(2/K). The same bound holds on the
common Fock extension. Since the number of edges and nonzero incidence
entries is fixed, ||H_K||<=B_L K. Put epsilon=K^-1/6 and delta=K^-1/3.

Let psi_epsilon and its normalized physical projection phi_K be as in the
primary note, and E_T=<psi_T,H_T psi_T>. The full canonical energy is

    <psi_epsilon,H psi_epsilon>=E_T+(dim Z)epsilon^2/4.

The weighted difference bound (10), the state-moment bound (11), and the
projection estimate (12) give

    |<phi_K,H_K phi_K>-E_T|
      <= |<psi_epsilon,(H_K-H)psi_epsilon>|
         +2||H_K|| ||phi_K-psi_epsilon||
         +(dim Z)epsilon^2/4
      <= A[K^-1 epsilon^-4+epsilon^2]
      <= A delta.                                  (A1)

Both vectors have norm one, so the middle term uses the ordinary bounded
operator expectation inequality. The linear-in-K Hamiltonian norm is needed
here; the projection error alone would not justify an energy statement.
The exact finite-qubit evolution conserves the left energy. The reduced
canonical evolution conserves E_T. Thus (A1) holds at every time, without
claiming H_K approaches H in global operator norm.

### Quantitative recovery of quadratic fields from their characteristic functions

For a single Heisenberg Weyl operator with real test z, the proof of the
primary note can be kept polynomial in ||z||. The two evolution differences
cost at most A delta independently of z. The linear-Weyl Duhamel term costs

    A K^-1 epsilon^-3 ||z||(1+||z||)^3,

because conjugation by the canonical Weyl operator translates Q,P linearly.
The squeezed-sector phase costs at most A epsilon^2 ||z||^2. Constants may
depend on the fixed field map, L, psi_T and time interval, but not K or z.
Since K^-1 epsilon^-3=K^-1/2<=delta, for either the commuting vector of
transverse electric components E_(T,K) or the commuting magnetic components
B_K this gives the sufficient bound

    |chi_K(z,t)-chi_T(z,t)|<=A delta(1+||z||)^4,
    |t|<=T.                                        (A2)

Different link momenta commute, as do different link coordinates, so these
two field families separately have ordinary joint spectral distributions.
No joint commutativity of E and B is assumed. The canonical fourth moments
of both families are bounded uniformly on the fixed time interval.

For a commuting vector X and 0<a<=1 define the bounded nonnegative function

    F_a(X)=[1-exp(-a||X||^2)]/a.

It satisfies 0<=F_a(X)<=||X||^2. In the canonical state,

    <F_a(X)> >= <||X||^2>-(a/2)<||X||^4>.            (A3)

The Gaussian Fourier representation

    exp(-a||X||^2)= E_(z~N(0,2a I)) exp(i z.X)

and (A2) imply

    |<F_a(X_K)>-<F_a(X_T)>|<=A delta/a,              (A4)

because E(1+||z||)^4 is bounded for a<=1 in the fixed finite dimension.
This step uses all real tests through their explicitly bounded polynomial
dependence; pointwise characteristic convergence without that control would
not give the rate in (A4).

### Electric constraint bound

The real orthogonal edge decomposition T plus Z gives exactly

    H_K = [||E_(T,K)||^2+||B_K||^2]/2
          +||E_(Z,K)||^2/2.

Apply (A3)-(A4) separately to transverse E and B, whose reduced total energy
is E_T. Positivity gives

    <[||E_(T,K)||^2+||B_K||^2]/2>
       >= E_T-A[a+delta/a].                         (A5)

Subtract (A5) from the conserved-energy estimate (A1). Choosing
a=sqrt(delta)=K^-1/6 yields

    sup_(|t|<=T) <||E_(Z,K)(t)||^2> <= A K^-1/6,
    sup_(|t|<=T) <||d_0^T E_K(t)||^2> <= A_L K^-1/6. (A6)

The harmonic electric components are included in Z and obey the same
control. The root-mean-square sufficient rate is K^-1/12. Magnetic divergence
and its zero harmonic flux are already exact at finite K. None of these
bounds asserts that electric Gauss commutes with the finite-K Hamiltonian.

The argument supplies a uniformly finite-energy sequence of actual qubit
states approaching the zero-charge observable sector over finite times.
The large number of Fock quanta in squeezed gauge coordinates does not
force a divergent physical energy because those coordinates lie in ker C.
The correlated state preparation and collective microscopic interactions
remain supplied structures; neither is produced by the permanent-record
formation process in this construction.

## IV. A separate uniformly local dilute curl limit

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

### 1. A fixed local Hamiltonian

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

### 2. Exact relation to free bosons and positivity

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

### 3. Uniform collision estimate for finitely many Fourier modes

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

### 4. Duhamel control through Euler times

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

### 5. The noncommuting limiting fields

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

### 6. What this resolves and what remains

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

## Verification and scientific scope

[The evidence packet](../.claude/science/mobile-record-positive-quantum-curl-20260921/README.md) preserves four arguments, unchanged
author computations, and three completed selective independent reviews with
pre-comparison evidence. The runner executes ten mathematical groups plus
source bookkeeping. Three mutations test occupation depletion, the incidence
adjoint and the dilute-sector commutator normalization.

The analytic-vector criterion was checked in Barry Simon's
[lecture notes](https://math.caltech.edu/SimonPapers/R4.pdf), Theorem 1.7,
printed pages 24-25. The application checks symmetry and a dense set of
analytic vectors. Its receipt records that coverage. The discrete-form
paper cited in Part II supplies context only; incidence identities are
proved directly.

Numerical controls use small physical blocks or fixed two-particle cubic
sectors, not full cubic many-body evolution. Rates follow from conditional
proofs, not numerical fits. Edge-motif missing projection probabilities
reported as zero at K>=32 are unresolved floating subtraction near one.
Independent 90-digit coefficients resolve positive tails at K=32 and 64;
no exact zero-tail assertion supports the proof. Failures and narrow repairs
are preserved.

The permanent-record interpretation, allowed moves, clock, correlated
preparation, joint spatial limit, interacting matter, gravity and empirical
identification remain open. No new primitive, physical constant or TOE is
asserted.
