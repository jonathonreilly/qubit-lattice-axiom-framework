# Uniform local spin-target to rotor transfer

Candidate analytic partial result for the finite-spin EFFECTIVE target, not the fast microscopic density. This is a separate part of the original contract. It does not invoke DEFECT_LEMMA and does not infer microscopic convergence from it. It retains both original instruments separately, all later sectors, bare Omega and fixed K,delta,kappa. The common rotor thermodynamic construction has the focused independent receipt58e6bb3e9657a3952b94120af8308b266e9ecbbb5a01d44a7c0e4f933a1554f6; the needed localization mechanism is restated below rather than treating thermodynamic existence as a missing premise.

## 1. Actual finite-spin coefficient, including its correction

The complete microscopic-energy parent section1 proves, on the P spin space,

 H4_S=-2 sum_(unordered dist(a,c)=2)(F_c,S F_a,S P)^*(F_c,S F_a,S P)
       -(1/(2C))sum_(ordered c=a or dist(a,c)=2){M_a,S,D_c},
 M_a,S=P F_a,S^*F_a,S P,  C=S(S+1).

The spin target is h_S=KD+delta H4_S and L_(m,S)=sqrt(kappa)P j_(m,S)F_a,S P. The anticommutator is kept; it is neither discarded as a scalar nor assumed negative in operator order. This is the canonical fixed-graph target of the actual compensated law.

Embed the spin links into integer rotors. For a LOCAL bounded extension of the correction, replace D_c/C in that formula by

 d_(c,S)=sum_(b~c)(1-n_b) [E_cb(E_cb-q_c)/C] 1_(|E_cb|<=S).

On the physical spin box this is exactly D_c/C. Outside that box it is a proof extension, not a new physical Hamiltonian. It is positive, has norm<=6, and tends strongly to0. Normalized U_S extended by zero outside[-S,S] and its adjoint are contractions tending strongly to U and U^*. Leave the electric term KD unchanged on the full rotor carrier. Every actual finite spin box reduces the extended law, and Omega lies in every box. Thus its physical spin evolution is exactly preserved by this extension.

All bounded target coefficients are now local, with uniform bounds on the full common carrier. The incidence Schur estimate gives ||F_a,S||^2<=12, ||M_a,S||<=12, and a pair term norm<=288delta. A center receives half of18 pair terms, at most2592delta. The19 ordered anticommutator terms centered at a have total norm at most19*12*6delta=1368delta. Hence an actual center decomposition obeys

    ||A_(a,S)||<=3960delta,
    ||Gamma_(a,S)||<=80kappa,
    sum_(m at a)||L_(m,S)||^2<=108kappa.              (S1)

For the loss bound: in the input sector with o occupied B neighbors, F has incidence product(6-o)(o+1), and the post-hop microscopic birth loss is at most2(5-o). The sector bounds are60,80,72,48,20,0 in units kappa. The spin weights never exceed1. Resolved B norms squared are<=9 and coherent ones<=18, proving the last inequality. These are operator bounds on every later sector, not only Omega.

A_(a,S) is supported within radius3. Exact conjugation by the strongly commuting electric D adds only one nearest-neighbor halo. In the electric interaction picture the center generator therefore has support in B4(a), cardinality129, and completely bounded norm at most

    lambda_star=7920delta+160kappa.                   (S2)

The rotor law has the same estimates with a smaller magnetic constant. The electric flow is strong-* continuous, not norm continuous on every local B(H_X); use trace-class Bochner and dual strong/ultraweak integrals just as in the explicit finite-volume construction.

## 2. Uniform localization followed by a fixed finite patch comparison

For initial observable support X the electric image is contained in X^+, cardinality<=7|X|. A string of n nonvanishing center generators has at most

    product_(j=0)^(n-1)129(7|X|+129j) <=16641^n(q)_n,
    q=max(1,ceil(7|X|/129)),

possible center labels. Every insertion enlarges radius by at most8. With a_star=16641lambda_star and R_(q,m)(z)=sum_(n>m)binom(n+q-1,n)z^n, two source restrictions agreeing through radius8m+1 obey

    ||T_(S,L,t)(O)-T_(S,patch,t)(O)||
            <=2||O|| R_(q,m)(a_star t),
    0<=t<=1/(2a_star),                              (S3)

uniformly in S and volume. The same inequality holds for the rotor target. Its proof uses the unital gain/loss cancellation and the norm bound on strong integrals; it does not require norm-Bochner continuity of the electric orbit.

For a chosen error eta>0, choose m from the explicit scalar tail, hence a finite patch independent of L and S. On this patch all bounded spin target coefficients and their adjoints converge strongly to the rotor coefficients. In the common electric interaction picture they act strongly continuously on trace class, are uniformly bounded, and converge there on every fixed input. The bounded Dyson series, finite-rank approximation and domination yield

    e_patch(S,T)=sup_(t<=T)||rho_(S,patch,t)-rho_(rotor,patch,t)||_1 ->0

from the same Omega. Consequently for every large enough torus,

    sup_(t<=T)||rho_(S,L,t)|_X-rho_(rotor,L,t)|_X||_1
                    <=4 R_(q,m)(a_star T)+e_patch(S,T).           (S4)

This is NOT a choice S(L) at fixed volume: the patch size and the subsequent S threshold are independent of L. For the finitely many even cubic periods below the chosen buffer, take the maximum of their finite-graph errors; it also tends to0. This proves convergence uniformly over ALL cubic tori in the contract on the common small-time interval.

Every finite T follows by uniform contraction composition, still with constants independent of S. Subdivide T into M slices<=1/(2a_star). At each slice choose a finite-region CP approximation using(S3), uniformly over the entire unit ball of the previous finite algebra. That bound applies even when the intermediate observable depends on S and time and is not norm continuous. Summing slice errors localizes the full finite-horizon map into one sufficiently large finite patch uniformly in S. Apply the same fixed-patch trace-class limit over the whole T. This proves(S4)'s qualitative uniform-volume conclusion on every finite horizon.

There is no asserted uniform rate for e_patch from a global norm difference U_S-U, which does not vanish. A constructive alternative is its finite-field history expansion: starting from Omega, n bounded-generator insertions reach each density leg's total absolute field at most4n. On that cap a shift weight differs from one by at most(s+1)^2/C, and d_(c,S) is O((s+1)^2/C). A fixed-order coefficient converges with an explicit polynomial/C bound; its factorial Dyson tail is summable at fixed patch and time. This supplies a finite tolerance procedure whose patch and spin resource depend on X,T,tolerance and the supplied couplings, never on the torus volume. It is not a feasible laboratory cost claim.

## 3. Exact original finite-region record outputs

For fixed monitored centers F, remove only their jump gains to form the no-monitored-event CP subunital propagator. All their losses and all exterior gains remain. Anchor the connected expansion on X^+ union_(a in F)B2(a); its size is<=7|X|+25|F|. Every specified original jump is in this fixed anchor. For fixed ordered marks and timestamps, the background insertion count is the same as above; summing background simplex volumes over the n+1 waiting intervals gives T^l/l! at order l.

Choose a COMMON reference dominating measure on F histories: its density is the product of9kappa for each resolved label, or18kappa for each coherent-edge label, on each ordered simplex. These dominate the respective ||L_(m,S)||^2 for every S and the rotor limit. Its total mass is exp(108kappa|F|T). Thus spatial localization bounds the integrated local quantum-output trace norm by this scalar mass times the tail in(S3), with the enlarged anchor. This estimate is uniform for outcome-dependent local tests and retains the actual coherent edge maps without revealing their sign.

On each fixed patch, the original marked output kernels converge in trace norm for a fixed finite label word and timestamps: the no-event propagators converge strongly on trace class uniformly on compact time intervals, each B_(m,S) and its adjoint converge strongly, and products follow by uniform boundedness and finite-net approximation of the compact limiting input orbit. Dominated integration and the uniform sum_(n>n0)(108kappa|F|T)^n/n! tail then give convergence of the full classical/quantum output density in L1 over finite-region timestamp histories. Unobserved exterior events are already included in each no-monitored-event propagator. Arbitrarily many later events are not removed.

For all finite T, first cut the monitored record-number tail, then use uniform finite-support approximation for each remaining finite product of no-event propagators/jumps, and finally remove the cut. Therefore the effective-spin-to-rotor comparison holds even for this finite-F exact-timestamp integrated trace topology, and in particular for every fixed deterministic bin instrument requested by the contract. This assertion is about the EFFECTIVE SPIN target; the fast microscopic instrument has no such proof here.

## 4. Weighted local observables of the targets

The bounded spin and rotor target terms change a local absolute field Q_R by at most4 for Hamiltonian/loss terms and2 for jumps. Their local strengths in(S1) are uniform in S. The diagonal cutoff d_(c,S) does not change field bandwidth. The exact commuting electric term preserves every Q_R. Integer-band decomposition gives ||Q_R^u O Q_R^-u||<=(2s+1)(1+s)^u||O|| for bandwidths. The usual quadratic-form Gronwall estimate therefore gives, from Omega,

    sup_(S,L,t<=T) Tr(Q_R^p rho_(S,L,t)) <=exp(C_(p,R)T)<infinity

for every fixed p,R,T. All constants use only the local uniform strengths above. Bounded truncation first passes these estimates to the rotor limits. Higher moments give uniform integrability; for a symmetric Q_R^2-relative local form A and Pi_R0=1_(Q_R<=R0),

 |Tr A rho-Tr Pi_R0 A Pi_R0 rho|<=2 C_A Tr(Q_R^4 rho)/R0^2.

Thus the target-spin local energy and current expectations also transfer to the common rotor process, using their actual finite-spin correction and the shared KD. This is not a statement about the fast microscopic energy or its moments. Initial actual microscopic energy per A is6delta epsilon^-2, while the rotor mean is-618delta, so such an identification would already fail at time zero.

## Remaining microscopic bridge

The full contract still needs a volume-uniform local comparison between the actual fast microscopic evolution from bare Omega and this spin target, including the original mark outputs. That is the target-strength obligation. The present result removes the separate uniform-volume spin-to-rotor step; it does not rename the harder first step or supply its field moments.
