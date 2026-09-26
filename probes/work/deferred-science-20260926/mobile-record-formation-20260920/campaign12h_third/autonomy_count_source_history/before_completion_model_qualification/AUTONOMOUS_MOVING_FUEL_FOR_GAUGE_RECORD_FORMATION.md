# Autonomous moving fuel implements a conditional record-formation channel

Date: 2026-09-22. Status: author construction with explicit hypotheses;
exact and analytic controls below. Independent check pending. This is a
supplied infinite-rail model, not a native M2-per-site dynamics or a derivation
of a physical clock, initial fuel state, or exact continuous record permanence.

## 1. Replace timed switching by a fixed spatial interaction

The fresh-probe construction specifies a unitary U on a local gauge/matter
system and a neutral fuel/spent qubit. Let

    V=V_+ + V_-,  P=V^dagger V,  R=VV^dagger,
    C=V tensor |spent><fuel|+V^dagger tensor |fuel><spent|,
    U=exp(-i theta C).

The preceding finite identities give [U,G_x]=0 and [U,D]=0, where
D=N_record+2 P_fuel. A fresh fuel qubit produces the channel Phi_theta with
Kraus operators I-P+cos(theta)P and -i sin(theta)V. Here these identities
are reused as premises and also reconstructed in the finite checker.

Give the probe a position on an infinite nearest-neighbor rail Z. Its
position and internal fuel/spent state together describe one carrier.
Supply a fixed hopping strength J>0 and define

    H_walk=-J sum_j (|j+1><j|+|j><j+1|),
    W=sum_(j<=0) |j><j| tensor I + sum_(j>=1) |j><j| tensor U,
    H_gate=W(H_walk tensor I)W^dagger.

Only the rail link 0->1 differs from ordinary hopping: its forward matrix
element is -J U, and its reverse matrix element is -J U^dagger. This is a
bounded self-adjoint Hamiltonian with norm 2J. All other rail links transport
the carrier without acting on the system. In a second-quantized description
restricted to one carrier, each rail site has states empty/fuel/spent; the
special link couples its two endpoint sites to the nearby matter pair and
gauge link. Thus it is finite range in this supplied rail geometry, although
its interaction is a deliberately engineered multi-body operator.

This use of a unitary-weighted clock link is established Feynman Hamiltonian
machinery. Section 2.1, equations (1)-(3), of
[Caha, Landau and Nagaj, arXiv:1712.07395v2](https://arxiv.org/abs/1712.07395v2)
provides the contextual construction. Here a single gate is used, with an
infinite outgoing lead and explicit preparation/error estimates. No new
general autonomous-computation principle is claimed.

The repository already contains the enlarged-cell discrete-time record-export
QCA of July 14 and the repeated energy-conserving Record apparatus note of
September 5. Both source notes were read completely at main revision
dee2310d375f37a0ca4c8641e9a12aa7fabb8577; their runners were not replayed or
imported. The former already exposes no-return and fresh-resource assumptions;
the latter supplies a more general spectral battery for changing matter
Hamiltonians while leaving spatial implementation and autonomous timing open.
The present difference is a continuous-time spatial passage with an explicit
uniform later-time error, applied to the local gauge-pair channel. Its simple
commuting rest-energy account is narrower than that earlier battery theorem.

## 2. Exact reduced dynamics and conserved energy

Prepare any normalized rail packet psi entirely on j<=0, independently of
an arbitrary local density sigma. Since W is identity on this input,

    exp(-it H_gate)(|psi> tensor |a>)
      = W[(exp(-it H_walk)|psi>) tensor |a>].

After tracing position, the joint system/probe density is exactly

    (1-p(t)) sigma + p(t) U sigma U^dagger,
    p(t)=sum_(j>=1) |(exp(-it H_walk)psi)_j|^2.

For a fresh fuel probe, tracing its internal state gives

    Psi_t=(1-p(t)) Identity_channel+p(t) Phi_theta.

This identity holds on arbitrary system inputs, including inputs entangled
with a reference. Consequently

    ||Psi_t-Phi_theta||_diamond <= 2(1-p(t)).

No external pulse is switched on or off. The packet's passage replaces the
specified interaction duration; its preparation and the rail remain supplied.
There is no assertion that Psi_t is a Markov semigroup.

Add the stated rest-energy Hamiltonian mD, m>0. It commutes with W, H_walk
and H_gate, so H_total=H_gate+mD is time independent and conserves the
separate resource D. A successful formation converts one fuel excitation
of energy 2m into two records of energy m each. In the interaction picture
of mD the channel is exactly the one above. Adding 2J I makes H_total
nonnegative without changing its dynamics. There is no unbounded-below
linear-momentum clock in this construction.

This accounts for the full energy of this specified rail-plus-rest-energy
model. It does not account for an additional interacting matter/field
Hamiltonian that fails to commute with U. Nor does it supply the fuel from
a lowest-energy vacuum. All neutral Gauss generators commute with H_total.

## 3. Compact incoming packets and a bound valid for all later times

For integers M>=1 and L>=M, choose a finite packet supported on -L,...,-L+M:

    psi_(-L+r)=i^r binomial(M,r)/sqrt(binomial(2M,M)),  0<=r<=M.

Its Fourier probability density is

    w_M(k)=4^M cos^(2M)((k-pi/2)/2)/(2pi binomial(2M,M)),
    -pi<=k<pi,

with the cosine power understood periodically. The distribution is centered
on right-moving k=pi/2. For H_walk the velocity operator is
v=2J sin(k), and on finite-moment states

    X(t)=X+t v.

The exact binomial sums give

    <X>=-L+M/2,             Var(X)=M^2/[4(2M-1)],
    <v>=2JM/(M+1),          Var(v)=4J^2(2M+1)/[(M+1)^2(M+2)],
    <{X-<X>,v-<v>}> = 0.

These follow, for example, from Vandermonde's sum and the shift overlaps
sum_r binomial(M,r)binomial(M,r+d)=binomial(2M,M-d), together with the
reflection r->M-r. Thus, putting a=L-M/2, b=Var(X), c=Var(v), vbar=<v>,

    mu(t)=vbar t-a,  variance(t)=b+c t^2.

For t>a/vbar, the one-sided variance inequality gives

    1-p(t)=Prob[X(t)<=0]
      <= B(t)=(b+c t^2)/(b+c t^2+(vbar t-a)^2).

For completeness, the inequality follows by applying Markov's inequality
to (Y-s)^2 on Y<=-mu for centered Y, choosing s=Var(Y)/mu. The ratio
(b+c t^2)/(vbar t-a)^2 has derivative
-2(ac t+vbar b)/(vbar t-a)^3<0. Hence for every t>=T>a/vbar,

    ||Psi_t-Phi_theta||_diamond <= 2 B(T).

This is a uniform bound on all unmeasured later reduced states on the
infinite rail. It is not a bound on an experiment that repeatedly measures
the carrier or the newly formed pair.

Examples at J=1 are:

| M | L | T | upper bound B(T) on nonpassage probability |
|---|---|---|---|
|16|32|40|17917/1122850, approximately 0.015957|
|40|80|100|118417/42549554, approximately 0.00278304|
|80|160|200|516317/674687394, approximately 0.000765268|

At theta=pi/2 and initially vacant endpoints, the same B(T) bounds the
probability of still having no pair, for every t>=T. For a fixed M this
estimate is conservative; it is not an exponential completion law.

## 4. Asymptotic channel and exponentially small directional preparation error

Under the free walk, X(t)/t converges in distribution to 2J sin(k) with
initial momentum density w_M(k). One direct derivation computes the
characteristic function of X/t in the evolved state: its momentum-space
integrand contains phi*(k) phi(k-s/t) and
exp[it(E(k)-E(k-s/t))], E(k)=-2J cos(k). Translation continuity and dominated
convergence give the characteristic function of E'(k). The limit has no
atom at velocity zero, so

    p(infinity)=integral_(0)^pi w_M(k) dk=1-epsilon_M.

The wrong-direction tail satisfies

    epsilon_M= [2*4^M/(pi binomial(2M,M))]
               integral_(pi/4)^(pi/2) cos^(2M)(u) du
      <= 2^(M-1)/binomial(2M,M)
      <= (2M+1)/2^(M+1).

The first inequality uses cos^2(u)<=1/2 on the stated interval. The second
uses binomial(2M,M)>=4^M/(2M+1), since the central term is maximal in a sum
of 2M+1 nonnegative terms totaling 4^M. For M=40 the last bound is
81/2^41, approximately 3.6835e-11. This asymptotic statement has no specified
finite convergence time; the preceding variance bound supplies a separate,
weaker finite-time guarantee.

The resulting limiting channel is epsilon_M Identity+(1-epsilon_M)Phi_theta.
It is close to one completed fresh collision, not an exact semigroup at
all times. A scattering state restricted to positive velocity can have
unit asymptotic passage, but would not be a strictly compact left-supported
preparation. No such stronger preparation is silently used here.

## 5. What remains before this can model permanent formation

The backward link contains U^dagger. A carrier returning through it can
reverse a formation. The uniform late-time channel bound does not turn a
finite-time event into an exactly absorbing microscopic subspace. A simple
control starts the free walker at j=0: symmetry and the return amplitude
give p(t)=[1-J_0(2Jt)^2]/2, which need not increase monotonically. Here J_0
is the Bessel function, distinct from hopping strength J. This control
belongs to this Hamiltonian and this preparation; it is not a universal
obstruction to autonomous models.

The infinite outgoing rail prevents a boundary reflection. A finite rail
has a different long-time problem. One carrier supplies at most one pair's
fuel; a continuing campaign of formation needs an actual population of
fresh carriers and a many-body interaction analysis. A rail direction and
packet phase are prepared resources; proper cubic covariance, homogeneous
native placement, continuous registration, and the initial arrow of motion
are not derived. These are precise residual questions rather than evidence
for a completed TOE.

The construction closes one limited implementation question: a bounded,
time-independent, finite-range Hamiltonian can approximate the coherent
fresh-fuel channel with a conserved positive energy account in its stated
geometry and a controlled late-time error. It uses existing clock machinery
and adds assumptions beyond the framework. The scoped reversal control and
other negative language remain private pending the negative-claim gate.

## 6. Executable controls

autonomous_gauge_birth_rail_check.py reconstructs the local pair/probe algebra,
two complete 216-dimensional finite defect Hamiltonians, their unitary
conjugacy, both plane-wave boundary equations, Gauss and energy-resource
commutators. It directly evaluates the packet's finite binomial sums for
M=1,...,16 and the three stated finite-time bounds. The directional integral
has an exact finite Fourier expression; reported decimal tails are diagnostics,
while the general upper bound is the analytic inequality above.

The localized control proves p(1)>p(2) at J=1 using rational alternating-
series brackets for J_0(2) and J_0(4), not a floating-point sign test. The
first complete execution passed. The infinite-rail velocity-limit proof,
all-M moment formulas and bound remain analytic arguments, not consequences
of the finite matrix sizes.
