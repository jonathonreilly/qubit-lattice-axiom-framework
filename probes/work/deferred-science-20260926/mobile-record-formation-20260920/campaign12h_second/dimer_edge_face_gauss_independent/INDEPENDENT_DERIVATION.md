# Edge/face and energy/Gauss reconstruction before author comparison

Both complete supplied notes were read, at hashes recorded in
PRE_COMPARISON_SOURCES.json. No author checker or results for this construction
have been opened. The unchanged finite-block weighted estimate and
self-adjointness application are reused at their independently checked
identities. No actionable defect has been found in either supplied argument.

## Incidence, adjoints and the observable sector

Let D_j be the forward differences and C_ik=sum_j epsilon_ijk D_j. Commuting
the D_j proves C d_0=0 and d_2 C=0 exactly. C is real, but generally not
symmetric. For complex d_j=exp(ik_j)-1, epsilon contraction gives

    ([d cross]^* [d cross])_jl
      =delta_jl sum_k |d_k|^2-d_j conjugate(d_l).

Thus the symbol Gram matrix is lambda I-d d^*, with lambda=4 sum sin^2(k_j/2).
Its two nonzero eigenvalues are lambda. Only k=0 has lambda=0, even on even
tori. Fourier decomposition gives rank C=2V-2, rank d_0=rank d_2=V-1, and
ker C=im d_0 orthogonal-sum the three constant edge fields. On the face side,
im C=ker d_2 intersect zero harmonic flux, of dimension 2V-2. Complex Fourier
coordinates obey the ordinary real-field conjugacy; the real count is
2V-2 canonical transverse coordinates.

For signed proper coordinate permutations the edge basepoint shifts by the
negative image direction when its orientation reverses. A face basepoint
shifts by each negative image of its two tangential directions. The face
orientation sign is the image normal sign because det R=+1. These rules give
d_0 R_0=R_E d_0, C R_E=R_F C and d_2 R_F=R_3 d_2. Omitting basepoint shifts
would not be the same cochain transformation. Physical spin rotations fix
the singlet and rotate the Cartesian triplets, supplying the same edge sign
on the retained pair matrix unit. This verifies covariance for the declared
edge architecture; it is not an assertion about the original site primitive.

For H=(P^T P+Q^T C^T C Q)/2, E=-P and B=CQ, the equations and bracket are

    E_dot=C^T B, B_dot=-C E, [E_e,B_f]=i C_fe.

The adjoint makes the two energy derivatives cancel. Both exact chain
identities yield the magnetic identity and conservation of d_0^T E. Taking
T=(ker C)^perp removes the electric gradient and harmonic directions and
leaves a strictly positive oscillator matrix at fixed L. The magnetic
readout already has zero harmonic flux because it is in im C. This is a
chosen observable sector. The full unreduced free gauge coordinates are
not assigned an impossible normalized exact P_Z=0 vector.

## Finite qubits and growing-state estimates

The one-mode link-block formula is the spin-K/2 lowering representation,
on K physical singlet/triplet pairs. Its common-space order is f_K(N_e)a_e.
The cutoff sector N_e<=K is reducing, including at its boundary. The
finite commutator is 1-2N_e/K. Consequently electric Gauss need not commute
with H_K, while d_2 B_K=0 remains an exact linear identity.

The previous weighted coefficient estimate never used C=C^T, only fixed
finite real coefficients in a sum of squares. It therefore gives

    ||(H_K-H)psi|| <= A_L/K ||(N_tot+1)^2 psi||.

Each incidence row has l1 norm four. The previous explicit product bound
gives, for M=3V, one sufficient A_L=(17M/2)(2+3sqrt(2)). This is not an
optimization or a uniform-volume estimate. Also, Q_K and P_K are
sqrt(2/K) times spin components, so their exact norm is sqrt(K/2).
Thus one may take B_L=17M/4 in ||H_K||<=B_L K, including the common Fock
extension. Unused pair sectors are not claimed to be a distinct physical
vacuum or to supply the original immutable dynamics.

The orthogonal T/Z coordinate change preserves total Fock number. The state
psi_epsilon has gauge Q standard deviation O(epsilon^-1), gauge P standard
deviation O(epsilon), and transverse moments fixed. Canonical quadratic
flows and finite field Weyl words apply bounded linear transformations and
translations at fixed times/tests. Since (N+1)^4 is degree eight in Q,P,

    ||(N_tot+1)^2 canonical_word psi_epsilon|| <= A epsilon^-4.

Likewise the (N+1)^(3/2) norm is at most A epsilon^-3. These bounds require
the stated finite transverse number moments and fixed L/word/time horizon.
They do not assert bounded number moments as epsilon tends to zero.

If some N_e>K, then N_tot>K. Commuting occupation projections and the spectral
Markov inequality give

    ||(1-Pi_K)psi_epsilon|| <= K^-2 ||(N_tot+1)^2 psi_epsilon||,
    ||phi_(K,epsilon)-psi_epsilon|| <= 2A K^-2 epsilon^-4

for sufficiently small tail. Normalization does not require an unbounded
inverse projection norm. A fixed field word is telescoped so every operator
difference acts on canonical evolutions/words. Unitarity bounds the other
factors; the preceding weighted domains justify Duhamel. This gives
K^-1 epsilon^-4 for Hamiltonian differences, K^-1 epsilon^-3 for Weyl
differences and K^-2 epsilon^-4 for the normalized initial projection.
No H_K-evolved number moment estimate is being assumed.

In the canonical theory B has no gauge coordinate and E_Z=-P_Z is constant.
The gauge pieces of a field word commute, so their expectation is exactly

    exp[-epsilon^2 ||sum_j a_(j,Z)||^2/4].

The remainder is its transverse field word, including all transverse
noncommutative phases. Balancing K^-1 epsilon^-4 against epsilon^2 gives
epsilon=K^-1/6 and error O(K^-1/3); the projection term is O(K^-4/3).
Constants depend on the fixed transverse vector, coarse volume, word and
time interval. Characteristic convergence of Gauss follows, but would not
by itself imply convergence of its second moment.

## Addendum: target energy and Gauss mean square

Use unshifted energies consistently in this step: E_T=<psi_T,H_T psi_T>.
The canonical gauge energy is (dim Z) epsilon^2/4. The weighted Hamiltonian
difference costs O(K^-1 epsilon^-4). The normalized projection costs at
most 2||H_K|| times its vector error, also O(K^-1 epsilon^-4) because
||H_K||=O(K). Therefore

    |<phi_K,H_K phi_K>-E_T| <= A(K^-1 epsilon^-4+epsilon^2)
                            =A delta, delta=K^-1/3.

Exact finite-Hamiltonian and reduced-Hamiltonian conservation make this
energy estimate uniform in time. This is convergence to the target energy,
not merely bounded energy.

For a single Heisenberg Weyl expectation, first compare the two evolved
state vectors. Their error is O(delta) independently of the real test z,
because the Weyl operator is unitary. Then apply the linear-generator
Duhamel estimate on the canonical evolved vector. Translation by the
canonical Weyl operator shifts Q,P by a vector O(||z||). Sixth moments give
the global bound

    A K^-1 epsilon^-3 ||z||(1+||z||)^3.

Together with the gauge phase O(epsilon^2 ||z||^2) and initial projection,
this proves |chi_K(z,t)-chi_T(z,t)|<=A delta(1+||z||)^4 for all real z at
fixed L and bounded times. In particular, no constant hidden in this bound
depends arbitrarily on z. For transverse E and B the gauge phase is actually
absent, though retaining the displayed upper bound is harmless.

Each of the two field families E_(T,K)(t) and B_K(t) consists of commuting
Hermitian components: they are unitary conjugates of linear combinations
of respectively commuting link P_K and link Q_K. The two families need not
commute with each other and are never assigned a common classical law.

For either family use its ordinary joint spectral measure and
F_a(X)=(1-exp(-a||X||^2))/a. The elementary scalar inequalities give
0<=F_a<=||X||^2 and, in the canonical state,

    <F_a(X)> >= <||X||^2>-(a/2)<||X||^4>.

The canonical fourth moment is uniform on compact time intervals. Gaussian
Fourier smoothing with z distributed as N(0,2aI) is exact and, for 0<a<=1,
integrates the polynomial characteristic bound to

    |<F_a(X_K)>-<F_a(X_T)>| <= A delta/a.

This yields a lower bound on each finite quadratic field moment. Adding
the transverse electric and magnetic bounds gives

    <(||E_(T,K)||^2+||B_K||^2)/2> >= E_T-A(a+delta/a).

The exact orthogonal operator identity
H_K=(||E_(T,K)||^2+||B_K||^2+||E_(Z,K)||^2)/2 and the target-energy upper
bound leave at most A(delta+a+delta/a) for <||E_(Z,K)||^2>. Taking
a=sqrt(delta)=K^-1/6 proves the addendum's O(K^-1/6) mean-square estimate.
The fixed operator norm of d_0^T transfers it to electric divergence; the
harmonic electric directions are already included in Z. Its sufficient RMS
rate is K^-1/12. This deduction does not assert exact finite-K electric
conservation or general convergence of all unbounded observables.

A useful countercontrol to a weaker argument is X_R=R with probability R^-2
and zero otherwise. Its characteristic functions converge uniformly to one,
yet E X_R^2=1. Thus neither characteristic convergence nor bounded energy
alone would replace the supplied convergence-to-target-energy and transverse
lower-bound argument.

## Decisive controls and failures preserved

The independent script builds exact integer incidence matrices for cubic
side 3 and 4. It verifies the full proper-24 cochain action including edge,
face and cube basepoint shifts. Ranks are respectively (52,26,26) and
(126,63,63) for curl, gradient and divergence. Frequency inventories have
one zero momentum at each side length. An exact real-space countercontrol
using E=e_0 and a single-coordinate Q gives wrong energy derivative +1 if
C replaces C^T. Correct use of the adjoint gives zero.

Spin norms/commutators are checked exactly for K=1,2,3,4. A two-edge row
C=(1,-1), d_0=(1,1) has a nonzero finite-K Gauss commutator; its squared
Frobenius norm is exactly four at K=1. This illustrates the microscopic
constraint distinction without simulating a whole cubic quantum system.

The same two-edge system has one transverse oscillator of frequency sqrt(2)
and one squeezed gauge coordinate. Its correlated edge-basis Gaussian
coefficients are computed by the exact Bargmann recurrence with analytic
infinite-Fock normalization. For K=2,4,8,16,32,64 the entire finite physical
sector is retained. The controls check projection tails, exact energy
decomposition/conservation and finite-time gauge moments/characteristics.
They corroborate the estimates but do not establish asymptotic exponents.
No canonical dynamical occupation cutoff is used.

Tiny projection tails cannot be resolved by subtracting a double-precision
norm from one. The original floating outputs (including an apparent zero at
K=32) are preserved. A separate 90-digit recurrence gives tail norms about
3.1986901749e-9 at K=32 and 6.4382721495e-14 at K=64. No exact-zero-tail claim
is made. The squeezed number moment polynomials were independently checked
by differentiating their generating function. That supplemental checker
first compared factored and expanded SymPy expressions structurally and
failed; the old source/log/receipt and exact-zero-difference diagnosis are
preserved under failed_attempts/precision_symbolic_equality. Only that
assertion was corrected. The successful runs have empty stderr.

No author controls or results have been read when this reconstruction is
sealed. It is a selective review of the supplied claims, not an independent
microscopic implementation search or an audit verdict.
