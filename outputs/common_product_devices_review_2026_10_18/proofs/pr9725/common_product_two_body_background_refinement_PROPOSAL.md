# A quadratic background allowance for the scaled two-body router

New source-exposed author derivation requiring a distinct check. A two-variable normalized effective operator improves the sufficient simulation bound when the ENTIRE scaled background norm is small compared with the ancillary penalty. All mixed terms are bounded, not discarded or assumed scalar. Paying the actual finite volume gives a sufficient physical horizon of order Lambda^-1 epsilon^-21 log^5(e/epsilon), instead of the preceding explicit family's epsilon^-27 log^5 order. This is a different sufficient scale prescription in the same enlarged interaction class, not a lower bound, optimality claim or practical-cost assertion.

## 1. Fixed device structure and the global norm that must be paid

Retain the complete reference family970a at accuracy0<tau<=1, with Lambda>0. Retain exactly c1cb's positive residual background Bbar, including mubar=Lambda/4 on every original head, the one record bias and both source/cap systems. Retain all twelve ancillary squares, their six shared data qubits, couplers, geometry and supplied cat+ states. Write K=48 and

    Delta=Lambda/4, nu=Delta alpha,
    scale=10Delta alpha^4/jbar,
    Hact=48nu I+H0+V+B, B=scale Bbar,
    Hbar_new=Bbar-(jbar/4) sum_l Omega_l,
    U=jbar Tbar=7ell/8, T=Tbar/scale=U/(10Delta alpha^4).

Thus B is ancilla-independent but generally does NOT commute with the data Paulis or their products. The exact target generator is

    Htar=scale Hbar_new+(48nu+s_joint)I,
    s_joint=-24nu^2/Delta+27nu^4/Delta^3.                (1)

The isolated joint calculation gives g=(5/2)Delta alpha^4=scale*jbar/4. It includes the mixed fourth-order scalar27; using twelve isolated scalars would still be wrong.

There are293+8ell listed positive blocks in Bbar: the389+8ell physical block count in c1cb minus96 ancillary gadget blocks. Each has full norm below Lambda by the checked original background incident bounds. Consequently the explicit, deliberately coarse ceiling

    ||Bbar||<=Bmax:=Lambda(293+8ell),
    ||B||<=beta:=scale Bmax                             (2)

is valid on ALL data/head occupation sectors and old-program fibers. It includes the uniform penalty's extensive norm, all scalar vacancies and source compensations. This argument does not replace the global norm by a one-head norm, local commutator, or unknown cancellation. The finite size is essential to this new analytic method. Bmax is a prescribed upper bound, not an assertion that it equals the actual norm.

## 2. Two-variable analytic low operator

Work within the reducing common ancillary X_all=+ sector, as licensed by the nominal cat input. Let J append cat+^12, P=JJ*, and define

    H(x,y)=H0+xV+yB.

Here x,y are COMPLEX analytic parameters; no physical time-dependent controls are introduced. H0 has zero space P and complementary spectrum at least2Delta. The data/rest multiplicity can be arbitrary. Since ||V||<=KDelta alpha, consider the closed bidisc

    |x|<=R_x=1/(16Kalpha),
    |y|<=R_y=Delta/(16beta).                            (3)

Each perturbation has norm at mostDelta/16 there. On the contour |z|=Delta/2, the unperturbed resolvent has norm<=2/Delta, the total Neumann ratio is<=1/4, and the perturbed resolvent has norm<=8/(3Delta). The resolvent identity and contour integration yield

    ||Pi(x,y)-P||<=1/3,
    ||H(x,y)Pi(x,y)||<=2Delta/3.                        (4)

The estimates hold in a neighborhood of the bidisc too, by the strict resolvent margin. They require no commutation of V's data factors with B.

Define the analytic inverse-square-root series and effective operator by

    C(x,y)=[J*Pi(x,y)J]^(-1/2),
    E(x,y)=C(x,y) J*H(x,y)Pi(x,y)J C(x,y).              (5)

All adjoints in (5) are of the FIXED injection J, not parameter-dependent adjoints. Thus (5) is jointly analytic even for complex parameters. The series about identity is valid by (4), ||C||^2<=3/2, and

    ||E(x,y)||<=Delta.                                 (6)

At real x,y, Pi is orthogonal and commutes with H. Therefore W=Pi J C is an isometry, E=W*H W, and H W=W E. This is the full degenerate normalized effective operator, not a single eigenvalue or scalar-column reduction.

Two exact structural facts control the coefficients. First, B acts only on data/rest, commutes with H0 and P, and BJ=JB. At x=0 the low eigenvalues of yB have modulus<=Delta/16 while all complementary H0+yB eigenvalues remain outside the contour. Consequently Pi(0,y)=P and

    E(0,y)=yB.                                        (7)

On the right of (7), B denotes its identical operator on the data/rest domain of J. This equality is exact throughout the y disc; no B^2 term survives on that axis.

Second, the product Z over all48 ancillas commutes with H0 and B, preserves every plus sector, fixes J pointwise and sends V to -V. Equations(4)--(5) consequently imply

    E(-x,y)=E(x,y).                                    (8)

This parity statement is valid with the noncommuting background. It eliminates every odd power of V, including putative first-order V B terms. It does NOT eliminate even mixed terms such as V^2 B, which need not be scalar or commute with B.

## 3. Uniform mixed remainder, with every term retained

Write E(x,y)=sum_(n,m>=0) E_nm x^n y^m. Banach-valued Cauchy estimates from (3),(6) give

    ||E_nm||<=Delta R_x^-n R_y^-m.

Let a=16Kalpha and b=16beta/Delta. Impose a<=1/2 and b<=1/2, so both analytic radii exceed or equal2. Equations(7)--(8) and absolute convergence give the exact identity

    E(1,1)-E(1,0)-B
       =sum_(n even>=2,m>=1) E_nm.

Thus

    ||E(1,1)-E(1,0)-B||
       <=Delta a^2 b/[(1-a^2)(1-b)]
       <=(8/3)Delta a^2 b
       <=Cmix alpha^2 beta,
    Cmix=16384 K^2.                                    (9)

Indeed the unrounded numerical coefficient is(8/3)*256*16=32768/3, less than16384. The bound includes ALL orders in B and all even orders>=2 in V; it neither truncates at V^2B nor presumes its coefficient. No reference/data dimension enters Cauchy's operator norm bound. The global volume dependence appears explicitly through beta.

On the y=0 axis, the checked b54c joint coefficient and even remainder apply unchanged:

    E(1,0)=s_joint I-g sum_l Omega_l+D6,
    ||D6||<=R6:=Delta(8Kalpha)^6/[1-(8Kalpha)^2].        (10)

Combining (9)--(10) yields

    ||E(1,1)-[B+s_joint I-g sum_l Omega_l]||
       <=R6+Cmix alpha^2 beta.                         (11)

This is a normalized operator comparison on the whole original Hilbert space, including multiple heads and arbitrary P/R fibers. Higher scalar shifts, nonscalar renormalizations and altered intermediate virtual denominators are all paid by (11). There is no fitted phase or assertion that the background commutes with the desired interaction.

## 4. Literal-state endpoint and all-output evolution

The sufficient conditions alpha<=1/(32K) and beta<=Delta/32 imply ||V||<=Delta/32. Compare the real projection Pi(1,1) directly with Pi(0,1)=P, rather than using a projection error proportional to ||B||. On |z|=Delta/2,

    ||(z-H0-B)^(-1)||<=32/(15Delta),
    ||(z-H0-B-V)^(-1)||<=16/(7Delta).

Resolvent subtraction therefore gives

    deltaPi:=||Pi(1,1)-P||
       <=(256/105)Kalpha<3Kalpha<=3/32<1/7.

For the real normalized W=Pi J C, the elementary inverse-square-root estimate gives ||W-J||<=2deltaPi<6Kalpha. The full operator H0+V+B has this W as an exact invariant low isometry in the common plus sector. Apply self-adjoint Duhamel between E(1,1) and the target inside W, then pay J/W at both literal endpoints. Restoring48nu gives, conservatively,

    ||exp(-itHact)J-J exp(-itHtar)||
       <=16Kalpha+|t|[R6+Cmix alpha^2 beta]             (12)

for every real t. The bound can also be capped at2. The extra margin from12 to16 in the endpoint constant is deliberate. The physical output includes every ancillary qubit; nothing is postselected, discarded or renormalized. All operators extend identically over passive references. The projection construction uses the spectral separation of the SMALL full background in this new family, unlike the earlier volume-independent rectangular method. Its hypothesis is established below, not presumed for the original unscaled device.

## 5. A simultaneous fixed-cap family

For0<epsilon_g<=1, choose alpha to be EXACTLY the following positive minimum, using Bmax from(2):

    min{1/(32K), epsilon_g/(48K),
        sqrt[5epsilon_g/(2(8K)^6 U)],
        sqrt[epsilon_g*jbar/(3 Cmix U Bmax)],
        [jbar/(320 Bmax)]^(1/4),
        [jbar/(10Delta)]^(1/4)}, K=48.                 (13)

Then define nu,scale,T as in section1. The final entry ensures scale<=1. The penultimate entry gives

    beta/Delta=10alpha^4 Bmax/jbar<=1/32,

while the first entry ensures16Kalpha<=1/2. Thus all analytic and endpoint hypotheses are simultaneous. The three evolution allocations are

    16Kalpha<=epsilon_g/3,
    T R6<=(2/15)(8K)^6 U alpha^2<=epsilon_g/3,
    T Cmix alpha^2 beta
       =Cmix alpha^2 U Bmax/jbar<=epsilon_g/3.          (14)

The second estimate uses1-(8Kalpha)^2>=3/4, a safe weaker bound on this smaller domain. Hence the complete simulation error is<=epsilon_g uniformly on|t|<=T. There is no unpaid volume/time term. Equations(13)--(14) replace only c1cb's scale prescription and simulation estimate, not its physical block class, input or finite-router target.

Positivity, fixed support range, actual counts and full-support cap follow as in c1cb because the same blocks are used, scale<=1, and the new alpha ceiling is smaller than1/768. In detail: background head loads with mubar are belowLambda/2, P belowLambda/2; gadget increments are12nu per entrance head and24nu per P/Q; ancillary loads2Delta+2nu<Lambda. The count remains175+4ell qubits and389+8ell listed positive blocks including all original-head penalties. The fixed Manhattan interaction range remains35. All unlisted couplings are absent by premise.

For tau and epsilon_g fixed positive multiples of a final accuracy epsilon,

    jbar=Theta(Lambda epsilon^2),
    U,ell=Theta(epsilon^-3 log(e/epsilon)),
    Bmax=Theta(Lambda epsilon^-3 log(e/epsilon)).

The six entries of(13) have orders respectively

    1, epsilon, epsilon^2/sqrt(log(e/epsilon)),
    epsilon^(9/2)/log(e/epsilon),
    epsilon^(5/4)/[log(e/epsilon)]^(1/4), sqrt(epsilon).

The fourth eventually is the smallest. Therefore this explicitly chosen family has

    alpha=Theta(epsilon^(9/2)/log(e/epsilon)),
    scale=Theta(epsilon^16/[log(e/epsilon)]^4),
    T=Theta(Lambda^-1 epsilon^-21 [log(e/epsilon)]^5).   (15)

Size and relative output window remain those of970a. The preceding epsilon^-27 family remains valid and unchanged. Equation(15) compares sufficient families at the same cap, same full-output metric and same supplied-state/interaction premises; it proves no necessity, optimality or feasible engineering scale. Both constants are extremely large.

## 6. Operation, phase and preparation contract

Use exactly the boundary input Q and the two physical emitters, with their supplied one-excitation dual-rail code. The arbitrary logical program/path state may be entangled with a passive reference. Its fixed joint rest/environment state is independent of that input and obeys

    ||omega-omega_ideal||_1<=epsilon_rest,
    omega_ideal=|vac_other_heads,0_R><...|
             tensor |cat+><cat+|^tensor12 tensor sigma_PE.

All old-program, environment and preparation outputs are retained. Correct separate marginals are not a replacement for this joint contract. No channel to prepare these states is constructed here. Actual preparation errors may leave the plus sector or add heads; full-unitary trace contraction pays them without projecting the physical evolution.

With ideal rest, combine(12)--(14) with the exact entrance gauge and970a at time scale*t. The final target has the same positively normalized beta_F(scale*t), coherent controlled path operation with logical program now in P, R1, all other original heads including emitters vacant, literal cat+^12, and old sigma_PE relocated to sigma_QE with identity on E. Its full comparison phase remains

    exp{-it[48nu+s_joint+scale*cbar+scale*mubar]},
    cbar=8bbar+8(sqrt(2)-1)jbar.                        (16)

All mixed scalar corrections beyond(16) are bounded in(11), not silently removed. The inelastic profile still has phase n q(k)+(ell+57)k-scale*t Ebar(k), amplitude -i sqrt(q'(k))g(k), q=acos(cos k+kappabar/(2jbar)), and positive finite normalization on n=1,...,ell. Scaling changes no channel threshold ratio, cutoff normalization or common momentum phase.

On [3ell/(4scale*jbar),T], the complete unhalved channel discrepancy is at most epsilon_rest+3tau/4+2epsilon_g. For every0<=t<=T, the SAME unnormalized finite profile and scalar(16) give absolute record-1 complete subnormalized discrepancy at most epsilon_rest+tau+2epsilon_g. Record projection is a contraction, and the ideal branch is a contraction by q-variable Parseval; no rare-success division is made. Joint final success, including the cat comparator subspace, is at least

    1-(3tau/8+epsilon_g)^2-epsilon_rest/2.

Thus tau=epsilon/4, epsilon_g=epsilon/8 and epsilon_rest<=epsilon/4 again give final channel<=11epsilon/16, branch<=3epsilon/4 and success>=1-49epsilon^2/1024-epsilon/8. The difference from c1cb is the proven sufficient runtime scale, not weakened output requirements.

The gadget still fails to conserve original head number, so no original energy-to-blank, ground or Gibbs preparation theorem is inherited. All original coefficients, INCLUDING uniform penalty and record bias, are scaled. Supplied finite-range arbitrary positive two-body matrices, complex Y couplers, twelve entangled cat states, physical input placement/energy and reference independence remain premises. No stronger physical block or preparation premise is added by this analytical refinement, but none of those existing premises is removed. There is no native supplier, nearest-neighbor routing, autonomous initializer, physical readout/capture, permanent flag or literal old-processor claim.

## 7. Exact sources, exposure and decisive check

Paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- common_product_two_body_scaled_operation/PROPOSAL.md c1cbdb0eb1b7cc4b865c3ad8b8323b646eeff47e195c3239e297f007f0884bb7, fully reread here; its complete distinct review common_product_two_body_scaled_operation_check/REVIEW.md 4a1bc10174a72991ef77648188deedce151ad69f3e196ed572648064de6e2f4f was read here and hash verified. It supports the actual residual background, geometry, counts, cap, gauge transfer and full-output contract, not the new quadratic remainder.
- Joint common_product_full_swap_gadget/PROPOSAL.md b54c6f29ea780efdcad7f33def048a0b5f9436fe8125ce3c2b2b416cabde4436 retains its immediately preceding complete read and verified identity. Its complete distinct review6dfaeacb3a3b1b2f2dfdcdf4c2f862b41687dac7a9dc08b35adae1865e4e90e3 was read and hash verified here. The review's exact enumeration was not rerun or represented as this author's execution. Only the checked pure-V normalized coefficient/parity/remainder is imported.
- Finite common_product_resonant_router_resources/PROPOSAL.md970a84e5e9157c6a9d5934f00df59491de19e6c88402efe0e14b44e68bc1479b and its reviewcb0e278a7311651ea9f8d258089cba00a10fb03bb37457d2f8db1d5864af5da7 retain the complete reads and checked identities from the immediately preceding composition. The direct boundary b58d047e8b7d6598951f84cb5c275d9709fe19b9b99e0383558536b581332ad9/reviewdcb52ff26e482a9d175d9e5c357624a51e2c5e40c8cbad72512853698ec2c901 and entrance gauge c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e are used only through their unchanged fully read complete-output interfaces.

ROOT suggested a two-variable effective-operator route, global-volume allowance and possible exponent21. This author derived the bidisc constants, exact axis/parity cancellation, all-order mixed sum, real endpoint estimate, volume ceiling and simultaneous prescription after that exposure. This is new source-exposed same-model author work, not independent validation or a novelty claim for perturbative gadgets generally. A distinct reviewer should particularly test analytic normalization for noncommuting B, E(0,y)=yB on the complex bidisc, the mixed coefficient sum, projection endpoint independence from beta, and the six-entry maximum with all runtime factors.

Only this proposal was created. No scientific executable, numerical sweep, delegation, old source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. The earlier local-commutator route and its fixed-scale failure remain valid at their scopes; the present result instead pays an explicitly small global background.
