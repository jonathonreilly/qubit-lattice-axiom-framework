# Uniform local ring dynamics with slow record formation

Date: 2026-09-22. Status: author conditional theorem and exact finite algebra
controls; independent reconstruction pending. This is a positive sufficient
regime for the supplied quantum gauge-record model. The statement concerns
local observables uniformly over finite cubic tori. It requires a finite local
preparation circuit and a birth rate tending to zero. It does not establish
the corresponding limit from a bare checkerboard quench at fixed birth rate.

## 1. Model and statement

Use the bosonic qutrit matter and spin-half links of
`HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md`. Fix dimension d>=2. Each
period is even and at least six. Let V be the number of vertices, A and B the
bipartition, q_x in {0,+1,-1}, and E_e in {-1/2,+1/2}. The selected Gauss sector is

    div E_x + 1_A(x) - q_x = 0.                         (1)

The total signed charge is Q=V/2. An occupied record hops to an adjacent vacant
site with its charge unchanged, shifting the link to preserve (1). Let T be
minus the sum of these unit-amplitude hopping operators. A normalized birth
operator j_(e,a) fills two vacant endpoints with opposite charges and makes
the corresponding link shift. Use either the two charge-resolved operators
per edge or one coherent sum of them. In both cases

    sum_a j_(e,a)^dag j_(e,a) = P_(e,vac),
    ||j_(e,a)|| <= 1.                                   (2)

Both coherent signs used as separate channels would double this normalization;
that is a different choice of beta. No equality of their full instruments is
assumed. All jumps and Hamiltonian terms preserve the selected Gauss sector
and total signed charge. Hopping preserves record number, while a birth adds
two. The finite-dimensional Lindblad dynamics is

    L rho = -i[H,rho] + beta sum_(e,a) D[j_(e,a)]rho.

The two potentials considered here are

    H_s = Delta N_B + t T,
    H_f = (Delta/2) sum_x(div E_x)^2 + t T.              (3)

The field-only form of H_f is homogeneous. The sector (1) and the preparation
still supply a checkerboard background. No native derivation of these Hilbert
spaces, statistics, time, Hamiltonians, reservoirs or Born probabilities is
asserted.

Fix J>0, beta_0>=0, a bounded observation interval [0,T_*], and set

    epsilon = t/Delta > 0,
    Delta = J/(2 epsilon^4),
    t = J/(2 epsilon^3),
    beta = beta_0 epsilon^(2d).                         (4)

Let P_m be the product matter projector onto plus at every A and vacancy at
every B. Let rho_ice be any field density supported on div E=0, including
arbitrary coherences, correlations and mixtures of flux components. The ring
Hamiltonian on that field space is

    H_ring = -J sum_p (W_p+W_p^dag).                     (5)

**Conditional local limit.** There are a finite-depth, finite-range,
number-conserving and gauge-preserving unitary circuit Y_epsilon and constants
epsilon_0,C_(X,T_*,J,beta_0,d), independent of V and rho_ice, such that the
physical initial density

    rho_epsilon(0) = Y_epsilon^dag
                       (P_m tensor rho_ice) Y_epsilon  (6)

obeys, for every field observable O_X of fixed finite support X,

    sup_(0<=tau<=T_*) |
      Tr[O_X rho_epsilon(tau)]
       -Tr[O_X exp(-i tau H_ring) rho_ice exp(i tau H_ring)]|
      <= C_(X,T_*,J,beta_0,d) ||O_X|| epsilon.           (7)

This holds for 0<epsilon<epsilon_0 and for either potential in (3). The circuit
depth, range, number of colors and gate norm bounds depend on d and a fixed
perturbative order, not V. The theorem specifies the circuit algebraically;
it does not compile its gates into the repository's minimal site primitives.
If beta_0>0, formation is enabled at each finite epsilon. Its rate relative to
J decreases in this family; in d=3, beta=beta_0 epsilon^6. No optimality of that
power is claimed. The constants and small-parameter threshold are existential
finite-order bounds, not numerically useful estimates for a laboratory setup.

## 2. An onsite integer penalty for both physical models

For H_s put N=N_B. For H_f use the following exact identity on (1):

    (1/2)sum_x(div E_x)^2 = N_(A,-) + N_(B,+).           (8)

To prove it, replace div E by q-1_A in (1), use q^2=n and
sum_x q_x=|A|, and expand. Equivalently, adding
`(Q-|A|)/2=0` to the left side gives

    sum_(x in A) (q_x^2-q_x)/2
      +sum_(x in B) (q_x^2+q_x)/2.

Each summand is the displayed one-site charge projector. Thus for H_f we may
analyze the full tensor-space extension N=N_(A,-)+N_(B,+). It agrees exactly
with the physical field-star Hamiltonian on the invariant sector. This
extension is a proof device, not a claim that the physical operator (3)
loses its homogeneity.

For either choice N is a sum of commuting onsite projectors, and every hop
changes it by +1 or -1. Each local term in T therefore has zero average under
conjugation by exp(i theta N). In the sector Q=|A|, N=0 forces precisely the
matter pattern P_m: for N_B this is immediate; for (8), N=0 permits only
0,+ at A and 0,- at B, and maximal signed charge forces all A plus and B
vacant. Intersecting with (1) then gives the ice field space. Write this
code projector as P. Every bare birth satisfies j_(e,a)P=0.

The doubled matter count is preserved by every unitary used below. The
circuit in (6) moves the existing V/2 plus records coherently; it does not
create pairs during preparation.

## 3. Finite circuit normal form with volume-uniform locality

Here is a constructive finite-order lemma. It supplies the locality step
that a finite-volume spectral perturbation theorem alone does not supply.
Schrieffer-Wolff block diagonalization is standard machinery; compare
[Bravyi, DiVincenzo and Loss, arXiv:1105.0675, section 4](https://arxiv.org/html/1105.0675).
The finite circuit construction and remainder estimate needed here are given
explicitly, rather than importing a ground-energy error as a dynamics bound.

For any fixed integer n there is a circuit Y_epsilon such that

    Y_epsilon (N+epsilon T) Y_epsilon^dag
       = N + sum_(r=2)^n epsilon^r D_r + R_tilde,
    [D_r,N]=0,
    ||R_tilde||_loc <= C_n epsilon^(n+1).               (9)

All interactions on the right have finite range and a bounded number of terms
per site, with constants depending on n,d but not V. Here a local interaction
norm can be taken as `sup_x sum_(Z contains x) ||A_Z||` for the constructed
decomposition. Every D_r and R_tilde preserves total charge, record number and
Gauss operators. Odd D_r vanish. For each fixed local A_X,

    support(Y_epsilon A_X Y_epsilon^dag) subset X^(R_n),
    ||Y_epsilon A_X Y_epsilon^dag-A_X||
          <= C_(X,n) ||A_X|| epsilon.                  (10)

The neighborhood radius R_n is independent of epsilon and V.

**Construction.** Suppose all orders below r have been made N-diagonal.
Decompose the coefficient A_r of epsilon^r into Hermitian local terms
A_(r,Z). Terms can be indexed by their original onsite/edge Hamiltonian
term and its finite circuit light cone. Define the support-preserving maps

    P_N(A) = (1/2pi) integral_0^(2pi)
                    exp(i theta N) A exp(-i theta N) dtheta,
    I_N(A) = sum_(k != 0) A_k/k,
    [N,A_k]=k A_k.                                     (11)

The integer onsite spectrum makes these definitions finite and local.
For Hermitian A, I_N(A) is anti-Hermitian and

    [N,I_N(A)] = A-P_N(A),
    ||I_N(A)|| <= (pi/2)||A||.                          (12)

The norm bound follows from the integral kernel i(theta-pi)/(2pi). Its kth
Fourier integral is 1/k for nonzero integer k, and its absolute integral is
pi/2. Onsite conjugation does not enlarge support.

Put S_(r,Z)=I_N(A_(r,Z)). Color their support-intersection graph so that
terms of the same color have disjoint supports. Its maximum degree is bounded
independently of V: before each finite step the interaction range, support
size and number of indexed terms through any site are bounded. A greedy
coloring therefore requires only a bounded number of colors. Apply, in a
fixed color order, all local gates exp(epsilon^r S_(r,Z)). Their first
contribution at order r is

    [sum_Z S_(r,Z),N] = -A_r+P_N(A_r).                  (13)

Thus the new coefficient is N-diagonal; lower orders are unchanged. The
ordering effects at higher orders are included when constructing the next
A_r. Iterate r=1,...,n. In particular, this is not a claim that a product of
overlapping gates equals the exponential of their sum.

Each finite stage has finite depth and bounded range, hence so does the
complete circuit. Conjugate each original onsite/edge term by that circuit.
Only the finitely many gates in its backward light cone matter. Their
number, support and generator norms are uniformly bounded. The resulting
local matrix is analytic in epsilon on a common disk about zero. A Cauchy
Taylor remainder bound on a smaller disk is therefore C_n epsilon^(n+1)
per indexed term. Only a bounded number of these enlarged terms meets any
site. Summing their Taylor remainders proves (9) in the stated local norm.
This argument uses no global operator-norm bound proportional to V.

Gauge and count symmetries hold term by term and are inherited by (11) and
the gates. Also C=exp(i pi N) sends T to -T. At each recursion the coefficient
of order r has C-parity (-1)^r, term by term. Choose the same coloring at
positive and negative epsilon. The entire construction is covariant under
epsilon -> -epsilon and conjugation by C. An N-diagonal coefficient with odd
parity must vanish, proving the assertion about odd D_r. Finally, a local
observable meets only a bounded circuit cone, and each gate differs from the
identity by O(epsilon^r); telescoping proves (10).

Coloring can break translation symmetry in the chosen identification. It
does not change the original physical Hamiltonian or generator. No uniform
global norm estimate ||Y-I||=O(epsilon) is asserted.

## 4. The code block is the ring Hamiltonian plus a small local correction

Apply (9) with n=2d+6 and restore Delta. Set

    K = Delta N + D,
    D = Delta sum_(r=2)^n epsilon^r D_r,
    R = Delta R_tilde,
    h = Delta epsilon^2,
    delta_R = C_n Delta epsilon^(n+1).                 (14)

D has local norm at most C_n h, R has local norm at most delta_R, and K
preserves P. Within P, the earlier complete two-hop and four-hop calculation
gives, with M=dV/2,

    P D_2 P = -M P,
    P D_4 P = M(2d-1)P - 2 sum_p (W_p+W_p^dag).         (15)

These are the bosonic coefficients, including folded normalization. A change
between analytic block identifications cannot change the first non-scalar
coefficient here: the second-order block is scalar, the zeroth block vanishes,
and odd orders vanish. Thus the finite circuit identification has (15), even
though its higher coefficients can differ from another Schrieffer-Wolff gauge.

Take the P_m matrix element of each local term D_r. This remains a local
field operator with no larger norm and commutes with field divergence.
The resulting field dynamics therefore preserves the ice subspace. On that
subspace, remove the scalars in (15) and replace its second- and fourth-order
operators by their equal ring expressions. The remaining field Hamiltonian is

    H_ring + E_epsilon,
    ||E_epsilon||_loc <= C_n Delta epsilon^6
                         = C_n (J/2) epsilon^2.        (16)

Its range is bounded independently of V. The extension off the ice subspace
is chosen only to apply a local dynamics bound; it agrees exactly with K on
every allowed initial field density. Standard finite-range locality and
Duhamel give, at fixed T_*, an O_(X,T_*,J)(epsilon^2) difference between these
code dynamics and (5), uniformly in V. Frozen components remain frozen under
(5); a nonzero coupling J does not imply that every ice word can move.

## 5. Local open-dynamics comparison, including no-event backaction

Transform the exact open dynamics by the same circuit. Its Hamiltonian is
K+R and its normalized jumps are B_(e,a)=Y j_(e,a)Y^dag. Each B has bounded
support, norm at most one, and by (10) and jP=0,

    ||B_(e,a) P|| <= C_n epsilon.                       (17)

For every density sigma supported on P,

    ||D[B_(e,a)] sigma||_1
      <= ||B P||^2 + ||B|| ||B P||
      <= C_n epsilon.                                 (18)

This includes the anticommutator/no-event terms. A small jump count alone
would not justify discarding them.

All terms of the transformed generator have finite range. Move Delta N into
an interaction picture. Its unitary is a product of onsite unitaries; it
changes neither supports nor norms. The remaining time-dependent local
generator has a Lieb-Robinson velocity bounded by

    v <= C_n (h+delta_R+beta).                          (19)

The bound applies to the full open evolution. One precise finite-range source
is [Barthel and Kliesch, arXiv:1111.4210v2, sections II-III and V](https://arxiv.org/html/1111.4210v2).
Its hypotheses hold here: finite-dimensional factors, local Lindblad terms,
bounded range and overlap number, and time-uniform norm bounds. The Hamiltonian
pieces are Hermitian local terms; each dissipative piece retains its actual
local jump operator. No extension of that theorem to nonlocal dissipators is
being assumed.

For clarity, the elementary summation used with this bound matters. The
number of term centers within distance r of a fixed X on a d-dimensional
torus is at most C_X(1+r)^d, uniformly in its periods. Combining the local
trivial norm bound with an exponential light-cone bound, and splitting the
sum at r proportional to vT, gives

    sum_centers min(1,C_X exp(vT-mu dist(center,X)))
       <= C_X (1+vT)^d.                               (20)

The exponentially decaying tail has the same bound by shell summation.
Replacing 1 by epsilon moves the splitting radius by O(|log epsilon|), giving

    sum_centers min(epsilon,C_X exp(vT-mu dist(center,X)))
       <= C_X epsilon (1+vT+|log epsilon|)^d.          (21)

These estimates are polynomial in the light-cone radius; using the exponential
bound everywhere would lose the useful scaling.

Let sigma_K(s) be the closed K trajectory from P_m tensor rho_ice. It stays
supported on P. In variation of constants compare this reference trajectory
with the full transformed open trajectory, evolving the observable backward
with the full open propagator. Near its light cone use 2||R_Z|| for a
Hamiltonian source and (18) for a birth source. Far away use the local
Lieb-Robinson bound. Equations (20)-(21), integration over [0,T], and the
bounded interaction densities yield

    |Tr[O_X(rho_full'(T)-sigma_K(T))]|
      <= C_X ||O_X|| T {
          delta_R (1+vT)^d
           + beta epsilon (1+vT+|log epsilon|)^d }.     (22)

This comparison is valid for arbitrarily entangled code densities. It does
not factorize correlations or assume that only one birth has occurred.

For the scaling (4), h=J/(2 epsilon^2), n=2d+6, and

    delta_R = O(J epsilon^(2d+3)),
    delta_R (1+vT_*)^d = O(epsilon^3),
    beta epsilon (1+vT_*+|log epsilon|)^d
                                      = O(epsilon).   (23)

The bounds hold uniformly for T in [0,T_*], since the logarithm is dominated
by a constant times epsilon^(-2) at small epsilon. Add the O(epsilon) local
observable change from Y O_X Y^dag to O_X, and the O(epsilon^2) field dynamics
error from (16). This proves (7).

## 6. Checks and remaining work

`local_normal_form_record_check.py` carries out a global-generator normal-form
recursion through order sixteen on the complete nine-state physical square
sector, with rational arithmetic. It verifies every block commutator, parity,
number conservation, the coefficients (15), and high-precision remainder and
dressed-birth amplitudes for both onsite penalties. This is an algebra control;
the volume-uniform locality argument above uses the finite circuit version.

`finite_circuit_normal_form_record_check.py` therefore separately retains a
Hamiltonian decomposition by its original site and edge terms, freezes all
order-r local generators, and applies their gates sequentially before moving
to order r+1. Through order twelve it includes every ordering correction and
checks all the same block/parity identities exactly. It retains the complete
rational generators and coefficients, including the first omitted order, and
checks numerical approach to that coefficient at ninety-digit precision.
The square control verifies algebra; it does not enumerate a large torus or
numerically certify the constants in (7).

The first global-generator runner used an unjustified guessed threshold
`residual < 10^8 epsilon^17`. It failed because the actual leading coefficient
is about 1.277e8. The exact order/parity tests had passed. The original source,
streams and receipt are preserved under
`local_normal_form_source_history/first_residual_screen/`. The repaired runner
derives the full first omitted coefficient exactly and compares against it.
No model or theorem was weakened to hide a lower-order term.

The principal new conclusion is a uniform-volume local dynamics statement
under explicit preparation and weak-formation hypotheses. It supplies a
controlled bridge from this microscopic record-motion model to its ring
Hamiltonian. It supplies neither a thermodynamic Coulomb phase nor a photon
dispersion; those require a separate analysis of (5). Keeping beta fixed,
starting from an undressed checkerboard, optimizing the rate scaling, and
implementing the preparation with approved native primitives remain open.
The one-dimensional transport calculation in
`BALLISTIC_FIELD_SIGNALS_FROM_RECORD_FORMATION.md` is a separate diagnostic,
not a counterexample to (7) or a proof of the fixed-beta microscopic limit.
