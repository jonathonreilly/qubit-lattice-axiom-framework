# Repeated formation with a nonvanishing fourth-order energy scale

Author conditional finite-model theorem, 2026-09-23. Independent reconstruction
pending. This is the complete four-leaf star from
FINITE_RATE_REPEATED_RECORD_FORMATION.md, with a different scaling. It gives
an all-time law for formation counts, with charge marks and quantum output
discarded. It does not give a general-graph density limit or a combined
photon/formation theorem.

## 1. Model and question

There is one A center and four B leaves. Sites carry hard-core states 0,+,-;
the four outward links have integer spin S=1 and normalized shifts. Work in
div E+1_A-q=0 with total charge one. The physical sector has 45 states;
the electric fields are E_leaf=-q_leaf, so every legal shift has amplitude
one. T is the negative charge-preserving hopping adjacency. Pair births
are either separate charge-resolved channels or the coherent plus combination
on each wholly vacant edge. Initially only the center holds a plus record.

At most two formations can occur: N advances 1->3->5. Both refill the same
center after a departure. The parent note proves the sector decomposition
and exact dark weights; the checker here rebuilds those spectral projectors
using the same microscopic-sector builder.

Set positive delta,kappa and supply

Delta=delta epsilon^-4,  t=delta epsilon^-3,
beta=kappa epsilon^-2,  epsilon>0.                   (1)

The Hamiltonian is H'=Delta W+tT, where W is the center-vacancy indicator,
and the jumps are sqrt(beta) j. Replacing H' with Delta N_B+tT changes it
by Delta(N-1). This is a scalar on each number sector, so the number-block
densities and event times considered here are unchanged.

Unlike the balanced finite-graph regime in the parent note,

t^4/Delta^3=delta                                    (2)

does not vanish. However t²/Delta=delta epsilon^-2 diverges. The purpose is
to test repeated formation with this hierarchy of scales, not to infer
that its much faster matter dynamics is harmless on a lattice with loops.

## 2. Exact reduction for both events

Before the first event the P space at N=1 contains just the initial center
state g. Its one-hole coupling has squared norm four. In the vacant-center
N=1 sector there are three empty leaves available for formation, so the
no-event decay term is -i 3 beta. The initial no-event state consequently
has exactly one occupied-center and one normalized bright direction.

Immediately after the first event, with its channel discarded, the normalized
N=3 occupied-center density is

sigma_3=(1/24) sum_j v_j v_j†,  v_j=j T g.            (3)

The common bright amplitude cancels on normalization. Thus sigma_3 is
independent of the first event time and of all three positive microscopic
parameters. Channel probabilities are included in the sum; a coherent
per-edge channel and two resolved channels give different sigma_3.

In N=3 write A=Pi_(W=1) T P and M=A†A. The occupied-center dimension is 18,
the vacant-center dimension is 12, and the exact M spectrum is

0(6), 1(3), 2(3), 3(2), 5(3), 6(1).

Its spectral weights w_lambda=tr(P_lambda sigma_3) are

| instrument | lambda=0 | 1 | 2 | 3 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| coherent per edge | 4/15 | 0 | 1/3 | 0 | 1/15 | 1/3 |
| resolved charge | 1/3 | 0 | 1/6 | 0 | 1/3 | 1/6 |

Singular-value decomposition of A decomposes the N=3 no-event evolution
into two-level blocks, one per positive lambda, with coupling t sqrt(lambda).
Their vacant-center loss is -i beta because one leaf remains empty there.
The zero-eigenvalue occupied-center subspace is exactly dark. It is
annihilated by T, W and every j at finite parameters.

Off-diagonal matrix blocks between distinct singular sectors do not contribute
to the no-event trace: the dynamics preserves those mutually orthogonal
sectors. Hence the waiting-time survival depends only on the weights above;
no assumption that sigma_3 is diagonal in the M eigenbasis is needed.

## 3. Exact two-level waiting density and its global error

Use lambda>0 for squared hopping strength and g_*=number of empty neighbors
after the hop. The first block has (lambda,g_*)=(4,3); subsequent bright
blocks have g_*=1. Put

b=g_* beta,  z=Delta-i b,
D=sqrt(z²+4 lambda t²), with Re D>0,
mu_s=-2 lambda t²/(z+D),  mu_f=z-mu_s,
gamma=-2 Im mu_s,  eta=2b-gamma,
C=2b lambda t²/|D|²,  omega=Re D.                    (4)

Both gamma and eta are positive. One way to see strict damping, independent
of the root formula, is that a no-loss eigenvector must have zero excited
component; nonzero coupling then forces its ground component to vanish.
The matrix is finite, so there is no surviving bright amplitude.

Starting in the occupied-center vector, the exact excited amplitude is
t sqrt(lambda)(exp(-i mu_s u)-exp(-i mu_f u))/D,
up to a sign irrelevant to its norm. Its event density is

f_(lambda,g_*,epsilon)(u)
 =C[exp(-gamma u)+exp(-eta u)-2 exp(-b u)cos(omega u)]. (5)

This density is nonnegative and integrates to one for every Delta,t,beta>0.
The apparent subtraction is the squared amplitude, not a signed event law.

Under (1), its limiting rate is

r_(lambda,g_*)=2 g_* kappa lambda.                   (6)

For all sufficiently small epsilon, define the exact positive bound

B_(lambda,g_*,epsilon)
 =(|C-r|+|gamma-r|)/gamma +C/eta+2C/b.                (7)

Then, on the entire half-line,

integral_0^infinity |f_(lambda,g_*,epsilon)(u)
                         -r exp(-r u)| du <= B.     (8)

To prove this, separate the slow exponential from the fast and oscillatory
terms. The slow difference is bounded by
|C-r|/gamma +r |1/gamma-1/r|;
the fast integral is C/eta; bounding |cos| by one gives 2C/b.
All terms are integrable. In fact (7)--(8) hold for every positive epsilon
for which (4) is used, though they are useful for the small-epsilon regime.

Expansion of the analytic square root around epsilon²=0 gives

gamma=r[1-3 lambda epsilon²+O(epsilon^4)],
C=r[1-4 lambda epsilon²+O(epsilon^4)],
eta=2g_* kappa epsilon^-2-r+O(epsilon²).

The leading differences have fixed signs for small epsilon. Substitution
in (7) therefore yields

B_(lambda,g_*,epsilon)=12 lambda epsilon²+O(epsilon^4). (9)

This is an all-time L1 estimate, not a finite observation-window fit.
Its remainder may depend on delta,kappa,lambda,g_*. Only finitely many
lambda values are needed in this model.

An additional exact check is the mean waiting time for a bright block:

E U =Delta²/(2b lambda t²)+b/(2lambda t²)+1/b
    =1/r+epsilon²/(g_* kappa)
          +g_* kappa epsilon^4/(2lambda delta²).    (10)

It follows by integrating u times (5), or by the two-level survival
Lyapunov equation. It is a conditional bright waiting mean. The
unconditioned second waiting time has infinite mean because w_0>0.

## 4. Joint event times and the entire count path

Let U_1 be the first waiting time and U_2 the time from the first event
to the second; allow U_2=infinity. Because (3) is time-independent, their
joint law factors exactly, at finite microscopic parameters, into

law(U_1)=f_(4,3,epsilon)(u)du,
law(U_2)=w_0 delta_infinity
            +sum_(lambda>0) w_lambda f_(lambda,1,epsilon)(u)du.  (11)

This independence is for the two waiting times after charge marks have
been discarded. It is not an assertion of identical renewal clocks.
It follows from the explicit first-event state and time-homogeneity,
not a classical closure of site occupations.

The limiting first law is exponential with rate 24kappa. The limiting
second law has atom w_0 at infinity and exponential components with rates
2kappa lambda and weights w_lambda. Product-measure triangle inequality,
with probability measures of total mass one, gives

||law(U_1,U_2)-law_0(U_1,U_2)||_L1
 <=B_(4,3,epsilon)+sum_(lambda>0) w_lambda B_(lambda,1,epsilon)
 =84 epsilon²+O(epsilon^4).                          (12)

The coefficient 84 is the same for both instruments: their sum
sum_lambda lambda w_lambda is three. It is a coefficient of this sufficient
bound, not the exact asymptotic statistical distance.

For definiteness total variation is half the L1 norm of the difference.
The count path C(tau)=1_(tau>=U_1)+1_(tau>=U_1+U_2) is a measurable
pushforward. Thus (12)/2 also bounds the total-variation distance between
the probability laws of the entire count paths on 0<=tau<infinity.
It also bounds every event-time CDF and any finite collection of count
observations. Charge-resolved marks and the outgoing quantum state are
not included in this statement.

The eventual two-event probabilities remain exactly 11/15 and 2/3 for all
positive microscopic parameters. The dark component is retained in both
measures; it is not discarded by taking the limit.

For an explicit count formula put r_0=24kappa and r_lambda=2kappa lambda.
Then

P_0(tau)=exp(-r_0 tau),
P_1(tau)=w_0[1-P_0(tau)]
 +sum_(lambda>0) w_lambda r_0
       [exp(-r_0 tau)-exp(-r_lambda tau)]/(r_lambda-r_0),
P_2(tau)=1-P_0(tau)-P_1(tau).                        (13)

As usual the coincident-rate quotient has its continuous value.
The model's listed bright rates do not coincide with r_0.

## 5. Verification and significance

fourth_scale_repeated_clock_check.py rebuilds the complete physical star
using the previously bound author sector builder. Exact rational spectral
projectors recover the weights, including their zero-eigenvalue atoms.
It evaluates the complete formula (5), normalization, exact mean and (7)
at five epsilon values from 0.2 to 0.0125, for both instruments, and compares
the exact count CDFs with (13) at nine times through five.

Twelve controls propagate the full 45-state microscopic Lindblad generator
at epsilon=0.2 and 0.1 and times 0,0.05,0.1. The largest discrepancy from
the exact clock/count formulas is 1.94e-14. These are separate calculation
forms from the same author, not an independent reconstruction. At
epsilon=0.0125 the sufficient whole-path total-variation bound is below
0.006554 for each instrument. Some coarse-epsilon bounds exceed one;
they are valid loose upper bounds, not probabilities.

The first checker execution failed an exact SymPy equality because a NumPy
one-hot vector introduced SymPy Float entries before division by 24.
The preserved source/streams/receipt and diagnosis show this failure.
The repair verifies integrality and converts the bright vector to integer
entries before the exact rational calculation. No mathematical formula,
tolerance or expected result changed. The repaired execution passed.

This supplies a nonzero repeated-formation clock while the algebraic
fourth-order scale t^4/Delta^3 remains finite. A star has no plaquette loops.
Equation (2) therefore does not establish finite magnetic dynamics in
this same model, and the divergent second-order matter generator cannot
be ignored when extending to a lattice with loops.

The original energy per extra pair still grows with Delta. Preparation,
quantum mechanics, the formation instrument, site/link resources and a
background remain supplied. A general-graph fast-matter/formation limit,
its compatibility with propagating fields, finite fuel, and native law
selection remain open. The result improves an explicit small-model
compatibility test; it is not evidence of TOE completion.
