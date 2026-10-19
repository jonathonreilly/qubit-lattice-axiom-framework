# Energy-resolved finite precision for the same mediated baseline

New author certificate requiring a distinct check. Keeping the polynomial numerator and physical forcing factors through the full L1/L2 integrals yields the explicit complete-certificate increment

    B_ret+max(0,o_box-o_nominal) < 5.3e6 epsilon.       (1)

This bound holds on the single baseline tuple for every error box0<epsilon<=1e-8 under the scalar-bond model and gates proved below. After deriving(1), choose the ONE conservative box epsilon=1e-13. Its increment is below5.3e-7, preserving the earlier infinite.00046 and finite.0005 ceilings. This is eleven orders larger than the preceding conservative1e-24 proposal, but remains a stringent supplied precision requirement. No optimality or practical implementation claim is made.

No program is run: the numerical work consists of the displayed analytical enclosing inequalities. The earlier cffe1f84 proposal is preserved unchanged and is not used as a checked premise. All bounds below are derived from the checked nonuniform formulas and the existing baseline enclosure.

## 1. Unchanged exact tuple and error model

Keep baseline243c1722/check080266c4 and earlierpoint4d0492b0/check450b226b. Thus J_m=.001,q=.0005,m=12,n1=n2=23,n3=12,g=5e-8,h=4e-6, the original calibrated.0027<j<.003, and the exact correlated nominal gamma_l prescription. Safe enclosing values are

    3e-18<lambda<3.1e-18, 3.93e-11<rho<4e-11,
    gamma_l<2e-5, Z2<1.001, sqrt(lambda)<2e-9.

Use positive P_w=w(I-X_xy), actual w=w0(1+e), |e|<=epsilon, with exact fixed2j new occupations and unchanged capped processor, receiver and product seed. The exact full-space identity H_P(w)=H(w)+C(w)I, C(w)=sum_newedges w, keeps all centered onsite coefficients fixed. The target remains exp(-itC(w)) times the prescribed NOMINAL normalized packet, with its original masses, lambda, physical phase,(-1)^12, old aging/W, record1 and every blank output. Actual correlated critical ratios need not remain exact.

Throughout the derivation assume only0<epsilon<=1e-8. This is a domain for the enclosing coefficients, not a claim that its largest box gives a useful final error. The single useful epsilon is selected in section6 after the full coefficient is bounded.

Use checked numerator dd9db7ee/check2ac75586 and complete reconstruction b06b088a/check8d6d4524. Their finite definitions of E_PP,E_PC,E_CP,E_CC,E_S,q0P,q0C,dqP,dqC,E_z,E_loc and B_ret are retained. All displayed ceilings below hold uniformly on BOTH physical windows/lips and every inherited record/parity sector, and tensor with arbitrary passive references.

## 2. All actual finite margins

For the entire enclosing domain epsilon<=1e-8,

    a_*=(1-epsilon)J_m-(1+epsilon)q>.00049,
    a_*-rho>.0004899999,
    b_*=.185-(1+epsilon)(J_m+q)>.18,
    d_A=2epsilon J_m=.002epsilon.

Actual endpoint magnitudes remain below2e-5 (the tighter baseline maximum is below1.85e-5). Hence endpoint squares<4e-10 and their sum<1.2e-9. With b0=46000/.0053+290/g<5.81e9 and a0=8e-18, e_rho<.24. The nominal and actual port/complement ceilings follow directly:

    nu<.002, tau_i<3e-9, sigma_i<3e-9,
    eta0_i<2e-8, eta_i<3e-8, r_i=1/(1-eta_i)<2,
    ||Gtilde_i||<400, cross-port e_i<.25,
    k_i>.18, G_*<400.                               (2)

Indeed nu*rho/j<3e-11, tau_i/.179<1.7e-8, and the remainder sigma_i e_rho<7.2e-10 gives eta_i<3e-8. The complementary source margin is greater than.185-1.2e-9/.18-(3e-9)^2*400>.18. Unequal actual endpoints use the larger endpoint bound and full cell compression. All installation Q-occupation inequalities would retain their original large slack as well, although positivity of the implemented P blocks needs no compensating occupations.

The unchanged nominal selected inverse coefficient H0=6/[s(1-zeta)] is below7 from the checked nominal s and zeta<.012344. The actual selected perturbation margin will be bounded explicitly below; it is not inherited from nominal zeta.

## 3. A polynomial numerator with numerical coefficients

Write x=|delta|. The exact inverse-power difference formulas in dd9db, using a_*>.00049 and rho²/a_*²<7e-15, give for each cell

    C_l<.02epsilon, R_l<2e5epsilon, E_l<7e-9epsilon.   (3)

For example C_l<=4e-10[3/(.00049)^2+.004/(.00049)^3]epsilon<.02epsilon. The cubic expression is bounded by replacing1/(1-rho²/a_*²) and its square by1.01, giving R_l<2e5epsilon. The closed difference is below4e-10[3/.18+.002/.18²]epsilon. None of these bounds has a length factor or a nonvanishing zero-error term.

Since ell=-log(1-epsilon)<=epsilon/(1-epsilon)<1.001epsilon and2n_l+1<=47, tau_l<48epsilon. The cofactor logarithmic coefficient B_l<1e9epsilon. Exponentiating using exp(y)<=1/(1-y) for0<=y<1 gives

    H_l<100epsilon, Q_l<2e9epsilon,
    H_l2<200epsilon, Q_l2<4e9epsilon,
    Theta_l<1e-10.                                  (4)

Here tau_l+B_l rho²<5e-7, so these deliberately loose ceilings hold on the WHOLE error domain. The nominal Theta bound uses n_l<=23 and rho²/a²<6.4e-15.

Keep the port selected variation as a polynomial:

    p_delta<epsilon(.02x+2e5x³), c_delta<7e-9epsilon.

Ordered port subtraction gives

    D_PP <=epsilon[3200x+3.2e10x³+4.375e-10],
    D_PC,D_CP<8e-7epsilon, D_CC<.002epsilon,
    D_K<3e-8epsilon,
    zCross_i<7.5e-10, D_Z,D_Y<2e-9epsilon.

The last two feedback products in D_eff have total below2e-17epsilon using k_i>.18. Consequently a convenient polynomial ceiling is

    D_eff<epsilon[5e-10+3300x+3.3e10x³].              (5)

This keeps the direct closed-source inverse difference and the selected return through both cross-port factors. No complementary channel is discarded.

Since G_E1<400+.25²*(3e-9)^2/.18<401 and3j<.009, substituting(3)--(5) into dd9db's exact selected numerator gives

    D(delta) <= epsilon P(x),
    P(x)=1000lambda+.061x+2e10lambda*x²+7e5x³.        (6)

For verification, the two source-hop constant coefficient is below174lambda, the third-hop constant below724lambda; their sum fits1000lambda. The source and third-hop quadratic coefficients sum below2e10lambda. The diagonal slope is below.06 and the port's additional slope is below30lambda, fitting.061. The cubic diagonal coefficient is below6e5, and the extra port cubic is less than3e8lambda, fitting7e5. The tiny constant in(5) is also covered by the slack in1000lambda. All comparisons use the FIXED nominal mass congruence and packet.

With R=sqrt(delta²+lambda²),

    theta_F<=7epsilon[1000+.061+2e10lambda*rho+7e5rho²]
            <7100epsilon<=7.1e-5<.001.              (7)

This proves the missing actual selected inverse gate over the entire domain. Complete real matching plus these nonzero finite Schur margins is the checked route to actual spectral identification; a kernel envelope alone is not used to exclude singular seed mass.

## 4. Source/forcing envelopes without replacing R by lambda

Define the energy-dependent selected difference ceiling

    F(delta)=50epsilon P(|delta|)/R².                (8)

Indeed H0²/(1-theta_F)<49/.999<50. We may use f0<=7/R,f1<=8/R. The physical third-hop quantities in completeb06 obey

    u0<.1sqrt(lambda), u1<.11sqrt(lambda),
    du<11sqrt(lambda)epsilon,
    p0<.2sqrt(lambda), p1<.22sqrt(lambda),
    dp<22sqrt(lambda)epsilon.                       (9)

The p_i explicitly pay sqrt(Z2)<2; mass factors are not removed from the actual forcing.

The full ordered cross-block formulas give

    x_i<1e-10sqrt(lambda), v_i<6e-10sqrt(lambda),
    dx,dy<9e-9sqrt(lambda)epsilon,
    dJ<1e-6epsilon,
    dV,dW<6e-8sqrt(lambda)epsilon.

For example the leading dx term is du*e1*tau1<8.25e-9sqrt(lambda)epsilon; its two remaining terms fit the stated slack. Restoring all four inverse blocks therefore permits

    E_PP=F,
    E_PC,E_CP<=6e-10sqrt(lambda)F
                            +4.2e-7sqrt(lambda)epsilon/R,
    E_CC<=1e-6epsilon+3.6e-19lambda F
                            +5.04e-16lambda epsilon/R,
    E_S<=2F+1e-6sqrt(lambda)epsilon/R+1e-6epsilon,
    S0<=8/R+6.                                      (10)

The direct dJ in E_CC is retained, and (10) bounds the actual bare-seed columns, including wrong-window inputs, after contractive physical congruence restoration.

For the NOMINAL pre-port forcing,

    q0P<=2sqrt(lambda)/R,
    q0C<=2e-8+1e-9lambda/R.

For its actual difference, direct substitution of(9)--(10) gives

    dqP<=.23sqrt(lambda)F+155sqrt(lambda)epsilon/R,
    dqC<=2e-10lambda F+1e-6lambda epsilon/R+5e-8epsilon.

In particular q0C contains the real direct tau0/k0 term; it has not been assigned a spurious sqrt(lambda) factor. The exact port inverse difference has dKp<=r1r0*max(p_delta,c_delta)*G_*<2e-5epsilon. Thus the full physical forcing difference and nominal forcing have safe envelopes

    E_z<=sqrt(lambda)F+400sqrt(lambda)epsilon/R+1e-6epsilon,
    z0<=6sqrt(lambda)/R+4e-8.                        (11)

These follow from zP=r1*dqP+dKp*q0P and zC=r1*dqC+dKp*q0C BEFORE adding the two prepared-input types. The order is Kp t3 psi2, not a scalar-density approximation. Both lips are bounded separately.

## 5. Integrating every local and traveling output

The following elementary bounds suffice; no quadrature is used:

    integral R^-2<=pi/lambda, pi<4,
    integral |delta|/R²=log(1+rho²/lambda²)<36,
    integral R^-1=2asinh(rho/lambda)<36,
    integral delta²/R²<=2rho,
    integral |delta|³/R²<=rho².

For the logarithms, rho/lambda<1.334e7; exp(18)>20^6=64000000 and exp(36)>20^12 bound the corresponding positive arguments. The inequality exp(3)>20 follows from its positive Taylor sum. Applying these bounds to(8) gives

    ||F||_L1<2.1e5epsilon.                           (12)

Its leading term is50*1000*pi*epsilon<200000epsilon; the slope contributes less than50*.061*36epsilon. The other two positive terms are negligible within the explicit slack.

For L2 retain the exact rational ceilings

    I0<=pi/(2lambda³), I1<=pi/(2lambda),
    I2<=2rho, I3<=2rho³/3.

Minkowski applied to(8) yields

    sqrt(lambda)||F||_2
      <=50epsilon[1000lambda sqrt(lambda I0)
          +.061sqrt(lambda I1)
          +2e10lambda sqrt(lambda I2)+7e5sqrt(lambda I3)]
       <8e4epsilon.                                 (13)

The first two bracket terms are below1500 and.0915 using sqrt(pi/2)<1.5. The last two are each below1 on the stated bounds, with very large slack, so the total is below80000 after multiplication by50. Finite rho is essential for I2,I3; no divergent full-line moment is used.

Equations(10)--(13), sqrt(lambda)<2e-9 and sqrt(2rho)<9e-6 then give

    ||E_S||_1<4.3e5epsilon,
    ||E_z||_1<5e-4epsilon,
    ||E_z||_2<8.1e4epsilon,
    ||S0||_1<289, ||z0||_1<5e-7.                    (14)

For example the two main L1 forcing contributions are below(2e-9)*(2.1e5)epsilon and400*(2e-9)*36epsilon, totaling.0004488epsilon. Its L2 terms are below80000epsilon+400sqrt(pi)epsilon+1e-6sqrt(2rho)epsilon<81000epsilon.

Each exact full mediator recovery map has M_l1<.05 and difference dM_l<.3epsilon, from d_l>.0004899999 and epsilon gamma_l/d_l+gamma_l*d_A/d_l². Consequently the complete physical nontraveling envelope satisfies

    ||E_loc||_1
      <=1.15||E_S||_1+(14000+60)||E_z||_1
                            +.9epsilon(||S0||_1+400||z0||_1)
       <5e5epsilon.

This includes every source and internal mediator head, all235 finite background heads and all closed slow tails, with the port counted once as output. Hence the two-window/two-lip Stone integral is

    B_local=(2/pi)||E_loc||_1<3.4e5epsilon.

The full physical row/flux conversion, two windows and BOTH propagation directions give

    B_travel=4*461sqrt(j/pi)||E_z||_2
                    <60*(8.1e4)epsilon=4.86e6epsilon.

The incoming column uses fixed real conjugation at the same positive physical time, not entrywise imaginary part or time reversal. Halfline restriction is contractive. Thus

    B_ret<5.2e6epsilon.                              (15)

For the ONE actual outside state use anchored c_min=c10-.02epsilon, c_max=c10+.02epsilon and the exact first-cell product bound. The nominal slope c10>=gamma1²/J_m²=7.5e-9 implies c_min>7e-9 throughout epsilon<=1e-8. The preparation function sqrt(2[1-1/sqrt(1+c)]) has derivative at most1/(2sqrt(c)), hence below12000 on this interval. Its increment is below240epsilon. The residual has sqrt(2)|t10|/rho<3e-7, relative product increment<100epsilon, and inverse-square-root increment<=.01epsilon. A safe total witness increment is therefore<1000epsilon. The min with1 preserves this upper difference. The baseline's sqrt(u) ceiling bounds the nominal witness's preparation term only. Its full outside allowance also includes the unchanged witnessed residual term and therefore bounds the full nominal witness. Replacing that full allowance by the anchored actual witness bound increases it by at most1000epsilon and requires no second nominal outside charge.

Combining this witness estimate with(15) proves(1). All terms vanish as epsilon tends to zero except the original nominal allowances. No difference of full unitaries on outside eigenvectors is asserted.

## 6. One larger explicit box and complete consequence

Only AFTER the finite coefficient(1), select

    epsilon=1e-13.                                  (16)

It is inside the proved epsilon<=1e-8 domain and has theta_F<7.1e-10. Its complete increment is below5.3e-7. This deliberately leaves slack rather than choosing the largest admissible error. No other error-box point was tested or selected.

The checked earlier nominal infinite ceiling is.00045445500576 for every t>=8e18. Thus, for every actual tuple in(16),

    error_actual,infinite(t)<.00045498500576<.00046.

At T1=1.6e19 the unchanged g-only cut with M=1920000000011 adds at most.00004. Its weight is zero on all erroneous source bonds and finite/infinite implementations have the SAME actual C(w). Therefore

    error_actual,finite(t)<.00049498500576<.0005
                                  on[8e18,1.6e19].

The target is the same nominal normalized infinite packet multiplied by exp(-itC(w)); all old aging, record and blank outputs and arbitrary references remain. Counts are unchanged:1920000000365 head qubits,1920000000370 apparatus qubits,1920000000366 head edges and at most3840000000536 listed positive blocks. The P graph has the same net count as the compensated Q realization, but different incident norm sums; no new norm-budget advantage is claimed. Single-read failure effect<=2.5e-7 I and unhalved channel ceiling.001 follow conservatively.

If only nominal C(w0) is known, its phase discrepancy2|sin(t[C(w)-C(w0)]/2)| is a separate vector error and is NOT bounded here by(1). Complete-channel comparison ignores the global scalar. Exact fixed2j occupations, scalar P-block shape, unchanged processor, physical identifications and initialization remain supplied. For the smallest endpoint gamma1~8.66e-8, relative1e-13 means absolute precision of order1e-20; no practical/native supply conclusion follows. Arbitrary onsite or downstream errors, repeated monitoring, capture/reset and finite permanent storage are not covered.

## 7. Evidence and limits

Primary checked interfaces: numerator dd9db7ee72ad2c3a779a193b68629bba402444fb3dbae529d54235e6a21b6b0c/check2ac7558630ede8e5f2a21c07781d1310587f49646a3ba86784b49c271b980f40; complete b06b088a789ad3230f32c8d4c30dab804b97f82af05b0d0c00f011111e868570/check8d6d452445b2e7e69be4294a57cc52e3189e22c30166594281bf7d1f3a36dd7e. The exact baseline and earlierpoint sources/checks are the same243c1722/080266c4 and4d0492b0/450b226b used in the previous coherent task. Positive identity8cad/65719 and cut/layout5bcb/d776/0c089 retain their original scope. Full identities and inherited matching restrictions are preserved in these exact primary sources; they are not recertified by numerical smallness here.

I authored the nonuniform sources and the prior coarse finite-box proposal. Root suggested retaining the energy-dependent denominator through the integrals; that was a proposed route, not a promised improvement. This new analytical finite evaluation needs a distinct check. Prior cffe1f8422d7e920721419a2d2109f86051f349119eee284e1681da08f76686c is not edited or promoted to an independently checked premise. The new proof re-establishes every used numerical ceiling from checked formulas.

Only this proposal was written. No scientific program, numerical integration, solver, dynamics, parameter sweep, rerun, W/Git/PR/checkpoint/prompt/axiom/model change or delegation occurred. No calculation receipt is claimed. All proof arithmetic and conservative substitutions are displayed, not hidden behind a floating-point PASS result.
