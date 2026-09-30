# Pre-exposure reconstruction: local original-output time compactness

Frozen before opening original-record-local-time-compactness-route/WORKING_PROOF.md or HOLDER_REFINEMENT.md. This is a focused independent check, not a formal source review. Exposure: I authored the checked DEFECT, mean-count and first-electric-moment inputs. Root supplied the target CONTRACT and mechanism briefs, including an enlarged electric cutoff, two-sided hole support, a proposed C epsilon+C/sqrt(R)+C_R|t-s| modulus and later the proposed 1/5 Holder optimization. Thus this is an independent reconstruction of the new argument, not a blind discovery of its mechanism. No author proof/code/results have been read. No numerical computation is needed or claimed.

Authority is origin/main fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7 and selected procedures7146. Read actual LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT source definitions, checked DEFECT in full, my first-field proof and the new target contract. Supplied spin/hard-core carrier, compensated Hamiltonian, original resolved/coherent marks and bare Omega remain imports. No native or audit status follows.

## Independent derivation

Fix the full stated output specification X,F,T,bins,M. The register is the actual capped word in original labels with their bin tags and order. Its cap only coarse-grains the output; jumps continue after overflow. Register maps are deterministic classical updates with complete Kraus columns. The dual channel is a contraction on the direct-sum algebra of system observables, even if the dimension grows with M. All monitored F centers must be included in an observable's interaction anchor. Unmonitored disjoint terms cancel their full gains and losses. Bin boundaries change coefficients but do not themselves change the recorded state (no added running-bin pointer).

For trace-norm duality take an arbitrary common-carrier Hermitian test O of norm<=1. Conditional expectation onto diagonal classical blocks preserves the norm and the expectation. Compress its rotor quantum factors to the exact finite-spin subspace; this is a contraction even if a chosen field cutoff R exceeds S. Let P_A fill all A factors of X and O0=P_A O P_A. The physical local-hole bound gives, uniformly in O,

    |<O-O0>_physical(t)| <= C_(X,T) epsilon.

O0 commutes with W and in fact with every individual vacancy projection: inside X it acts only on the fully occupied A block, and outside X it is the identity. Choose a finite electric set Z_E containing every link in each diagonal compensated electric term that can fail to commute with O0. This is a bounded one-step enlargement of X, including occupation-dependent terms at nearby A/B factors. Put P_R=prod_(e in Z_E)1_(|E_e|<=R) and O_R=P_R O0 P_R. The first-field moment and gentle compression give error C_(X,T)/sqrt(R). Adding P_R does not trigger an infinite enlargement of the electric set: every diagonal electric term commutes with P_R, so [D,O_R]=P_R[D,O0]P_R.

The exact local circuit Y gives ||Y*O_RY-O_R||<=C_X epsilon uniformly in R,S,M, since O_R has fixed support and norm<=1. Registers do not change the circuit cone. Thus physical output increments differ from increments of the SAME O_R in the exactly rotated joint state by C epsilon+C/sqrt(R). To bound the latter, use the full original joint generator.

A pointwise local rotated-hole bound is available although Y's coloring need not preserve translations:

    Tr sigma(t)w_a =Tr rho(t)Y*w_aY
                    <=2Tr rho(t)w_a+C epsilon² <=C_T epsilon².

The square is essential here; mere ||Y*w_aY-w_a||=O(epsilon) is insufficient. The elementary projection commutator inequality proves it. It extends unchanged when summing over classical record blocks because the quantum marginal is the exact original ensemble.

The singular second Hamiltonian coefficient decomposes as D2=D_mot+D_el/[S(S+1)], where

    D_mot=sum_a F_a F_a* +sum_a F_a*F_a(Q_gate,a-1)
                                  +sum_(a!=c)[F_a,F_c*].

D_el is exactly sum_(a,b~a) n_a(1-n_b)E_e(E_e+k_(a,b,q))Q_gate,a, with k=+/-1 and the actual orientation convention. Each local D_mot term annihilates the all-A-occupied subspace on BOTH sides of a bounded neighborhood. F_aF_a* needs a hole at a; the gated difference needs a neighboring A hole; a cross term transfers a pre-existing hole between the two A sites. For the finite interaction sum meeting O_R, enlarge its A set to include both the terms and the support of O_R. Because O_R preserves all those vacancies, its commutator with D_mot is Q_A[.,O_R]Q_A for Q_A=1-prod n_a on that set. Its norm is C_X independent of R and S. Hence its expectation is O(epsilon²), not O(epsilon); the prefactor delta epsilon^-2 costs O(1).

The electric contribution has the EXACT coefficient K, using epsilon²S(S+1)=delta/K. Sandwiching every noncommuting term by P_R bounds its commutator norm by C_X K(R²+R). This remains valid when R>S, since then the pertinent spin fields are already bounded by S<R. It is not permissible to use only a cutoff on links belonging literally to X when coefficients on a neighboring star multiply an occupancy changed by O0.

For bare original jumps, the complete registered gain/loss acting on O_R is supported on a finite anchor X_R union F. Each bare j has right input factor w_a. The registered gain j*O_updated j and both losses are two-sided hole-supported on an enlarged finite A set (O_R preserves its all-occupied block). Its expectation is O(epsilon²), so kappa epsilon^-2 again costs O(1). Coherent signs remain within their original j; no split is used.

The first transformed jump coefficient j1=[-F+F*,j] has grades0,-2, while j has grade-1. On grade-zero O_R every COMPLETE polarized gain/loss cross term has grade +/-1, also when the register is updated. Its local norm is C_X,F. On an all-A-filled neighborhood its diagonal block vanishes. The positive local-hole estimate therefore bounds its expectation by C epsilon. Its coefficient epsilon^-1 costs O(1). All remaining dissipative terms have local norm O(1), since J=j+epsilon j1+O(epsilon²). D4,epsilon²D6 and R_H also have bounded local commutator norms. The huge W term vanishes on O_R. These arguments show, almost everywhere in physical time,

    |d/dt <O_R>_sigma(t)| <= C_(X,F,T)(1+R²),

uniformly over the unit ball of all common-carrier tests, spin, safe volume and register dimension. Finite bin boundaries do not produce state jumps, so integrate this bound across them without an extra atom. The constants may depend on the fixed geometric support/F; no extensive volume factor occurs.

Consequently the proposed modulus follows, and choosing R=max(1,|t-s|^(-2/5)) yields

    ||Gamma(t)-Gamma(s)||_1 <= C epsilon+C_T |t-s|^(1/5)

for 0<|t-s|<=1 (larger times are trivial after enlarging C). No upper restriction R<=S is necessary or desirable.

## Compactness and limits of this reconstruction

First-field tails put each fixed-time output in a uniformly approximable finite-dimensional set after field cutoff. The capped, fixed-bin original register is already finite; if a subsequently uncapped output is wanted, the old count-overflow bound supplies that separate limit. For epsilon_n->0 and arbitrary safe volumes, pointwise precompactness plus the asymptotic modulus gives a uniformly-in-time trace-norm convergent subsequence on a dense countable time set and then on [0,T]. This is the elementary diagonal/finite-grid proof of asymptotic Arzela-Ascoli; individual family members need not have a uniform derivative before the O(epsilon_n) error is removed. The limit is 1/5 Holder with the stated constant.

Nothing here identifies the limit, shows uniqueness/boundary independence, provides a joint purification or continuous-timestamp total variation, proves physical energy uniform integrability, or controls the epsilon^-2 hole-weighted quadratic field source. Gauss is retained by the actual dynamics; no gauge-violating preparation is introduced by using ambient test operators or mathematical compressions. A separate passage of local Gauss constraints is possible but is not required to establish this target.

## Specific comparison risks to check in the author proof

1. Electric cutoff includes every coefficient link whose occupancy factor can be changed by O0; it commutes with all diagonal terms, so the enlargement terminates.
2. The D_mot commutator and full bare registered jump action have two-sided, not merely one-sided, local-hole support.
3. The local rotated-hole estimate is O(epsilon²), obtained quadratically, not by O(epsilon) conjugation norm.
4. The first cross dissipator uses all recycling/loss terms and exact grades; registers anchor every F center.
5. Uniformity is over the entire test unit ball, including common-carrier tests compressed to spin boxes and R>S.
6. Bin conventions do not add deterministic record discontinuities. Cap is only output coarse-graining, not jump suppression.
7. Moment cutoff gives trace-norm pointwise compactness, then asymptotic equicontinuity upgrades it uniformly in time; no stronger process convergence follows automatically.
