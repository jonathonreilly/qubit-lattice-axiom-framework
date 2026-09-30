# Connected electric ledger and the remaining displacement Gram

Author discovery, not yet independently checked. The contract c038f2f1 fixes the actual supplied compensated law, bare Omega, both original instruments separately, fixed K,delta,kappa,T, epsilon^2 S(S+1)=delta/K, and every finite safe torus with n=|A|. Constants below are independent of n,S,epsilon (for the checked small-epsilon range); they may depend on T and the fixed physical couplings. The original observable is Q=sum_e E_e^2, over 6n oriented A-to-B links. All old frozen proofs are unchanged. No full-H energy or work interpretation is attached to the diagnostic quantities below.

## 1. Exact inputs and the question this proof does not answer

Use sigma=Y rho_micro Y*, P_m=1_(W=m), r_e=kappa epsilon^-2 and the exact finite-spin operators from EXACT_ONE_HOLE_REDUCTION62202b03:

 H_1=P_1 P_W(H')P_1-delta epsilon^-4 P_1,
 K_mu=P_1 J_(mu,0) P_1,
 E_mu=P_0 J_(mu,-1) P_1,
 I(s)=r_e sum_mu J_(mu,+1)P_0 sigma(s)P_0 J_(mu,+1)*,
 tau_0=P_1 sigma(0)P_1.

Here J_mu=Y j_mu Y* retains the complete original mark. In the coherent instrument, no branch inside j_mu is resolved. P_W is algebraic grade averaging, not an observed new record. The exact killed generator and driven kernel are

 D(tau)=-i[H_1,tau]+r_e sum_mu D[K_mu](tau)
                    -r_e/2 sum_mu {E_mu*E_mu,tau},
 Z_u=exp(uD),
 chi(t)=Z_t(tau_0)+integral_0^t Z_(t-s)(I(s))ds.            (1)

This retains all exact neutral recycling, evolving B backgrounds, D4,D6 and the exact same-grade remainder. The positive forcing uses the SAME actual microscopic sigma(s), not a stationary or W0 target replacement.

The checked inputs are

 Tr tau_0+integral_0^T Tr I(s)ds <= C_T epsilon^2 n,
 sup_(t<=T)||P_1 sigma(t)P_1-chi(t)||_1 <= C_T epsilon^4 n^(7/2), (2)

and the checked quadratic result WORKING_PROOFfe8e48e5 gives

 sup_(t<=T) Tr rho_micro(t)Q <= C_T[n+n^2+epsilon n^(7/2)]. (3)

Its physical/rotated mean return costs C_T epsilon n. The checked signed-current reduction, neutral recycling/slow estimates and exit-commutator estimate will be stated explicitly in section4. Their focused receipts are c8b4de10, db0b07b6 and 2c0d2830. These are provisional focused checks, not formal source reviews or authority changes.

The new target remains a bound C_T n on Tr rho Q. We do NOT prove that bound here. We prove an exact connected cancellation and a quantitative equivalence, in a declared joint window, to a positive actual-source field-displacement Gram. Unlike an endpoint capacity estimate, that Gram contains no unchanged spectator electric energy. Bounding it still requires a new dynamical argument.

## 2. Trace-preserving absorbing completion with the original records

For each u>=0 complete Z_u by adjoining absorbing copies of the physical W0 space, one for each original exit label mu. The Hamiltonian on the alive W1 block is H_1, and is zero on the absorbing blocks. The neutral jump is sqrt(r_e) K_mu on W1 and zero on absorbing blocks. The exit jump is sqrt(r_e) E_mu from W1 to its absorbing copy, and is zero thereafter. This is a bounded GKSL generator at each finite S,n, with no loss of trace. A further ordinary trajectory environment may keep every original neutral label and continuous event time before exit, as well as the exit label/time. This does not split a coherent mark into its path summands. Finite-dimensional bounded-rate Dyson/Kraus expansion gives a trace-preserving channel T_u and an isometry V_u into the output plus trajectory environment. No apparatus implementation or physical grade detector is claimed.

Put the SAME link operator E_e on every alive/absorbed output block, tensor identity on the history environment. It equals its value at exit on an absorbed branch. Let Q_out=sum_e (E_e^out)^2. Trace preservation and the absorbing construction give, for every positive W1 input tau,

 Tr Q_out T_u(tau)
  =Tr Q Z_u(tau)
    +r_e integral_0^u sum_mu Tr Q E_mu Z_v(tau)E_mu* dv.  (4)

This is the exact original electric observable at the alive or exit output. In particular, exit energy is not replaced by exit probability times a local energy, and a field left behind by a moving hole is still present. The completion is diagnostic and source dependent when used in(1); it is not a claim that the actual process measures W or freezes after exit.

Define a bounded column operator on the W1 input carrier for every link,

 A_e(u)=E_e^out V_u-V_u E_e,
 R_u=sum_e A_e(u)* A_e(u) >=0.                           (5)

The sums are finite. At finite S each factor is bounded; no rotor-domain assertion is needed. The same construction with the full original history environment, or with its redundant labels isometrically enlarged, gives the same expression below. Equivalently,

 R_u=sum_e[T_u*(E_e^2)+E_e^2
                    -T_u*(E_e)E_e-E_e T_u*(E_e)].        (6)

Thus the Gram is determined by the channel and the fixed input/output fields, independently of its Stinespring representation. In(6), T_u* includes the absorbing copies and original records, with E_e read as the common output operator. This is not an initial field measurement or a classical two-point measurement convention: input field coherences remain intact.

Expansion of (E_e^out V_u)=(V_u E_e+A_e), using V_u*V_u=I, gives the exact identity

 T_u*(Q_out)-Q=R_u
                 +sum_e[E_e V_u* A_e+A_e* V_u E_e].      (7)

For a positive, not necessarily normalized input tau, Hilbert--Schmidt Cauchy implies

 |Tr tau[T_u*(Q_out)-Q-R_u]|
                 <=2[Tr Q tau]^(1/2)[Tr R_u tau]^(1/2). (8)

Indeed the cross term is the real inner product of the columns V_u E_e sqrt(tau) and A_e sqrt(tau), summed over e. This proof makes no diagonal-state or independent-field assumption. If a link is an exact spectator, E_e^out V_u=V_u E_e and its Gram and cross contribution both vanish IDENTICALLY. Exact spectators cancel before taking norms. No assertion that a dynamically reached link is a spectator follows from this fact.

## 3. Actual-source superposition and the spectator cross price

For each observation time t define

 G(t)=Tr R_t tau_0+integral_0^t Tr R_(t-s) I(s)ds >=0,
 A_Q(t)=Tr Q tau_0+integral_0^t Tr Q I(s)ds,
 B_Q(t)=Tr Q chi(t)
       +r_e integral_0^t sum_mu Tr Q E_mu chi(s)E_mu* ds. (9)

Fubini is valid for positive integrands in the bounded finite-spin carrier. Combining(4),(7) over the initial atom and the actual source times gives

 B_Q(t)-A_Q(t)=G(t)+X(t),
 |X(t)|<=2 sqrt(A_Q(t) G(t)).                            (10)

The Cauchy inequality is over the links, initial atom and source-time measure together. It does not coherently superpose different source times or replace I(s) by its norm. Every original neutral and exit mark remains in T, and every original positive mark remains inside I(s). G is nonnegative but need not be monotone in t; it is not a residence time or a dissipated-work functional.

There are two useful bounds. First, ||E_e||<=S, sum_e E_e^2<=6nS^2 and(2) imply

 A_Q(t)+B_Q(t)<=C_T n^2,
 G(t)<=2[A_Q(t)+B_Q(t)]<=C_T n^2.                        (11)

The inequality for G is the elementary column estimate ||a-b||^2<=2||a||^2+2||b||^2. This is only the old capacity scale; it does not close the desired C_T n bound.

Second, the actual injected energy is much smaller in a useful joint window. Write Qbar=I+Q. The exact local displacement estimates for Y and J imply

 ||Qbar^(1/2) J_(mu,+1) Qbar^(-1/2)||<=C epsilon^2.       (12)

Here is the needed weighted justification, rather than a substitution of an unweighted norm. A local spin-shift word with net integer shift v satisfies

 (1+|E+v|^2)^(1/2)/(1+|E|^2)^(1/2)<=sqrt(2)(1+|v|).

All matter gates and grade projections commute with Qbar. The exact fixed-cone analytic series for the circuit-conjugated jump has an absolutely convergent row/column displacement norm weighted by 1+|v|, uniformly in S,n; exponentiating each fixed local generator preserves this norm. Its grade+1 coefficients of orders0 and1 vanish as OPERATORS, so the same Taylor remainder starts at order epsilon^2 in this weighted norm. This proves(12). It uses no global Schur bound for Y and no polynomial electric moment of the input beyond the displayed Qbar form.

Consequently, summing O(n) original marks and using positivity and [P_0,Q]=0,

 Tr Q I(s)<=C epsilon^2 n[1+Tr Q sigma(s)].               (13)

The initial local preparation estimate is Tr Q tau_0<=Tr Q sigma(0)<=C epsilon^2 n. Combining(3), its checked physical return and(13), for n>=1,epsilon<=1,

 A_Q(t)<=C_T epsilon^2 n^3[1+epsilon n^(3/2)],
 |X(t)|<=C_T epsilon n^(5/2) sqrt(1+epsilon n^(3/2)).     (14)

Both statements are valid with their literal prices, without fixing volume first. One may also take the minimum with the capacity bound(11). In particular, if epsilon n^(3/2) is bounded, the input/displacement cross term is O_T(epsilon n^(5/2)); its DENSITY is bounded in this window. This is a real cancellation of the spectator endpoint cost, but NOT a bound on G. The source estimate is not obtained by replacing global n by a local support: every one of the O(n) possible source marks has been counted.

## 4. Relation to the exact signed quadratic ledger

Use Q_1=P_1 Q P_1, Q_0=P_0 Q P_0 and H_1=delta epsilon^-2 P_1D2P_1+V_1. The previously checked exact balance is

 Tr Q chi(t)-Tr Q tau_0
 =delta epsilon^-2 integral_0^t Tr chi(s)i[D2,Q]ds
   +Slow(t)+Neutral(t)-ExitEnergy(t)+ExitComm(t)
   +integral_0^t Tr Q I(s)ds.                           (15)

Here ExitEnergy is exactly the positive integral in B_Q(9),

 Slow=integral Tr i[V_1,Q_1]chi,
 Neutral=r_e integral sum_mu Tr D[K_mu]^*Q_1 chi,
 ExitComm=r_e integral sum_mu Re Tr E_mu* C_mu chi,
 C_mu=Q_0 E_mu-E_mu Q_1.

The checked bounds, with the full exact local remainder and complete original neutral gain-minus-loss, are

 |Slow|+|Neutral|<=C_T epsilon n^2,
 |ExitComm|<=C_T n.                                    (16)

The latter uses exact exit activity O(epsilon^2 n), sum_mu C_mu*C_mu<=C S^2P_1 and time/mark Cauchy. It does not treat an anticommutator with Q as positive. Combining(10),(15) yields the connected current identity

 delta epsilon^-2 integral_0^t Tr chi i[D2,Q]
       =G(t)+X(t)-Slow(t)-Neutral(t)-ExitComm(t).         (17)

Thus all unchanged input field energy has been subtracted exactly. Neither a positive exit energy nor the positive source energy is separately bounded by a local surrogate.

The checked actual current passage, using the W1 trace error, the finite-spin current norm and the factorial multihole estimate, is

 |Tr rho_micro(t)Q
    -delta epsilon^-2 integral_0^t Tr chi(s)i[D2,Q]ds|
                       <=C_T[n+epsilon n^(7/2)].       (18)

This is the original microscopic state and original Q. It retains physical coordinate return, all off-grade coherent losses/gains and all later original events. It is not a conclusion that chi approximates the full microscopic state in a weighted norm.

Equations(14),(16)--(18) prove the new quantitative comparison

 sup_(t<=T)|Tr rho_micro(t)Q-G(t)|
                       <=C_T[n+epsilon n^(7/2)].       (19)

For completeness, the cross estimate(14) is bounded by C epsilon n^(7/2), since sqrt(1+epsilon n^(3/2))<=sqrt(2)n for n>=1,epsilon<=1. The other errors are smaller at the displayed scale. No extra volume restriction is required merely to state(19).

In a joint family with epsilon n^(5/2)<=C_*, (19) has O_T(n) error. Therefore a volume-uniform bound on the ACTUAL quadratic electric density is equivalent, up to constants depending on C_*, to

 sup_(t<=T) G(t)/n <=C_T.                               (20)

This is an exact SOURCE-DEPENDENT positive-Gram consumer, not its proof. It contains the actual initial tau_0, actual continuously varying I(s), complete exact kernel including neutral recycling, all original marks and all elapsed times t-s. An input first moment, a fixed-fast-age bound, a prepared dark fiber or a global B-count bound cannot simply be substituted into(20). The existing capacity estimate is only G<=C_T n^2. Consequently this packet does not improve the final n-power of the actual Q bound.

## 5. Scope and failed shortcuts

The useful new cancellation is operator-level spectator subtraction, together with an actual-source price for the cross term and the explicit relation(19). It isolates a positive field-DISPLACEMENT estimate rather than positive HOLE-FIELD residence. These are different sufficient consumers; neither is established at volume-uniform density here. The latter may overprice reversible current cancellation, whereas G includes it automatically through the complete channel.

The source and endpoint are not independent; positivity in(10) is not a factorization of their fields. Locality of the generator is not locality of R_u on physical times of order one, because its leading hopping speed is order epsilon^-2. The actual channel may change fields far from its initial hole before exit. A sum of current commutator squares followed by time Cauchy gives a ballistic age cost and does not bound(20). A spatial cutoff introduces a boundary flux weighted by the exterior field; telescoping that flux recovers the same connected displacement rather than removing it.

The distinction between the physical H and Q remains exactly as in the checked energy packet: the bare-Omega full H mean is 6 delta epsilon^-2 n and the gap term is not erased. No heat/work or apparatus ledger follows from(19). No quadratic uniform integrability follows either: even a uniform Q mean would not suffice for that. No new numerical evidence was run for this analytic proof. Its new identities and bounds require focused independent reconstruction before substantial reuse.
