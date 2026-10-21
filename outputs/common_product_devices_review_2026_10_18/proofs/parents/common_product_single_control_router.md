# One physical program qubit for the supplied finite router

New bounded author derivation requiring a distinct check. Replace the twelve legal program controls of the four-cell matching router by one ordinary qubit at its unused square center. The proposed positive local Hamiltonian is exactly intertwined with the old Hamiltonian restricted to its two legal program strings, on the full finite head/record Hilbert space. No physical encoder is performed. The finite endpoint-seed and record contracts consequently transfer with all outputs and phases retained. A conservative load-cap choice scales all energies down by four and physical times up by four; it does not preserve the old absolute runtime.

This removes one supplied correlated-program preparation requirement in an engineered Hamiltonian. It does not derive a native interaction, coefficient supplier, input-state preparation, Record/readout mechanism or permanent halt. The derivation was prompted by ROOT's preparation-gap assessment and the author's central-site observation; source and design exposure are recorded below.

## 1. Actual local positive core

Use the endpoint positions and edge labels of core60bc:

    I0=(0,0,0), O0=(2,0,0),
    I1=(2,2,0), O1=(0,2,0).

Straight edges are (I0,O0),(I1,O1); cross edges are (I0,O1),(I1,O0). Each edge e has its distinct midpoint head m_e. Write V for the four endpoint sites, E for the four edges, and P for a NEW physical program qubit at(1,1,0). No old program qubit is retained. To avoid confusion, the comparison isometry below is called W, not V.

Let P_p=|p><p| on P, n_x=|1><1| on each head, and a_x=|0><1|. Supply b>0,D1>D0>2b, j=b²/D0, and the full positive head block

    Q_b(x,y)=b[n_x+n_y-a_x^dagger a_y-a_y^dagger a_x].

It has norm2b and gives double-occupation energy2b; that column is not deleted. Define mediator blocks

    M_e=[(D0-2b)P0+(D1-2b)P1]n_m_e,  e cross,
    M_e=[(D1-2b)P0+(D0-2b)P1]n_m_e,  e straight. (1)

The proposed physical core is

    H_core,new = sum_(e={u,v}) [Q_b(u,m_e)+Q_b(m_e,v)
                                      +b(I-n_u)+b(I-n_v)+M_e]
                       +2j sum_(v in V) n_v.                 (2)

Every displayed block is positive on its full one-/two-qubit support. Each M_e has full norm D1-2b; the reversed labels do not change that norm. Each fixed endpoint occupation has norm2j. All four M_e share the same physical P. Their head factors are distinct, and they conserve P, as does the rest of (2). No free Hamiltonian on P is included. Head number is conserved.

Keep the eight vacancy terms separate in the inventory, including the two identical terms incident to each endpoint. This convention gives eight Q_b blocks, eight vacancies, four M_e blocks and four fixed endpoint occupations:24 positive blocks. There are eight core heads plus P, hence9 core qubits. Combining identical vacancies is permissible but would be a different listed-block convention; it is not used in the counts below.

Expand the Q_b diagonals and vacancies without restricting head number. Each edge contributes the true scalar2b, and cancels its endpoint b n terms. Each mediator receives2b n from its two Q_b bonds, completed to D_e(p)n by (1). Thus in program sector p,

    H_core,new,p =8b I+2j sum_(v in V)n_v
                    +sum_e D_e(p)n_m_e
                    -b sum_(e={u,v})[X_h,u m_e+X_h,m_e v],   (3)

where X_h,xy=a_x^dagger a_y+a_y^dagger a_x. D_e(0)=D0 on cross edges and D1 on straight edges, and D_e(1) reverses them. Equation (3) is a full occupation-operator identity, including vacuum and all simultaneous head occupations. No one-particle approximation or fermionic identification enters it.

## 2. Geometry, shared-control load and record attachment

The four mediators are(1,0,0),(2,1,0),(1,2,0),(0,1,0), exactly four distinct unit neighbors of P. Their two endpoint contacts and new control contact are nearest-neighbor bonds. Endpoint fixed occupations and vacancies are onsite. Endpoints now have two inward mediator bonds and one external lead/cable bond, while each mediator has its two endpoint neighbors and P. P uses four of its six available cubic neighbors. No nonlocal identification of old controls has occurred.

For the checked record geometryc913 translate this entire core by(20,0,0). P is at(21,1,0). Keep unchanged both34-edge cables, both24-head writers and their single shared R=(0,0,0). Keep the input rays I0->(19,0,0)->(19,0,1)->... and I1->(23,2,0)->(23,2,1)->..., and final rays from(1,+/-8,1) in +x. P is distinct from all these sites and all core heads. Its four neighbors are precisely the four mediators; its +/-z neighbors are unused. The removed controls were at z=+/-1 above/below endpoints or mediators, not at P. Original cable vertices have x=20 or22 near the core, or y=-10 or12 farther away; none is P. The existing collision-free ray/cable arguments therefore remain applicable after deleting controls and adding this one center site. Unlisted interactions remain absent by supplied installation, not by an inferred property of adjacency.

Full-support incident norm sums, including one external j bond at each endpoint, are

    endpoint: 4b+2b+2j+2j =6b+4j,
    mediator: 4b+(D1-2b)=D1+2b,
    program P: 4(D1-2b).                                    (4)

The program load counts all four blocks, not only the smaller coefficients on a selected branch. For comparison the old endpoint load was6b+6j, because its two independently supported endpoint-program blocks each had norm2j. The new identity on the legal subspace does not require equality of old and new full-space block-norm sums.

Other incident sums remain those ofc913 and finite728: shared R has8j, ordinary arms/cables/rays4j, phase endpoints(4+sqrt(2))j, junctions(1+3sqrt(2))j, source emitter3j, source-adjacent5j and F cap3j. None exceeds8j. There is one physical R and one distinct physical P, with no contact between them. All record dependence remains in the original terminal blocks j n_T(I+X_R).

For Lambda>0 choose

    D1=Lambda/8, D0=zeta D1, b=eta D0,
    0<eta<=1/8, 0<zeta<1/2.                                (5)

Then D0>2b, b<Lambda/128 and j<Lambda/1024. Equation (4) gives program load<Lambda/2, mediator load<9Lambda/64, endpoint load<13Lambda/256, and all other listed loads<Lambda/128. Hence every incident sum is below Lambda. The margin is conservative and no optimal scaling is claimed.

The exact physical scalar remains8b for the bare core and

    c_new=8b+2c_R, c_R=4(sqrt(2)-1)j                         (6)

with the two writers. Fixed endpoint occupations, source blocks and terminal caps introduce no extra scalar. In particular there is no p-dependent vacuum phase.

## 3. Exact comparison with the old twelve-bit device

Let H_old denote the finite positive network at the SAME parameters and with precisely the same heads, rays, emitters, caps, writers and record, but with the old twelve controls and original cell blocks739e99. For each p let s_p be its legal control string: all three bits of an active cell are0 and all three bits of an inactive cell are1. Thus each endpoint belongs to one active and one inactive cell.

On the full finite head/record Hilbert space K define

    W: C²_P tensor K -> (C²)^(tensor12) tensor K,
    W(|p> tensor psi)=|s_p> tensor psi.                     (7)

It is an isometry, whose range is the old legal-program subspace. It is not an onto unitary on the old full Hilbert space and makes no claim about inconsistent old program strings. No physical use of W, additional register or preparation of s_p is required in the new device.

Every old control occupation is conserved, so the range of W is reducing for H_old. On its p column, old edge e has exactly D_e(p) at its mediator. At every endpoint the two original programmed terms sum to

    2j[(1-q_e(p))+(1-q_f(p))]n_v=2j n_v,                  (8)

because q_e(p)+q_f(p)=1. All original bonds and both original vacancy terms at that endpoint are retained unchanged. Consequently (3) is also the exact old legal-sector core operator, without any restriction on head number. Every remaining apparatus block acts as identity on old/new program factors and identically on K. It follows that

    H_old W = W H_new.                                    (9)

This includes arbitrary record states and all occupations of the finite head sites, not just recordblank or one-head vectors. Bounded finite-dimensional functional calculus gives, for every real t,

    exp(-itH_old) W = W exp(-itH_new).                     (10)

Tensoring W with the identity on any passive reference preserves these identities and norms. Coherent alpha|0>+beta|1> programs are covered by linearity with their relative phases intact; this is not an averaging of two classical programs. The equal scalar in(3) is essential for that statement.

The all-head identity is finite-device algebra. Infinite auxiliary scattering leads, when used to import packet estimates, are considered only in the bounded one-head Hilbert space with finite internal/program/record fiber. No unbounded infinite sum over arbitrary many-head configurations is asserted by (9).

## 4. Direct physical seed and complete comparison targets

Let D=C²_program tensor C²_path tensor H_ref be the abstract input space. The new seed isometry E_new places the program factor directly in the physical P, puts the one path head at I0,M or I1,M, supplies R in|0>, and makes every other head vacant. It permits arbitrary joint program/path/reference input xi. For product computational input, the unused apparatus is literally a product of vacant heads and recordblank. Entanglement already in xi is supplied, not generated as a claim about blank apparatus.

With the same abstract input labeling the old encoded seed satisfies

    E_old=W E_new.                                        (11)

Define the controlled path action C=sum_p |p><p| tensor C_p with C0=X_path,C1=I_path. Let J_new,F put the path head on the two final rays, retain P and reference, and set every other head vacant. The output target keeps the physical program qubit; it does not erase it. The old target uses the old legal control string instead, so J_old,F=W J_new,F on this input/radial/record domain.

For any normalized scalar radial vector beta(t) and common scalar phase, isometry of W and (10)--(11) give the exact equality of error norms

    ||exp(-itH_new)E_new
         -exp(-ict)J_new,F[beta(t) tensor C tensor|1>_R]||
     =||exp(-itH_old)E_old
         -exp(-ict)J_old,F[beta(t) tensor C tensor|1>_R]||.  (12)

All outputs are included. No actual output is projected or traced away in (12); unused heads, emitters, mediator/writer/cable coordinates and erroneous record output remain charged on both sides. Equality also holds for arbitrary passive-reference extensions. Thus this replacement adds ZERO approximation error to any valid old complete-output bound at the same parameters/time. It does not itself establish a dynamics bound for arbitrary many-head inputs; that stronger input domain belongs to (9), while the imported performance theorem remains a one-head theorem.

## 5. Fixed cap requires changed physical time

Let barred quantities be any of the specified old finite recipes with bar D1=Lambda/2, fixed eta,zeta,rho,h, fixed valid writer inverse ceiling, and selected ell,u0. Rescale EVERY energy coefficient by1/4:

    D1=bar D1/4, D0=bar D0/4, b=bar b/4,
    j=bar j/4, gamma=bar gamma/4, c=bar c/4.                (13)

This respects j=b²/D0 and scales all head bonds, vacancies, endpoint occupations, programmed detunings, writer contacts and source/cap terms consistently. The old encoded Hamiltonian at these parameters is exactly bar H_old/4. Combining with (9), for new physical time t=4s,

    exp(-itH_new) = W^* exp(-is bar H_old) W.              (14)

The restriction to range W in this identity is automatic because it is reducing; W^* is only a comparison operation. No compression of a time-dependent physical evolution is implemented.

The band energy becomes E(k)=bar E(k)/4 and velocities become bar v/4. Hence tE(k)=s bar E(k), tv=s bar v, jt=bar j s and ct=bar c s. The common Fourier sequence is exactly

    B_n,new(t)=(-i)/sqrt(2pi) integral
                exp(i[n+ell+57]k-itE(k))g(k)dk
             =B_n,old(s).                                (15)

Both the -i phase and the shift57 are retained, as is exp(-ict). The actual positive cutoff mass and g depend on rho and h only and are unchanged. So are all dimensionless scattering, k-derivative and internal amplitude ceilings: the mediator factors b/(D-E) and jb/(D-E)², writer matrices divided by j, and all feedback factors are invariant under (13). In particular T0 used to choose the flag-policy rho does not change. This gives a direct algebraic check on dimensionless budget reuse, in addition to the exact evolution identity.

Lengths and seed locations remain ell,M=ell+1; matching and observation times become

    t0=4 bar t0=u0/j,
    t_minus=4 bar t_minus=3ell/(4j),
    t_plus=4 bar t_plus=7ell/(8j).                         (16)

The relative window width remains1/6. There is no physical switch at any of these comparison times. Claiming the old absolute duration at the new cap choice would be false: (14) pays an explicit factor4.

## 6. One explicit checked-parent finite/flag prescription

For a concrete instantiation use the unchanged finite728 and absolute-flag e7b prescriptions, with their completed distinct reviews60896 and e548. No later resource improvement is needed as a premise of this replacement. Choose0<epsilon<=1 and

    h=eta²=zeta=epsilon/10^5, D1=Lambda/8,
    D0=zeta D1, b=eta D0, j=Lambda epsilon²/(8*10^10).

For finite output alone take rho=epsilon sqrt(h)/1024 and the finite parent's valid fixed writer bound. For the additional all-horizon absolute branch select its checked B=10 and conservative local constants20,800,56000, recompute q1,q2,T0,T1 as specified in e7b and packet3477, then choose

    rho=min{epsilon sqrt(h)/1024,
                    [epsilon/(4096(1+T0))]^2}, gamma=rho j.

Use the same real quintic cutoff and positive normalization g=chi F/sqrt(p_chi), with

    F=-i sqrt(2/pi)rho exp(ik)/[(2-rho²)cot k-i rho²].

The parent's explicit inequalities give p_chi>1/2. For either selected policy keep its conservative constants

    g1=80/rho, g2=1200/(h rho³), bminus=82/rho,
    H1=g1+q1, H2=g2+2q1g1+q2,
    J0=T0, J1=T0g1+T1,
    A_i=g2+(12j/v_min)g1+(4j/v_min+48j²/v_min²),
    A_o=H2+21H1+154,
    K=max{1,eta^-1,rho^-2,bminus,g1+1,H1+1,J1+J0,A_i+A_o,g1+7},
    u0=(10^6 K/epsilon)^2, ell=ceil(100u0), M=ell+1.

Here v_min=2j cos h. Every formula is unchanged dimensionlessly by (13). The twelve parent allowances remain respectively

    K/u0, 2K/u0, 2K/sqrt(u0), 4sqrt(3)epsilon/1024,
    8K/sqrt(u0), 4K/sqrt(ell), 3K/ell, 2K/u0,
    6K/sqrt(ell), epsilon/256, 56K/ell, 28K/sqrt(ell).

They correspond in order to actual/reference contact, source survival, incoming launch, spectral loss, right early projection, early lead match, early internal match, finite boundary, late incoming, scattering, late internal and final F truncation. Each is below epsilon/32 by the checked parent derivation. This replacement changes none of them: the contact ratio b/j, scaled time integrals and boundary velocities retain the same dimensionless values. Intermediate normalization conditions remain satisfied before defining beta_F as the positive normalization of B_new on1<=n<=ell.

Consequently (12)--(16) transfer the complete finite-output operator bound<3epsilon/8 throughout the new final window. It includes both emitter vacancies, all other apparatus heads vacant in the comparator, R=1 and the original ordinary input program qubit retained coherently. The unhalved output-channel ceiling is<3epsilon/4, with arbitrary passive references.

For the absolute-flag policy let P_R1 be the mathematical projection onto record1 on all outputs. It commutes through W: P_old,R1 W=W P_new,R1. Use the SAME unnormalized target at every horizon time,

    V_new(t)=exp(-ict) J_new,F[
                    P_(1<=n<=ell) B_new(t) tensor C tensor|1>_R].

Equations (14)--(15) and the parent's branch theorem therefore give

    sup_(0<=t<=t_plus)||P_R1 exp(-itH_new)E_new-V_new(t)||
                    <epsilon/2.                           (17)

The corresponding subnormalized unhalved channel discrepancy is<epsilon. No time-dependent target redefinition or normalized rare-success inference is introduced. The separate complete final-output theorem gives record1 probability, and joint record1/F-support probability, greater than1-(3epsilon/8)² throughout the final window. These are mathematical projector probabilities, not a supplied physical measurement procedure.

Any other valid old finite recipe admits the same exact transport through (12)--(16), but its premises, constants and status must be retained. No unchecked newer exponent is adopted here. At fixed dimensionless recipe this construction has unchanged ell and dimensionless duration, physical time multiplied by4 and every energy magnitude divided by4. It removes correlated control preparation rather than establishing a faster algorithm or an optimal resource family.

## 7. Full inventories and exact limits

The finite internal record network before external-ray extensions now contains9 core qubits+48 writer heads+one R+66 cable-interior heads=124 qubits. Its blocks are24 core+68 writer+68 cable=160. Two I extensions contribute2(ell+1) sites/blocks, and two F extensions contribute2ell sites and2ell+2 blocks. Therefore the actual finite device has

    126+4ell qubits, 164+4ell positive blocks.              (18)

These are exactly eleven fewer qubits and four fewer listed blocks than the old137+4ell and168+4ell counts at the SAME ell. Both old endpoints of every cable and all external origins were already counted. Source blocks retain their combined-block convention and vacancies retain their separate repeated convention. The full head inventory itself does not change; only the program register is reduced.

The input program is now a single ordinary physical qubit; the path input remains an independently supplied one-head encoding across two emitters, possibly entangled with that program and a passive reference. Arbitrary logical inputs are not claimed to be tensor products among themselves. What is removed is preparation of the redundant twelve-control legal string/superposition. The remaining apparatus heads are vacant and R blank as previously supplied. There is no physical fanout, encoder clock, timelike preparation stage or new prepared incident wavepacket.

Positivity, cubic locality and exact intertwining are statements about the displayed installed Hamiltonian. They do not select an occupation basis from a native theory, produce the exact coefficients, suppress unwanted bonds dynamically, prepare blanks or supply a measurement/readout. The one input program qubit is not identified as a native framework Record merely by being conserved. Program updates during operation, perturbation tolerance and arbitrary unknown environments are not included.

The finite-time record branch has the parent's absolute meaning only. Returning heads can alter the flag after the certified horizon. No capture, reset, irreversible completion, permanent finite halt, old literal processor transfer or native Hamiltonian derivation follows. In particular the exact equivalence here relates the NEW one-control device to the OLD LEGAL SECTOR OF THIS ROUTER, not to the historically distinct literal processor.

## 8. Exact sources, exposure and required check

All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Fully read the following core premises in the immediately preceding assessment, preserving their exact hashes:

- mediated_common_product_program/PROPOSAL.md:739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088.
- common_product_stage_separated_router/PROPOSAL.md:60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182.
- common_product_stage_record_core/PROPOSAL.md:c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729; full distinct review61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1 was also read completely.

For the new finite-interface transfer, fully reread:

- common_product_stage_record_finite_seed/PROPOSAL.md:7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995.
- common_product_stage_record_finite_seed_check/REVIEW.md:60896f1b1b4b76d27158ce46e097565d1ed777d45ee4dc1c394b02d52ac71a9f.
- common_product_stage_record_flag_branch/PROPOSAL.md:e7b53eeda3fc7df96986d3b55f68d9e5af4f1b6657ba068b6f33d03e18a37ee0.
- common_product_stage_record_flag_branch_check/REVIEW.md:e548a664449546f76fbad2b24d5c7bcf5e0d318ecb6dd75f4234fb078ccdae5a.

Their packet347719/check17029, writer sharpening22bca/checkd96ed and scalar launch/derivative premises are reused at the exact scopes/pins recorded by those fully read sources and earlier coherent work. No unproved change in their derivative estimates is needed. Their completed checks do not independently check the new central-control construction.

The initiating assessment is next_physical_supply_opportunities/ASSESSMENT.md,d1c58b809dd37ff1e784f271eb2ded3df3644209879a0beca36a8c167d62ac59. ROOT requested preparation-supply alternatives; the author noticed endpoint cancellation and the common unused center during exact-source rereads. ROOT then requested this separate derivation and highlighted whole-space identity, load, scaling and counts. This is source-exposed continuation by an author of several parent components, not independent or blind review.

A distinct check should reconstruct (1)--(10) for all finite head occupations, inspect the center against the final translated geometry, verify the full-support program load and every count, and challenge the transfer of physical phase, normalized targets, flag projection and fourfold times. A success would remove the correlated-program preparation premise within this supplied architecture; it would not confer native or retained status.

Only common_product_single_control_router/PROPOSAL.md was created for this separate derivation. The frozen assessment and all parent sources remain unchanged. No scientific executable, numerical solver/simulation/sweep, W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. Verification is author algebra and file/hash bookkeeping; distinct review is pending.
