# Blind finite-rate formation reconstruction

The supplied finite-graph model has a controlled local effective Lindblad
limit for arbitrary initial densities supported on P, including internal and
field coherences. An explicit second-order density-map intertwiner proves an
O(epsilon) trace-norm error on each fixed time interval. Its constants can be
chosen independent of the link spin S at fixed graph. No invertibility of the
entire fast population generator is assumed or needed.

Eventual filling is false. On the four-leaf star, the initially occupied A
center reaches a six-dimensional nonfull dark subspace with probability 1/3
for resolved births and 4/15 for coherent births. The respective full-filling
probabilities are 2/3 and 11/15. These are exact for every epsilon,delta,kappa>0
and every integer S>=1 on that example, as well as for the effective process.
Thus subsequent probabilities distinguish the two instruments even though
their bare loss operators agree.

This is a pre-author-source reconstruction of the neutral supplied model.
The independent checker, its complete logs, a separately assembled charge-word
control, and the preserved helper-labeling failure are included. No new author
formation/locality files or results have been accessed. This is scientific
evidence, not an audit or publication determination.

## 1. Exact generator and loss

Write V=delta T, ell_j=sqrt(kappa)j, and

    L_epsilon = epsilon^-2 L0 + epsilon^-1 L1,
    L0(rho) = -i[delta W,rho] + sum_j D[ell_j](rho),
    L1(rho) = -i[V,rho].

Here j denotes the supplied resolved or coherent channel list. The finite
physical Hilbert space is invariant. Hopping preserves total record number N,
births increase it by two, and each birth fills exactly one A vacancy:

    [W,j] = -j,       jP=0,       PVP=0.

Hopping changes W only by +/-1. The two charge-resolved outputs are orthogonal,
so j_+^dagger j_-=0. Consequently the *loss* is identical in the two instruments:

    Gamma = sum_j ell_j^dagger ell_j
          = 2 kappa sum_e q_vac(x) q_vac(y)
                         [1-E_e^2/(S(S+1))].                  (1)

This identity includes the spin endpoints; the vanishing forbidden shift is
already accounted for. Gamma commutes with W and is positive. It does not make
the recycling maps equal: resolved recycling omits j_+ rho j_-^dagger and its
adjoint, which coherent recycling retains.

At finite epsilon the exact population identity is

    d E[N]/dt = 2 epsilon^-2 Tr(Gamma rho_t) >= 0.             (2)

This is monotonic expected population, not a completion theorem. Parity,
capacities, spin constraints, or coherent dark subspaces may prevent filling.
For the closed finite graph Gauss gives total signed charge |A|; full occupancy
is even compatible with that parity only when |B| is even. The star
counterexample below satisfies this necessary condition.

## 2. Effective operators, including recycling

Let Q_m project onto W=m, and regard P Hilbert space as isometrically embedded
in the full space. Define operators on Q_m, for m>=1,

    K_m = m delta I - i Gamma_m/2,   R_m=K_m^-1,
    ||R_m|| <= 1/(m delta).

The nonzero real detuning, not a fast dissipative gap, establishes this bound.
Set

    V_+ = Q1 V P,             V_- = V_+^dagger,
    X = -R1 V_+,
    Z = -R2 Q2 V Q1 X.                                      (3)

Z is zero if there is no W=2 sector. With the final P projection understood,

    H_eff = -1/2 V_- (R1+R1^dagger) V_+,
    J_eff,j = ell_j X = -ell_j R1 V_+.                       (4)

Every J_eff,j maps P into P and increases N by two. H_eff preserves N. The
effective generator is

    L_eff(rho) = -i[H_eff,rho] + sum_j D[J_eff,j](rho).        (5)

The minus sign common to an individual J_eff has no effect on its dissipator;
relative route and charge amplitudes inside one channel must be retained.
In particular, coherent effective births combine the two charge amplitudes
before forming the dissipator. Neither implementation is a rule that measures
the intermediate configuration or selects a single virtual hopping route.

To verify (5), let Z0=V_-X. Since

    R1-R1^dagger = i R1^dagger Gamma_1 R1,
    Z0-Z0^dagger = -i sum_j J_eff,j^dagger J_eff,j,

the P block -i(Z0 rho-rho Z0^dagger), together with the returned recycling,
is exactly (5). Omitting recycling would give a nonconservative evolution and
would miss all repeated formation.

## 3. Complete fixed-time error proof

For an operator rho on P define full-space linear maps

    S0(rho)=rho,
    S1(rho)=X rho + rho X^dagger,
    S2(rho)=X rho X^dagger + Z rho + rho Z^dagger
            -1/2 {X^dagger X,rho}.                          (6)

The last anticommutator lies in the P block. These maps preserve Hermiticity;
Tr S1=Tr S2=0. Direct block multiplication gives the exact identities

    L0 S0=0,
    L0 S1+L1 S0=0,
    L0 S2+L1 S1=S0 L_eff.                                   (7)

The Q1-Q1 block of L1 S1 cancels against L0(X rho X^dagger).
The recycling of that latter term lands in P and produces
sum J_eff rho J_eff^dagger. The Q2-P block is canceled by Z rho and its adjoint.
The normalization term in (6) is annihilated by L0. These observations prove
(7) without discarding multiple-A-vacancy configurations. No Q_m population
resolvent or inverse of L0 is used.

With E_epsilon=S0+epsilon S1+epsilon^2 S2, (7) implies the exact defect

    L_epsilon E_epsilon - E_epsilon L_eff
      = epsilon (L1 S2-S1 L_eff)-epsilon^2 S2 L_eff.          (8)

Although the truncated E_epsilon need not be positive, this does not obstruct
the estimate. Both physical and effective semigroups are completely positive
and trace preserving, hence contract trace norm on Hermitian inputs. For
sigma_t=exp(t L_eff)rho_0 and rho_0 supported on P, Duhamel and (8) give

 ||exp(tL_epsilon)rho_0-sigma_t||_1
 <= 2(epsilon a+epsilon^2 b)
    + t[epsilon(2v b+a ell)+epsilon^2 b ell],                (9)

where v=||V||, a bounds ||S1|| on Hermitian trace-class inputs, b bounds ||S2||,
and ell bounds ||L_eff|| there. This includes the bare initial layer through
||rho_0-E_epsilon rho_0||_1; no dressed initial-state hypothesis is required.
The derivation is uniform over all initial P density matrices, including
coherences between different allowed N sectors.

For a graph with m edges, each edge hopping block has norm at most one, so
||T||<=m. Both channel conventions obey sum_j ||ell_j||^2<=2 kappa m. It is
therefore sufficient to use

    v=delta m,        a=2m,        b=3m^2,
    ell=2m^2(delta+2 kappa m).                              (10)

Indeed ||X||<=m, ||Z||<=m^2/2 and
||S2||<=2||X||^2+2||Z||. For 0<epsilon<=1 and 0<=t<=T,
(9) is at most C_graph,delta,kappa,T epsilon, with

    C=2(a+b)+T[2v b+(a+b)ell].                              (11)

These deliberately loose constants are explicit, independent of S, and not
uniform in graph volume. Finite dimensionality is used for the elementary
semigroup presentation, not for an S-dependent gap. The same bounded-operator
argument works directly on the finite-graph unit-rotor Hilbert space.

The complete S=1 path control tests (7) exactly on all 16 P matrix units for
both instruments at delta=2,kappa=3. Its W multiplicities are 4,4,1; Z is
nonzero. There are lossless excited basis states with W=1 and W=2. Thus an
argument asserting that the entire fast excited density sector decays would
already fail on this requested example, while (7)-(9) still hold.

## 4. Locality and the fixed-graph spin-to-rotor limit

Split V_+ by the A site a whose vacancy is created: V_+=sum_a V_a. In the W=1
sector the hole location a is definite and Gamma is diagonal. Its loss only
sees the vacant B neighbors of a and the corresponding link fields. On that
sector the inverse is the local diagonal function

 R_a = [delta-i kappa sum_{b~a, b vacant}
                          (1-E_ab^2/(S(S+1)))]^-1.          (12)

Returning to P requires either refilling that same a by a hop or forming a
pair there. Therefore H_eff is a sum of star-supported terms
-V_a^dagger(R_a+R_a^dagger)V_a/2, and each effective birth is star-supported.
This is finite-range locality, despite the nonpolynomial local denominator.
The Hamiltonian includes two-hop record rearrangements through the same A
site when other B neighbors are occupied. It is not just a diagonal energy
shift. For general edge orientations the shifts acquire the usual orientation
sign; (1), (12), support, and the argument are unchanged.

Embed the spin electric basis into the unit-rotor basis l^2(Z), extending its
weighted shift by zero outside [-S,S]. Then U_S and U_S^dagger converge
strongly to the bilateral rotor shifts, with uniform operator norm at most
one. The finite sums V_S, Gamma_S converge strongly on the full finite-graph
space. The inverses in (3) converge strongly by the resolvent identity and
their uniform 1/(m delta) bounds. Consequently H_eff,S and each J_eff,S and
their adjoints converge strongly, with uniformly bounded norms.

It follows first on finite-rank trace-class operators, and then by trace-norm
density, that the effective generators converge strongly on trace class.
Duhamel gives convergence of their semigroups uniformly on compact times for
every family of embedded initial densities rho_S -> rho in trace norm.
Physical initial densities can be approximated by normalized electric cutoffs:
these cutoffs commute with P and every Gauss operator. The S-independent (9)
then gives, for any such family and any joint epsilon->0,S->infinity,

 sup_{t<=T} ||rho_{epsilon,S}(t)-exp(tL_eff,rotor)rho||_1 ->0. (13)

There is no claim of operator-norm convergence of U_S, a rate for arbitrary
trace-class tails, a uniform volume limit, or a limit uniform over all
S-dependent initial states. This bare model contains no unbounded electric
energy term; adding one would require a separate domain/moment analysis.

## 5. Complete finite sectors and repeated-birth counterexample

For all tree controls the electric values determine the matter charge through
Gauss. The independent builder enumerates every electric tuple in [-S,S]^m,
retaining exactly those with q_x in {0,+1,-1}. It then assembles every legal
hop and every resolved birth, with exact spin amplitudes; coherent channels
are their sums. It verifies Hermiticity, Gauss-preserving indexing, W changes,
and (1). It does not restrict the basis to configurations believed reachable.

### Two B leaves

The full sector has six states: three one-record positions and three full
three-record states. Start with the A center occupied by + and both leaves
vacant, all E=0. The effective first-birth rate is

    r_2=4 kappa delta^2/(delta^2+kappa^2).                    (14)

That one birth fills the graph with probability one. Resolved and coherent
births have the same final diagonal probabilities: minus at the center with
probability 1/2 and at either leaf with probability 1/4. Their terminal
densities differ: the first-event purities are respectively 3/8 and 5/8.
There is no subsequent nontrivial motion when all sites are occupied.

The exact finite-epsilon first-birth mean is

    E tau_1=1/r_2+epsilon^2/kappa.                           (15)

It follows by solving the no-event two-level Lyapunov equation, not by
assuming exponential waiting at finite epsilon.

### Four B leaves

The full sector has 45 states, of which 29 have W=0. At N=3 the P and Q1
dimensions are respectively 18 and 12. All legal star shifts have amplitude
one, for every S>=1, because leaf Gauss permits only E=0,+1,-1 and every legal
shift connects zero to +/-1. These sector dimensions and exact matrices are
therefore independent of S.

Index the leaves by 0,1,2,3. In the 18-dimensional P,N=3 space let u_ij denote
center +, leaf i +, leaf j -, and v_ik=v_ki denote center -, leaves i,k +.
The positive hopping incidence A has one row for each Q state with plus
leaves i,k and minus leaf j, all distinct. Its row contains

    u_ij + u_kj + v_ik.                                     (16)

There are 12 such rows; rank A=12 and dim ker A=6. Every vector in this kernel
is annihilated by the *full* T, W, and every birth operator. It is an exact
nonfull dark state, not merely an effective-order cancellation. The separately
assembled charge-word checker obtains eigenvalues of A A^T as

    6 (once), 5 (three times), 3 (twice),
    2 (three times), 1 (three times).                        (17)

Starting with the lone + center, before the first birth only that state and
the symmetric superposition of the four one-record leaf states are involved.
The excited loss is 6 kappa/epsilon^2 times identity there. Every first-birth
channel thus produces, apart from one common time-dependent amplitude,

    p_c=sum_{b!=c} u_bc,       m_c=sum_{b!=c} v_{bc}.

The normalized post-first-birth densities are exactly

    rho_res = (1/24) sum_c (p_c p_c^dagger+m_c m_c^dagger),
    rho_coh = (1/24) sum_c (p_c+m_c)(p_c+m_c)^dagger.         (18)

The first birth happens with probability one. Its effective rate and exact
finite-epsilon mean are

    r_4=24 kappa delta^2/(delta^2+9 kappa^2),
    E tau_1=1/r_4+epsilon^2/(3 kappa).                       (19)

Let D=I-A^T(AA^T)^-1 A, the exact orthogonal dark projector. Direct rational
calculation, performed once from full electric matrices and independently
from (16), gives

    Tr(D rho_res)=1/3,       Tr(D rho_coh)=4/15.              (20)

For completeness, the N=3 transient Hamiltonian in P,Q1 blocks is

    [ 0, -delta A^T/epsilon;
      -delta A/epsilon, delta I/epsilon^2 ],

and the Q1 loss is 2 kappa I/epsilon^2. Singular-value decomposition of A
reduces every bright block to a damped two-level system with strictly
positive coupling and loss. Each such block decays completely into a second
birth, whereas ker A is stationary. This proves, for the full finite-epsilon
model, that the dark weights (20) are the only surviving nonfull weights.
The second birth necessarily fills the five-site star.

| Implementation | Full-filling probability | Expected total births | Terminal E[N] |
| --- | ---: | ---: | ---: |
| Resolved | 2/3 | 5/3 | 13/3 |
| Coherent | 11/15 | 26/15 | 67/15 |

Both births, when they occur, take place at the same A center. This explicitly
tests repeated formation after a record has moved away. Coherent births do
not guarantee completion; their higher completion probability in this example
is not asserted to be a universal ordering. Because the trapped probability
is positive, the unconditional hitting time of full occupation has infinite
mean here.

### Path A0-B1-A2-B3

The S=1 full physical sector has nine states and P dimension four. At S=2 an
additional full state becomes allowed, giving ten states. The S=1 exact
intertwiner check includes the W=2 state with both B sites occupied and both
A sites vacant. This state has no bare birth loss. A W=1 lossless state also
occurs. Both are retained in the full generator and in the block calculation.

The six-dimensional N=2 transient sector has three lossless basis states.
The hopping boundary from these three states to positive-loss states has rank
two. Its remaining kernel is one basis vector, which hopping immediately
maps outside that kernel; the diagonal W term cannot cancel this escape.
Thus no nonzero loss-free invariant subspace exists. The path fills after one
birth almost surely for every positive epsilon,delta,kappa and every S>=1.
`path_absorption_control.py` verifies this exact boundary-elimination argument
at S=1,2; the N=2 hopping matrix and positive-loss support do not change at
larger S. This graph-specific result does not remove the star counterexample.

As a numerical corroboration only, the independently assembled full S=1
Liouvillian at delta=kappa=1, initial plus records on both A sites, t=0.7 gives
the following trace-norm distances to the effective state:

| epsilon | Resolved | Coherent |
| --- | ---: | ---: |
| 0.2 | 0.208476774358 | 0.211471254816 |
| 0.1 | 0.160145649581 | 0.160350270637 |
| 0.05 | 0.0601994470042 | 0.0602126718951 |

Trace defects are below 9.2e-15; negative eigenvalues are numerical roundoff.
These three points do not establish a rate by regression. The rate is proved
by (6)-(11), and the controls test signs, recycling and W=2 normalization.

## 6. Evidence, failure preservation, and limits

`finite_control.py` builds complete physical sectors and exact operators;
`star_analytic_control.py` independently constructs the 12-by-18 charge-word
incidence, the rational projector and first-event densities, and the exact
two-level mean. `run_control.py` records command, timestamps, exit status,
source identity and both complete streams. `path_absorption_control.py` tests
the path's exact loss-free invariant-subspace elimination, reusing only the
independent sector builder. All three final controls exit zero. Complete
results are in FINITE_CONTROL_RESULTS.json, STAR_ANALYTIC_RESULTS.json and
PATH_ABSORPTION_RESULTS.json.

The first finite-control run contained a helper interpretation error: it
reported every N=3 dark state as a *nonfull* trap even on the two-leaf star,
where N=3 is already full. That incorrect field, original source, both streams,
receipt and diagnosis are preserved under
failed_attempts/full_dark_vs_nonfull_dark_label/. The correction separates
exact dark weight from nonfull trapped weight and simplifies scalar displays;
no matrix or physical parameter was changed. The original exit-zero output
is not presented as a correct completion assertion.

The proof does not use finite-matrix evidence as a replacement for an
all-graph argument. Conversely the graph-specific absorption probabilities
are not promoted to a universal classification. Fixed finite time is distinct
from infinite-time completion; the latter was independently analyzed on the
stars. The local target does not by itself furnish a volume-uniform error.
No fuel source, microscopic energy conservation, physical photon regime,
native-site encoding, or axiom derivation is established. Positive bare
formation intensity and a monotone population do not remove the demonstrated
coherent traps.

All source and evidence identities, including preserved failures, are listed
in PRE_COMPARISON_SEAL.json. No author-source comparison is included in this
report; any later comparison must be a separate file and preserve this seal.
