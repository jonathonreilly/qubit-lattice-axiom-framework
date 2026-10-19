# Nonuniform mediator numerator: separate slope and product sensitivities

New author derivation requiring distinct checking. The earlier finite-Schur interface594461 remains unchanged. The main improvement here is a selected three-source error numerator separating length-uniform O(epsilon) diagonal slopes from O(m epsilon) hopping products, while retaining ordered port and complementary-source feedback. Along the fixed-supplier shrinking-band family, the local logarithmic integral of the slope term is O(m epsilon), not automatically O(m² epsilon). This is not yet a complete nonuniform all-head/output tolerance theorem.

## 1. Domain and comparison convention

Use the positive scalar bond error model of594461: w=w0(1+e), |e|<=epsilon<1; exact fixed new occupations2j, unchanged capped processor and slow receiver. Work after subtracting the ACTUAL scalar C(w). The nominal physical phase, old K/W, reference packet, lambda, and limiting masses Z0,Z1,Z2 remain fixed. The actual final target would have the explicit exp(-it C(w)) factor. No actual mass congruence or linewidth is substituted into that nominal target.

For one cell of nominal length2n, nominal internal adjacency A0 has strong J_m, weak q, endpoint gamma, gap a=J_m-q. The actual adjacency A1 and endpoint diagonal matrix Gamma1 need not be reflection symmetric. Define

    a_*=(1-epsilon)J_m-(1+epsilon)q>rho>0,
    d_A=2epsilon J_m,
    x=rho²/a_*²<1,
    b_*=.185-(1+epsilon)(J_m+q)>0.

Then ||A1-A0||<=d_A by the degree-two row bound, both inverse gaps are at least a_*, and complementary resolvents are bounded by1/b_*. Using J_m as the largest nominal bond in this internal estimate is valid since q<J_m; endpoint changes are handled separately. Require all original physical window/background hypotheses. Bounds hold on both lips and in every inherited fiber sector.

The exact cell self-energy has unequal diagonal functions s_L(D),s_R(D) and a common reciprocal off-diagonal t(D). All are real functions of the same D before attachment. Closed-channel estimates below apply on its entire complementary spectral subspace. No commutation with actual G is used.

## 2. Length-independent diagonal perturbations

Let c_L,c_R be the positive slopes -s_L'(0),-s_R'(0). With nominal gamma on both ends put

    C_l=gamma²[(2epsilon+epsilon²)/a_*²+2d_A/a_*³],
    R_l=gamma²{(2epsilon+epsilon²)/[a_*^4(1-x)]
             +(d_A/a_*^5)[4/(1-x)+2x/(1-x)²]},
    E_l=gamma²[(2epsilon+epsilon²)/b_*+d_A/b_*²].       (1)

Then the endpoint-pair diagonal differences satisfy

    max(|Delta c_L|,|Delta c_R|)<=C_l,
    max(|Delta s_L(delta)|,|Delta s_R(delta)|)
                              <=C_l|delta|+R_l|delta|³,
    ||Delta Sigma_l(D_C)||<=E_l.                     (2)

These bounds do not grow with n at fixed gap. To prove them, separate the two endpoint coefficient changes from the internal inverse change. For p>=1, telescoping inverse powers gives

    ||A1^(-p)-A0^(-p)||<=p d_A/a_*^(p+1).

The slope uses p=2. By bipartite parity, each diagonal resolvent entry after removal of its linear term is the series -sum_(k>=0)delta^(2k+3)(A^(-2k-4))_aa. Summing the inverse-power difference gives the two terms of R_l; endpoint coefficient variation gives its first term. Both negative and positive eigenvalues are allowed in this argument. On the complement the ordinary resolvent identity and endpoint variations give E_l. The diagonal compression of the endpoint-pair matrix does not increase its norm. These are difference estimates, not independent remainder ceilings that would remain nonzero at epsilon=0.

## 3. Length-dependent hopping products at nonzero energy

For each real positive nonuniform cell, its n positive singular magnitudes sigma_i are at least a_*. The exact tridiagonal cofactor formula gives

    t(delta)=t(0) product_i(1-delta²/sigma_i²)^(-1),
    t(0)=(-1)^(n-1)gamma_L gamma_R product q_i/product J_i.

Let ell=-log(1-epsilon), tau_l=(2n_l+1)ell, and

    B_l=2n_l d_A/[a_*(a_*²-rho²)].

Weyl's singular-value bound |sigma_i1-sigma_i0|<=d_A and differentiation of log(1-delta²/sigma²) give

    |log(t1(delta)/t0(delta))|<=tau_l+B_l delta².       (3)

The ratio is positive: no sign gauge changes. Define

    H_l=exp(tau_l)-1,
    Q_l=B_l exp(tau_l+B_l rho²),
    H_l2=exp(2tau_l)-1,
    Q_l2=2B_l exp(2tau_l+2B_l rho²).

Consequently

    |t1/t0-1|<=H_l+Q_l delta²,
    |(t1/t0)²-1|<=H_l2+Q_l2 delta².                 (4)

The comparison is with the NOMINAL finite-energy function, not just its value at zero. In particular the even-factor derivative is not inferred from a small real reflection. Let Theta_l=(1-rho²/a²)^(-n_l)-1. Then |t0(delta)|<=|t0(0)|(1+Theta_l). Finite limiting-mass normalization of the nominal family is retained exactly; its nominal zero-energy normalized hoppings equal a1=lambda/sqrt3, a2=lambda sqrt(8/3), kappa=sqrt(3jlambda). The integer lengths are n1=n2=2m-1,n3=m.

## 4. Ordered port and complementary feedback differences

Index nominal by0 and erroneous by1. Use s_p,i=s_3R,i(D), not the left endpoint value. For each tuple require the explicit port Neumann margins eta_i<1 and complementary inverse margins k_i>0, obtained as in loaded5f909 with actual upper endpoint coefficients, actual gap and unequal endpoint self-energies. Equivalently directly certify the stated finite operator bounds below; no actual critical-ratio identity is required for these port/complement gates.

Write Gtilde_i=G(I-s_p,i G)^-1. Let B_i bound its norm, and let e_i(delta) bound BOTH off-diagonal P/C blocks. The same comparison to the commuting G0=m_j(D) gives

    e_i(delta)<= (a0+b0|delta|)/[(1-eta0_i)(1-eta_i)].

Uniform eta0_i,eta_i on the band may be used. Define

    p_delta=C_3|delta|+R_3|delta|³, c_delta=E_3.

Exact subtraction is

    Gtilde_1-Gtilde_0=Gtilde_1(s_p,1-s_p,0)Gtilde_0.  (5)

Because Delta s_p is block diagonal in P/C, the following bounds retain its selected and closed actions separately:

    D_PP=B1 B0 p_delta+e1 e0 c_delta,
    D_PC=B1 e0 p_delta+e1 B0 c_delta,
    D_CP=e1 B0 p_delta+B1 e0 c_delta,
    D_CC=e1 e0 p_delta+B1 B0 c_delta.                (6)

This is the important replacement for a full norm estimate that would turn the closed O(epsilon) change into an unsuppressed selected constant. In (6), a closed change reaches the selected port only through two off-diagonal kernel factors. All e_i are evaluated at the same physical delta; the calibration floor is retained.

Let tau_i bound ||t_3,i(D_C)|| and K_i be the full complementary three-source block in the fixed nominal mass convention (identity congruence on C). Let ||K_i^-1||<=1/k_i. The closed hopping difference is at most E_3, since it is an entry of Delta Sigma_3. Put

    D_K=sum_l E_l
          +E_3(B1 tau1+tau0 B0)+tau0 tau1 D_CC.     (7)

Each cell's source-local complementary compression costs at most E_l; the last three terms are the ordered difference of t_C Gtilde_CC t_C. Thus ||K1-K0||<=D_K and ||K1^-1-K0^-1||<=D_K/(k1 k0).

In the selected source Schur complement the effective port is

    G_eff,i=Gtilde_i,PP
       +Gtilde_i,PC t_Ci (K_i^-1)_22 t_Ci Gtilde_i,CP.

Take

    zCross_i=e_i tau_i,
    D_Z=D_PC tau1+e0 E_3,
    D_Y=tau1 D_CP+E_3 e0,
    D_eff=D_PP+D_Z zCross1/k1
                 +zCross0 zCross1 D_K/(k1 k0)+zCross0 D_Y/k0. (8)

The zCross_i are feedback bounds, distinct from the limiting source masses Z0,Z1,Z2. Equation (8) follows by three-term subtraction of the ordered product Z K^-1 Y and is valid without identifying opposite rectangular blocks as adjoints on one lip. No direct complementary inverse or closed forcing is deleted.

## 5. Selected difference numerator in the fixed nominal congruence

Let F_i be the selected Schur complement after applying the SAME nominal T_P and fixed sign gauge to both tuples and eliminating their own complementary blocks. Define

    C_sum=sum_l C_l, R_sum=sum_l R_l,
    h12=max_(l=1,2) H_l, q12=max_(l=1,2) Q_l,
    Theta12=max(Theta1,Theta2).

Let G_E1 bound ||G_eff,1|| (for example B1+e1² tau1²/k1). Then the explicit numerator is

    ||F1-F0|| <= D(delta),
    D(delta)=C_sum|delta|+R_sum|delta|³
       +sqrt3 lambda(1+Theta12)(h12+q12 delta²)
       +3j lambda(1+Theta3)²
            [(H_32+Q_32 delta²)G_E1+D_eff(delta)].    (9)

The first line uses ||T_P||<=1 and the cellwise diagonal difference (2). The two source hopping differences form a three-site chain whose norm is the Euclidean norm of its two edge coefficients, yielding sqrt3 lambda. For the final term subtract t_sel,1² G_eff,1 - t_sel,0² G_eff,0 in that order. After the fixed nominal source2 mass, t_sel,0²<=3jlambda(1+Theta3)²; (4) handles its squared relative change. This proves (9) without retuning masses, source normalization or packet.

If the nominal selected inverse is bounded H0/R, R=sqrt(delta²+lambda²), require the new finite gate

    theta_F=sup_delta H0 D(delta)/R<1.

Then

    ||F1^-1-F0^-1||<=H0² D(delta)/[(1-theta_F)R²].    (10)

The nominal source masses and seed factors must still be restored physically. Equation (10) is a selected source inverse comparison only; it has not yet reconstructed all erroneous mediator coordinates or wrong-window prepared columns.

## 6. The logarithm distinction and what is actually obtained

Keep J_m,q,gamma_l,g,h fixed with gap margins bounded away from zero, let lambda~r^(2m), rho=sqrt(a lambda) eventually, and restrict the error boxes to m ell<=c with fixed finite c. All constants suppressed in this paragraph may depend on these fixed suppliers, the prescribed c and strict inverse margins, but not on m or epsilon. In particular B_i,tau_i,1/k_i and port margins must have uniform bounds; these are explicit conditions, not a conclusion from the internal gap alone.

Then C_l,R_l,E_l=O(epsilon) uniformly in m, whereas H_l,H_l2=O(m epsilon), Q_l,Q_l2=O(m epsilon) at fixed gap: their exponential arguments remain bounded since m ell is bounded and m rho² tends to zero. The closed-return structure (6)--(8) gives

    D_eff(delta)=O(epsilon)[|delta|+|delta|³+(a0+b0|delta|)²],

with harmless higher powers on the bounded band absorbed into the constant. Thus (9) has a length-dependent hopping term lambda O(m epsilon), a length-independent slope term O(epsilon)|delta|, and controlled higher powers. Calibration-floor differences enter multiplied by lambda; they are not replaced by zero.

Integrating (10) uses

    int lambda/R² <= pi,
    int |delta|/R² =log(1+rho²/lambda²),
    int |delta|³/R² =rho²-lambda² log(1+rho²/lambda²),
    int delta²/R² <=2rho.

The logarithm is O(m) along this fixed family. Therefore the SELECTED source inverse L1 difference furnished by (9)--(10) is O(m epsilon), conditional on a uniform theta_F<1. The latter can be ensured by a sufficiently small bound on m ell, with its threshold depending on the fixed supplier/margin constants. This is a sufficient scaling statement, not a numerical tolerance or an arbitrary-m fixed-epsilon theorem.

The selected raw L2 structure from checked7b74 is compatible with the same scaling: a numerator alpha lambda+beta|delta| contributes proportional to alpha+beta after multiplication by kappa=O(sqrt(lambda)) and the rational integrals. Here alpha=O(m epsilon) and beta=O(epsilon). However a full perturbed raw proof must ALSO subtract actual t3, the ordered K_p action, complementary prepared columns and physical mass/recovery factors. Equation (9) alone is not that proof.

The earlier observation that an absolute local beta|delta| estimate creates a logarithm remains true, but a logarithm is not by itself an obstruction to O(m epsilon). A beta already O(m epsilon) would give a potential m² term; the length-independent slope estimate (1) avoids that particular loss. This is the precise refinement of594461, not a change to its proved coarse certificate.

Remaining load-bearing work is full nonuniform block-inverse reconstruction and all mediator recovery differences (with unequal endpoint injections), then physical source/core L1 and both incoming/outgoing L2 synthesis with one actual outside state. No all-apparatus O(m epsilon) conclusion is claimed here. The coarse complete interface594461 remains a separate sufficient fallback, not an independent proof of the sharper scaling. Independent diagonal errors, P-block shape errors, native supply, unknown scalar phase and arbitrary downstream changes remain outside scope.

## 7. Exposure and pins

This is source-exposed author work. Root identified the O(epsilon) versus O(m epsilon) slope distinction and suggested separating those coefficients; the inequalities above are newly derived rather than presumed. I authored594461 and the energy-resolved raw refinement, authored recovery ancestors and checked several loaded/complete interfaces. A distinct check is required.

Unchanged exact sources: mediator_coefficient_precision/PROPOSAL.md ec94570c294d760dadda17370fb8e65634880aa346709bc2d28fc6f3245f0084 (check2c6f4d9d); mediated_positive_bond_precision/PROPOSAL.md8cadb35ee3c41e02b984906030297c2e1a5d5daf5a576ef0e2dfb4531f3da616 (check65719cf1); loaded5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22 (checkf6303bb3); energy-resolved7b74e1850a59a4d809edf0a049aa1fb5e773ddb5fdfb88aea563b2ba6db6fa44 (checkbe74e1e896b508bcfa2e50d65ae2ff87663eefeecd785e3a5819fa87e821a1cc). These full arguments were read in the preceding coherent task and are reused within their qualified scope. The earlier proposal remains SHA594461345ee6546318179e1ef649dcbeac9ea64a1b8f5cd7907c40ee5c7640ac, provisional pending its own distinct check.

Only this proposal was written. No source changes, simulation, parameter sweep, numerical performance point, canonical/W/Git/PR/checkpoint/prompt/model changes or delegation occurred.
