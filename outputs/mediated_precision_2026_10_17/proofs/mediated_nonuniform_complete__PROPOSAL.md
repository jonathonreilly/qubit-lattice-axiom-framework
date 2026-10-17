# Complete nonuniform mediator-bond reconstruction

Status: new conditional author theorem requiring a distinct check. This supplies explicit finite error expressions for every source/mediator head, the unchanged finite background and closed slow tails, and both traveling terms. Under stated fixed-supplier uniform margins, their sum is O(m epsilon). The reference remains the prescribed nominal critical packet; the actual scalar phase is explicit. No numerical tolerance, operating point, native supplier or finite permanent-halt claim is made.

## 1. Exact domain and notation

Use the error model and fixed nominal congruence of checked `mediated_nonuniform_numerator/PROPOSAL.md` dd9db7ee72ad2c3a779a193b68629bba402444fb3dbae529d54235e6a21b6b0c, review2ac7558630ede8e5f2a21c07781d1310587f49646a3ba86784b49c271b980f40. This review was read fully. Only positive scalar path-bond errors |w/w0-1|<=epsilon<1 are allowed; exact new2j occupations, unchanged capped background, all internal operators, physical geometry and product seed are retained. Center H_P(w) by its actual C(w)=sum_newedges w_e. Write centered operators H_i, i=0 nominal, i=1 actual. Both use the same physical windows c_att+2j+b+[-rho,rho], b=1,3, and the same nominal lambda, Z0,Z1,Z2 and sign gauge.

All finite gates of dd9db apply, including positive actual internal/closed gaps, rho<a_*, port margins eta_i<1, complementary margins k_i>0 and the selected perturbation margin theta_F<1. Retain complete analytic background matching and actual spectral identification as in the checked regularity source. The finite nonuniform Schur matrices and their nonzero margins give the same fixed-m continuation/Stone identification; real-axis norm envelopes alone are not substituted for that premise.

Below every scalar ceiling is a nonnegative function of |delta| on [-rho,rho], uniform on both lips, both physical windows and inherited record/parity sectors. All identities act on full internal fibers and extend to arbitrary passive references. No complementary input or output is identified with zero. Let R=sqrt(delta²+lambda²). Reuse from dd9db its explicit D(delta), D_PC,D_CP,D_K, E_3, H_3,Q_3, Theta3, B_i,e_i,tau_i and k_i. Here e_i is the cross-port kernel ceiling, not coefficient epsilon. Define

    f0=H0/R, f1=H0/[(1-theta_F)R],
    E_F=H0² D/[(1-theta_F)R²], c_i=1/k_i,
    u0=kappa(1+Theta3), kappa=sqrt(3jlambda),
    du=u0(H_3+Q_3 delta²), u1=u0+du,
    p_i=sqrt(Z2)u_i, dp=sqrt(Z2)du.                 (1)

The u_i bound the selected third hopping AFTER the fixed nominal source2 mass; p_i bound the physical hopping. Nominal and actual physical hoppings have the same sign. No actual mass factor is canceled by changing the target. Bounds, rather than exact scalar hopping values, are used throughout (1).

## 2. Full three-source inverse differences

In the fixed nominal mass congruence write the full source matrix as

    S_hat_i=[[A_i,X_i],[Y_i,K_i]],
    F_i=A_i-X_i K_i^-1 Y_i.

The labels K_i here denote complementary source matrices, not old logical K. On a single lip X_i and Y_i are not replaced by adjoints. Their only origin is the last-source term -t3 Gtilde_i t3. Therefore put

    x_i=u_i e_i tau_i,
    dx=du e1 tau1+u0 D_PC tau1+u0 e0 E_3,
    dy=du tau1 e1+u0 tau1 D_CP+u0 E_3 e0,
    v_i=x_i/k_i,
    dJ=D_K/(k1 k0),
    dV=dx/k1+x0 dJ,
    dW=dy/k1+x0 dJ.                                (2)

These bound ||X_i||,||Y_i|| by x_i, their differences by dx,dy, and the differences of V_i=X_i K_i^-1 and W_i=K_i^-1 Y_i by dV,dW. Equations (2) follow by subtraction of each ordered product. In particular D_PC and D_CP keep their distinct lip order and closed-channel factors.

The exact full inverse is

    S_hat_i^-1=[[F_i^-1, -F_i^-1 V_i],
               [-W_i F_i^-1, K_i^-1+W_i F_i^-1 V_i]].

Subtracting, without moving factors, gives the four block bounds

    E_PP=E_F,
    E_PC=E_F v1+f0 dV,
    E_CP=v1 E_F+dW f0,
    E_CC=dJ+v1² E_F+f0(dW v1+v0 dV).                (3)

For example the last line subtracts W1 F1^-1 V1-W0 F0^-1 V0 as W1(F1^-1-F0^-1)V1+(W1-W0)F0^-1 V1+W0 F0^-1(V1-V0). The direct dJ term is essential. Nominal block bounds are f0,f0 v0,f0 v0,c0+v0²f0.

Restoring the SAME physical U T on both sides is contractive because ||T||<=1. Right multiplication by the actual product-seed embedding is also contractive. Thus a full prepared-source difference and nominal-column bound are

    E_S=E_PP+E_PC+E_CP+E_CC,
    S0=f0(1+v0)²+c0.                               (4)

No physical seed or mass factor is set equal to one; dropping factors bounded by one is a conservative norm bound. The target still uses the original nominal masses and bare preparation. Equation (4) covers all three source endpoints and every prepared input on either window, including the wrong-window column.

## 3. Actual ordered port forcing and both kinds of input

The exact eliminated-background forcing is

    z_i=Kp_i t3_i(D) psi_i,2,
    Kp_i=(I-s_p,i(D)G)^-1, s_p,i=s_3R,i(D).          (5)

It is the actual background forcing, not just the source2 amplitude. Keep the physical sign convention of the checked raw/recovery sources; the same fixed gauge is used for both tuples. Let

    r_i=1/(1-eta_i), G_*=1/j+a0+b0 rho,
    ds=max(C_3|delta|+R_3|delta|³,E_3),
    dKp=r1 r0 ds G_*.

The ordered identity Kp1-Kp0=Kp1(s_p,1-s_p,0)G Kp0 proves dKp. We do not need a small full ds on the selected sector to obtain the scaling below, because the resonant forcing already carries sqrt(lambda).

For selected prepared input, bound the nominal pre-port forcing and its difference by

    q0P=f0(p0+tau0 v0),
    dqP=p1 E_PP+tau1 E_CP+dp f0+E_3 v0 f0.

For complementary prepared input on the other window, use

    q0C=p0 f0 v0+tau0(c0+v0²f0),
    dqC=p1 E_PC+tau1 E_CC+dp f0 v0
                                  +E_3(c0+v0²f0).   (6)

These inequalities split actual source2 OUTPUT into P and C before applying t3. In particular the direct tau0 c0 and E_3 c0 terms are retained. They are not assigned a spurious resonant sqrt(lambda) factor. Set

    zP=r1 dqP+dKp q0P,
    zC=r1 dqC+dKp q0C,
    E_z=zP+zC, z0=r0(q0P+q0C).                     (7)

Then E_z bounds the full prepared-input forcing difference and z0 bounds nominal forcing. This triangle over P/C inputs is deliberately conservative; it requires no claim of orthogonal physical outputs. The unchanged actual port column is G z, so its difference is at most G_* E_z and its nominal norm at most G_* z0.

## 4. Every mediator head and the full nontraveling background

For cell l, with actual endpoint injection Gamma_li and adjacency A_li, the physical internal recovery map is

    M_li(D)=-(D tensor I+A_li)^-1 C_end Gamma_li.

It maps the JOINT two-endpoint vector to every internal cell head. Let d_l=min(a_*-rho,b_*)>0, with the corresponding cellwise gaps if different. Valid finite ceilings are

    M_l1=(1+epsilon)gamma_l/d_l,
    dM_l=epsilon gamma_l/d_l+gamma_l d_A/d_l².        (8)

The difference formula R1 Gamma1-R0 Gamma0=R1(Delta Gamma)+(R1-R0)Gamma0 and the resolvent identity prove (8). No growing closed power is separately bounded: it is already in the exact gapped inverse on the full fixed physical cell. The operator norm does not acquire sqrt(n_l) merely because the output has many heads. This uses the spectral gap, not a sum of individual entry ceilings.

Each cell's two endpoints are a subset of the three source endpoints plus p. A safe joint-endpoint ceiling is source norm plus port norm. Thus a per-energy majorant for all new source/mediator heads and the unchanged finite-background/closed-tail outputs is

    E_loc=E_S+14000 E_z
       +sum_l {M_l1(E_S+G_* E_z)
                          +dM_l(S0+G_* z0)}.         (9)

The checked L0=14000 map includes every background finite head and every closed slow tail for full port forcing; it excludes propagating rays. The port already belongs to that output. Its appearance inside mediator recovery in (9) is a source for a distinct physical output, not a second counted port output. Summing cell norms is conservative even though their mediator outputs are disjoint.

Both lips and both windows therefore give the retained nontraveling difference, uniformly for all real t,

    B_local=(2/pi) int_(-rho)^rho E_loc(delta) ddelta. (10)

The constants 2/pi retain the two-lip Stone normalization and triangle across two windows. No rectangular jump is replaced by entrywise imaginary part. Closed/open window decompositions are embedded in the same physical space before summation.

## 5. Both traveling terms and the complete bound

The physical unchanged background row has full-forcing ceiling461 before connector flux conversion. The exact checked Jacobian/flux identity gives the one-window outgoing coefficient estimate

    ||Delta F||_L2(k)<=461 sqrt(j/pi)||Delta z||_L2(delta).

It retains the physical transmission coefficient and slow momentum; there is no missing inverse slow velocity. Two windows by triangle, and outgoing PLUS incoming, give

    B_travel=4*461 sqrt(j/pi)
                           [int_(-rho)^rho E_z(delta)² ddelta]^(1/2),
    B_complete,ret=B_local+B_travel.                (11)

The incoming statement uses real assembled matching and the actual lower/upper rectangular columns, with fixed conjugation at the SAME positive physical time. It does not identify the old multiplier W-star with W. We compare actual and nominal physical coefficients before invoking the nominal W/W-star target interface. Halfline restriction is contractive. No normalization of an erroneous packet is performed.

Equations (1)--(11) are one named finite coefficient expression, built entirely from the checked numerator and finite inverse margins. They are usable without an asymptotic slogan or a time-dependent perturbation norm. They imply

    ||e^(-itH1)E_1(I)V-e^(-itH0)E_0(I)V||
                                  <=B_complete,ret   (12)

for all real t and arbitrary passive references.

Use the actual nonuniform product-witness bound o(w) or its error-box ceiling o_box in594461 equations(11)--(12), with exact unequal first-cell slope and zero-energy product. This includes ALL outside spectral types. Let b0(t) be the nominal retained-window-to-fixed-normalized-target allowance from complete6ed86, with nominal eps_out removed. Then

    ||e^(-itH_P(w))V-e^(-itC(w))T0(t)||
                        <=o_box+B_complete,ret+b0(t). (13)

Only ONE actual omitted vector is added. The target T0 has its prescribed nominal critical denominator, packet phase61.5q+.5k+172k_old, fixed (-1)^m, c_att+2j carrier, old aging exp(-itK)W, record1 and every prescribed blank register. It is common to all old/reference inputs. The actual scalar C(w), not a fitted phase, multiplies the entire target. At epsilon=0, B_complete,ret=0 and the witness ceiling returns the nominal one. Thus (13) perturbs the nominal complete certificate rather than silently changing its waveform.

Equation (13) applies wherever that nominal normalization/time certificate applies. If it is bounded after a nominal onset T0, the additive tolerance is uniform for every t>=T0 on the infinite receiver. It is not an early-time relative-error guarantee. A separate unchanged output-ray cut may transfer a finite horizon with the same actual scalar on both sides; no finite window, receiver size or error threshold is selected here.

## 6. Conditional O(m epsilon) family theorem

Fix the supplied nominal J_m,q,gamma_l, g,h and calibrated processor. Let lambda_m=Lambda r^(2m-2), rho_m=sqrt(a lambda_m) once it lies inside the certified band. Take error boxes with m[-log(1-epsilon)]<=c for some fixed finite c, and impose UNIFORM positive actual gaps and port/complement/selected inverse margins as in section1. In particular H0,1/(1-theta_F),1/k_i,1/(1-eta_i) and the cell recovery bounds must remain bounded independently of m. These are explicit conditions; an internal gap alone is insufficient. Select c small enough for the selected inverse gate if required by the checked numerator. Constants below may depend on the fixed suppliers, c and these margins.

The checked numerator yields, uniformly on the shrinking band,

    D(delta)<=C[lambda m epsilon+epsilon|delta|
                      +epsilon|delta|³+lambda m epsilon delta²
                      +lambda epsilon(a0+b0|delta|)²].            (14)

Here and only in this scaling section C denotes a finite supplier-dependent constant, unrelated to the physical scalar C(w). Polynomial higher powers bounded on the fixed band may be absorbed. The exact finite expression to use for certification remains dd9db equation(9).

The ordered cross estimates imply

    v_i=O(sqrt(lambda)), dV,dW=O(sqrt(lambda)m epsilon),
    dJ=O(epsilon), dp=O(sqrt(lambda)m epsilon), dKp=O(epsilon).

Consequently (3)--(7) give safe scaling envelopes

    E_S=O(E_F)+O(sqrt(lambda)m epsilon/R)+O(epsilon),
    E_z=O(sqrt(lambda)E_F)
                            +O(sqrt(lambda)m epsilon/R)+O(epsilon),
    S0=O(1/R)+O(1), z0=O(sqrt(lambda)/R)+O(1).        (15)

All direct complementary terms survive in O(epsilon) or O(1); these symbols do not declare their jumps zero. Since the interval and suppliers are fixed in this asymptotic family, lambda is bounded above and the omitted smaller lambda terms can be absorbed.

From (14), int E_F=O(m epsilon): the lambda m epsilon term uses int R^-2<=pi/lambda, and epsilon|delta| uses log(1+rho²/lambda²)=O(m). Also

    sqrt(lambda)||E_F||_2=O(m epsilon),
    int R^-1=2asinh(rho/lambda)=O(m),
    ||R^-1||_2<=sqrt(pi/lambda).

The first L2 assertion follows termwise from the exact rational integrals of checked7b74, retaining the finite rho bound for cubic terms. No scalar spectral density is substituted for a physical column. The potentially extra factor m in sqrt(lambda)m epsilon int R^-1 is harmless because sup_m m sqrt(lambda_m)<infinity for the fixed geometric family. Therefore (15) yields int E_S=O(m epsilon), int E_z=O(m epsilon), and ||E_z||_2=O(m epsilon).

Finally dM_l=O(epsilon), while int S0=O(m) and int z0=O(sqrt(lambda)m+rho). Equations(9)--(11) prove

    B_complete,ret=O(m epsilon).                    (16)

This completes the all-head and both-ray scaling that the selected numerator alone did not prove. It does not rely on a multiple-pole perturbation assertion.

For the witness increment, the first-cell slope sums are uniformly Lipschitz at fixed gap and their nominal value is bounded below by gamma1²/J_m²>0. Their square-root preparation term therefore changes by O(epsilon). The exact hopping product contributes at most O(m epsilon)|t_10|/rho=O(m epsilon sqrt(lambda)). Thus max(0,o_box-o_nominal)=O(m epsilon). Combining with (13), the complete NOMINAL certificate increases by at most O(m epsilon), uniformly in time on its certified domain. This is not a statement that the full actual and nominal unitary evolutions differ by O(m epsilon) on outside eigenvectors: those are paid by the single actual witness allowance.

No uniform bound is asserted for fixed nonzero epsilon and unbounded m, for closing gaps, varying g without new margins, unknown C(w), arbitrary onsite/block-shape error or an independently changed processor. No numerical value of the supplier-dependent coefficient is certified. For any finite tuple, the named expressions(1)--(13), rather than asymptotic notation, are the proposed evaluation interface.

## 7. Sources and exposure

Primary new checked input: dd9db7ee72ad2c3a779a193b68629bba402444fb3dbae529d54235e6a21b6b0c, distinct ROOT review2ac7558630ede8e5f2a21c07781d1310587f49646a3ba86784b49c271b980f40. The full new review was read and its limits retained. The exact nonuniform recovery identity was reconstructed above, not inferred from a stationary product law.

Unchanged scoped premises previously read fully in this coherent lane: positive implementation8cadb35e/check65719cf1; stationary precisionec94570c/check2c6f4d9d; loaded5f909e1e/checkf6303bb3; recovery83530c67/check6f1b0755; actual regularityf8153ddb/check9d837417; raw26392923/check111aaeff; energy-resolved7b74e1850a59a4d809edf0a049aa1fb5e773ddb5fdfb88aea563b2ba6db6fa44/checkbe74e1e896b508bcfa2e50d65ae2ff87663eefeecd785e3a5819fa87e821a1cc; source73116231/check496164c0; complete6ed86c33b624ffc8f672e0f2380194fb624c9678b6f477ccab6f5cb59eef57f7/checke9d6b346. Full identities are recorded in dd9db and594461; the latter's coarse full-Schur result is not used to infer (16). Its witness and nominal-target bookkeeping are rederived in section5.

I authored the selected numerator, energy-resolved refinement and several recovery/geometry ancestors, and checked loaded/complete interfaces after shared exposure. ROOT suggested the possible full reconstruction scaling; it was a route to test, not evidence. This is new author work, not a distinct review, and needs its own independent check before use. No earlier artifact was changed. No parameter sweep, numerical integration/dynamics, operating point, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Native block/diagonal supply, physical preparation and Record identification remain supplied premises.
