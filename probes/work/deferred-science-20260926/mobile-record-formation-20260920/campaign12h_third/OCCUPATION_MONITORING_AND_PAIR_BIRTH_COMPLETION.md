# Occupation monitoring makes contact pair formation complete on finite graphs

Date: 2026-09-22. Status: author conditional theorem, exact four-site controls,
independent check pending. No native-axiom or retained-grade claim.

## 1. The supplied model and claim

Let G be a finite connected simple graph with at least two vertices. At every
vertex use H_x = C|0> direct-sum K, with finite-dimensional occupied-record
space K. Let q_x project onto vacancy and n_x = I-q_x onto occupation. Define

    Q = sum_x q_x,
    H = H_0 + sum_{<x,y>} kappa_xy T_xy,
    T_xy = sum_a (|0,a><a,0| + |a,0><0,a|)_xy.

Here each kappa_xy is real and nonzero, {|a>} is an orthonormal basis of K,
and the Hermitian H_0 commutes with every n_x. The exchange moves the complete
internal record state, including entanglement with other records. It is not
restricted to diagonal color mixtures.

Supply local occupation-dephasing jumps D_x = sqrt(d_x) n_x, with every d_x > 0.
The equivalent choice sqrt(d_x) q_x gives the same Lindblad dissipator. These
measure vacancy versus occupation without directly measuring occupied content.
They still disturb coherent superpositions of different occupation patterns.

On any nonempty subset F of graph edges, supply pair-birth channels

    J_{e,alpha} = sqrt(beta_{e,alpha}) |b_{e,alpha}><0,0|,
    |b_{e,alpha}> in K tensor K, ||b_{e,alpha}|| = 1,
    beta_e = sum_alpha beta_{e,alpha} > 0.

Birth vectors can carry arbitrary internal pair entanglement. All jumps act as
identity off the indicated sites. In particular,
sum_alpha J^dagger J = beta_e q_x q_y. No existing record is erased by a birth.
The full generator is -i[H,rho] plus the usual Lindblad dissipators of D and J.

**Conditional finite-graph theorem.** For every initial density operator
supported in the even-vacancy sector, the probability of full occupation tends
to one. On each fixed finite graph and for each fixed set of positive rates,
the completion-time tail admits an exponential upper bound and has finite
mean. The theorem does not assert a uniform size-dependent rate or a unique
stationary internal record state. It covers one birth-source edge as well as
birth on every edge.

The parity premise is necessary: births change Q by two, so an odd initial
number of vacancies cannot reach zero. In particular an initially vacant
graph must have even size for this claim to apply.

## 2. Proof: monotone count and stationary support

H and D preserve Q and [Q,J] = -2J. Therefore

    d Tr(Q rho)/dt = -2 sum_{e in F} beta_e Tr(q_x q_y rho) <= 0.

Let rho be a stationary density operator in the even-vacancy sector. Every
summand on the right is nonnegative, hence every Tr(q_x q_y rho) vanishes.
For positive rho this implies q_x q_y rho = rho q_x q_y = 0: factor rho by its
positive square root and use zero Hilbert-Schmidt norm. Consequently each
birth dissipator vanishes separately on rho.

Stationarity reduces to Hamiltonian evolution and the Hermitian dephasing
jumps. Taking its Hilbert-Schmidt pairing with rho gives

    0 = Tr(rho L(rho))
      = -1/2 sum_x d_x ||[n_x,rho]||_HS^2.

The Hamiltonian contribution is zero by cyclicity. All d_x are positive, so
[n_x,rho] = 0 for every x. Thus rho is block diagonal in the complete
occupation pattern. This does not diagonalize the internal record contents.
With the dissipators now zero, stationarity also gives [H,rho] = 0.

Write rho_S for its positive block at vacancy set S. Suppose S' is obtained
from S by exchanging a vacancy and an occupied neighbor. The off-diagonal
(S',S) block of [H,rho] = 0 is

    kappa_xy (U_{S'S} rho_S - rho_{S'} U_{S'S}) = 0,

where U is the unitary identification that carries the moved record's entire
K factor with it. H_0 has no off-diagonal occupation block. Since kappa_xy is
nonzero and U is invertible,

    rho_{S'} = U rho_S U^dagger, hence Tr rho_{S'} = Tr rho_S.

## 3. Connectivity of the exclusion configuration graph

For every fixed m, the graph of m-element vacancy subsets joined by allowed
nearest-neighbor vacancy/occupation exchanges is connected. Here is an
elementary proof that does not assume a mixing theorem.

It suffices to retain a spanning tree. Fix a leaf v and a target vacancy set.
If v already has its target status, keep it fixed. If it does not, follow the
tree from v to the nearest site with the opposite status; such a site exists
because the initial and target sets have the same size and disagree at v.
Every preceding site on this path has v's status. Successive exchanges along
the path bring the opposite status to v. Now remove v and work on the remaining
connected tree, whose initial and target vacancy counts agree. Induction on
the number of vertices completes the transformation. The cases m=0 and m=V
are single-configuration graphs.

It follows that Tr rho_S is the same for all S of a given size m. For every
m >= 2 choose a vacancy set containing the endpoints of a birth-source edge.
Its weight is zero by the stationary-support condition in section 2. Thus
every m >= 2 block has zero weight. In the even sector, only m=0 remains.
Every stationary density operator is therefore supported on full occupation.

## 4. Convergence and a finite mean, without a claimed uniform rate

The fully occupied subspace is invariant: hopping and births annihilate it,
dephasing is trivial there, and H_0 preserves it. No trajectory can leave it.
Hence p_full(t) is nondecreasing. The finite-dimensional Cesaro average
rho_bar(T) = T^-1 integral_0^T rho(t) dt has stationary limit points, since
L(rho_bar(T)) = (rho(T)-rho(0))/T tends to zero. Every such limit point is fully
occupied by sections 2-3. Monotonicity then implies p_full(t) -> 1 for every
initial density operator in the even sector.

For completeness, this gives more than convergence in time average. Compress
the semigroup to the complement of full occupation. Because the full subspace
is invariant, this is a completely positive, trace-nonincreasing semigroup
T_t on the transient operator space. Survival for an initial transient state
sigma is Tr(T_t sigma) = Tr(sigma T_t^* I). The positive operators T_t^* I
decrease in t and converge pointwise to zero on every state. In finite
dimension they therefore converge to zero in operator norm. Select t_0 > 0
and c < 1 with ||T_{t_0}^* I|| <= c. The semigroup property gives

    Pr(tau > n t_0) <= c^n,
    E[tau] <= t_0/(1-c).

For an initial state with definite vacancy number, or an incoherent mixture
of such states, tau is the first full-occupation time under the birth-jump
unraveling; its distribution agrees with p_full(t). For an initial coherence
between different vacancy numbers, first measure Q and discard the outcome.
This leaves p_full(t) unchanged: the generator is covariant under exp(i theta Q)
and full occupation commutes with Q. The resulting counted trajectories give
the same completion distribution. A first-hitting interpretation for an
unmeasured superposition of different Q sectors is not being assumed.
Neither t_0 nor c has been bounded uniformly in graph size or in a vanishing
monitoring rate. Internal record degrees of freedom can remain entangled or
undergo H_0 evolution after occupation completes. Full occupation is not a
claim of convergence to a single pure or maximally mixed internal state.

## 5. Exact four-cycle waiting time and singular limits

Use one occupied color, a four-cycle, H_0 = 0, uniform coherent hopping kappa > 0,
pair-birth rate beta > 0 on every edge, and monitoring rate d > 0 at every
site. Initially take the normalized two-vacancy dark state

    |D> = (|{0,2}> - |{1,3}>)/sqrt(2).

Its mean completion time is exactly

    T_D = 1/d + 3/(2 beta) + 1/(beta+d) + 1/[2(beta+2d)]
          + (2d+beta)/(16 kappa^2).

To derive it, exploit only the cycle's symmetry in the six-dimensional
two-vacancy sector. Let o be each of the two opposite-pair diagonal entries,
a each of the four adjacent-pair diagonal entries, c the real opposite-pair
off-diagonal entry, q the off-diagonal entry between adjacent pairs sharing
one site, r that between disjoint adjacent pairs, and i y the coherence with
row an opposite pair and column an adjacent pair. The transient equations are

    o_dot = -8 kappa y,
    a_dot = 4 kappa y - beta a,
    c_dot = -8 kappa y - 2d c,
    q_dot = 4 kappa y - (beta+d) q,
    r_dot = 4 kappa y - (beta+2d) r,
    y_dot = kappa(o+c-a-2q-r) - (d+beta/2)y.

Initially o=1/2, c=-1/2, with the remaining variables zero. By the theorem,
all transient entries tend to zero. Their integrals, denoted capitals, obey

    Y = 1/(16 kappa), A = 1/(4 beta), C = -1/(2d),
    Q_int = 1/[4(beta+d)], R = 1/[4(beta+2d)],
    O = -C + A + 2 Q_int + R + (d+beta/2)/(16 kappa^2).

The survival integral 2O+4A gives T_D above. The runner constructs the full
six-by-six transient density generator directly and verifies this integrated
matrix solves L_trans(X) = -|D><D| entry by entry over symbolic positive
kappa,beta,d. Thus the check does not merely substitute the proposed answer
into the reduced scalar equations.

At kappa=beta=d=1, T_D = 161/48. Its exact limiting behaviors are

    d T_D -> 1               as d -> 0+,
    T_D/d -> 1/(8 kappa^2)   as d -> infinity,
    T_D/beta -> 1/(16 kappa^2) as beta -> infinity.

Weak monitoring eventually frees the dark state but can take arbitrarily
long. Strong monitoring or very rapid birth also slows completion through
backaction. A positive finite-graph theorem alone would conceal both limits.

More generally, start in any exact two-vacancy dark eigenstate and use uniform
monitoring d with jumps sqrt(d) q_x. Before its first monitoring jump the state
only gains a Hamiltonian phase and a no-jump scalar, since sum_x d q_x = 2d I
on this sector; every birth jump annihilates it. Thus

    Pr(tau > t) >= exp(-2dt), and E[tau] >= 1/(2d).

This lower bound uses an equivalent unraveling of the same master equation.
It establishes a singular d -> 0 limit without extrapolating numerical data.

## 6. Verification and scope

`pair_birth_dephasing_check.py` also builds the complete four-site
even-vacancy-sector Liouvillian (Hilbert dimension 8, operator dimension 64).
At unit positive parameters its exact stationary-operator nullities are:

| Case | Nullity |
| --- | ---: |
| Birth on all edges, monitoring, hopping | 1 |
| Birth on all edges, no monitoring, hopping | 4 |
| Birth on one edge, monitoring, hopping | 1 |
| No birth, monitoring, hopping | 3 |
| Birth on all edges, monitoring, no hopping | 3 |

It checks trace preservation, full occupation as a stationary state, count
preservation by hopping/monitoring, and the decrease by two for every birth.
The final run uses exact Gaussian-rational DomainMatrix elimination. An
earlier generic symbolic rank calculation was stopped after more than six
minutes and is archived with its source and interrupted logs; it was a
performance interruption, not a failed scientific assertion.

The analytic theorem covers internal record spaces that this one-color runner
does not numerically enumerate. Its load-bearing step is the unitary transport
map between neighboring occupation blocks. A hop that projects or erases
record content, a disconnected movement graph, or a restricted configuration
graph needs a different proof. No claim has been made for the old model with
permanent partner adjacency constraints.

Monitoring, the coherent hop, and the pair-birth instrument are supplied
physical assumptions. The result does not derive them, choose their rates,
prove Lorentz invariance, or identify a quantum field phase. It does show that
irreversible record creation and content-preserving coherent motion admit a
conditional finite quantum construction with reliable reuse of vacant sites.
