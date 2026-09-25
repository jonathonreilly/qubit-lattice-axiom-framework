# Two original marks: coincidence counts and optical background normalization

Personal root derivation, 2026-09-25. Conditional candidate, not independently
reconstructed. This addresses the count functional used in a two-detector
optical comparison. It keeps the supplied common Hamiltonian and every
original formation channel. It does not select a laboratory detector, supply
a stationary photon source, change the instrument, or establish agreement
with an experiment.

## 1. Two supplied physical probes and one reference excitation

Place two translated copies of the exact charged J_- preparation of PR9143
in disjoint finite patches of an even cubic torus. A separation of at least
twelve links with the corresponding torus separation also at least twelve
suffices for the patches used here. Each copy has the same two negative A
sites, four positive B records, relative minus sign and fixed Gauss-compatible
integer flow as that source. Their local matter changes and original marked
stars are disjoint. The combined isometry J_-- is the four-arm sum with
coefficients (+1,-1,-1,+1)/2 and the sum of the two common flows. The four
matter configurations are orthogonal, and each satisfies Gauss. This is a
supplied preparation, not a derived native formation or reset protocol.

Let B_1,B_2 be the two translated original resolved marks. Their stars are
disjoint, so the operators commute on P. All Wilson factors commute with
the other patch's matter map. The single-probe output identity therefore
gives the exact initial effects on the reference field:

    J_--* B_i* B_i J_-- = R_i=1-cos(theta_i),
    J_--* (B_2 B_1)* B_2 B_1 J_-- = R_1 R_2.               (1)

The same joint identity holds in the opposite order. This follows by keeping
the actual output matter ket of each mark, with amplitude proportional to
(W_i-1)/sqrt(2); the two factors multiply. It does not replace an output by
a classical branch mixture or replace the original jumps by photon-number
annihilation operators.

Use the full h_g=K D+delta H4 and original dissipator sum, K=g^2/(2 tau),
delta=1/(4 tau g^2). D retains its empty-B gate. For the initial packets only,
write theta_i=g X_i, X_i=c_i.x, where c_i is its plaquette circulation and x
is the rescaled transverse coordinate. Gauge and harmonic zero directions
are removed from the reference oscillators. The harmonic-angle fiber is Haar;
contractible plaquettes annihilate it. Fixed Gauss strings shift momenta and
do not change the angle probabilities in (1).

For a normalized reference one-excitation alpha, in the real transverse basis,

    d_ir=(c_i.f_r)/sqrt(2 Omega_r), Omega_r=sqrt(lambda_r),
    v_i=sum_r d_ir^2, c=sum_r d_1r d_2r,
    chi_i=sum_r alpha_r d_ir, A_i=|chi_i|^2,
    T=Re(conj(chi_1) chi_2).                               (2)

The real number c is a vacuum covariance, not the speed of light in this
note. It obeys |c|<=sqrt(v_1 v_2). The two input families are the normalized
compact reference vacuum and one-excitation embedded by J_--. No physical
photon identification or equality with full charged energy is implicit.

## 2. Exact Gaussian moments behind the original effects

For the uncut reference Gaussian, creation/annihilation algebra gives

    <exp[i(s X_1+t X_2)]>_1
       =exp[-(v_1 s^2+2cst+v_2 t^2)/2]
                            [1-|s chi_1+t chi_2|^2].       (3)

The vacuum expression omits the bracket. Differentiating twice and four
times gives the one-excitation moments

    M_i=<X_i^2>_1=v_i+2 A_i,
    M_12=<X_1^2 X_2^2>_1
       =v_1 v_2+2c^2+2v_1 A_2+2v_2 A_1+8cT.              (4)

In vacuum they are v_i and v_1 v_2+2c^2. For example, the coefficient of
s^2 t^2 contributed by (-2stT)(-cst) in (3) is 2cT, and the four derivatives
multiply it by four, fixing the last factor8. The moments are real even for
complex alpha. Equations(3),(4) also extend to a density matrix in the
one-particle space, replacing A_i by Tr(rho |d_i><d_i|) and T by the real
cross matrix element. They are not arbitrary multiphoton statements.

At each fixed graph the compact Gaussian cutoff and normalization errors
are exponentially small up to fixed powers of g. Thus (1) gives

    <R_i>_1 = g^2 M_i/2 + O(g^4),
    <R_1 R_2>_1 = g^4 M_12/4 + O(g^6),                    (5)

and the analogous vacuum formulas. These initial effects are not by
themselves finite-time counting probabilities.

## 3. A positive-window result for the actual full process

Let p_i^(n)(b) be the probability of at least one selected mark i during
[0,b], and p_12^(n)(b) the probability of at least one of each, for input
n=0,1. Every other original channel remains enabled. At fixed finite graph,
fixed alpha, fixed tau>0 and fixed kappa tau>0, a sufficient window schedule is

    b/(tau g^4) ->0 as g->0.                              (6)

Then the actual effective process obeys

    p_i^(1)/(kappa b g^2) -> M_i/2,
    p_i^(0)/(kappa b g^2) -> v_i/2,
    p_12^(1)/(kappa^2 b^2 g^4) -> M_12/4,
    p_12^(0)/(kappa^2 b^2 g^4) ->(v_1 v_2+2c^2)/4.         (7)

Here is a sufficient error argument that keeps the full h_g. Put
Q=sum_j B_j*B_j, q=||Q||<infinity on the fixed graph, and let
N_t=exp[t(-i h_g-kappa Q/2)] be the no-jump contraction. Compact oscillator
packets, after fixed strings and any fixed finite product of B_j, lie in D(D).
Their electric second derivatives are O(g^-2); H4 is bounded at fixed graph.
Consequently ||h_g eta||<=C/(tau g^2) for each initial or once/twice-marked
vector eta needed below, with fixed-graph constants. Bounded Q adds the same
kind of bound. Duhamel gives

    ||N_t eta-eta|| <= C t/(tau g^2).                      (8)

The exact two-jump trajectory amplitude for order1 then2 is
N_(b-t2) B_2 N_(t2-t1) B_1 N_t1 Psi. Replace the three no-jump factors
successively by identity, using contractions and bounded B_j. The norm error
is at most C b/(tau g^2). Its flat amplitude has norm O(g^2) by (1),(5).
Hence its squared norm differs from ||B_2 B_1 Psi||^2 by at most

    C[b/tau + b^2/(tau^2 g^4)].                           (9)

The two time-ordered simplexes each have area b^2/2. The opposite order has
the same flat amplitude. Their sum therefore contributes
kappa^2 b^2 <R_1 R_2>, with (9) times kappa^2 b^2 as an error bound. A
trajectory with three or more total jumps has probability at most
(kappa q b)^3/6 by the bounded total intensity. This accounts also for every
unobserved channel and extra selected mark. Dividing by kappa^2 b^2 g^4,
all errors vanish under (6). Equivalently, a sufficient joint estimate is

    p_12^(1)=kappa^2 b^2 [g^4 M_12/4+O(g^6)
                +O(b/tau+b^2/(tau^2 g^4)+kappa b)],        (10)

where constants include the fixed graph and q. The same reasoning for one
jump uses flat amplitude O(g), giving the usual sufficient b=o(tau g^3)
single-count law; (6) is stronger and suffices for both. This establishes
probabilities at strictly positive windows, not microscopic initial rates.

The existing finite-history-register method can lift any fixed positive
window comparison to the microscopic instrument by recording the two flags
in a four-state classical register. Its spin/register error must be chosen
below the probabilities in (7) before taking (6). This is the parent's
ordered comparison procedure, not a new joint uniform spin/volume/time bound
or a claim about unbounded microscopic energy moments.

## 4. Raw coincidence ratio and background subtraction

Define the operational raw ratio for the one-excitation trial by
G_raw=p_12^(1)/(p_1^(1) p_2^(1)). Equation(7) gives

    lim G_raw = M_12/[(v_1+2A_1)(v_2+2A_2)].               (11)

For A_1 A_2>0, define a subtraction using separate vacuum preparation trials:

    G_sub = [p_12^(1)-p_1^(0) p_2^(1)-p_2^(0) p_1^(1)
                              +p_1^(0) p_2^(0)]
               /[(p_1^(1)-p_1^(0))(p_2^(1)-p_2^(0))].      (12)

This is a count estimator, not a positive operator or automatically the
correlation of a separable signal process. Algebra using (4),(7) gives

    lim G_sub = (c^2+4cT)/(2 A_1 A_2).                     (13)

It can be negative when the subtracted components are correlated. That is
not a negative event probability; it warns against interpreting an
independence-based correction as a physical signal correlation without
checking that independence.

If c=0, the underlying vacuum quadratures are independent, and

    lim G_sub=0,
    lim G_raw=1-rho_1 rho_2,
    rho_i=2 A_i/(v_i+2 A_i).                              (14)

For the uncut Gaussian INITIAL effects, these identities are even exact at
each g when rho_i is defined from the exact single effects: (3) gives
<R_1 R_2>_1=z_1 z_2+s_1 z_2+s_2 z_1, where
z_i=1-exp(-g^2 v_i/2), s_i=g^2 A_i exp(-g^2 v_i/2).
There is no s_1 s_2 term. The actual full-process statement remains the
limit(14); it is not an exact finite-window claim.

For c=0, the two vectors d_i/sqrt(v_i) are orthonormal. Bessel's inequality
gives eta_1+eta_2<=1, eta_i=A_i/v_i. Therefore

    lim G_raw=(1+2 eta_1+2 eta_2)
                  /[(1+2 eta_1)(1+2 eta_2)] >=3/4.         (15)

At fixed t=eta_1+eta_2, their product is at most t^2/4; the resulting ratio
(1+2t)/(1+t)^2 decreases on 0<=t<=1 and reaches3/4 at eta_i=1/2.
Thus positive raw coincidences coexist with zero subtracted coincidences.
Equation(15) cannot be tested against a background-corrected experimental
zero; those are different statistical quantities.

## 5. The decorrelation condition and low-band examples

No exact c=0 geometry of two single lattice plaquettes is assumed to have
been constructed here. For translated parallel xy plaquettes separated by
integer R in the x direction, the actual finite-torus covariance is

    c_L(R)=(1/(2L^3)) sum_(k!=0)
               [D_xy(k)/sqrt(D(k))] cos(k_x R),
    v_L=c_L(0), D=4 sum_mu sin^2(k_mu/2).                  (16)

The symbol is continuous at k=0 after assigning value zero there. At each
fixed R, the Riemann sums converge as L->infinity to its Fourier coefficient.
The Riemann-Lebesgue lemma then gives c_infinity(R)->0 as R->infinity.
Meanwhile v_L has a positive limiting value. These are iterated static
limits. Fixed-volume dynamical errors in (7) have not been made uniform.

For a fixed cutoff 0<epsilon<=2, the same argument applies to the band
symbol multiplied by 1_(0<sqrt(D)<=epsilon): its discontinuity surface has
measure zero, and it is integrable. Let u_i=P_epsilon d_i. When their sum
is nonzero, take alpha=(u_1+u_2)/||u_1+u_2||. Then

    A_1=A_2=(v_band+c_band(R))/2,
    <alpha,Omega alpha><=epsilon.                        (17)

In the stated static large-volume then large-separation limit, v_band tends
to a strictly positive constant for fixed epsilon, while both covariances
tend to zero. Equations(13),(17) show G_sub tends to zero after taking the
controlled g/window limit at each selected finite geometry. An ordinary
diagonal choice of sufficiently large L and sufficiently small g,b for each
R realizes these iterated conclusions. No numerical physical scale or
uniform laboratory error is supplied by that existence argument.

The optical-band restrictions are not evaded. A very small epsilon gives
very small A_i/v_i and therefore a very small model rho_i. Recovering the
subtracted statistic requires errors smaller than the small product A_1 A_2;
an unquantified approximation to raw counts is not enough. This construction
is a supplied one-excitation with two separated wavepacket components, not
a derived beamsplitter, emitting atom, or photon absorption mechanism.

## 6. Primary optical comparison: what has and has not been matched

Brouri et al. quant-ph/0007032v1, https://arxiv.org/pdf/quant-ph/0007032v1,
normalize two-APD coincidences using C_N=n_coinc/(N_1 N_2 w T) and correct them
by [C_N-(1-rho^2)]/rho^2 with rho=S/(S+B). Their quoted rho=0.34 would make
a hypothetical exact corrected zero correspond to raw C_N=0.8844. This is
the same algebraic pattern as (14). It is not a digitization or a fitted
claim about the actual zero-delay bin. The exact primary PDF and prior
complete primary-reading evidence are pinned separately.

The experimental rho measures a separately estimated stray-background
fraction under its independence assumptions. Our rho compares two supplied
vacuum/one-excitation preparation trials. These have not been physically
identified. The paper uses a stationary continuous fluorescence history and
a delay histogram; (7) concerns a fresh prepared state and a shrinking
positive window. No stationary source or conversion between those protocols
has been derived. Its1ns bin also remains outside any provided finite-g
error certificate under the earlier conditional tiny clock scale.

The result therefore gives a concrete coincidence functional and identifies
the vacuum-correlation term that a physical comparison must control. It
shows why neither a nonzero raw coincidence nor a zero corrected coincidence
alone decides whether this supplied probe describes the experiment. A match
to the measured detector, source, backgrounds, energies and time scales
remains open. No parameter was physically selected and no TOE or empirical
success is asserted.

## 7. Controls and claim status

The root personally derived (1)--(17) and wrote coincidence_controls.py.
Thirty finite-Fock operator checks use six levels in each of three modes;
four position operations on a one-excitation state never leave that cutoff.
They test real and complex states, unequal variances, correlated and
uncorrelated quadratures, and a completely unseen one-excitation. All moments
agree with (4) to floating precision. The120 finite-g rows evaluate exact
uncut Gaussian initial effects, not compact rotor evolution. The16 spatial
rows use actual finite-torus Fourier covariances and the low-band construction
(17); they are floating diagnostics, not interval or large-volume proofs.

N1: different source histories, correlated backgrounds, collective matter
and other physical detector identifications remain possible. N2: raw and
subtracted counts, energy increments and energy power are separate quantities.
N3: the supplied two-probe state, one-particle sector, disjoint original stars,
fixed graph, ordered shrinking windows and decorrelation limit are explicit.
N4: all channels and the full Hamiltonian are retained in the trajectory
error argument. N5: no experiment or framework is excluded by (15). N6:
(13),(14) provide a positive partial comparison while naming the missing
covariance and protocol identifications. N7: reproduction of a quantum-optics
normalization pattern is not a selected physical theory. N8: prior one-click
and optical-energy restrictions remain; this does not replace them with an
uncontrolled laboratory claim. Independent reconstruction remains required
before publication promotion.
