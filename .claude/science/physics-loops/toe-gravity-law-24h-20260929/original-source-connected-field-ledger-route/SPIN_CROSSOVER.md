# Spin crossover: a positive-Gram bound from unweighted surviving input mass

New author proof attempt under CROSSOVER_CONTRACTd6c187a7, separate from the earlier connected-ledger argument. It is not yet independently checked. This proves a sufficient ACTUAL-source estimate, not the survival hypothesis it exposes. No fixed-U rotor theorem is extrapolated to the growing U below. All operators on the left are the exact finite-spin killed/absorbing channel of CONNECTED_LEDGER, with all original neutral records and original exit labels retained.

## 1. Rescaled exact absorbing generator and its field columns

Write T_t for the trace-preserving absorbing completion in CONNECTED_LEDGER section2 and use fast time u=t/epsilon^2:

 Ttilde_u=T_(epsilon^2 u),   Ltilde^*=epsilon^2 Labs^*.

On the alive W1 block its Hamiltonian is

 Htilde=delta P_1D2P_1+epsilon^2 V_1,
 V_1=P_1[delta D4+delta epsilon^2 D6+P_W R_H]P_1.

It is zero after exit. Its jumps are sqrt(kappa)K_mu for the exact neutral maps, and sqrt(kappa)E_mu for the exact exits. Recall K_mu=P_1J_(mu,0)P_1=O_local(epsilon), while E_mu=P_0J_(mu,-1)P_1 is the full grade-minus-one map, not just the bare j. Define the self-adjoint drift and positive jump-gradient forms for every original link,

 B_e=Ltilde^*(E_e),
 Gamma_e=Ltilde^*(E_e^2)-E_e B_e-B_e E_e
         =kappa sum_(all jumps A) [E_e,A]*[E_e,A].        (C1)

For exit jumps the commutator means E_e^out A-A E_e^in, with the same original field on both blocks. All terms vanish on absorbed inputs. The basic exact column bounds are

 sum_e Gamma_e <=c[1+epsilon^2 n] P_alive,
 sum_e B_e^2 <=c[1+epsilon^4 n] P_alive.                 (C2)

The constants are independent of S,n. Here is the complete price of each class.

(a) The electric part of D2 is diagonal and commutes with every E_e. The remaining Hermitian H_h has at most756 absolute two-hop path weight per W1 input and output row, by the checked complete path classification. Every path has total integer field displacement l1 norm at most2. For an arbitrary vector psi, row Cauchy and then the column bound give

 sum_e ||[E_e,H_h]psi||^2
       <=756 sum_(paths x->y) |coefficient| |psi_x|^2
                                      sum_e |Delta E_e|^2
       <=4*(756)^2 ||psi||^2.                           (C3)

This includes all gates, B masks and normalized spin coefficients. It is not a replacement of the global n by a local support: the factor is independent of n because the input has exactly ONE hole and the complete canceled path count is per input hole. Diagonal returning words contribute zero to(C3). Multiplication by delta is included in c.

(b) Each exact negative-grade J_(mu,-1), and each of its field commutators, annihilates a locally filled A cone. Indeed it would have to lower the local nonnegative hole number by one, while outside the exact circuit cone it acts as identity. Let Q_U be the projection onto at least one hole in that fixed cone. The local displacement norm bounds ||[E_e,J_(mu,-1)]|| and ||J_(mu,-1)|| uniformly, and the former is zero if the edge is outside that cone. Thus the jump-gradient sum for this mark is <=c Q_U. Bounded cone incidence gives sum_mu Q_U<=c W, so on W1 the total exit Gamma is <=c P_alive.

For the exit contribution to B_e use the COMPLETE self-adjoint expression

 B_(mu,e)^exit=kappa/2[J_(mu,-1)*[E_e,J_(mu,-1)]
                         +[J_(mu,-1)*,E_e]J_(mu,-1)].  (C4)

Every summand has two-sided Q_U support, norm at most c, and only a fixed number of mu cones meet a given e. Therefore (sum_mu B_(mu,e)^exit)^2<=c sum_(mu:e in U_mu) Q_(U_mu). Summing e and using bounded incidence again gives <=cW. This proves the exit part of the second bound(C2) without a conditional field moment or a spin loss floor. Coherent branches inside a mark remain inside the same J in(C4).

(c) For every exact neutral mark K_mu, the fixed-cone weighted displacement norm gives ||K_mu||+sum_e||[E_e,K_mu]||<=c epsilon. Thus its Gamma sum is <=c epsilon^2 I. There are O(n) marks, giving c epsilon^2 n in the first bound(C2). At a fixed e only O(1) such cones occur, so the complete neutral drift has norm <=c epsilon^2 at that e. Summing its SQUARED norms over the 6n links gives c epsilon^4 n in the second bound(C2). This keeps every neutral gain and anticommutator, including later births. A global norm squared c epsilon^4 n^2 is unnecessary because the field columns are summed AFTER the bounded-incidence edge estimate.

(d) Every edge commutator with the slow Hamiltonian epsilon^2 V_1 has norm <=c epsilon^2. The fixed local displacement norm of its exact remainder is used; a bound involving ||E_e||=S is not used. Summing squared edge norms costs c epsilon^4 n. Combining the Hamiltonian, exit and neutral columns with ||x+y+z||^2<=3(||x||^2+||y||^2+||z||^2) proves(C2).

Global P_1 projections commute with E_e and do not enlarge any of these norm bounds. The assertions concern the finite-spin physical Gauss carrier, where every factor is bounded. No unbounded-rotor stochastic calculus or norm continuity assumption is needed.

## 2. A direct channel proof of the short-age Gram estimate

Let R_t be the exact displacement Gram(5)--(6) of CONNECTED_LEDGER. For a positive alive input tau of mass m, set

 y(u)=Tr R_(epsilon^2 u) tau,   y(0)=0.

Differentiate the channel expression(6). With a Stinespring isometry V_u for Ttilde_u and A_e=E_e^out V_u-V_u E_e, the result is

 y'(u)=sum_e Tr Ttilde_u(tau) Gamma_e
          +2 Re sum_e Tr[(A_e sqrt(tau))* B_e^out V_u sqrt(tau)]. (C5)

To verify the second term, expand A_e*B_e V_u and its adjoint; these give Ttilde_u*({E_e,B_e})-Ttilde_u*(B_e)E_e-E_e Ttilde_u*(B_e), exactly the remaining differentiated terms. It is not necessary to choose V_u differentiably: the left side is differentiated from the finite-dimensional channel, and any Stinespring representation at this u gives the displayed algebraic identity.

The channel is trace preserving even after absorption. With a=c(1+epsilon^2 n), b=c(1+epsilon^4 n), (C2) and column Cauchy imply

 y'<=a m+2 sqrt(b m y).

A scalar comparison, or the supersolution m(sqrt(a u)+sqrt(b)u)^2, yields

 0<=R_(epsilon^2 u)<=c[(1+epsilon^2 n)u
                           +(1+epsilon^4 n)u^2] P_alive. (C6)

At u=0 the comparison follows by a positive regularization and its limit. The inequality holds for every positive tau, hence as an operator form. It prices a finite/growing fast age directly in the ACTUAL finite-spin channel. There is no assumption that a leading rotor channel approximates it at that age. The bound is ballistic and by itself is not sufficient at full physical ages of order one.

## 3. Exact split at a finite fast age

Composition of two channel isometries gives an exact displacement cocycle: final-minus-initial field equals final-minus-intermediate plus intermediate-minus-initial. Column Cauchy therefore gives the operator inequality

 R_(s+t)<=2 R_s+2 T_s*(R_t).                             (C7)

This follows on an enlarged common environment representing the composed channel; equation(6) makes the Gram representation independent. Once a trajectory exits, T acts as identity on its field and R_t vanishes on that absorbed block. Spin capacity gives on the whole alive/absorbed carrier

 R_t<=24 n S^2 P_alive.                                 (C8)

Indeed each of the 6n field differences has squared norm at most4S^2. At physical ages t>=epsilon^2 U, (C6)--(C8) imply

 R_t<=2c[(1+epsilon^2 n)U+(1+epsilon^4 n)U^2]P_alive
                           +48 n S^2 T_(epsilon^2 U)*(P_alive). (C9)

For a shorter age use(C6) alone. The alive probability in(C9) is EXACTLY Tr Z_(epsilon^2 U)(tau), even with arbitrarily many original neutral events before U. It is not the probability of no original mark whatsoever, and confusing those events would invalidate the estimate.

For the actual initial atom and continuously varying positive source define

 M_U(t)=1_(t>=epsilon^2 U) Tr Z_(epsilon^2 U)(tau_0)
        +integral_0^max(0,t-epsilon^2 U)
                         Tr Z_(epsilon^2 U)(I(s)) ds.   (C10)

This is the total mass of the actual injected inputs old enough to have survived that fixed physical age. Later neutral histories are included; absorption occurs only on the exact grade-minus-one exit used by the diagnostic kernel. It is not a microscopic conditional hazard or a changed recorded process. Positivity and the source-mass bound(2) now yield

 G(t)/n <=C_T epsilon^2[(1+epsilon^2 n)U
                                  +(1+epsilon^4 n)U^2]
                            +C epsilon^-2 M_U(t).       (C11)

The last factor uses S^2<=delta/(K epsilon^2). No locality substitution has been made: the remaining capacity is global nS^2, and it is multiplied only by the TRUE surviving mass(C10).

## 4. The spin crossover and the exact missing source estimate

Set U=epsilon^-1, corresponding to physical age epsilon. The first term(C11) is bounded by C_T[1+epsilon^3 n] for epsilon<=1. Together with CONNECTED_LEDGER(19), this proves the ACTUAL inequality

 sup_(t<=T) Tr rho_micro(t)Q/n
 <=C_T[1+epsilon n^(5/2)+epsilon^3 n]
       +C epsilon^-2 sup_(t<=T) M_(epsilon^-1)(t).       (C12)

This is a new finite-spin crossover estimate, not merely the old capacity applied to all source mass. It keeps the complete exact kernel, actual source and every original mark before the bound. Its remaining sufficient condition is

 sup_(t<=T) M_(epsilon^-1)(t)<=C_T epsilon^2.             (C13)

In the declared comparison window epsilon n^(5/2)<=C_*, (C13) would prove a volume-uniform actual quadratic electric density. The default checked mass bound is only M_U<=C_T epsilon^2 n, so it does NOT imply(C13). No result in this packet proves(C13). In terms of the source mass per volume, it asks for a remaining fraction O(1/n) by physical age epsilon; that volume price must not be omitted.

More generally, any chosen U(epsilon,n) can be used in(C11). The short-age term and the actual survival term must both be paid. A fixed-U comparison followed by an unproved exchange of U and epsilon limits does not do so. A decay estimate only for the leading rotor channel at fixed global B count also does not apply to(C10)'s evolving arbitrary background. The thin-strip example illustrates why a scalar low global B density is not automatically sufficient, but it gives no lower bound on(C10).

The condition(C13) is UNWEIGHTED and does not require an integrable age tail or a positive hole-field residence bound. It is a genuinely different sufficient consumer from the earlier weighted-residence target. It can still be hard: long-lived dark components, same-grade evolution and actual source weights have all been retained. We do not call the condition established, necessary, or target-independent. This proof narrows the needed dynamical estimate; it does not settle the volume-uniform energy question or quadratic uniform integrability.

## 5. Evidence and restrictions

This argument is analytic. The nearby strip runner does not test(C1)--(C13), and no finite numerical check replaces the exact column proof. No new full quantum-law identification, source replacement, thermodynamic limit, energy/W1 convergence, physical work law or native selection follows. The actual signed-ledger input, local normal-form displacement estimates and their precise provisional checks are listed in SOURCE_BINDINGS. This additional proof has not been covered by the root's earlier Stinespring PRE merely because it is in the same directory.
