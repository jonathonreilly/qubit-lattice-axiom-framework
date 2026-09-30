# Local finite-spin original response with a capacity-priced Gauss completion

Authored conditional construction, September 30, 2026. This packet requires a focused independent check before substantial reuse. It is not formal review, audit, a new primitive or the microscopic M4 theorem.

There is a concrete local finite-spin-to-rotor first-event comparison under explicit regional count, charge and total-field caps. The actual distant background may have arbitrary occupation, charges, fields and coherence within the spin carrier, and may be entangled with the region. The original resolved or coherent-edge marks, their continuous timestamps, and bounded local postmark quantum output are preserved. The full finite-spin diagonal compensation is retained.

Two compatibility steps are needed. First, a compact Gauss completion has both an explicit maximum field and an explicit global total-field price, independent of torus volume. It is therefore a legitimate input in the same spin box and in the checked global weighted response theorem. Second, the diagonal compensation is treated exactly in an interaction picture; a separate local channel restores the physical readout. A global field moment of the actual arbitrary background is never assumed.

## 1. Frozen domain and imports

Main is 30a9461ee19a49b99fa6628fe942f08e504e8903, freshly confirmed with the open inventory before this route. Procedures 7146fe17a76de41badcaca3c3c7cac6d11eb2a00 remain selected. Actual local compensation, original formation maps and Gauss conventions were read completely in the continuing session. Source identities are bound separately. All quantum spaces, laws, rates, preparation and fast time are supplied model assumptions, not consequences of native M2 or selected axioms.

The precise model is the compensated leading W=1 finite-spin law on an even cubic torus, with integer S>=1, C=S(S+1), q=0,+1,-1, oriented A-to-B links and div E=q-1_A. Write

    H2_S=C_S+[F_S,F_S*]=Hbar_S+Delta_S,
    Delta_S=sum_a(D_a,infinity-D_a,S)Q_a,
    A_S=-i delta H2_S-kappa G_S/2,
    G_S=sum_m j_(S,m)*j_(S,m),
    Z_S(t)=exp(t A_S).

Q_a is the original eighteen-neighbor A-occupancy gate. F_S and j_S contain the actual normalized-spin shifts, including their boundary zeros. The original j is either resolved by edge/sign or the unnormalized coherent sum of the two signs on each edge, applied separately throughout. It fills the unique A hole and a vacant B site. The first-event dynamics stops at that original mark; no later postmark evolution is included by this response definition. Time is the leading fast time of this supplied law, not a uniform approximation to the full microscopic process.

The cancelled Hbar_S has the checked one-hole blocks

    P_h Hbar_S P_h=P_h[F_h,S F_h,S*-
                      sum_(a:dist(a,h)=2)F_a,S*F_a,S]P_h,
    P_a Hbar_S P_h=P_a[F_a,S,F_h,S*]P_h.

It obeys ||Hbar_S||<=744, so M=1092 is safe, and 0<=G_S<=12. Same-hole B rearrangements remain. No norm of the extensive global F is used.

Take a graph ball D=B_R with internal links only; crossing links are outside its tensor factor. The physical input density, including an arbitrary noninteracting ancilla Z, has global W=1 and support

    hole in B_r, R>=r+5,
    K_D=N_B(D)+|Q_D|<=K,
    Q_D=sum_(x in D)(q_x-1_A(x)),
    F_D=1+sum_(links internal D)|E|<=F,                (1)

where K,F are fixed positive integer caps. These are regional spectral support hypotheses, not source-derived conclusions or physically performed measurements. There is no empty annulus, static B mask, vanishing crossing flux, classical exterior or independence assumption. The observed quantum cell set X has all endpoints in B_(R-4); all original mark/time labels remain observed.

Set

    B=R+K+3,
    L even, L>=max(28,4K,2B+4),
    D0=2K+2(F-1), N=(2B+1)^3,
    M_ref=F+D0+N(D0+K),
    S>=3K+2F.                                        (2)

The constants are deliberately conservative. The completion and bounds below explain every resource in (2).

The checked inputs are the finite-global-k rotor absorption and polynomial response, the local rotor response, and the global finite-spin response, at their original scopes. The latter two source/check pairs are 74b15d0f/eb146a0c and d0a96836/c3669299. Their full arguments were read. No result about dense-background absorption or global moments of the actual input is imported.

## 2. Compact physical completion with maximum-field and total-field bounds

Let p,m be the numbers of plus/minus B records in D and a the number of minus A records. There is exactly one A hole in D. Then

    Q_D=-1-2a+p-m,
    sum_D |q-1_A|=1+2a+p+m=2p-Q_D<=2K.               (3)

Thus the count/charge cap also controls all regional charge deviations, without measuring any charge word.

For every regional boundary vertex define the commuting integer deficit

    d_x=q_x-1_A(x)-div_internal E_x.

It vanishes at interior vertices by physical Gauss. Its l1 norm and sum obey

    sum_boundary |d_x|<=2K+2(F-1)=D0,
    sum_boundary d_x=Q_D, |Q_D|<=K.                   (4)

The bound uses the actual internal field l1 cap; crossing-field circulations may still be arbitrarily large and are not retained by the reference.

Physical Gauss equates d to exterior crossing divergences. Distinct d sectors therefore have orthogonal exterior support. The reduced state on D and Z is exactly block diagonal in d, although it may retain arbitrary internal charge/field/ancilla coherence within each block. This is the same spectral fact used in the checked local rotor theorem, not a new detector or classical-background assumption.

For each allowed d construct a reference exterior only inside the cube C_B=[-B,B]^3. Its complement to D within that cube is connected. For example, from an exterior point move a nonzero coordinate away from zero to a cube face without decreasing graph distance from zero, and use the connected outer faces to reach a fixed root. Every boundary vertex of D has a crossing neighbor in this finite exterior. The plane x=B supplies at least K exterior B sites. The side condition in (2) embeds the entire cube and its links without periodic aliasing.

Choose one crossing edge per boundary vertex and assign its oriented integer field to supply d_x. These edges are distinct by their inside endpoints. Keep every exterior A plus, place |Q_D| exterior B charges with sign minus sign(Q_D) at fixed sites of the plane, and leave the other exterior B vacant. Outside C_B use Omega. The crossing fields contribute total exterior divergence -Q_D, exactly matching the added exterior charge. The remaining internal exterior divergence is zero-sum and has l1 norm at most D0+K.

Choose one fixed tree spanning C_B minus D. Integer subtree flows solve that divergence. Each tree-edge flux is a sum of a subset of the zero-sum demand and hence has absolute value at most(D0+K)/2. Crossing fluxes have magnitude at most D0, and unchanged regional fields at most F-1. Consequently every completed link obeys

    |E_link|<=max(F-1,D0,(D0+K)/2)<=D0+K<S.           (5)

The slack in (2) is not needed for Gauss but makes the physical spin-box condition immediate. No capacity-violating flow is silently embedded into a finite spin.

The completed global total-field weight Q_global=1+sum_alllinks|E| satisfies

    Q_global<=F+D0+(N-1)(D0+K)/2<=M_ref.              (6)

This price is independent of L. A tree over the entire torus would not give this statement and is not used. The maximum-field bound alone would not give the needed global fourth moment; (6) is separately required.

The appended exterior basis vector chi_d depends only on d, not on any finer coherent internal word. Thus

    E_D(sigma)=sum_d V_d P_d sigma P_d V_d*,
    V_d psi=psi tensor chi_d,                         (7)

is a physical CP completion preserving the exact D-plus-Z marginal. The append is identical for all words in a d block. It introduces no extra observed mark and does not clone a nonsuperselected electric state. Every reference word has W=1 and

    N_B^ref=N_B(D)+|Q_D|<=K,
    Q_global<=M_ref,

and lies in the same spin box. The B count is odd because Q_D is congruent to N_B(D)-1 modulo two. Inter-count coherences within a d block are preserved. The finite-global-k response bounds apply to their direct sum. The reference is a mathematical physical state, not a claim of preparation by the actual source.

## 3. Exact local dressing by the full diagonal compensation

On the full finite tensor carrier, including W=0 outputs, write

    Delta_S=sum_(e=a->b) d_(e,S),
    d_(e,S)=n_a(1-n_b)[1-|u_(S,-q_a)(E_e)|²]Q_a.      (8)

The n_a factor removes the q_a=0 case. Every summand is diagonal, mutually commuting and lies between 0 and 1. It uses the link e, sites a,b and the eighteen distance-two A sites around a, so its vertex support lies within radius two of a and has diameter at most four. The total norm may grow with volume; it is never bounded by a volume-independent scalar here.

For a bounded local O, only d_e whose support meets O contribute to

    alpha_t(O)=exp(i delta Delta_S t)O exp(-i delta Delta_S t).

All other diagonal factors commute with O and with the retained factors and cancel at once. Therefore alpha_t(O) has a single radius-four support enlargement for every t, and unchanged norm. There is no repeated geometric expansion caused by commuting diagonal factors.

Let U_Delta(t)=exp(-i delta Delta_S t), and define

    Y_S(t)=U_Delta(t)* Z_S(t),
    A_S^I(t)=-i delta alpha_t(Hbar_S)-kappa G_S/2,
    J_S^I(t)=alpha_t(J_S),                             (9)

where alpha on the rectangular marked stack uses the same diagonal law on its W1 input and W0 output. G_S commutes with Delta_S. Thus ||A_S^I(t)||<=b:=delta M+6kappa and ||J_S^I(t)||<=sqrt(12), uniformly in S,L,fields and t. At each finite L the diagonal and all coefficients are bounded, so their time-ordered integrals are ordinary norm-continuous finite-volume expressions; no norm-continuity theorem for an unbounded rotor electric generator is borrowed. The uniform estimates come from (9), not the extensive Delta norm.

Each original Hbar word from input hole h accesses radius three and moves the hole at most two. Its dressed version therefore accesses at most radius seven and has the same possible hole displacement. An original marked edge has radius one about the input hole; its dressed version accesses at most radius five and still fills that hole and the same B neighbor. Dressing changes exact phases, not observed labels or shift patterns. These conservative7/5 radii suffice; the geometry control below finds the sharper6/4 for the listed full supports, which are not needed in the proof.

A time-ordered word of j interaction-picture generator factors from B_r consequently accesses only B_(r+2j+5). A final dressed original j_m has the same bound, including j=0. Hence, with

    m=floor((R-r-5)/2), n=m+1,                        (10)

all no-event and marked Dyson coefficients through m are regional operators on D. They agree for actual and completed spin inputs under exterior purification alignment. The alignment is possible because (7) preserves the D-plus-Z marginal; it commutes with these regional coefficients. It need not commute with the full generators or be a physical reset of the actual exterior.

The Dyson remainder with the bound b is

    u_n(t)=exp(bt)(bt)^n/n!.

The two aligned interaction-picture vectors differ by at most2u_n(t), and their original marked stacks by at most2sqrt(12)u_n(t). This includes arbitrary coherent inputs and ancillas, not just basis-word paths.

## 4. Restore the actual quantum readout

The interaction-picture marked vector is not the physical output and cannot simply replace it. In fact

    j_(S,m)Z_S(t)psi
      =U_Delta,out(t) j_(S,m)^I(t)Y_S(t)psi.          (11)

For the retained cell set X, let Delta_X be the finite sum of d_e whose support meets X. Its support lies inside D by the radius-four condition on X. The remaining Delta terms act only outside X and commute with Delta_X. Moving their unitary to the end and taking the exterior partial trace therefore gives, for every input output-density w,

    Tr_outsideX[U_Delta(t) w U_Delta(t)*]
      =Tr_outsideX[exp(-i delta Delta_X t)
                         w exp(i delta Delta_X t)].   (12)

The right side is the same regional CP output channel for both aligned states. It is norm contractive and preserves the actual local charge/field readout. The same formula applies to the terminal no-event branch. The time-dependent channel in (12) is mathematical bookkeeping for the original evolution, not an externally scheduled operation added to it. Nonzero original compensation phases in the control below explicitly show why dropping (11)-(12) would be wrong.

Set T=n/(8b), q=exp(9/8)/8<1. Then u_n(t)<=q^n for 0<=t<=T. The survival-plus-mark dilation has unit norm by original loss conservation, also in this interaction picture. Its aligned difference is at most2sqrt(1+12kappa T)q^n. Applying (12), the pointwise rank-one trace inequality and Cauchy–Schwarz in time gives the physical finite-prefix instrument bound

    epsilon_loc=4sqrt(1+12kappa T)q^n.                (13)

This is a Bochner-L1 original time/mark instrument with quantum output on X,Z. No diagonal trace-class multiplication operator on nonatomic L2(time), artificial hole-exit measurement or extra boundary mark is used.

## 5. Reference transfer, late tails and the all-time estimate

Use the checked rotor constants uniformly over odd global j<=K:

    C_K=max C_j, gamma_K=min gamma_j>0.

For the reference spin-to-rotor comparison, use the checked weighted coefficient constants a0=10000delta+12kappa, b0=8sqrt(kappa), M=1092. Put beta=5C_K delta M and

    R2(t)=1+8beta t+4beta²t²,
    L1=C_K[gamma_K^-1+8beta gamma_K^-2+8beta²gamma_K^-3],
    L2=C_K[integral_0^infinity exp(-2gamma_K t)R2(t)²dt]^(1/2),
    B_K=a0 L1+b0 L2,
    e=B_K M_ref²/[S(S+1)].                            (14)

This application now has actual justified hypotheses: the completed state is in the same spin box, its global B count is at most K, and (6) gives Tr(Q_global^4 rho_ref)<=M_ref^4. The arbitrary actual distant background has not been assigned this global moment.

The checked theorem gives all-horizon reference spin/rotor instrument distance at most2e, and reference spin survival amplitude at T at most

    C_K exp(-gamma_K T)+e.

Combining this with the interaction-picture prefix estimate bounds the actual spin survival amplitude by

    C_K exp(-gamma_K T)+e+2q^n.                       (15)

No absorption theorem for the actual arbitrary-background spin law has been assumed.

The actual spin first-event output after T has total mass at most the square of (15), including the possibility of permanently missing first-event mass. The completed rotor late mass is at most C_K²exp(-2gamma_K T). Add these positive masses to the early physical difference (13) and the reference transfer error 2e. The actual spin response and completed rotor response satisfy

    distance <= eta_spin,
    eta_spin=min{2, epsilon_loc+2e
       +[C_K exp(-gamma_K T)+e+2q^n]^2
       +C_K²exp(-2gamma_K T)}.                        (16)

The same bound controls every finite-horizon instrument with its terminal no-event LOCAL quantum density. If the horizon is at most T, the early argument suffices. If it exceeds T, the sum of later first-event mass and terminal surviving mass on each side equals its survival mass at T, by the same loss identity. No limiting surviving quantum state is asserted. Letting the horizon increase gives the entire positive-time first-event instrument by monotone convergence of its nonnegative integrated distance.

## 6. Same-input actual local spin-to-rotor comparison

Embed the SAME actual physical spin input rho into the rotor carrier on the SAME torus. Its global B occupation and field norm can be arbitrarily large; only (1) is assumed. The checked local rotor theorem compares this actual rotor response with the completed rotor reference because they have the same regional marginal and the reference has global count at most K. Its proof applies to the compact completion (7), not just the earlier volume-sized tree choice.

For explicit constants put

    n0=floor((R-r-1)/2)+1, T0=n0/(8b),
    eta_rot=min{2, 4sqrt(1+12kappa T0)q^n0
       +[C_K exp(-gamma_K T0)+2q^n0]^2
       +C_K²exp(-2gamma_K T0)}.                       (17)

The same early/late decomposition includes a finite-horizon terminal local density, as in section 5. The triangle inequality through the identical completed rotor state yields the actual same-input result

    sup_horizon distance(I_spin^X,Z(rho), I_rotor^X,Z(rho))
                     <=min(2,eta_spin+eta_rot).        (18)

All original edge/sign or coherent-edge labels, continuous first times and bounded postmark quantum outputs on X,Z are retained. Neither generator is projected to D; no spin transition is restored; no original record is replaced by a proxy.

For fixed K,F,r,delta,kappa, M_ref=O(R³). Thus R->infinity with R=o(S^(1/3)) makes both errors in (18) vanish uniformly over all safe L and all actual distant backgrounds. For example R=floor(S^(1/4)) gives e=O(S^-1/2), with exponentially small buffer terms for those fixed constants. The rate constants may be extremely large in K. This is a genuine joint local finite-spin/volume response statement for the declared input class, not fixed-volume convergence with volume dependence hidden in a constant.

An approximate-support version is available without performing a measurement. On the physical W1 input let P impose the three regional conditions in (1), and epsilon=Tr((I-P)rho). For either original instrument the full finite-horizon map is CPTP (including its terminal branch), and its infinite-time first-event map is trace nonincreasing. The gentle estimate||rho-P rho P||_1<=2sqrt(epsilon), applied on both sides, gives

    distance(actual spin output from rho, actual rotor output from rho)
      <=4sqrt(epsilon)
          +min(2,eta_spin+eta_rot) Tr(P rho P).         (19)

The good-support projection commutes with Gauss but is only a proof estimate. It is not observed, and epsilon remains a source-state obligation.

## 7. Exact controls and preserved failure

The first job passed its compact-completion and geometric assertions, then failed in a definitions loader: importing a previous script's bootstrap attempted to raise the already-fixed hard CPU limit 20 to 25. No mathematical assertion failed, no final output was written, and exact CPU/RSS were not emitted. Its exact code, price and failure record are preserved in `history/definition-loader-failure/`. The corrected loader extracts only the earlier checked function/class AST definitions and executes no previous bootstrap or run. The same mathematical controls were explicitly repriced; no old artifact was edited.

The corrected job passed in 1.426734 CPU seconds and 42483712 bytes peak RSS, under 20 CPU/120MiB. It checks five compact graph-ball completions, including positive, negative and zero regional charge, nonzero opposing boundary deficits, internal circulations and an A-minus word. All Gauss equations, count parity, same-spin capacity, exact regional data and total-field bounds are checked. A second coherent internal circulation has the identical boundary vector and appended exterior, preserving its offdiagonal coefficient. The cube/tree construction is embedded without aliasing at two allowed torus sizes in each case. Observed maximum reference fields are2,5,19,7,9 and total Q at most38,76,480,232,300, beneath the deliberately much larger proved bounds.

The exact indexed-term halo control retains every site/link factor of (8). The complete raw Hbar access region has radius3; its diagonal dressing has radius6 with 377 site and 510 link factors. The original dressed jump has radius4 with 129 site and 114 link factors. These finite counts corroborate the conservative7/5 support proof and are not a Hilbert-space enumeration.

Finally the actual rational Delta differences are computed for 61 original one-hole Hbar output words and 10 resolved birth outputs at S=6 and 9, both with and without a distant actual two-B birth word and an exterior circulation. Total incoming Delta changes from 0 to 24/7 or 8/5, but every near-field phase difference Delta_out-Delta_in agrees exactly. All ten birth phases are nonzero, and both phases within a coherent edge remain attached to that SAME original edge mark. Every generated charge/field word is checked against Gauss. These tests establish specific source bindings and phase controls; the all-input estimates follow from the analytic support, CP and passive arguments above.

The controls explicitly reuse only this agent's earlier checked elementary rotor word definitions, hash 2376287209496819d10d0e919682bee4f88527cbdda287cebe13f4420fe589a5. Capacity routing, bounds, diagonal compensation and dressing comparisons are new code here. The phase control enumerates actual rotor-word candidates with exact spin compensation values; it is not an operator-norm proof or a numerical all-time evolution. No dense carrier or full-torus state enumeration was used. Both STOP forms, deadline and one-thread resource conditions were enforced. No job remains active.

## 8. Failed shortcuts, closest prior and remaining theorem strength

A direct composition of the earlier local rotor completion with the global finite-spin response estimate was insufficient: it neither bounded the completed global Q moment uniformly in volume nor ensured the same spin capacity. The compact construction (3)-(7) supplies both missing statements under the new explicit REGIONAL field cap. A global Q4 condition on the actual arbitrary background remains unavailable and is not inserted.

Dropping Delta_S would also be wrong. Its global norm can be extensive and its original birth phases are nonzero. The exact commuting interaction picture and restored physical output channel (12) supply a separate locality argument. A static B shell, scalar field proxy or random independent exterior is never used. A direct unweighted spin absorption theorem is neither proved nor required.

The closest landed commuting-electric locality note was read in full. It gives a one-step diagonal halo and a continuity-aware locality proof for the A-occupied effective target. Its statement explicitly leaves microscopic volume-uniformity open. Here the diagonal is the actual finite-spin W1 compensation, the bounded propagated part is the exact cancelled fast operator, and the new compatibility issue is a physical capacity/moment-priced Gauss reference. The relevant inspected PR9399 sections likewise concern effective thermodynamic maps and do not supply (18). Repository/proposal search coverage is scoped, not an exhaustive novelty claim.

Equation (18) reduces a real compatibility gap for leading original first responses. It still does not prove that the actual microscopic source has small epsilon in (19), that its regional K,F grow slowly enough with R for the estimate to be useful, or that simultaneous holes and repeated sources can be reduced to these responses. At positive density K can grow as R³ while gamma_K is exponentially small; merely increasing R does not solve that dependence. Microscopic remainder accumulation, finite-time source coupling, dressed corrections, recurrent formation and unbounded local energy outputs remain open. No new native carrier, record law, physical clock or foundation has been adopted. This packet is frozen for independent checking before reuse.
