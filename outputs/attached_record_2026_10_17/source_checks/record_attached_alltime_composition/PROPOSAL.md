# All-time unnormalized record-1 map for the infinite attached device

Status: authored conditional composition, awaiting distinct review and specifically PROVISIONAL on the sharp recovery argument below. The checked seed-mass, outgoing and incoming results do not alone establish this theorem; the full recovery leg is essential. No quantitative onset, finite-device all-time transfer or native Record claim is made.

## Conditional theorem and physical target

Use exactly the frozen infinite attached apparatus: the original shared old/source registers and two-converter device, input stub ell=20, equal-diagonal emitter with kappa=1e-8, eighteen output cable sites v0=(82,1,1) through v17=(99,1,1), and the transformed 24-head record gate whose input is p=(100,1,1) and output is o=(100,2,2). The final output ray is o_n=(100,2+n,2). The free output comparison below uses ONLY n>=1: the port o=o_0 belongs to the finite gate/core budget. There is no extra free input lead at v0. Retain the same four old/source qubits and one shared record qubit, the supplied source-vacuum/emitter-occupied/record0 initialization, all installed PSD blocks, and the selective-coupling premise for uninstalled neighboring pairs.

Let H_att be that bounded self-adjoint one-head operator, including its actual common scalar

    c_att=c_total+4(sqrt(2)-1)j,

and all shared B/contact interactions. The full physical qubit Hamiltonian preserves this seeded sector. This does not assert a bounded norm for an infinite many-head Hamiltonian. Let V embed the entire four-dimensional old input into the supplied apparatus seed. Let P_1 project onto computational record1, retaining ALL other coordinates. Identify its range with the remaining system plus an explicit record1 factor. The actual unnormalized record map is A_1(t)=P_1 exp(-it H_att)V.

The literal target is

    W=((9+12i)/25)I+((-16+12i)/25)X1X2,
    K=2I+Z1Z2.

They commute with one another and have the common real old basis labeled by b=1,3 and parity. This does not imply [H_att,K]=0. W has unit-modulus parity eigenvalues omega_+=(-7+24i)/25 and omega_-=1.

Put h=4e-6, J_q=[pi/2-h,pi/2+h], w=exp(iq), E(q)=2j(1-cos q), and

    D_ref(q)=E(q)-2j+(kappa^2/j)w,
    rho_att(q)=-i w^40 rho_n(q),
    F(q)=i E'(q) kappa rho_att(q) w^21/
                         [sqrt(2pi) j D_ref(q)].

Here rho_n is the SAME supplied common converter phase, equivalently rho_n=zeta exp(172ik(q)); no input-dependent phase is selected. Define the unnormalized reference packet on n>=1 by

    beta_t(n)=(1/sqrt(2pi)) integral_Jq
                       F(q) exp(iqn-itE(q)) dq.       (1)

Let J_out embed this packet with the head on the final free ray, all other head sites blank, shared source in its vacuum and record1. The common comparison map is

    T_1(t)=exp(-it c_att) J_out[beta_t tensor exp(-itK)W]. (2)

Under the pinned source premises and the provisional sharp recovery lemma specified below, for EVERY t>=0,

    ||A_1(t)-T_1(t)|| < .0045.                       (3)

This is an operator norm on arbitrary old inputs, and the identical bound holds after tensoring ANY passive reference identity. It is an absolute unnormalized state-map statement. It does not assert small relative conditional error when the record1 probability is tiny.

Write p0=integral_Jq |F(q)|^2 dq. Then

    1-1.1e-6<p0<=1,    ||beta_t||^2<=p0,
    lim_(t->infinity)||beta_t||^2=p0.                 (4)

Thus the packet NORM tends to sqrt(p0), while its SQUARED norm tends to p0. The distinction matters for the success inequalities below.

## Sources, status and exposure

I read the complete changed mass, corrected outgoing and incoming proofs and their checks. Exact SHA256 identities are:

| Source under the renewal directory | Proposal SHA256 | Distinct check SHA256 |
|---|---|---|
| record_attached_seed_mass | be7ff80c9667e80dd87d104e9bd03766b5fa14265deecab0a9b800278579a3dc | e3e40799fe208c336612c9f35805051f4fde468772cb9f0e7796be1835780999 |
| record_attached_outgoing_profile | 52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788 | 44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026 |
| record_incoming_alltime | 1def426f0919789b6a1a8c4048756c3a95a6a2b9ed4b5223c90e0ca321db8bf7 | 8ea2e16b8683ecc1eb9c2f92397d372d9ddb55cdc87c780bcd1755677cb76caf |
| record_core_operator_difference | 69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac | ad38a71087013fcee8f9ef7f00f62177d053c7ff03ba5573b524bbc3f9993357 |

Each proposal is `../<source>/PROPOSAL.md`; each check is `../<source>_check/REVIEW.md`, except the incoming source/check names already follow that same rule. These sources are imported as their complete mathematical arguments and explicit premises, not as conclusions inferred from filenames or status labels. The outgoing source is the CORRECTED version retaining wrong-window prepared-input rows and its non-strict center inequality.

The additional load-bearing recovery source is my `../record_attached_recovery_sharp/PROPOSAL.md`, SHA256 `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`. Its separate review was assigned but not yet available for this composition. Its physical filter/finite-coordinate recovery and integration constants are explicit PROVISIONAL premises of (3). I cannot independently check my own sharp lemma by composing it here.

Previously completely read and unchanged dependencies are attachment fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457/check7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005; gate inverse3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82/checkcebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f; attached endpoint2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9/check30bb3f38752c5d6fc2b036042315c7ccb82f2f932805e04476e9a886822b6fa3. Original source, scalar and geometry premises remain pinned to the canonical original note71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, via the exact dependency chains in these sources; no original calibration is recomputed.

I authored the abstract core interface, sharp recovery argument, prior resource check and converter publication draft, but neither the mass/outgoing/incoming proof nor the local gate construction. Their arguments and requested target were exposed. This is authored synthesis, not blind discovery, independent review or retained/audit certification. No scientific execution, sweep, solver, delegation, Git/W/checkpoint/publication/model/prompt edit occurred. This proposal is the sole new deliverable.

## 1. Common windows and the omitted state

Use physical energy Lambda and the SAME union for every old input and record sector:

    I_b=[c_att+b+2j-d,c_att+b+2j+d],
    d=2j sin h, b=1,3, I=I_1 union I_3.

The two intervals are disjoint. On each interval and each old parity there is one open B channel and seven closed channels; the record-X sectors remain separate until recombination. All actual old/source coordinates are retained. The checked full seed-matrix mass proof gives

    ||E_Hatt(R outside I)V||<epsilon_sp=.001057.    (5)

This includes all omitted spectral types and both old-energy input columns, including their off-diagonal seed measure. It is not a reference-tail substitution. Evolution preserves this norm and P_1 is contractive, so (5) is charged ONCE for the entire final comparison, not separately for core and ray.

The same mass proof supplies local spectral regularity from the complete finite matching inverse chain: original source, both converters, input deletion, gate/load, closed returns, selected feedback and emitter. Branch thresholds are separated from the closed windows. Real determinant nonvanishing yields local analytic inverse neighborhoods, excluding hidden dark finite modes and seed singular mass on I, including cutoffs. This does not provide a quantitative contour strip or a time scale.

## 2. Exact two-lip synthesis on the actual graph

Let s=+,- denote record-X, and let V_s be its common old-input seed embedding. For each finite coordinate restriction Q_y the cross spectral measure is absolutely continuous on I. Indeed absolute continuity of the seed measure implies that a null set annihilates E_Hs V_s, and hence its cross measure. The coordinate resolvent boundary values obtained by the full matching system give its density by Stone's formula:

    Q_y dE_Hs(Lambda)V_s/dLambda
       =[Q_y R_s^down(Lambda)V_s
                   -Q_y R_s^up(Lambda)V_s]/(2pi i). (6)

This is a rectangular-column identity; no scalar imaginary-part shortcut is used. All matrices, coordinate embeddings and the chosen old basis are real, so the lower column is the conjugate of the upper column in fixed domain/range conjugations. This is a statement about matrix entries defining LINEAR maps on complex inputs, not complex conjugation of the input state.

For the open component on the final ray n>=1, let A_s,b(q) be the complete retarded seed-to-output row on physical window I_b. The upper coordinate is exp(iqn) A_s,b, and the lower coordinate is exp(-iqn) conjugate(A_s,b). Since dLambda=E'(q)dq, define

    F_s,b(q)=i E'(q) A_s,b(q)/sqrt(2pi).

Equation (6) then gives exactly the SUM of the outgoing and incoming Fourier integrals,

    (1/sqrt(2pi)) integral_Jq exp[-it(c_att+b+E(q))]
       [exp(iqn)F_s,b(q)+exp(-iqn)conjugate(F_s,b(q))]dq. (7)

The sign in both terms is positive: the lower-minus-upper jump and the factor i in F supply it. Record0 preparation and record1 projection take one half the DIFFERENCE of sectors, so put C_b=(F_+,b-F_-,b)/2 in (7), and conjugate(C_b) in its incoming term. No additional probability or amplitude factor is introduced.

Equality (7) first holds at every finite ray coordinate. Fourier isometry gives the corresponding l2 ray vectors; equality of all coordinates identifies these vectors with the open portion of the actual spectral evolution. The infinite closed portions have uniform decaying roots and bounded finite recovery, so their geometric l2 sums and energy integrals converge in norm. Thus neither an unbounded stationary open-wave norm nor an exchange of an uncontrolled infinite sum is used.

## 3. Complete outgoing and incoming coefficient comparison

The corrected outgoing proof bounds the selected diagonal coefficient by

    |C_b,j(q)-omega_j F(q)|
                   <(2e-13+400u)|F(q)|.

It also explicitly bounds the other prepared old-energy input on the SAME I_b through the ordered complementary emitter inverse; its outgoing coefficient row is not set to zero. That wrong-window contribution has total coefficient allowance <1e-34. With the checked reference moment M2<1.9e-17 and the two potentially overlapping old-input errors within a parity, the complete coefficient error is

    epsilon_coef=2.5e-6.                            (8)

This includes the union of both physical windows. Parities are orthogonal; passive references preserve the resulting operator norm. Wrong-window terms retain physical phase exp[-it(c_att+b_output+E(q))], not an input-energy phase. These rowwise unitary multipliers and Fourier isometry preserve (8). Restricting to n>=1 is contractive. Only the IDEAL diagonal term factors as exp(-itK)W in (2); no such factorization is imposed on the actual source evolution.

Real conjugation of the entire coefficient matrix preserves the same norm bound for the incoming error. The ideal incoming term has conjugate(omega_j) conjugate(F(q)), hence the old multiplier W^* in this real common eigenbasis, rather than W. It is not absorbed into (2). Its norm is bounded and charged as an unwanted contribution.

The checked incoming scalar theorem, with its actual phase exp[-i61q-i172k(q)], bounds that reference on n>=0 for all t>=0 by .00105 even after normalization by sqrt(p0). Our unnormalized version and the stricter n>=1 restriction have no larger norm. Different ideal old channels are orthogonal, so their common scalar norm is also the arbitrary-input/reference map norm. Consequently

    ||actual in-band incoming open contribution||
                 <.00105+epsilon_coef, t>=0.        (9)

Incoming and outgoing occupy the SAME ray; their errors are added by triangle inequality. No time-dependent orthogonality is assumed.

## 4. Finite coordinates and complete closed tails

The common emitter and coupling give exact full-fiber Schur columns

    F_s^core=[T_s; -kappa L_s T_s],
    Delta F^core=[kappa^2 T_+ DeltaG T_-;
       -kappa DeltaL T_- -kappa^3 L_+T_+DeltaG T_-]. (10)

Here L_s retains all 193 upstream noncable heads, eighteen cable sites, 24 gate heads including o, and their full internal coordinates. The downstream closed tails beyond o are separately included using the exact geometric recovery; the open ray begins at n=1 and is covered by (7). The emitter itself occupies the first block of (10). B and K need not commute with the recoveries or inverses.

The provisional sharp source provides, on each window and both lips,

    ||T_s||<1/[.98 sqrt(delta^2+gamma^2)],
    ||DeltaG||<1e-47+1.21e7|delta|,
    ||DeltaL||<22001+5.3e9|delta|,
    ||L_s||<4e5, gamma=kappa^2/j.

Its derivation pays finite-site aggregation, all input coordinates, finite-input/cable growing-root cancellation and every downstream closed tail. The latter projection is fixed within each window but differs between windows; therefore their integrated contributions are added by triangle inequality, not declared orthogonal to the other window's open channel.

Applying (6), the record half-difference and the abstract interface gives jump factor 1/(4pi), or 1/(2pi) after equal bounds on both lips. The exact energy integrals are

    I_G=2a_G arctan(d/gamma)/gamma
                         +b_G log(1+d^2/gamma^2),
    I_L=2a_L asinh(d/gamma)
                  +2b_L(sqrt(d^2+gamma^2)-gamma).

With d/gamma<720000, the sharp source obtains <.00108 per window for the combined represented emitter/core/closed-tail record1 map. Summing TWO physical windows in a parity gives

    epsilon_local=.00216.                          (11)

This is a full operator bound, including inputs whose energy labels differ from the current window. It includes no omitted spectral remainder; (5) is still charged only once. Different parity blocks combine by a maximum. The absolute bound is uniform in t because every remaining real-energy time factor has modulus one. The direct kappa DeltaL T term is retained and is responsible for much of (11).

## 5. Total error and arbitrary references

Decompose the actual record1 map into the represented finite/closed contribution, represented outgoing and incoming open terms, and the single omitted state. Equations (5), (8), (9), (11) give

    ||A_1(t)-T_1(t)||
       <.001057+.00216+.00105+2*(2.5e-6)
       =.004272<.0045,       t>=0.                 (12)

This conservative triangle budget pays the two spectral lips, both physical windows, all wrong-window input columns, every finite coordinate, all closed tails, and both same-ray traveling terms. No finite packet is renormalized. The apparatus-independent old/reference map bound follows before choosing an input, so tensoring an arbitrary passive reference leaves the ceiling unchanged. The result is conditional on the sharp review and inherited full inverse/calibration premises, not an assumption that the desired total .0045 had to hold.

## 6. Reference escape and honest success consequences

Extend the coefficient F on J_q by zero to a 2pi Fourier interval. Its full integer-lattice Fourier evolution has squared norm p0 at every t. The dispersion velocity E'(q) is bounded below by .0053 on J_q. For a smooth coefficient compactly supported in its interior, integration by parts in the phase qn-tE(q) bounds amplitudes at n<=0 by C/(|n|+v t), with v>0, for large t. Squaring and summing gives a quantity tending to zero. This follows since the phase derivative has magnitude at least |n|+v t; the derivative of the denominator contributes another uniformly controlled term of the same order. Smooth compactly supported coefficients are dense in L2(J_q), and full Fourier evolution and restriction have norm at most one. Approximation therefore extends the vanishing left-halfline norm to the actual hard-band F. No analyticity of the cutoff is assumed. This proves (4), including removal of the gate coordinate n=0.

For any normalized old/reference pure input psi put r(t)=||beta_t|| and p_psi(t)=||A_1(t)psi||^2. The operator estimate gives at every t>=0

    max(0,r(t)-.0045)^2 <= p_psi(t)
                  <=min(1,(r(t)+.0045)^2).          (13)

Thus, uniformly in input,

    liminf_(t->infinity) p_psi(t)
       >=(sqrt(p0)-.0045)^2>.991.                  (14)

There is no claimed convergence of the actual probability to p0: the fixed absolute error permits persistent residual motion. Equation (14) implies an eventual lower ceiling uniformly over inputs, but supplies no numerical onset time. The theorem concerns a single read at a chosen time; repeated measurements change the dynamics and are not covered.

Whenever r(t)>.0045, the actual record1 branch is nonzero for every normalized input. Its normalized state differs from the normalized ideal beta_t/r(t) tensor exp(-itK)W psi, with the same scalar phase and blank apparatus, by at most 2*.0045/r(t). This follows by adding and subtracting the unnormalized vectors divided by r(t), and using the reverse triangle inequality for their norms. As t tends to infinity its limsup is at most .009/sqrt(p0)<.0091. No useful uniform RELATIVE early-time statement follows when r(t) is small; (3) remains an absolute map estimate there.

## 7. Separate asymptotic complete-state corollary

There is a stronger asymptotic statement about the COMPLETE unprojected evolution. It does not replace the all-time branch estimate. Write U_seed(t)=exp(-itH_att)V, retaining both record values. Then the same source premises imply

    limsup_(t->infinity)||U_seed(t)-T_1(t)||
                     <=.001057+2.5e-6=.0010595.     (15)

Here T_1 is embedded in the complete Hilbert space with record1. Unlike (3), this comparison also controls the record0 branch. Its proof is as follows.

First consider one record-X sector, one parity and one energy window. Every finite-coordinate resolvent column has continuous boundary values on the compact window by the checked finite inverse chain. At the fixed nonzero kappa the resonance denominator is bounded away from zero; it may be small, but its energy integral is finite. Thus the finite-coordinate spectral-jump column is Bochner integrable in the Hilbert space of finite coordinates. The same holds for the entire closed output tail: the amplitude at its origin is continuous and bounded and every root obeys |s_l|<1/60. Its geometric l2 norm is uniformly bounded, and the tail depends continuously on energy in l2 by uniform geometric domination. This is a Hilbert-space-valued L1 density, not an argument that individual site convergence controls an infinite norm.

For an L1 density with values in this Hilbert space, its time Fourier transform tends to zero in norm. One elementary proof approximates it in L1 by finite sums of constant Hilbert vectors times interval indicators. Each interval's Fourier integral tends to zero, and the norm of the approximation error bounds the transform error uniformly in time. The finite-dimensional old input domain permits the same conclusion in operator norm by approximating all columns, and passive-reference tensoring leaves that norm unchanged. Summing the two windows and parities therefore shows that every represented finite/core/closed-tail sector contribution vanishes. This qualitative argument needs full inverse regularity and recoverability; it does not require the particular sharp numerical recovery constants used in (11).

Second, the actual incoming coefficient is L2 on its compact momentum interval, including all wrong-window rows. For a smooth interior approximation the phase -qn-tE(q) has derivative of magnitude n+tE'(q)>=n+vt on n>=1. The integration-by-parts and square-sum argument of section 6, followed by uniform L2 approximation, proves that its physical positive-halfline norm tends to zero. Apply it to every matrix column and both windows. This conclusion uses actual coefficients, not just the small all-time bound on the reference incoming wave.

Third, the outgoing profile proof supplies the SAME 2.5e-6 complete-input coefficient error for EACH record-X sector relative to s omega_j F: its selected estimate and complementary-input bound are sectorwise before taking the half-difference. After Fourier synthesis this is a uniform outgoing error per sector. The initialized record0 has sector weights 1/sqrt(2); the ideal record1 has the corresponding opposite signs. The errors in the two orthogonal record-X ranges therefore have squared norms averaging, so their joint operator bound is again 2.5e-6, not twice that number. No record projection discards an unbounded record0 remainder. The actual omitted spectral state still costs the single .001057 from (5). Combining these facts proves (15).

For sufficiently large t let a_t=beta_t/||beta_t||. Replacing the unnormalized target by

    T_norm(t)=exp(-it c_att) J_out[a_t tensor exp(-itK)W]

costs 1-||beta_t||. Its limiting cost is 1-sqrt(p0)<5.6e-7, because 1-p0<1.1e-6 and sqrt(p0)>sqrt(1-1.1e-6). Consequently

    limsup_(t->infinity)||U_seed(t)-T_norm(t)||<.001061. (16)

This is a complete old/reference state-map bound, with source vacuum, all upstream head sites blank and record1 in the ideal. In particular its projection to record0 gives the stronger asymptotic success implication

    liminf_(t->infinity) inf_(||psi||=1) p_psi(t)
                         >=1-(.001061)^2.

The uniformity follows from operator-norm convergence estimates, not a pointwise time chosen separately for each input. Neither (15) nor (16) gives a numerical onset or asserts convergence of the actual error to zero. Omitted point/singular spectrum may persist within its charged norm. This corollary was requested by root during composition and is a new exposed proof step requiring distinct review; it is not evidence for an uninspected temporal proposal.

## Scope and next check

The apparatus, source vacuum, record0 preparation, exact correlated coefficients and readout projection are supplied mathematical data. No native Record identification, autonomous initialization, physical units, manufacturing tolerance removal or new precision premise is derived. The infinite output lead is essential to the all-time and asymptotic statements. A finite cap admits recurrence; no finite all-time halt, permanent completion latch, reset or reuse theorem follows. A separate bounded-time finite transfer would require its own checked onset, horizon and resources. No pending concentration-time or finite-length candidate is imported here.

Distinct review must first resolve the sharp recovery proof, then check this composition's actual two-lip sign/normalization, cross-window prepared-input coverage, all closed-tail integration, single omitted-state charge, n>=1 reference support and asymptotic norm argument. If the sharp lemma changes, (11)–(14) must be recomputed from its actual replacement constants rather than preserving the proposed .0045 by fiat.
