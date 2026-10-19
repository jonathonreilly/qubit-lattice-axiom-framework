# Conditional scaled operation with twelve positive two-body gadgets

New source-exposed author composition, requiring a distinct check. The joint-gadget source is a provisional dependency at this writing; the local-background source has its scoped distinct check. Conditional on the joint source's stated isolated coefficients, a simultaneous energy rescaling closes the full finite-router comparison below. This uses arbitrary positive, possibly complex, two-qubit matrices of fixed range at most35, twelve supplied cat+ states, and a supplied physical boundary input. It is not a realization in the former nearest-neighbor primitive class or a preparation theorem.

## 1. Reference and actual positive device

Fix 0<tau<=1 and Lambda>0. Use the entire explicit resonance family970a, including its prescribed cutoff, rho, u, ell, physical finite sources/caps and time window. Write its quantities with bars. Thus

    jbar=Lambda tau^2/(8*10^12), bbar<=Lambda/(8*10^9),
    Tbar=7ell/(8jbar), U=jbar Tbar=7ell/8,
    U=Theta(tau^-3 log(e/tau)).

Add the ordinary input Q and replace the two ordinary entrance bonds by c97b's SWAP entrance bonds. Install the optional uniform penalty with the definite choice mubar=Lambda/4 on ALL original heads; it is absent on Q,P,R and new gadget ancillas. This defines the reference Hbar_new. Its target is the boundary-input theorem's complete output, with old P/environment relocated to Q/environment. The one-head gauge proof works for the new length/time family because it is an exact operator intertwiner for every finite length, and970a proves the same full isometry and flag contracts at that length. The reference errors are d<3tau/8 on [3ell/(4jbar),Tbar] and f<tau/2 on [0,Tbar]. The uniform penalty contributes exactly exp(-imubar t) on the nominal one-head comparison, not on arbitrary error states.

Define Bbar by retaining every reference block except the two SWAP entrance blocks. At each entrance insert instead the THREE positive blocks

    Q_(jbar/2)(i,j), (jbar/2)n_i, (jbar/2)n_j.

These residual blocks act on heads only. Then, on the FULL original Hilbert space,

    Hbar_new=Bbar-(jbar/4) sum_(l=1)^12 Omega_l.          (1)

The twelve Omega_l and their shared six data qubits are exactly those of b54c; (1) includes all head-occupation sectors. Bbar is positive as a sum of its displayed blocks. Q has no background coupling. P retains its original diagonal mediator controls. No gate is applied at a selected time.

Choose Delta=Lambda/4, alpha>0, nu=Delta alpha and

    scale=10Delta alpha^4/jbar <=1,
    T=Tbar/scale=U/(10Delta alpha^4).

The actual installed Hamiltonian is

    Hact=scale Bbar+48nu I+H0+V,                        (2)

where the last three terms are the 96 positive blocks of b54c on48 new ancillas. Thus g=(5/2)Delta alpha^4=scale jbar/4. Its scalar effective coefficient is

    s_joint=-24nu^2/Delta+27nu^4/Delta^3.

The comparison generator is scale Hbar_new+(48nu+s_joint)I. All reference coefficients, INCLUDING bias, uniform head penalty, source gamma and compensations, are scaled together. The dimensionless band, velocities, times and twelve source/cut allocations are therefore identical at reference time scale*t. There is no retained unscaled head gap.

## 2. General rectangular background estimate for K=48

Here the joint proof must replace an isolated four-column argument. Work in the common ancillary plus sector. Let J append the twelve literal cat+ states, P=JJ*, and Pi be the isolated low projection of H0+V. Set W=Pi J C, C=(J*Pi J)^(-1/2). For K single-data Pauli couplers V=nu sum_(r=1)^K O_r X_br, assume the same zero-space and complementary gap>=2Delta, and alpha<=1/(16K). The contour |z|=Delta/2 gives

    ||Pi-P||<=2Kalpha/(1-2Kalpha)<=1/7,
    ||W-J||<=2||Pi-P|| <5Kalpha.                       (3)

These estimates use ||V||<=Knu, not mutual commutation of its data factors. The joint b54c construction has K=48 and verifies its normalized isolated coefficient and even analytic remainder

    ||E-E_lead||<=R6,
    R6=Delta(8Kalpha)^6/[1-(8Kalpha)^2].                (4)

Let B act on the data/rest but not the ancillas and put C_B=sum_r||[B,O_r]||, with repeated data terminals counted once PER coupler. Resolvent commutation, valid without any bound on global ||B||, gives

    ||[B,Pi]||<=2alpha C_B/(1-2Kalpha)^2.

Since BJ=JB, the binomial inverse square root yields ||[B,C]||<.64||[B,Pi]|| and ||C||<1.081. Consequently

    ||BW-WB||<=6alpha C_B.                             (5)

The numerical factor6 remains valid for K=48 because 2Kalpha<=1/8. It does NOT come from summing twelve isolated effective evolutions. Combining the joint isolated intertwining with (5) and integrating the rectangular residual gives

    ||exp(-itHact)J-J exp[-it(scale Hbar_new+48nu+s_joint)]||
       <=10Kalpha+|t|(R6+6alpha C_B), K=48,            (6)

with B=scale Bbar. Both propagators are unitary on their full spaces; the actual dressed space need not be invariant under B. Equation(6) retains all leakage, arbitrary data occupations, old P/environment and passive references. No spectral gap of Hact or global-volume norm is used.

## 3. Actual local coefficient and cap

For any single-site Pauli O at v, ||[Bbar,O]||<=2L_v, where L_v is the full-support incident sum of Bbar's listed blocks. There are six couplers at each of the four entrance heads, twelve at P and twelve at Q. The latter background load is zero. The ordinary one-control inventory and residual replacement imply

    L_i<=4jbar+mubar,
    L_j<=6bbar+4jbar+mubar,
    L_P=4(D1bar-2bbar)<Lambda/2, L_Q=0.

The residual contact has load3jbar/2 on either head, smaller than the removed ordinary Q_jbar load2jbar. Thus the ordinary endpoint upper bounds above remain valid; no four-site SWAP load is counted in Bbar. The two entrances have identical ceilings. Therefore

    Cbar=sum_(r=1)^48 ||[Bbar,O_r]||
       <=2[6(4mubar+12bbar+16jbar)+12(Lambda/2)]
       =24Lambda+144bbar+192jbar <25Lambda.             (7)

This includes X/Y program terms, which do NOT commute with programmed detunings. Using only the ZZ commutator cancellation would be invalid for this assembly. Bias and remote terms commute with the data Paulis; the full local-load ceiling already covers every retained coupling. Scaling gives C_B=scale Cbar.

The original head loads with mubar are <Lambda/2 on this exact family: endpoints are bounded as above, mediators by D1bar+2bbar+mubar, source heads by5jbar+mubar and ordinary heads by4jbar+mubar. Original P has load<Lambda/2 and R has8jbar+kappabar. Scaling cannot increase them. New ancillary loads are2Delta+2nu<Lambda; the added head loads are12nu, and P,Q loads24nu. At alpha<=1/768 these are at most Lambda/256 and Lambda/128 respectively. Hence every actual full-support incident sum is <Lambda. All added blocks are positive; this cap statement is not confined to one-head dynamics.

Use the exact disjoint coordinates in b54c: square l has vertices (24,4,2l),(25,4,2l),(25,5,2l),(24,5,2l), l=1..12, with the fixed six entrance/Q/P data sites. Existing rays and writers avoid these vertices for every ell. Coupler range is at most35 in Manhattan distance; square penalties remain nearest-neighbor. Unlisted couplings are absent by premise. This is a finite-range two-body construction, NOT a routed nearest-neighbor construction.

There are175+4ell qubits: the126+4ell reference qubits, Q, and48 ancillas. The physical block count without the uniform penalty is265+4ell: replace two bonds by six residual blocks and add96 gadget blocks. Including124+4ell original-head penalties gives389+8ell blocks. Ancillas are not counted as original heads and receive no uniform head penalty.

## 4. Simultaneous scaled choice and sufficient orders

For a desired vector simulation allowance 0<epsilon_g<=1, choose alpha to be EXACTLY the minimum

    min{1/(16K), epsilon_g/(30K),
        sqrt[5epsilon_g/(2(8K)^6 U)],
        epsilon_g jbar/(450Lambda U),
        (jbar/(10Delta))^(1/4)}, K=48.                 (8)

Every term is positive. The last ensures scale<=1. The three contributions in (6), uniformly |t|<=T, obey

    10Kalpha<=epsilon_g/3,
    T R6 <=(2/15)(8K)^6 U alpha^2<=epsilon_g/3,
    6alpha T scale Cbar
       <=150alpha Lambda Tbar<=epsilon_g/3.            (9)

Here the denominator of (4) is at least3/4. This proves a full operator simulation bound <=epsilon_g throughout the entire horizon, with exactly the selected finite router parameters. In contrast to fixed-scale matching, reducing alpha now reduces the background cost because the whole background strength decreases as alpha^4. No isolated-error cancellation between gadgets is assumed.

With tau and epsilon_g proportional to a final small tolerance epsilon, the fourth entry in (8) has order epsilon^6/log(e/epsilon), and eventually is the smallest entry. The other orders are constant, epsilon, epsilon^2/sqrt(log(e/epsilon)), and sqrt(epsilon). Therefore this particular sufficient family has

    alpha=Theta(epsilon^6/log(e/epsilon)),
    scale=Theta(epsilon^22/[log(e/epsilon)]^4),
    T=Theta(Lambda^-1 epsilon^-27 [log(e/epsilon)]^5),
    ell=Theta(epsilon^-3 log(e/epsilon)).                (10)

This is an asymptotic consequence of the explicit minimum, not a fitted exponent or a necessary cost. The constants are extremely large. Exact coefficient magnitudes are not fabrication tolerances. No optimality or practical advantage is claimed.

## 5. Complete boundary input, outputs and branch

Supply the ordinary Q program and the TWO physical I emitters as the input B, with the exact dual-rail identification of b58d. Arbitrary coherent program/path/reference input is allowed. The rest comprises all other original physical qubits and the48 new ancillas, together with a retained passive environment E. It is fixed independently of the input. Require a JOINT trace-distance contract

    ||omega_rest,E - omega_ideal||_1<=epsilon_rest,
    omega_ideal=|vac_other_heads,0_R><...|
                 tensor |cat+><cat+|^tensor12 tensor sigma_PE. (11)

Correct ancilla marginals alone do not suffice. Alternatively projecting onto the displayed rest/head/record/cat subspace with failure q gives (11) with2sqrt(q) and a normalized sigma_PE. This is a state certificate, not a procedure preparing it. The environment E is never manipulated. All preparation-device outputs must be retained in E or another explicitly declared spectator factor.

On the ideal comparator, apply (6), then the exact entrance gauge and970a at time scale*t. The final common target uses beta_F(scale*t), puts the input program in P, applies its coherent controlled path operation, has R1, every non-F original head INCLUDING emitters vacant, all48 ancillas in their twelve supplied cat+ states, and relocates old sigma_PE losslessly to sigma_QE. Its phase is EXACTLY

    exp{-it[48nu+s_joint+scale*cbar+scale*mubar]},
    cbar=8bbar+8(sqrt(2)-1)jbar.                        (12)

Here cbar is the scalar vacancy coefficient, distinct from Cbar in (7). The radial sequence remains the positively normalized restriction of

    B_n(scale*t)=(-i)/sqrt(2pi) integral
      exp[i n q(k)+i(ell+57)k-i scale*t Ebar(k)]
                                 sqrt(q'(k))g(k) dk,
    q(k)=acos(cos k+kappabar/(2jbar)), n=1..ell.

There is no extra record-bias phase. Actual ancillary or head leakage is included in the error, never projected away. The actual gadget does NOT conserve original head number; mubar contributes a scalar only in the reference one-head target. Equation(6) pays the actual excursions.

The final window is [3ell/(4scale*jbar),T]. Its vector error for ideal rest is d+epsilon_g, hence the actual complete channel error is

    <=epsilon_rest+3tau/4+2epsilon_g.                  (13)

For all0<=t<=T keep the SAME unnormalized finite B profile and the same scalar(12), with the cat and old-program outputs included. Since record projection is a contraction and commutes with the gauge, its absolute complete subnormalized channel error is

    <=epsilon_rest+tau+2epsilon_g.                     (14)

No normalization of a rare record event occurs. Joint final success includes the original retained-F/R1/vacancy event AND the cat comparator subspace; its probability is at least

    1-(3tau/8+epsilon_g)^2-epsilon_rest/2.              (15)

For example tau=epsilon/4, epsilon_g=epsilon/8, epsilon_rest<=epsilon/4 gives final channel<=11epsilon/16, branch<=3epsilon/4, and success>=1-49epsilon^2/1024-epsilon/8. Every output and arbitrary passive reference remains in these bounds. The event is mathematical, not a supplied readout device.

This removes the four-site entrance interaction only CONDITIONAL on the enlarged finite-range arbitrary-positive two-body block class and the cat states. It uses the direct boundary-input contract, not a black-box loader that discards old information. Ordinary single-qubit-to-dual-rail conversion, input placement/energy supply, preparation/start time, cat preparation, native coefficients and physical readout/release remain supplied or open. The physical gadget has extra sectors and no original head conservation; old ground, energy-to-blank or Gibbs criteria are NOT inherited, even though the nominal penalty was scaled consistently. No indefinite flag, permanent halt, thermal result or old literal processor realization follows.

## 6. Exact evidence and open checks

All paths below are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- Joint isolated source common_product_full_swap_gadget/PROPOSAL.md b54c6f29ea780efdcad7f33def048a0b5f9436fe8125ce3c2b2b416cabde4436, fully read and hash verified. Its distinct check is pending at this writing; its mixed fourth-order scalar and normalized analytic coefficient are provisional dependencies, not newly independently verified here.
- Background source common_product_loader_component_background/PROPOSAL.md e7d3efb291b47ce6d6265b293ea448de917380ae5a36322664bee857ca7312aa, authored previously and fully reread. Its distinct review common_product_loader_component_background_check/REVIEW.md 9fc08fb322d2e323d9f8cbaf1669c1b6bcc5954c6857296e5e9adb8e1821738b was fully read before freezing this composition and supports the isolated background scope. Section2 explicitly rederives its rectangular estimate for the noncommuting joint K48 source instead of importing the four-data-column premise.
- Finite source common_product_resonant_router_resources/PROPOSAL.md 970a84e5e9157c6a9d5934f00df59491de19e6c88402efe0e14b44e68bc1479b and complete review common_product_resonant_router_resources_check/REVIEW.md cb0e278a7311651ea9f8d258089cba00a10fb03bb37457d2f8db1d5864af5da7, both fully read here; the review hash was verified. Only its checked supplied-device operational scope is used.
- Boundary source common_product_boundary_input_contract/PROPOSAL.md b58d047e8b7d6598951f84cb5c275d9709fe19b9b99e0383558536b581332ad9 and complete review common_product_boundary_input_contract_check/REVIEW.md dcb52ff26e482a9d175d9e5c357624a51e2c5e40c8cbad72512853698ec2c901 were fully read; the review hash was verified. Its state/input quantifiers are retained, but its restricted energy certificate is not transferred to Hact.
- Exact gauge source common_product_autonomous_loader_interface/PROPOSAL.md c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e and one-control inventory76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 retain their complete prior reads and unchanged scopes. The joint source supplies the new coordinates and full-support coupler counts.

ROOT proposed the overall scale prescription, provisional25Lambda ceiling and possible time order. This author reconstructed the actual residual background, full-support ceiling, joint commutator extension, simultaneous allocations, phase, preparation/channel contracts and counts after that exposure. This is same-model author work, not independent checking. New distinct scrutiny must cover the joint coefficient dependency, K48 projection estimates, all data incidences, energy scaling, full-output phase and boundary-state transfer before this can be promoted beyond conditional status.

Only this proposal was created. No scientific executable/sweep, delegation, source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. The frozen fixed-scale failure and isolated sources remain unchanged; this new sufficient rescaling does not contradict their stated limitations.

ROOT additionally reported related cat-sector perturbative-gadget prior art by Jordan and Farhi (arXiv:0802.1874). This report was not used as a theorem premise here and was not independently inspected for this source. No novelty claim is made for the general cat-mediated perturbative-gadget paradigm; the claim is the explicit conditional composition and its stated bounds.
