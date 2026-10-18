# A size–arrival–dwell tradeoff for the exact binomial clock

New bounded author derivation requiring a distinct check. The scalar probability and window bounds below are proved directly. Their physical exact-loader application is CONDITIONAL on the engineered coefficient realization in source b8bbfb7d, whose distinct review is pending at this writing. No pending coefficient/cap result is promoted to accepted status.

The new conclusion is a tunable relative window, not the earlier central-third window. At fixed accuracy, allowing a longer engineered clock makes the certified completed-output interval arbitrarily long relative to its own first certified arrival. It also delays that arrival and increases hardware. The finite coherent clock still returns. Exact supply, passive-reference and initialization premises are retained.

## 1. Exact premise and notation

Read the complete `exact_engineered_clock_operation/PROPOSAL.md`, SHA256 `b8bbfb7d40c491aff6b893df6423b98e68edad91ef6596124dac10f3620c53f8`, in `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Its proposed scalar operator on x=0,...,L is

    h_L=C I-alpha sum_(r=1)^L sqrt(r(L+1-r))
                       (|r><r-1|+|r-1><r|),
    Jstar=Lambda/40, alpha=2Jstar/(L+1), C=4Jstar.

The coefficient-realization proposal identifies the retained external output as x>=75. Its complete physical output gauge there is -U_f, with

    U_f=I_a tensor[X_R C_P^(b) SWAP_QP].

The exact initial clock site is0. The one-head input may be coherent on the selected two a=1,b rails, with arbitrary Q/P and passive references, blank R and every other head vacant. This is not a supplied wavepacket; the endpoint coherence and apparatus blanks remain supplied. These physical premises and the claimed counts/cap are adopted conditionally, not proved anew here.

The scalar amplitude formula can be checked without that realization: on the normalized symmetric weight-x states of L mathematical spins, sum X has matrix elements sqrt((x+1)(L-x)). The commuting-spin exponential therefore gives

    f_x(t)=exp(-iCt) sqrt(binomial(L,x))
                  [i sin(alpha t)]^x [cos(alpha t)]^(L-x).       (1)

These mathematical spins are not additional physical qubits. The squared moduli form Bin(L,p(t)) with p(t)=sin^2(alpha t), and sum to one. The phase exp(-iCt), i^x and the sign of cos are retained. Define the bad external-output probability

    q(t)=Pr{X<=74}, X distributed as Bin(L,p(t)).                (2)

## 2. A directly proved mean-dependent tail bound

For any L independent Bernoulli variables of common probability p, let m=Lp. Markov's inequality applied to exp(-X) gives

    Pr{X<=74} <= exp(74) E exp(-X)
      =exp(74)[1-p(1-exp(-1))]^L
      <=exp[74-(1-exp(-1))m].                                  (3)

The last inequality is 1-y<=exp(-y) for0<=y<1; at p=1 it remains valid since y=1-exp(-1)<1. No central-limit approximation or asymptotic binomial estimate is used.

If m>=148, then74<=m/2. Also exp(-1)<3/8: indeed e>1+1+1/2+1/6+1/24=65/24>8/3. Hence

    74-(1-exp(-1))m <=-(1/2-exp(-1))m <-m/8,
    q(t)<=exp(-m/8).                                           (4)

The loose non-strict final ceiling is used below. It holds uniformly for every integer L and p satisfying Lp>=148. The relevance of mean rather than a fixed fraction of L is that the required outgoing threshold75 stays fixed while L can grow.

Fix0<epsilon<=1 and define

    delta=epsilon^2/256,
    m_epsilon=max{148,8 log(256/epsilon^2)}.                    (5)

Whenever Lp>=m_epsilon, (4) proves q<=delta. This condition is sufficient, not the exact binomial quantile. Its constants are explicit and intentionally conservative.

## 3. A window extending from early arrival to the symmetric return

Choose ANY integer

    L>=max{296,ceil(2m_epsilon)}.

Set

    theta=arcsin sqrt(m_epsilon/L),  0<theta<=pi/4,
    t_arr=theta/alpha,
    t_end=(pi-theta)/alpha,
    D=t_end-t_arr=(pi-2theta)/alpha.                            (6)

For every t in the CLOSED interval [t_arr,t_end], sin^2(alpha t)>=sin^2 theta=m_epsilon/L. Equations(3)--(5) give

    sup_(t_arr<=t<=t_end) q(t)<=epsilon^2/256.                   (7)

This interval contains the original central-third interval and is strictly larger: theta<=pi/4<pi/3. For this mean-threshold certificate, t_arr is the first certified time in the initial increasing half-cycle. It is not claimed to equal the exact earliest high-success time of the physical distribution.

Let z_t be the restriction of the FULL complex f(t) to x=75,...,L, divided by sqrt(1-q(t)), a positive real number. Its norm is one and its phase is unchanged. Under the conditional physical gauge, the complete target is the external-head embedding of

    -z_t tensor U_f xi.                                       (8)

All source/interior heads are vacant in this comparator and all old-state and passive-reference outputs are retained. Since the physical and scalar maps are unitary, the exact squared complete-vector difference is

    q+(1-sqrt(1-q))^2=2-2sqrt(1-q)<=2q.

In particular the looser convenient bound2sqrt(q)<=epsilon/8 holds uniformly on(6). The unhalved complete-output channel distance is at most epsilon/4, and external success is at least1-epsilon^2/256. No projection or normalization is applied to the actual evolved state. The target normalization is a mathematical comparison, not an input-preparation or measurement primitive.

The exact all-time blank-R branch of the physical gauge, if that realization is accepted, remains a separate statement. Its event includes virtual73 and final origin74 after the coordinate shift, so it is at least as probable as external arrival. It is not used to replace the external-only complete target in(8). The scalar proof itself has no physical record qubit.

## 4. Exact relative dwell and absolute cost

The dwell-to-certified-arrival ratio is exactly

    D/t_arr=pi/theta-2.                                      (9)

For0<=y<=1/sqrt(2), integration of the derivative of arcsin gives

    y<=arcsin y<=sqrt(2)y.

Consequently

    (L+1)/(2Jstar)*sqrt(m_epsilon/L)
       <=t_arr
       <=(L+1)/(2Jstar)*sqrt(2m_epsilon/L),                    (10)

and

    (pi/sqrt(2))*sqrt(L/m_epsilon)-2
       <=D/t_arr<=pi*sqrt(L/m_epsilon)-2.                     (11)

Because theta<=pi/4, there are also direct dwell bounds

    pi(L+1)/(4Jstar)<=D<pi(L+1)/(2Jstar).                     (12)

Thus at fixed epsilon and L tending to infinity, certified arrival is Theta(sqrt(L)/Jstar), dwell is Theta(L/Jstar), and their ratio is Theta(sqrt(L)). There is a genuine relative-window gain, but the arrival becomes later in absolute time. No speedup at fixed hardware or fixed arrival time is inferred.

More explicitly choose an independent requested relative ratio R>=2 and let

    L_R=ceil max{296, m_epsilon/sin^2(pi/(R+2))}.              (13)

Since sin^2(pi/(R+2))<=1/2, this automatically meets the previous length requirement. It gives theta<=pi/(R+2), hence

    D/t_arr>=R.                                               (14)

This is an explicit two-parameter prescription: epsilon fixes an accuracy threshold and R fixes a desired relative dwell. L may also be chosen larger than L_R. It is not a claim that one fixed L satisfies arbitrary epsilon at the same broad window.

For useful size estimates, put a_R=pi/(R+2)<=pi/4. Concavity of sin on[0,pi/2] gives2a_R/pi<=sin a_R<=a_R. Therefore

    m_epsilon(R+2)^2/pi^2
        <=m_epsilon/sin^2 a_R
        <=m_epsilon(R+2)^2/4.

The right-hand side is at least592, since m_epsilon>=148 and R>=2, so it also bounds the296 term. Including the ceiling,

    m_epsilon(R+2)^2/pi^2 <= L_R
                   <=m_epsilon(R+2)^2/4+1.                   (15)

Together with(10)--(12), this proves uniform sufficient-recipe orders for R>=2:

    L_R =Theta(m_epsilon(R+2)^2),
    t_arr=Theta(m_epsilon(R+2)/Jstar),
    D=Theta(m_epsilon(R+2)^2/Jstar).                           (16)

Here m_epsilon=Theta(1+log(1/epsilon)); the fixed148 threshold is not discarded at moderate accuracy. With Jstar=Lambda/40 the factors1/Jstar are40/Lambda. At fixed epsilon these become size quadratic in the requested ratio, arrival linear and dwell quadratic. They are properties of this explicit certificate, not necessary costs or optimal control bounds.

## 5. Conditional physical resources and supply tradeoff

If the pending engineered realization is supported at its claimed scope, its exact unchanged inventory applies for each selected L:

    physical head qubits=4(L+1), total qubits=4L+7,
    nonzero positive blocks=8L+172,
    range<=18, incident norm cap<=Lambda.

Equation(15) therefore turns the relative-dwell request into explicit qubit/block ceilings by substituting its upper bound for L. For example the qubit count is at most m_epsilon(R+2)^2+11 and the block count at most2m_epsilon(R+2)^2+180. These are conditional consequences of the realization inventory, not an independently checked layout in this note.

The minimum engineered hopping is

    kappa_min=2Jstar sqrt(L)/(L+1).

Increasing L lengthens the dwell while decreasing this endpoint coefficient, of order Jstar/sqrt(L). The full square-root profile and positive compensating occupations must remain exactly supplied and correlated across arms and rails. This coefficient magnitude is not a fabrication accuracy, error-correction or native-Hamiltonian guarantee. No unstructured perturbation bound is invoked without its own positivity, support, vacuum, conservation, load-margin and probability-floor hypotheses.

The original pending source chooses a short logarithmic-length recipe for its central-third window. The present source does not claim that recipe was wrong or that(13) always uses fewer resources. It trades larger hardware and a later certified arrival for a longer relative dwell, while keeping the same constant incident cap and exact conditional logical action.

## 6. Limits on interpreting “earliest” and recurrence

There are elementary necessary tests for any actual external success at a time in the first half-cycle. If q(t)<=delta, then

    Lp(t)=E X >=75 Pr{X>=75}>=75(1-delta).

Also the bad event contains X=0, so(1-p)^L<=q<=delta and hence

    p(t)>=1-delta^(1/L).

Thus every such time obeys

    t >= alpha^-1 arcsin sqrt(max{75(1-delta)/L,
                                             1-delta^(1/L)}). (17)

This is only a necessary bound, not an exact hitting-time formula. It prevents interpreting(6) as a proved optimal earliest arrival. For fixed epsilon, the right-hand side has order sqrt(L)/Jstar as L grows, consistent with the sufficient arrival's scaling. It also exhibits the accuracy dependence through log(1/delta) in the large-L expansion; no approximation was used in the exact inequality(17).

The probability profile is symmetric about pi/(2alpha), so the first broad high-success excursion has a corresponding return side. At t=pi/alpha, equation(1) is exactly

    exp(-i C pi/alpha)(-1)^L |0>,

with zero external-output probability. The finite state recurs up to this common phase. The certified interval ends t_arr before this return time. Making D/t_arr large does not provide permanent confinement, a halt, a latch, irreversible record, readout, reset or reuse. No nonzero-success interval can span this exact return. Different acceptance events or a separately installed capture environment would require new transport analysis.

For a fixed finite L, arbitrarily accurate transfer still occurs at the exact transfer instant, but this note's broad-window prescription may cease to apply as epsilon decreases. It is not a lower bound ruling out narrower windows or another coefficient family. No environmental coupling, including the separately proposed record-environment interaction, is installed or analyzed here.

## Exposure and work record

ROOT suggested investigating a longer relative completed-output interval by selecting L independently of the earlier minimal accuracy prescription. The new contribution here is the mean-threshold estimate(3)--(4), the arrival-to-return window(6), its independent relative-dwell parameter(13), and the explicit sufficient tradeoff and necessary qualifications. The scalar spin/binomial solution and proposed physical coefficient realization were visible before this derivation. I previously checked the exact global gauge and structured family, with substantial shared source ancestry. This is same-model source-exposed author work, not independent validation of those premises or a literature-novelty claim.

The global source f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946/check41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6 and structured source515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2/check273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8 retain their complete reads at accepted scopes. They do not themselves validate b8bbfb7d's new physical coefficient and cap realization. That dependency is pending. This new dwell derivation also requires its own distinct check before acceptance.

Only this PROPOSAL.md was created. Work was analytical, with full source reading and deterministic hash/directory bookkeeping. No scientific executable, solver, simulation, sweep, external search, delegation, Git/W/checkpoint/axiom/editable-prompt/model change or publication occurred. No editable prompt changed. No empirical prediction, physical preparation/cooling mechanism, active old-environment operation, generic precision claim or formal retained status is assigned.
