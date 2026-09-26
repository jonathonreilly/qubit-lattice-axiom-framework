# Independent autonomous-carrier and formation-count reconstruction

The supplied carrier implements an exact arrival-weighted gate channel. The
specified compact packet gives an explicit uniform later-time error bound,
but has a strictly positive asymptotic wrong-direction probability at every
fixed finite M. The birth model has a bounded conserved observable
chi^((K-N)/2) T, including chi=0. The specified monitored ring completes and
has terminal density (I+chi^(K/2) T)/2 on its two full physical states.

Two hypothesis distinctions are essential. The electric-monitoring dual law
needs [E_e,N]=0 in addition to the two displayed E/T relations. Arbitrary
additional N,T-commuting jumps preserve the count identity but need not
preserve occupation completion. Exact countercontrols for both statements
are included. Neither distinction invalidates the physical electric fields
or the ring with only the specified monitoring, hopping, H0 and births.

This report is sealed before any new author autonomy, count, clock or ring
observability source or result is opened. It is a selective mathematical
check, not a publication or audit decision.

## 1. Exact rail reduction and its physical boundary

Write S|j>=|j+1>, H_w=-J(S+S*), and assume J>0 for the supplied right-moving
packet. The bounded bilateral Hamiltonian and the step unitary W give

    H_g = -J sum_(j != 0) (|j+1><j| tensor I + adjoint)
          -J (|1><0| tensor U + |0><1| tensor U*).                 (1)

Thus the only dressed rail bond is 0--1. This is locality on the supplied
rail coupled to the finite system/probe gate support; it is not a proof of
a native single-site-qubit or fixed three-dimensional embedding.

Let the normalized initial rail packet be wholly in j<=0 and independent
of an arbitrary system/probe density sigma. W* acts trivially on this input.
Putting psi_t=exp(-it H_w)psi and p_t=sum_(j>=1)|psi_t(j)|^2, the exact
evolution is W(|psi_t><psi_t| tensor sigma)W*. Tracing the rail gives

    Phi_t(sigma) = (1-p_t) sigma + p_t U sigma U*.                (2)

The statement remains valid with an arbitrary reference system entangled
with sigma. In particular ||Phi_t-Ad_U||_diamond <= 2(1-p_t). A rail/input
correlation, or an initial right-side component, requires a different
initial-state calculation; neither is silently included here.

For a fresh fuel probe the local algebra V*V=P, VV*=R, PR=0 and V^2=0 gives
C^3=C and U=I+(cos(theta)-1)C^2-i sin(theta)C. After tracing the probe the
arrival branch has Kraus operators

    M_0=I+(cos(theta)-1)P,       M_1=-i sin(theta)V.

The actual reduced system channel is (1-p_t)Id+p_t E_theta. Its formation
probability is p_t sin^2(theta) Tr(P rho), not p_t on arbitrary inputs.
Here 1-p_t is an arrival/gate-error bound, not a universal birth-failure
probability. It can overestimate channel error, for example when U=I.

Since [N_record,V]=2V, C commutes with

    C_count=N_record+2 P_fuel.

W and H_g also commute with it. For m>=0 the supplied rest energy m C_count
is positive, commutes with the gate Hamiltonian, and can be added without
changing rail transport. More precisely the channel in (2) then has the
common conjugation exp(-it m C_count) around both branches. That phase is
irrelevant in a fixed C_count sector, but not on arbitrary superpositions
of sectors. Because H_g is unitarily equivalent to H_w tensor I,
H_g+m C_count+2J I is positive. The last shift is a constant energy zero.
This proves conservation for that supplied rest-energy assignment; no
arbitrary interacting field/kinetic energy conservation is inferred.

## 2. Packet moments, uniform later-time bound and directional limit

Let Z_M=binomial(2M,M), M>=1, L>=M, and

    psi(-L+r)=i^r binomial(M,r)/sqrt(Z_M),   0<=r<=M.

Vandermonde's identity normalizes the state. Use the Fourier convention
hat(psi)(k)=sum_j exp(-ikj)psi(j). Its density is

    |hat(psi)(k)|^2 = [2(1+sin k)]^M / Z_M,

with measure dk/(2pi). The position velocity is
V_w=i[H_w,X]=iJ(S-S*) and has symbol 2J sin k. It commutes with H_w, so
X(t)=X+t V_w on the position domain. Direct binomial sums give

    E X = -d,                 d=L-M/2,
    Var X = a=M^2/[4(2M-1)],
    E V_w = v=2JM/(M+1),
    Var V_w = b=4J^2(2M+1)/[(M+1)^2(M+2)],
    (1/2) E{X-E X,V_w-E V_w}=0.                                (3)

For example <S>=-i M/(M+1), <S^2>=-M(M-1)/[(M+1)(M+2)]. The symmetrized
position/velocity covariance vanishes because the adjacent-binomial product
is symmetric about the packet center. Consequently

    E X(t)=vt-d,              Var X(t)=a+bt^2.

The spectral measurement of X(t) is an ordinary real random variable. Its
one-sided variance inequality therefore yields, for t>d/v,

    1-p_t <= (a+bt^2)/[a+bt^2+(vt-d)^2].                        (4)

This is also a uniform bound for every later time t>=T>d/v, with the right
side evaluated at T. Indeed r(t)=(a+bt^2)/(vt-d)^2 has derivative
-2(btd+va)/(vt-d)^3<0, and the displayed bound is r/(1+r). This is a
monotone upper bound, not a claim that p_t itself is monotone.

One fully explicit choice is T=2d/v. At every t>=T,

    1-p_t <= A_M/(1+A_M),
    A_M = a/d^2 + 4b/v^2
        <= 1/(2M-1) + 4(2M+1)/[M^2(M+2)].                      (5)

This tends to zero as M grows, with the stated time/packet preparation.
For fixed M the exact infinite-time error is smaller but nonzero:

    lim_(t->infinity)(1-p_t)
      = delta_M
      = integral_(sin k<0) [2(1+sin k)]^M dk/(2pi Z_M)
      = I_(1/2)(M+1/2,1/2),
    0 < delta_M <= 2^(M-1)/Z_M.                                (6)

Here I is the normalized incomplete beta integral; the preceding elementary
integral is its definition for this purpose. In particular
delta_1=1/2-1/pi and delta_2=1/2-4/(3pi). The inequality uses 1+sin k<=1 on
the negative-velocity half of the circle. It decays exponentially in M, but
does not vanish at any fixed finite M. L changes the waiting distance, not
this directional limit. With J<0 the direction reverses; J=0 does not
transport the packet.

For completeness, the limiting step is not imported from an unverified
walk theorem. X(t)/t=V_w+X/t. On the finite-support packet,
||X exp(is V_w)psi|| <= ||X psi||+|s| ||[X,V_w]||. Duhamel's formula applied
to characteristic functions thus shows convergence of the spectral law of
X(t)/t to that of V_w. The latter has no atom at zero under the continuous
Fourier density above, so its distribution at the left/right cut converges.

The whole evolution remains reversible. A returning carrier applies U*,
and a finite rail can recur. The directed packet, fresh fuel preparation,
infinite rail, and discarding/ignoring the outgoing carrier are explicit
resources. Equation (2) is not a Markov birth semigroup, and this single
carrier does not establish an autonomous supply of infinitely many fresh
probes or permanent formation at every intermediate time.

## 3. Count-weighted dual law

Take a finite-dimensional system with even N in {0,2,...,K}, K even, and
write m=N/2 and M_*=K/2. T is a unitary involution, hence Hermitian, and
commutes with N. The local branch algebra gives V_+*V_-=0, orthogonal
vacancy-domain projections P_+ and P_-, and P_e=P_++P_-. The stipulated
common loss is Gamma_e=beta_e P_e. From T V_+=V_- T and its reverse,

    sum_mu J_(e,mu)* T J_(e,mu) = chi Gamma_e T.                (7)

For every real function f of the even count,

    L* [f(N)T] = Gamma [chi f(N+2)-f(N)]T,
    Gamma=sum_e Gamma_e,                                      (8)

on nonfull sectors; the full-sector loss is zero. H and any other jumps
commuting with both N and T contribute zero. For such jumps their adjoints
also commute with f(N)T, so this cancellation does not require unitality.
Likewise L*N=2 Gamma.

Set

    A_chi = chi^((K-N)/2) T,                                  (9)

using 0^0=1. Then ||A_chi||<=1 and L*A_chi=0. At chi=0 it is exactly
Pi_(N=K) T, so no inverse power or limiting division is needed. At chi=-1
it includes the parity of the number of missing pairs. The conclusion is
independent of the positive edge rates beta_e. It does use a common real
chi, the branch-exchange action of T, and the stated N/T symmetries.

For additional Hermitian field-monitoring jumps sqrt(delta_e) E_e with

    E_e^2=I/4,    {E_e,T}=0,    [E_e,N]=0,

one obtains D_(E_e)* A_chi=-(delta_e/2) A_chi. Hence

    E A_chi(t) = exp[-t sum_e delta_e/2] E A_chi(0).             (10)

The count commutator is indispensable in the abstract extension. An exact
four-dimensional counterexample is
N=diag(0,2) tensor I, T=I tensor sigma_x,
E=(sigma_x tensor sigma_z)/2, chi=1/2, K=2.
It obeys E^2=I/4 and {E,T}=0 but not [E,N]=0. The residual
D_E*A_chi+A_chi/2 has off-diagonal entries -1/8 in the first two-dimensional
block and +1/8 in the second. The physical electric fields in the ring are
diagonal in the bit basis and do satisfy [E,N]=0.

## 4. Ring completion and terminal density

The physical ring Hilbert space has basis b in {0,1}^K, with
Q_i=b_i-b_(i-1), n_i=b_i xor b_(i-1), and T the bit complement. Every
occupation pattern has even N and exactly two complementary preimages.
For K even the full sector consists of the two alternating bit words.

Flipping b_i toggles n_i and n_(i+1). The hop condition
b_(i-1) != b_(i+1) is equivalent to these occupations being unequal, so an
ordinary hop lifts precisely one adjacent particle/vacancy exchange. Each
such off-pattern map is the nonzero scalar hop amplitude times a unitary
between the complete two-dimensional occupation fibers. Adjacent exchanges
connect all occupation patterns with a fixed N: one can sort the binary
occupation word along a cut-open chain using adjacent swaps. Every lifted
hop component consequently projects onto all those patterns.

For N<=K-2, some such pattern has two neighboring holes, and that pattern
has positive birth loss. The N=0 fibers are already birth-active. The
partial-bijection completion criterion therefore holds at every nonfull
level. This uses nonzero hop amplitudes, positive occupation monitoring on
every site, a nonempty accessible positive birth set (in the supplied model
every edge has beta_e>0), and occupation-preserving H0. Coherent births with
any real chi in [-1,1] have the same scalar vacancy loss, so the criterion
does not require resolving charge orientation or measuring the field.

One can also see the key argument directly. In a stationary density the
monotone count forces Tr(Gamma rho)=0, so all birth terms vanish. The
Hilbert-Schmidt inner product with the remaining Hamiltonian/dephasing
equation forces [rho,n_i]=0. Off-pattern commutator blocks then propagate
equal positive traces through the unitary hop maps. Any nonfull component
reaches a positive-loss occupation fiber, forcing all its traces to zero.
Thus every stationary density is full. The transient corner is a finite
trace-decreasing positive semigroup; a nondecaying corner would have a
nonzero stationary positive density by finite-dimensional averaging.
Therefore its spectral bound is strictly negative, yielding fixed-model
constants C,c>0 with noncompletion probability <=C exp(-ct), and a finite
mean first-completion time. No size-uniform rate follows.

For the stated empty cat (|00...0>+|11...1>)/sqrt(2), the initial count is
zero and T expectation is one. The birth generator is T-covariant because
chi is real and both branches have the same loss beta_e. The occupation
monitors are T-invariant; the hopping and H0 must commute with T, as in the
specification. Thus T rho(t) T=rho(t). On the full two-dimensional sector
this symmetry makes the density a linear combination of I and T. Completion
and (9) then determine the actual limit:

    rho_infinity = (1/2) [[1, chi^(K/2)], [chi^(K/2), 1]],        (11)

in the two alternating-bit states. The full restriction of H0 commuting
with T cannot rotate this state, and occupation monitoring acts trivially
there. No spatial uniformity of the nonzero hop amplitudes, positive birth
rates or positive monitoring rates is required. The full physical density
is not claimed to be uniquely stationary for arbitrary initial states.

With fixed nonzero total physical electric-monitoring rate, completion
still holds (the added Hermitian monitoring only strengthens the
Hilbert-Schmidt dissipation), while (10) and T covariance instead give the
limiting equal mixture I/2. If that monitoring is absent, (11) includes
chi=0 and both endpoints +/-1. Dropping T covariance or changing the
initial state does not in general leave (11) unchanged. Odd K has no full
physical alternating word and is excluded; K=2 is not the supplied simple
ring geometry.

## 5. A scope countercontrol: count identity is broader than completion

Additional arbitrary N,T-commuting jumps are harmless for (8), but their
dissipation can offset the hopping equation used by the completion proof.
Here is an exact example within the physical four-ring Hilbert space.
Let H be the sum of unit-amplitude hop matrices and let P project onto
occupation pattern (1,0,1,0), namely bit states 3 and 12 in the checker's
least-significant-bit-first convention. This pattern has no adjacent holes,
so Gamma P=0. Also P H P=0 and P commutes with N,T. Define

    rho=P/2,              L=P+2i P H.

L commutes with N and T, and D_L(rho)=i[H,rho]. Consequently the Hamiltonian
and this dissipator cancel exactly. Occupation monitoring and all birth
maps vanish on rho. It is a stationary nonfull density with N=2. This
counterexample does not belong to the specified monitored-Hamiltonian ring;
it prevents extending its completion result to every broader commuting
jump allowed in the count identity. The parent was notified before any
author-source comparison and confirmed that these scopes are intended to
remain separate.

## 6. Independent controls and reproducibility limits

Both standalone scripts passed their first executions. No failed scientific
or helper attempt occurred in this packet. Complete stdout, empty stderr,
command receipts and full result JSON files are preserved.

`carrier_check.py` checks all rational moment formulas for M=1,...,16 at
two offsets each, including the symmetrized covariance. It evaluates (6)
at high precision and separately sums the bilateral Bessel propagator at
four times for six packet sizes. The latter numerical sums have total
mass within 2.3e-14 of one in these tests and obey (4). They are controls,
not a substitute for the analytic uniform proof. A separately assembled
13-site reflecting rail and arbitrary mixed system/probe input give an
arrival-mixture residual about 1.1e-16, a dressed-bond residual about
1.2e-15, and zero rest-energy commutator. That finite rail test makes no
infinite-time claim.

`count_ring_check.py` builds physical bit states directly. For K=4,6,8,10,
every nonfull hop component contains a birth-active state, and every
nontrivial component projects onto all fixed-N occupation patterns.
Exact symbolic K=4 controls verify (8)-(10), including chi=0, L*N=2Gamma,
and both counterexamples above. A complete 256-dimensional Liouvillian is
assembled independently with nonuniform hops, birth and occupation
monitoring, and nonzero occupation/T-preserving H0. For chi=-1,-1/2,0,1/2,1
and an extra electric-monitoring case, its evolution agrees with the dual
law and approaches (11) or I/2 to below 1.7e-14 in the tested final block.
These finite numerical tolerances are not rigorous spectral-gap bounds.

The same control explicitly distinguishes terminal selection from the
clock: at t=1 the full probabilities for chi=-1 and +1 are approximately
0.397404 and 0.427687 for the chosen nonuniform model. Equal vacancy loss
and the terminal count law do not imply identical interacting histories.

Reproduce with `python3 carrier_check.py` and `python3 count_ring_check.py`
from this directory. The scripts import standard numerical/symbolic
libraries only, no author checker. No new external literature is needed.
The seal records exact dependency and output identities; the previously
checked corrected local algebra and partial-bijection theorem are reused
only at their verified bytes. No autonomous stream, all-state quantum
controllability, thermodynamic completion rate, native-site realization,
or unchanged permanent-record projector dynamics is inferred.
