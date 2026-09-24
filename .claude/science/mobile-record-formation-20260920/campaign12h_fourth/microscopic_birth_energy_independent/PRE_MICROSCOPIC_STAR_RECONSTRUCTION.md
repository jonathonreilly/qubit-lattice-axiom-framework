# Independent reconstruction: microscopic energy on the compensated three-leaf star

PRE reconstruction, September 24, 2026 UTC. This is a conditional finite-model
calculation for the supplied Hamiltonian and the unchanged supplied births.
It is neither an audit verdict nor a claim that these laws arise from native
axioms. No author energy packet or existing microscopic builder was consulted
before the PRE seal. The full source bindings and execution history accompany
this note.

## 1. Model and complete physical space

Take A={0}, B={1,2,3}, with edges 0->b, local q=0,+1,-1, occupancy n=q²,
integer spin S>=1, E=S_z and U=S_+/sqrt(S(S+1)). Supply

    div E = q - 1_A,
    H = delta epsilon^-4 (W + epsilon T + epsilon² C_S),
    L_(b,c) = sqrt(kappa)/epsilon j_(b,c),

or the coherent edge channel L_b=sqrt(kappa)/epsilon (j_(b,+)+j_(b,-)).
Here delta,kappa,epsilon>0, W=1-n_0, T=-(F+F*), and F is the unsigned sum
of outward charge-preserving hops from the occupied center to vacant leaves.
The local source defines

    C_S = F*F - D_S + D_infinity,

because the gate Q_0 is the empty product. A hop 0->b of charge c shifts
E_b by -c. Birth j_(b,c) acts only when center and leaf b are both vacant,
creates charges c,-c there, and shifts E_b by c.

At a leaf the Gauss equation forces E_b=-q_b. At the center it then forces
sum_x q_x=1. Consequently every physical field has |E_b|<=1, so all
physical site words with total charge one occur for every integer S>=1.
Their record number is N=1 or N=3. There are four N=1 words and twelve
N=3 words: the complete physical Hilbert space has dimension 16.
There are no extra electric circulation sectors on this tree.

Every nonzero local hop or birth changes one link between E=0 and E=+1
or E=-1. Its normalized spin amplitude is exactly one:
1-E(E+k)/[S(S+1)]=1 for these transitions. In particular this statement
also includes the S=1 boundary. If an outward hop is eligible, its target
leaf is vacant and hence its link has E=0. Thus D_S=D_infinity exactly,
and

    C_S = F*F                                               (1)

on the entire physical space, independently of S.

Here is an explicit basis, with the unique Gauss fields understood:

* g: center +, all leaves vacant.
* x_b: center vacant, leaf b +, other leaves vacant.
* r_b: center -, leaf b vacant, other two leaves +.
* s_(b,a), a!=b: center +, leaf b -, leaf a +, third leaf vacant.
* z_b: center vacant, leaf b -, other two leaves +.

Then P=1-W is spanned by g, the three r_b and six s_(b,a), while Q=W
is spanned by the three x_b and three z_b. Direct local action gives

    Fg = x_1+x_2+x_3,
    F r_b = z_b,       F s_(b,a)=z_b,
    F x_b=F z_b=0.                                      (2)

In the N=1 sector, dim P=1 and dim Q=3; in N=3, dim P=9 and dim Q=3.
Equation (2) decomposes F into four rank-one rows of squared singular
value three: one row in N=1 and three in N=3. Thus rank F=4 and, writing
M=F*F, M²=3M. This classification is a complete physical-space argument,
not a dynamically truncated basis.

## 2. Exact factorization, spectrum and positive-overlap preparation

Set a=1+3epsilon² and theta=delta epsilon^-4. By (1),

    h := H/theta = (W-epsilon F)*(W-epsilon F).          (3)

In the P,Q ordering this is

    h = [ epsilon² F*F     -epsilon F* ]
        [ -epsilon F            I_Q  ].

Every nonzero singular direction of F gives the two-by-two block
[[3epsilon²,-sqrt(3)epsilon],[-sqrt(3)epsilon,1]], with eigenvalues
0,a. Six P-dark directions have eigenvalue zero; two Q-dark directions
have eigenvalue one. The complete microscopic energy spectrum is

| Sector | Microscopic energy and multiplicity |
|---|---|
| N=1 | 0 (1), theta (2), theta a (1) |
| N=3 | 0 (9), theta a (3) |
| Full space | 0 (10), theta (2), theta a (4) |

This holds for every epsilon>0 and S>=1. The low cluster is exactly the
zero eigenspace; its graph is {(p,epsilon Fp):p in P}. Let

    P_b=M/3, Q_b=FF*/3, P_d=P-P_b, Q_d=Q-Q_b.

The positive-overlap block rotation is

    U = P_d+Q_d + a^-1/2[P_b+Q_b+epsilon(F-F*)].        (4)

It is unitary, has strictly positive P and Q diagonal overlaps, and
U*hU=Q_d+a Q_b. Its P isometry is
(P+epsilon F)(P_d+a^-1/2 P_b). Therefore the requested exact dressed
preparation of g is

    d = [g+epsilon(x_1+x_2+x_3)]/sqrt(a),    Hd=0.      (5)

Its density differs from the bare density gg* by trace norm
2sqrt(3epsilon²/a). Equation (4) is the continuation of the source's
canonical positive-overlap convention, rather than a nonorthogonal
Schur-coordinate replacement.

For any normalized vector phi in the P part of N=3, define

    m_phi = <phi,M phi> = ||F phi||².

The Q-dark energy is absent from its spectral measure. Its probability
of microscopic energy theta a is exactly

    p_high = epsilon² m_phi/a,                         (6)

and its remaining probability is at energy zero. One can obtain (6)
either from the singular blocks or from the projector
Pi_high=(h-Q_d)/a. Hence, for every integer n>=1,

    <H^n>_phi = m_phi delta^n epsilon^(2-4n) a^(n-1).   (7)

In particular

    <H> = m_phi delta/epsilon²,
    <H²> = m_phi delta² a/epsilon^6,
    Var(H) = m_phi delta²[1+(3-m_phi)epsilon²]/epsilon^6. (8)

These are moments of the full microscopic Hamiltonian, including the
compensation term.

## 3. Actual marks and their outputs

Fix leaf b, and write {a,d} for its other two leaves. Applying the actual
local births to (5) gives

    j_(b,+) d = epsilon v_(b,+)/sqrt(a),
    v_(b,+) = s_(b,a)+s_(b,d),

    j_(b,-) d = epsilon v_(b,-)/sqrt(a),
    v_(b,-) = r_a+r_d.                                 (9)

For the coherent mark b use v_b=v_(b,+)+v_(b,-). The normalized outputs
are v_(b,c)/sqrt(2) for resolved marks, and v_b/2 for coherent marks.
These are the actual states immediately after applying the jump; no
projection back into a dressed low space has been added.

The local maps (2) give

    F v_(b,+)=2z_b,
    F v_(b,-)=z_a+z_d,
    F v_b=2z_b+z_a+z_d.

Thus all intensities and microscopic conditional moments follow directly:

| Actual mark | Number of marks | ||v||² | Intensity at d | m_phi |
|---|---:|---:|---:|---:|
| Resolved (b,+) | 3 | 2 | 2kappa/a | 2 |
| Resolved (b,-) | 3 | 2 | 2kappa/a | 1 |
| Coherent b | 3 | 4 | 4kappa/a | 3/2 |

For each row substitute m_phi into (6)--(8). The total instantaneous
formation rate is 12kappa/a for either instrument. The rate-weighted
mean microscopic energy immediately after a birth is
3delta/(2epsilon²) for either instrument, although their output
densities differ. A relative sign in the coherent channel changes its
density even in cases where these particular energy moments stay equal.
Energy agreement therefore does not identify the instrument.

The N=3 sector contains only one vacancy, so every birth vanishes there.
After a formation there is unitary microscopic evolution but no second
formation. The energy distribution (6), and all moments (7), are
unchanged by that subsequent unitary evolution.

For completeness the marked output statement also holds at every possible
first-event time, not only at time zero. Define the normalized symmetric
state u=(x_1+x_2+x_3)/sqrt(3). The exact no-event vector stays in span(g,u)
and obeys i d/dt( alpha,beta ) = K_no( alpha,beta ), where

    K_no = theta [ 3epsilon²       -sqrt(3)epsilon ]
                   [ -sqrt(3)epsilon      1       ]
             - i (2kappa/epsilon²) |u><u|.            (10)

The initial amplitudes are (1,sqrt(3)epsilon)/sqrt(a) for (5), or (1,0)
for the bare g. Here sum_j j*j=4 times the N=1 Q projector, for either
instrument. The unconditioned first-event density per resolved mark is
2kappa|beta(t)|²/(3epsilon²); the coherent density per edge is
4kappa|beta(t)|²/(3epsilon²). Dividing these by
|alpha(t)|²+|beta(t)|² gives the corresponding no-event conditional
hazards. Whenever a mark has nonzero density its normalized output is
exactly the state in (9), independent of the event time.

## 4. Full initial GKLS energy derivative and bare preparation

For the actual GKLS generator,

    d/dt tr(H rho) = sum_j [
      tr(H L_j rho L_j*) - tr(H {L_j*L_j,rho})/2 ].    (11)

The Hamiltonian commutator has zero trace against H. At rho=dd*, the
entire anticommutator contribution is exactly zero because Hd=0;
this does not assume that the no-event term vanishes as an operator.
Using all actual channels and their distinct conditional means,

    d/dt tr(H rho(t)) |_(t=0,rho=dd*)
      = 18kappa delta/[epsilon²(1+3epsilon²)].         (12)

For resolved marks the plus contribution is 12kappa delta/(a epsilon²)
and the minus contribution is 6kappa delta/(a epsilon²). Three coherent
marks give the same sum. Thus (12) is a full initial GKLS derivative,
not merely a Hamiltonian energy estimate or a selected recycling term
with an unexamined loss term.

The bare state g has a different microscopic preparation:

    <H>_g=3delta/epsilon²,
    <H²>_g=3delta² a/epsilon^6,
    Var_g(H)=3delta²/epsilon^6.                        (13)

All jumps annihilate g, so its initial total jump rate is zero and its
full initial energy derivative is zero. The Hamiltonian part still
changes its density. Trace-norm closeness of g and d consequently does
not equate their initial energies, initial jump rates, or initial energy
derivatives. Both are legitimate distinct preparations of the same
Hamiltonian.

## 5. Effective target and joint resource limit

For this star, Pi_2=0, C_1=0 and C_0=M. The supplied effective formula
therefore gives H2^C=H4^C=0. Its diagonal D is also identically zero:
every eligible edge in D has a vacant leaf and E=0. The target
Hamiltonian KD+delta H4_infinity^C is zero on its complete P space.
This star contains no independent field loop.

The effective jumps B_j=-PjQTP=jF give B_j g=v_j. They have the exact
normalized outputs (9), total rate 12kappa and no further births on N=3.
Writing

    sigma_res = (1/12) sum_(b,c) v_(b,c)v_(b,c)*,
    sigma_coh = (1/12) sum_b v_b v_b*,

the effective density from g is exactly

    rho_eff(t) = exp(-12kappa t) gg*
                  +[1-exp(-12kappa t)] sigma_instrument. (14)

The provided uniform microscopic-target theorem applies to bare g.
Contractivity and the explicit trace distance after (5) extend that
O(epsilon) approximation to the dressed preparation as well. No
additional microscopic energy estimate follows from this argument.

In the joint limit epsilon² S(S+1)=delta/K, put C=S(S+1). Then

    a=1+3delta/(KC),
    theta=K²C²/delta,
    theta a=K²C²/delta+3KC,
    <H>_phi=m_phi KC,
    <H²>_phi=m_phi(K³C³/delta+3K²C²),
    Var(H)_phi=m_phi K³C³/delta+m_phi(3-m_phi)K²C²,
    d/dt <H>_d|_0 = 18kappa KC/[1+3delta/(KC)].         (15)

Meanwhile p_high=m_phi delta/(KC+3delta) tends to zero and the total
birth rate tends to 12kappa. Although all these physical Hilbert spaces
are identical as vector spaces, H depends on S through the resource
scaling and its norm diverges. The small high-energy weight has
divergent energy; the zero target Hamiltonian does not track it.

There is also a finite-time demonstration. Let p_birth(t) denote the
actual probability that the single allowed birth has happened.
The no-event energy is nonnegative by (3). Each marked post-event
branch preserves its conditional energy and has the fixed mark ratios
following (10). Hence, exactly,

    tr(H rho(t)) = E_no(t)
                       +(3delta/2epsilon²) p_birth(t),
    E_no(t)>=0.                                       (16)

By density/count convergence, p_birth(t) tends to
1-exp(-12kappa t), strictly positive for every fixed t>0. Thus the
microscopic energy diverges at every such time, even though the
complete density converges to (14) and the effective energy is zero.
One can make the same statement for higher positive integer moments
using (7). This is a concrete failure of inference from density
convergence to these changing microscopic observables; it is not a
claim that bounded-observable convergence fails.

For each normalized immediate output phi, its normalized projection
onto the exact zero-energy cluster has trace distance
2sqrt(p_high) from phi. Thus even comparison with an exactly zero-energy
dressed output leaves an O(epsilon) density defect alongside the
divergent energy in (8). In fact the bare P output and the target
output density already agree exactly at the instant of the mark:
their assigned Hamiltonians differ.

The unchanged birth generator therefore supplies positive microscopic
energy in this explicit compensated model. These calculations do not
construct an autonomous reservoir, nor do they decide whether some
separately specified reservoir realization is possible. They show why
a trace-class effective limit alone cannot establish bounded
microscopic cost per birth or energy conservation of such a realization.

## 6. Verification and scope

The accompanying Python control enumerates every site word and every
finite electric word in the full tensor product, filters the local
Gauss equations, and builds each local hop and birth directly. It uses
no existing campaign builders and does not construct its basis from
the reduced analytic sector list above. Exact symbolic checks cover
the complete Hamiltonian, spectrum/projectors, canonical rotation,
both actual instruments, jump loss, energy moments and full GKLS
derivative. S=1,2,4 finite enumerations corroborate the analytic all-S
argument; finite samples alone are not its proof. Complete floating
Liouville propagation corroborates density convergence and (16).

The PRE receipt specifies completed controls, preserved failed
attempts, mutation probes and exact artifacts. The analytic scope is
this four-site star, the explicit supplied compensation, the supplied
instruments and the stated preparations. No general-graph spectrum,
macroscopic limit, native-law selection, empirical claim, formal
audit status or source-landing judgment is supplied.
