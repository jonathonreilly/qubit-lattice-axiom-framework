# Connected response of the first actual hole-producing source

Provisional analytic support, pending focused independent check. No formal
review, audit or microscopic local-limit claim is made.

This route does not prove the positive-time conditional local cluster tail.
It proves a narrower, source-bound estimate: the first positive-grade
microscopic jump coefficient on bare Omega has a spatially summable SIGNED
response under the complete leading finite-spin fast law, uniformly in spin,
allowed torus volume and response horizon. Original regional records and
bounded field outputs are retained. The sum carries its actual epsilon^2
source coefficient. The proof keeps an early CP gain-plus-terminal instrument;
it does not replace coherent-state localization error by a survival probability.

The useful new step is uniform spatial summability for this actual source.
The formula for the source and its coefficient360 were already proved in
DARK_WORD.md. They are reconstructed and controlled here, not claimed as new.
The finite-spin waiting-time and connected-output estimates below are new
candidates. Arbitrary positive-time occupied backgrounds remain outside them.

## 1. Exact model, source and scope

Main remains30a9461ee19a49b99fa6628fe942f08e504e8903; selected procedures
remain7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The refreshed open heads are
unchanged. The exact global count, initial-cluster, local-tilt and defect
proofs were fully read in the preceding route. The new tilted-defect author
REPORT19dc0b16 and root receiptb284dfa were fully read before reuse here.
They do not supply a local exponent. DARK_WORD and the complete checked
finite-spin-fast-response REPORTd0a96836 and its focused receipt were fully
read for this proof. SOURCE_IDENTITIES records exact hashes and read scopes.
The newer local-spin packet and the other agent's new sparse-dark multiplier
are not premises of this proof.

Use Z3's physical finite-change representation over Omega, or even cubic tori
with L>=28. The latter is within the checked global-k3 spin-transfer domain.
All site charges, link fields, orientations, occupancy gates and compensation
are exactly the supplied model. S is any integer>=1; the rotor is denoted
S=infinity. The actual leading fast coefficient is

    H_S=C_S+[F_S,F_S*]=Hbar_S+Delta_S,
    Delta_S=sum_a(D_a,infinity-D_a,S)Q_a,
    A_S=-i delta H_S-kappa G_S/2,
    G_S=sum_(original marks mu)j_mu,S* j_mu,S.

The full local cancellation gives ||Hbar_S||<=744 on W=1 and0<=G_S<=12.
Delta_S is the complete diagonal compensation, not subtracted from the law.
Physical spin boxes are invariant. Original marks are either resolved signs
per oriented edge or the unnormalized coherent sum per edge, separately.
Fast time is u=t_physical/epsilon^2. The fast coefficient is only part of
H_micro=delta epsilon^-4(W+epsilon T+epsilon^2 C_S), with original
L_mu=sqrt(kappa)epsilon^-1 j_mu. Higher normal-form terms are not included in
A_S by a change of notation.

Let P0 denote all A plus, all B vacant, with physical divergence-free fields.
Bare Omega additionally has every E=0. The first unitary dressing generator
is S1=-F+F*. For a fixed original mark mu on an edge incident to A center a,

    B_mu := J_(mu,+1)^(2)
          =(1/2)[F,[F,j_mu]]=-F_a j_mu F_a.           (1)

This is a coefficient of the ORIGINAL dressed mark, not a newly measured
channel. Outward F_a commute, F_a^2=0, and[F_c,j_mu]=0 for c!=a: when they
share the B site both orders are blocked, and otherwise the factors commute.
Second-order local circuit ordering can add only W-grade-zero generators,
whose commutator with j has grade-1. It cannot change (1).

The diagonal positive-grade contribution of this coefficient to the scaled
original dissipator is kappa epsilon^2 D[B_mu]. Off-grade interference terms
and other order-epsilon^2 coefficients also exist. They are NOT discarded
from the actual microscopic law or proved negligible here. Selecting (1) is
an algebraic source-vertex diagnostic, not a rule for identifying extra
observed events in the original process.

## 2. Exact bare source, including coherent interference

Put b_mu=B_mu Omega. It has W=1, global NB=3, and Q=1+sum|E|=4.
Every changed field is0 to+/-1 and every normalized-spin amplitude is one,
for all integer S>=1. Thus b_mu is the SAME vector for finite S and rotors.
Original positive-coordinate edge orientations are retained. Labeling the
following cases by the charge created at A is only explanatory: on an edge
whose tail is B, the corresponding original sign label is reversed.

For created A charge plus, the two outward hops choose an unordered pair of
other edges. Their two orders give the same physical output with amplitude-2:
10 words, norm squared40. For created A charge minus, the plus/minus output
charges distinguish the two outward hops:20 words of amplitude-1, norm
squared20. A coherent edge mark has both sets, with the original coherences,
and norm squared60. Consequently

    c_mu=||b_mu||^2 in{40,20,60},
    sum_(mu at a)c_mu=360                           (2)

for either original instrument. Adding squared path weights before combining
identical outputs would give240 per A and is wrong. This exact coefficient
is PRIOR ART in DARK_WORD; the present sparse control independently rebuilds
it before comparison. On the rotor P0 sector the stronger identity
P0 B_mu*B_mu P0=c_mu P0 holds for arbitrary fields: distinct output charge
patterns are orthogonal and each net open-link translation is unitary. The
finite-spin statement used below requires only the exact bare-Omega vector.

## 3. Actual finite-spin absorption and a uniform fourth waiting moment

Throughout W=1, NB=3 the hole has at least three vacant B neighbors.
For a vacant edge with field integer E inside[-S,S], the TWO original signs
have total loss

    g_edge=2-2E^2/[S(S+1)]>=2/(S+1).                 (3)

At E=+/-S the outward sign is zero but the inward sign has exactly the stated
weight. Coherent recycling is different from resolved recycling, but their
losses agree because the two final charge ranges are orthogonal. Therefore
as an operator on the entire physical spin-supported W1,NB3 sector,

    G_S>=6/(S+1),
    ||exp(u A_S)||<=exp[-3kappa u/(S+1)].             (4)

This uses no field cutoff, no favorable position and no missing boundary
matrix element. Self-adjoint H_S plus bounded loss gives the norm-loss
identity on the generator domain, then by density. Every finite S has exact
first-event absorption in this sector. For rotors G_infinity>=6, so the
survival amplitude is at most exp(-3kappa u).

The checked fixed-global-k spin-transfer theorem supplies a finite B_3,
dependent only on delta,kappa and its explicit k3 constants, such that

    ||Z_S(u)psi-Z_infinity(u)psi||
                 <=B_3 ||Q^2 psi||/[S(S+1)], all u.   (5)

Its full proof, including Delta_S and graph domains, was read. We only need
its terminal amplitude estimate. For normalized psi_mu=b_mu/sqrt(c_mu),
||Q^2 psi_mu||=16. Set

    A=16 B_3, B=1+A, C=S(S+1),
    u0=log(C)/(3kappa), d_S=6kappa/(S+1).

The constants B_3 are explicitly those of the checked report's equations3-5:
a0=10000delta+12kappa, b0=8sqrt(kappa), B_3=a0 L1+b0 L2, with its finite
polynomial-weighted rotor integrals L1,L2. They do not depend on volume,
source location, sign choice or S. Equations(4)-(5) imply for the ACTUAL
survival probability p_S(u)=||Z_S(u)psi_mu||^2,

    p_S(u)<=2e^(-6kappa u)+2A^2/C^2, all u,
    p_S(u0+v)<=B^2/C^2 e^(-d_S v), v>=0.             (6)

The second bound uses the semigroup composition and the exact all-domain
spin contraction AFTER u0; it is not inferred from small missing mass alone.
The first bound is only integrated up to u0 below. Early bounds exceeding
one cause no problem. Since (4) gives total absorption, p_S is the survival
function of the original first-event waiting time tau_S.

Here is one explicit uniform fourth-moment bound. Write x=S+1>=2, so
C>=x^2/2 and log C<=2log x. Splitting4 integral u^3 p_S(u)du at u0,
using(u0+v)^3<=4(u0^3+v^3), and
sup_(x>=1)(log x)^r/x^a=(r/(ae))^r, gives

    E tau_S^4 <= M4,
    M4=48/(6kappa)^4
       +128 A^2/(81 e^4 kappa^4)
       +256 B^2/(81 e^3 kappa^4)
       +384 B^2/(6kappa)^4.                          (7)

For clarity, the unsimplified positive bound is

  48/(6kappa)^4 +2A^2 u0^4/C^2
       +16B^2/C^2 [u0^3/d_S+6/d_S^4].

The three volume/spin-uniform estimates leading to (7) follow separately
from C^-2<=4/x^4; no limit exchange is needed. Rotors also satisfy (7).
Thus every moment p<=4 is bounded uniformly, and moments p<4 have uniform
tails, for example E[tau^3 1_(tau>R)]<=M4/R. This proof does not assert
uniform integrability of the fourth moment itself or a p>4 bound: its late
estimate scales as S^(p-4). An insufficient upper bound is not a divergence
proof. The fourth moment is enough for the spatial summation below.

## 4. Retain Delta through an exact local interaction picture

An extensive Delta norm cannot be inserted into a propagation speed. Instead
use its exact diagonal unitary U_D(u)=exp(-i delta u Delta_S). All Delta_a
commute. In this interaction picture,

    Hbar_S(u)=U_D(u)* Hbar_S U_D(u),
    j_mu,S(u)=U_D(u)* j_mu,S U_D(u),
    G_S(u)=G_S,

and ||Hbar_S(u)||<=744. The W0 sector is stationary in this picture: Hbar_S
and every bare j annihilate it. Thus a completed first event has no further
interaction-picture fast evolution. In the physical picture the complete
post-event Delta evolution is restored by the SAME U_D(T) on every branch
at a fixed final horizon T. We never stop the physical clock at an unobserved
far-away birth.

Support remains finite despite arbitrarily long u. A diagonal factor that
commutes with a local operator before conjugation still commutes after any
other diagonal factors, so only initially noncommuting factors contribute.
For the explicit one-hole Hbar words, such Delta centers lie within distance4
of the incoming hole, and their supports extend to distance6. Here:

- same-hole B/charge exchanges change only sites/links within distance3;
- moving the hole by two can change a Q_a only at centers within distance2
  of the old/new hole;
- each Delta_a has radius-two support.

Consequently the interaction-picture Hbar terms active at a hole h have
support in B6(h), and move the hole by at most two. An original j term has
support in B4(h) and removes the hole. A conservatively chosen radius8 will
be used below. Source conjugation at an insertion time also has bounded
support and leaves its source field Q=4. All phases and Q_a gates are retained.

For a physical bounded readout with site/link support X, conjugation by
U_D(T) enlarges X at most to X+=B4(X), independent of T,S and volume.
Thus |X+|<=129|X|. Include the endpoints of observed edges and all monitored
mark locations in X. The timestamps/labels themselves are unchanged.

## 5. The signed source kernel and why probability, not square root, applies

Fix an actual source center a and original mark mu. Inject b_mu at fast time
zero and include the original source label mu in the underlying mark history.
Evolve under the full leading spin law, keeping every subsequent original
mark, quantum field and terminal no-event state. On this sector there is at
most one subsequent fast birth. At a fixed horizon T, work in the interaction
picture just described, and marginalize the observed output to the FIXED
regional marks in X (arbitrary finite timestamp bins) and the final quantum
state in X+, with any spectator ancilla. All other original marks remain in
the dynamics but are unobserved in this marginal.

Define the signed source response as this gain output minus the local loss
term from D[B_mu], evolved on W0. At bare Omega that loss is simply
c_mu |Omega><Omega|, with no source mark. Denote the resulting regional signed
output by V_(a,mu;X,T). Keeping a far source label as an observed output would
make the following locality assertion false; it is deliberately marginalized.
There is no extra observed grade, exit flag or chosen-path label.

The distinction between a late instrument branch and a coherently projected
state is central. Split the ACTUAL first-event instrument at an intermediate
u. Its early gain branches plus its positive terminal no-event density form
a TP CP instrument. Their total trace is c_mu. On the early completed
branches, later interaction-picture evolution is exactly stationary.
The only further evolution is a TP CP instrument on the terminal density,
whose trace is c_mu p_S(u). Replacing that subsequent instrument by keeping
the terminal density therefore costs at most

    2 c_mu p_S(u)                                    (8)

in total CQ trace norm. This is a difference of two positive outputs with
that trace. It is NOT a gentle projection of a coherent state onto a spatial
region. Internal early/terminal decomposition is a proof device; erasing
unobserved labels is a contraction afterward. No square root is taken or
silently omitted.

To obtain a LOCAL comparison before applying (8), let D=B_R(a). Keep only
the complete interaction-picture local Hamiltonian terms and original jumps
whose structural supports lie in D. Pair adjoint Hamiltonian terms together.
The resulting auxiliary generator is CP and TP and acts only in D; it is not
asserted to be the actual law. The omitted terms annihilate W0. On W<=1 the
full and cut generators, including finite marked registers, have induced
trace norm at most

    b=2delta*744+24kappa.                             (9)

The row/column triangle budget proving744 is termwise and survives this cut;
G_cut<=G<=12. Removing Delta through its exact interaction picture, rather
than dropping it, is essential for (9).

A sequence of j generator factors starting at a can move the hole at most
2j and only use the bounded support just specified. Thus the time-ordered
Dyson coefficients of full and cut instruments agree through degree n-1
on the positive source gain, whenever

    n=floor((R-8)/2)+1>=1.

The W0 loss branch is stationary in both. This statement includes all
original gains and losses, not only non-Hermitian evolution. Time-dependent
phases and timestamp-bin transitions have the same support and norm bounds.
For u<=n/(8b), both Dyson remainders give a CQ trace error at most

    2c_mu q^n,   q=e^(9/8)/8<1.                      (10)

The estimate follows from e^(bu)(bu)^n/n! and n!>=(n/e)^n. It is uniform in
the number and placement of the finite timestamp bins. No ordinary
volume-uniform physical propagation velocity is assumed: (9) is only the
bounded fixed-excitation fast generator after the diagonal picture change.

If D is disjoint from X+, the cut early-gain-plus-terminal CP instrument,
COMBINED WITH its source loss, has exactly zero regional signed output.
It is a local TP continuation of the local trace-annihilating map D[B_mu].
Partial tracing a local TP map preserves the complementary state, including
an entangled ancilla. The source and every cut mark are outside the fixed
observed region. A positive gain alone would not justify this cancellation.
Only after this local cancellation do we bound the true late branch by (8).

Take u=min(T,n/(8b)). If T<=n/(8b), (10) alone suffices. Otherwise use (8)
and (10). In either case

    ||V_(a,mu;X,T)||_1
        <=2c_mu [q^n+p_S(n/(8b))]                    (11)

when D is disjoint from X+. The crude bound2c_mu always holds. This proves
a uniform-in-horizon connected source bound using actual marked CP branches,
not a probability estimate substituted for an amplitude error.

## 6. Explicit spatial summation and its limited microscopic consumer

Let d=dist(a,X+) in the periodic or infinite L1 metric. Choose R=d-1.
For d>=16 the preceding conservative n satisfies n>=d/4. Set

    alpha=log(8)-9/8>0,
    D4=M4(8b)^4,  z=exp(-alpha/4).

Markov's inequality applied to (7) gives

    ||V_(a,mu;X,T)||_1
       <=2c_mu [exp(-alpha d/4)+256D4/d^4], d>=16.    (12)

For closer centers use2c_mu. Cubic L1 shells contain4r^2+2<=6r^2 sites.
A ball of radius15 is certainly bounded by31^3 sites. Summing first around
each point of X+, with harmless overcounting, and using(2), gives

    sum_(a,mu)||V_(a,mu;X,T)||_1 <= C_conn |X+|,
    C_conn=720 [31^3+6z(1+z)/(1-z)^3+1536D4/15].       (13)

The bound is uniform in S, all declared volumes, all T and all original
regional timestamp bins. Periodic identifications only decrease the sum
relative to a choice of shortest Z3 representatives. For source centers at
distance at least R>=16, a uniform tail is

    720|X+|[6 sum_(r>=R)r^2 exp(-alpha r/4)
                                      +1536D4/(R-1)].           (14)

It tends to zero uniformly as R increases. No volume factor n appears.
The power-three spatial count costs a fourth waiting moment in this explicit
Markov implementation. Equivalently the third waiting moment plus its UI
controls the shell integral; (7) supplies both. A square-root survival bound
would not give the same conclusion from the available S^-4 plateau.

The exact source coefficient in the actual scaled dissipator is kappa
epsilon^2. Therefore the source functional made from ONE insertion of this
specified positive-grade quadratic source on bare Omega, followed by the
complete leading fast response, has regional CQ norm at most

    129 kappa epsilon^2 C_conn |X|                    (15)

at any horizon. Integrating such a single-insertion kernel over a physical
interval of length T_phys costs at most the right side times T_phys.
Time-shifting the insertion only changes the exact diagonal-picture phases;
its normalized source still has Q=4 and the estimates remain uniform.

Equation(15) controls a precise connected source vertex that occurs in a
microscopic expansion. It is NOT a bound for the complete actual microscopic
state at positive time, nor a declaration that the grade+1 component is an
observed independent channel. It retains the actual source operator and the
actual complete leading finite-spin propagator, rather than a proxy stress,
a scalar walk or an independently imposed dilution law. Other algebraic
source components and all interactions with later occupied backgrounds are
outside this single-vertex functional. The combined scaling epsilon^2
S(S+1)=delta/K may be imposed without changing its uniform constant.

## 7. Why the all-source local problem is still open

The first gain has k3 and a strict rotor loss; spin boundaries weaken that
loss but (5)-(7) recover the required moments from the finite-field source.
After two preceding original births, the same actual coefficient can create
the known W1,k7 dark word. DARK_WORD supplies that exact source component.
There is no universal lower G proportional to W then. At extensive positive
time, a fixed bound on the GLOBAL number of preceding marks is unavailable.

The complete finite-excitation cascade does give a harmonic lift of bounded
W0 observables with norm<=||O||, independent of its lifetime. A Poisson time
integral is different and generally pays the absorption time. Local SOURCE
summation needs spatial influence moments even when the global harmonic
map is contractive. Thus contractivity alone cannot be inserted for the
missing connected bound in a source expansion.

If one estimates each stage using the presently checked fixed-global-k
rates, one-hole inverse rates grow exponentially with k and multi-hole
bounds as exp[O(k log(m+1))]. At source order r, k,m can grow with r. Paying
a separate spatial-response cost at each stage yields upper majorants of
the form exp(C r^2), or exp(C r^2 log(r+1)) with the multi-hole bound, before
the source series is summed. Even a time-ordering r! does not certify a
positive radius for those majorants. This is an insufficiency of the stated
bounds, not a lower bound on actual coefficients or proof that the physical
series diverges. A connected resummation might pay a cluster cost once;
no such step has been proved here.

A new sparse-dark local multiplier is being developed independently by the
matter agent, and a local finite-spin transfer packet has been checked by
root during this task. Neither was imported into this proof. Even a local
response bound would still need the actual positive-time weight of its bad,
dense input complement, with all off-grade mark coherences retained.

The exact live statistical obligation remains the actual conditional cluster
UI from bare Omega, or a strictly weaker signed bound for a stated local
current. The global tilted-hole theorem cannot replace its volume n by an
island size. Our (15) retires only the first source-vertex summability issue.
It does not prove cluster UI, microscopic electric moments, all-later-birth
control, full M4 or a new physical source/clock principle.

## 8. Controls, prior-art correction and handoff

check_source.py is an independent implementation of the actual six-edge
positive-coordinate oriented star, retaining original sign labels, integer
charges, link translations and all interfering paths. Before comparison it
reproduced the already-known40/20/60 and360, all Gauss equations, W1/NB3,
Q4, and the nested-commutator coefficient for18 original mark choices.
The exact full DARK_WORD proof was then read, and novelty is credited there.
The final control additionally checks4224 exact finite-spin edge losses for
S1 through64, including every boundary zero and equality at|E|=S.

The initial source-only control cost0.007641 CPU seconds,19,136,512 bytes.
After adding the genuinely new loss-bound checks, the final run cost0.089001
CPU seconds,0.089233 wall seconds,19,070,976 bytes. Both runs passed; no
failure was hidden or test relaxed. Each was guarded by the original campaign
deadline and STOP checks, a25-second CPU cap and one thread. These finite
controls corroborate exact algebra, not the all-volume propagation or moment
proof. No dense Hilbert enumeration or unmanaged job was used.

The independent-check priorities are: the exact all-domain loss lower bound,
the waiting-time plateau/composition and fourth-moment constants, the
commuting-Delta support enlargement, and the CP early-gain-plus-terminal
argument before the survival-probability tail. In particular verify that only
fixed regional labels are observed during spatial summation, and that the
late bound is never used as a gentle projection estimate.

All files are confined to this new directory. Old source packets, main,
reviewer-owned files, audit state and remote branches are unchanged. The
candidate needs a focused independent check before downstream reuse.
