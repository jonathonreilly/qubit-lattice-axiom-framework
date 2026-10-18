# Product endpoint seed to a complete finite cat-preparer output

Author derivation; requires a distinct composition check. The stationary network and its cubic geometry are checked dependencies at their stated scopes. This note proves a conservative finite-window interface for that actual network. It does not attach the output cats to continuously operating mediator gadgets.

## 1. Device and statement

Use the six-stage cat-preparer and the exact cubic geometry pinned in section 10. The stages are the real Hadamard splitter, four paired writer stages, and the single-control core. All four targets A1,...,A4 are ordinary qubits. A1 is both the first writer target and the final core control. Consequently the GLOBAL operator is not diagonal in A1: throughout this proof every scattering and internal map acts on the whole 16-dimensional target space, tensored with any passive reference. Only individual local inverse calculations use their own conserved target sector.

The fixed geometry has 204 module heads, 604288 cable-interior heads and four targets. Its five equal paired cable lengths are

    20935, 40122, 60222, 80222, 100648.

Write C=604288, Lmax=100648 and D=90+sum L=302239. There are four external rays, whose origins belong to the modules; their radial indices are n=1,2,... . Retain the frozen disjoint +z continuations. Unlisted nearest-neighbor couplings are absent, as in the parent construction.

For an integer ell, truncate BOTH input rays at M=ell+1. Use ordinary Q_j bonds through n=ell and the combined positive source block

    B_gamma(ell,M)=Q_gamma+(2j-gamma)n_M+(j-gamma)n_ell,
    gamma=rho j.

Thus there are ell ordinary bonds followed by this block on each input. On BOTH output rays retain sites 1,...,ell, their ell ordinary bonds, and the positive terminal repair j n_ell. All one-head external diagonals remain 2j, including the emitters. These are fixed-diagonal cuts, not Laplacian edge deletions. The combined source has norm 3j and incident load at its neighboring lead site at most 5j. Output terminal load is 3j.

The initial state has exactly one head, at input I0,M; every other head is zero and A1...A4=0000. This is a product state of the physical qubits. A passive reference may be in an arbitrary state, including with a purification of any spectator supplies; this reference is never acted upon. No entangled ancilla or incoming packet is supplied. This is not a theorem for arbitrary initially correlated target errors.

There are exactly

    604498+4ell qubits,     604606+4ell displayed positive blocks.       (1)

The infinite geometry's 604602 blocks include cable and module blocks but no external ray blocks. Adding 2(ell+1) input blocks and 2(ell+1) output blocks proves (1). Source blocks are counted as combined blocks, not three separate summands.

The scalar vacancy contribution is

    c=8b+36(sqrt(2)-1)j.                                             (2)

Write K=H-cI in the one-head sector. There is no uniform head penalty, record bias, or target-only Hamiltonian here. The full actual finite Hamiltonian H is the displayed positive sum. Its one-head subspace is invariant, while target flips are allowed. Relative to (2), the head vacuum has energy zero for EVERY target state.

For every 0<epsilon<=1 and Lambda>0, the explicit prescription below supplies finite parameters and a positive-width interval

    3ell/(4j) <= t <= 7ell/(8j)                                     (3)

on which the complete physical state is within epsilon/8 in vector norm of

    exp(-ict) |beta_ell(t)>_F1 tensor |cat+>_(A1...A4),               (4)
    cat+=(|0000>+|1111>)/sqrt(2).

Every head outside the indicated single-head output packet is vacant, including both emitters and all internal heads. The packet and its positive normalization are specified below; no phase is fitted. The unhalved trace error is less than epsilon/4, including arbitrary passive references. The probability of the joint subspace with cat+, a head on this finite F1 ray, and all other heads vacant is greater than 1-epsilon^2/64. This is a moving output over a finite window, not permanent storage, stopping, or a receiving-gadget initialization.

## 2. Physical and envelope parameters

Set

    h=epsilon/10^6, eta^2=zeta=epsilon/10^6,
    D1=Lambda/16, D0=zeta D1, b=eta D0, j=eta^2 D0,
    rho=epsilon sqrt(h)/10^4, gamma=rho j.                          (5)

Thus j=Lambda epsilon^2/(16*10^12). These satisfy eta<=1/8, zeta<1/2, rho<=1/2 and rho^2<=h<=10^-3. The frozen local incident-load checks apply: in particular A1 has 4(D1-2b)+4j, other targets 4j, core endpoints at most 6b+4j, mediators D1+2b, writer heads at most 12j, splitter heads less than 6j and ordinary cables 4j. The new source/cap loads above are also below Lambda. The large number of sites does not increase an individual incident load.

Let F(k) be the EXACT outgoing amplitude of the checked equal-diagonal standalone emitter, with ||F||_L2(0,pi)=1. In q=k-pi/2 notation it is equivalently

    F(k)=-i sqrt(2/pi) rho sin(k) exp(ik)
                    /[(2-rho^2)cos(k)-i rho^2 sin(k)].             (6)

Use the real quintic cutoff chi: one for |q|<=h/2, zero for |q|>=3h/4, and on the transition put chi=1-10s^3+15s^4-6s^5, s=4(|q|-h/2)/h. Define

    p=||chi F||_2^2, g=chi F/sqrt(p),
    P=3rho^2/h, G0=2, G1=80/rho, G2=600/rho^3.                    (7)

The checked launch measure and narrow-cutoff derivative lemma give p>=1-P>1/2, ||F-g||_2<=2sqrt(P), ||g^(a)||_1<=Ga for a=0,1,2. The same holds for conjugate g. The cutoff is a comparison function, not a physical pulse or timed operation. Its C2 regularity and compact support are enough here. Endpoint band mass is paid, not discarded.

The exact stationary network obeys, on this band,

    ||S(k)-z^D [[0,U_b],[U_f,0]]|| <= d_s,
    delta=max(33h,13eta^2+5zeta)=33epsilon/10^6,
    d_s=49delta/(1-6delta)<epsilon/512, z=exp(ik).                  (8)

The ordered word U_f=C_A1 W4 W3 W2 W1 H sends |I0,0000> to |F1,cat+>. This word cannot be reordered, and U_b=U_f*. The denominator is positive. No target-sector sum or classical-program interpretation is used in (8).

## 3. Explicit complete stationary maps and derivative ceilings

The following deliberately loose constants are dimensionless k-derivative bounds. They are finite uniformly in (5); dependence on the fixed long cables is retained.

For each module let H_v/j be its actual relative one-head matrix, including the diagonal contribution of its attached external uniform leads. Set

    M_v=H_v/j-e(k)I-z Pi_ports, e(k)=2(1-cos k),
    L_v=-2i sin(k) M_v^-1 E_ports,
    S_v=E_ports* L_v-I.                                           (9)

These equations follow from psi_1=z psi_0+(z^-1-z)incoming. Module origins and every internal mediator/arm head are components of L_v.

Here ||M_v^-1||<=B=11 is valid for every module and every target fiber. For a writer, the checked orthogonal two-chain reduction gives inverse less than 10 on |q|<=10^-3, including both X_target sectors and the scalar + specialization. For the splitter, M=z^-1 I-V with V^2=I and V self-adjoint; its inverse is at most 2 on the band. For the core, the mediator diagonal inverse is at most eta^2/(1-3eta^2), and the mediator-endpoint coupling norm is at most 2/eta. The endpoint Schur complement is z^-1-1+V_P(E), with V_P(E) self-adjoint for real E. Its inverse has norm at most 1/sin k<=2. The block inverse consequently has norm at most

    2(1+2eta/(1-3eta^2))^2+eta^2/(1-3eta^2)<4.

This is the actual core Schur complement, not an effective low-energy replacement. Local P sectors prove the bound for the full core map; the subsequent network composition retains their noncommutativity with upstream writers.

Since ||M_v'||,||M_v''||<=3, inverse differentiation and (9) give

    ||L_v||<=2B,
    s1=6B^2+2B >= ||L_v'||,||S_v'||,
    s2=36B^3+18B^2+2B >= ||L_v''||,||S_v''||.                     (10)

Each local scattering matrix is unitary, so its zeroth bound is 1. Direct sums over stages use maxima, including the two paths of each writer stage.

For the exact network partition S_local into external/internal port blocks. Let P_c pair the 20 internal ends across their cables, with phases z^L. Then

    R=(I-P_c S_ii)^-1,
    S=S_ee+S_ei R P_c S_ie.                                     (11)

The ideal internal transition is nilpotent of order 6, so the checked feedback argument gives ||R||<=r0=6/(1-6delta). Define

    a1=Lmax+s1, a2=Lmax^2+2Lmax s1+s2,
    r1=r0^2 a1, r2=2r0^3 a1^2+r0^2 a2,
    y0=r0, y1=r1+r0 a1, y2=r2+2r1 a1+r0 a2,
    v0=1+r0, v1=y1,
    S1=s1+s1 r0+r1+r0 a1,
    S2=s2+s2 r0+2s1 r1+2s1 r0 a1+r2+2r1 a1+r0 a2.              (12)

Product differentiation in the stated order proves ||S'||<=S1, ||S''||<=S2. In particular it does not commute writer flips past core projectors. Unitarity of the full S follows by summing local flux identities and canceling paired cable flux. This uses all 16 channels at once.

Let I_in embed the I0 input port with arbitrary target fiber, and Q=z^-D S I_in. Put

    Q1=S1+D, Q2=S2+2D S1+D^2,
    H0=G0, H1=G1+Q1G0, H2=G2+2Q1G1+Q2G0.                     (13)

These bound the L1 derivative integrals of Qg of orders 0,1,2. The constant target column selected later is |0000>; (13) holds in operator norm before this specialization.

The COMPLETE internal map T, restricted to incidence through I0 but acting on every target fiber, includes all module heads (including ports) and every cable-interior head, exactly once. Its bounds are

    T0=2B v0+2sqrt(C)v0,
    T1=s1 v0+2B v1+2sqrt(C)[(Lmax+s1)v0+v1],
    J0=T0G0, J1=T1G0+T0G1.                                     (14)

To prove this, stage incoming coefficients are (x,R P_c S_ie x), with norm <=v0 and first derivative <=v1. Stage outgoing coefficients have norm <=v0 and derivative <=s1v0+v1. At a cable's interior position a the field is z^a outgoing_left+z^(L-a) outgoing_right. Each row is bounded by 2v0 and its derivative by 2[(Lmax+s1)v0+v1]; summing squares over C sites and then adding the module bound proves (14). This includes all eight writers' 192 heads, all eight core heads, all four splitter heads, and all 604288 cable-interior heads. No internal output is suppressed by calling it an apparatus spectator.

## 4. Exact normalized infinite packet

Let u=jt, f(k)=exp(iell k)g(k), and xi be any unit target/reference vector. On external sites n>=1 define

    Psi_n(t)=(2pi)^-1/2 integral exp[-itE(k)]
        [exp(-ink) I_in+exp(ink)S(k)I_in] f(k) xi dk.              (15)

Its internal vector is the same integral with the already input-restricted T(k) of (14), instead of the square bracket. E=je. The scalar c is omitted only in this relative evolution; the physical state is exp(-ict)Psi.

All stationary equations, including the cable recurrences, hold exactly, so (15) solves the bounded one-head Schrödinger equation. Boundedness here follows from a finite internal matrix and four bounded lead operators; no infinite many-head sum is being treated as bounded. Differentiating under the compact-band integral is legitimate.

The packet has EXACT norm one. In the remote past the full-integer incoming Fourier field has norm ||g||_2=1 by Parseval; its restriction to n>=1 loses a norm tending to zero by nonstationary integration. Outgoing positive-ray fields and the finite internal vector tend to zero by the same integration by parts. Thus the norm of (15) tends to one as t tends to minus infinity, and exact unitary evolution makes it one at every time. This argument neither proves nor needs asymptotic completeness or absence of localized eigenstates of the network.

## 5. Tail estimates used below

For a compact C2 vector amplitude a write b_i=||a^(i)||_1. A phase of the form ±nk+Lk-u e(k), with |phi'|>=n+g_*, g_*>=1, has |phi''|,|phi'''|<=2u. One integration by parts and sum_(n>=0)(n+g_*)^-2<=2/g_* give

    tail <= [b1+2u b0/g_*]/sqrt(pi g_*).                         (16)

Two integrations give the pointwise bound

    |integral a exp(i phi) dk|/sqrt(2pi)
    <= [b2/g_*^2+(6u b1+2u b0)/g_*^3
                       +12u^2 b0/g_*^4]/sqrt(2pi).              (17)

For example, differentiate a/phi' once, divide by phi' again and differentiate: the resulting terms are a''/(phi')^2, -3a'phi''/(phi')^3, -a phi'''/(phi')^3, and 3a(phi'')^2/(phi')^4, up to irrelevant factors of i. Boundary terms vanish. These are norm inequalities for vector amplitudes and hence remain valid with passive references.

Define

    Bin=G2+6G1+14G0,
    Bout=H2+24H1+200H0.                                         (18)

On the input-boundary sites ell,ell+1,ell+2 the incoming derivative has magnitude at least 1.9u>=u. On every external boundary coordinate n in that set, the outgoing derivative n+ell+D-u e' is at least ell/4 for u<=7ell/8. Thus (17) bounds incoming amplitude by Bin/(sqrt(2pi)u^2) and outgoing amplitude by 16Bout/(sqrt(2pi)ell^2). All four ports are treated as one vector, so no target-dimension factor appears.

## 6. Literal source comparison before contact

For the early comparison only, extend each input through its origin into an artificial negative-index chain, disconnect its actual splitter contacts, and retain the actual rest (including both finite output cuts) on the complementary head sites. Keep the origin diagonal 2j. This gives two independent reversed standalone launchers with coordinate x=ell-n, emitter M, plus a spectator rest which annihilates its head vacuum after subtraction of c. Initial targets remain 0000 on this reference trajectory. The unused input has the identical weak emitter even though it initially carries no head.

The difference between this reference and the actual extended finite operator is supported at the input origins and their immediately adjoining artificial/splitter sites. Its norm is at most 4j: the splitter's I-to-O hopping block has norm j, and the two artificial continuation edges together have norm j, so even the sum of their two Hermitian edge operators is at most 2j; 4j is a safe allowance. All origin diagonals match exactly. Large core mediator energies act only on the vacuum reference rest and do not enter the reference propagation bound. The actual and reference extensions use the same additional sites, with unused artificial chains decoupled in the actual operator.

The emitter is at graph distance M from the origin contact. The standalone reference has norm at most 4j, so Duhamel and its Taylor expansion at time t0=u0/j give

    Econtact <= 4u0 sum_(m>=M)(4u0)^m/m!
              <=4u0 exp(4u0)(4e u0/M)^M <= exp(-ell/2),           (19)

provided ell>=100u0 and u0>=1. Indeed 4u0<=.04M and log(4e/100)+.04<-2, which is stronger than needed. This comparison includes the whole physical state, not just a source expectation value.

The checked reference decomposition is exactly emitter A(t), outgoing O_t F and incoming I_t conjugate(F). Its occupied-emitter amplitude is at most 1/(rho^2 u0). Replace F by the normalized g in (7). The two spectral replacements cost at most 4sqrt(P). The unwanted incoming lead field and the part of the full-integer outgoing field lying beyond the emitter each have norm at most (G1+2G0)/sqrt(u0), by (16). After reversal, the full-integer outgoing field is precisely the incoming field in (15), with the SAME exp(iell k) factor. No emitter rephasing or selected target-dependent phase is allowed.

Compare this full-integer field to Psi(t0): its missing n<=0 incoming part and Psi's unwanted outgoing positive rays have total norm at most 2(G1+G0+H1+H0)/sqrt(ell), since ell>=100u0. The complete internal vector is at most 2(J0+J1)/ell. Hence

    Einit = exp(-ell/2)+rho^-2/u0
       +2(G1+2G0)/sqrt(u0)+4sqrt(P)
       +2(G1+G0+H1+H0)/sqrt(ell)+2(J0+J1)/ell                  (20)

bounds the full-vector difference between the actual seeded state at t0 and the exact infinite packet, in a common extended Hilbert space.

In particular, no claim is made that the ACTUAL finite or infinite network has the scalar launcher's spectral measure. It can reflect coherently into targets and have localized states. Their possible contribution from this seed is already charged by (20) and the subsequent full-vector unitary comparison; no projection onto an unproved complete scattering basis is taken.

## 7. Finite boundary propagation and late complete target

Embed the finite device in the infinite packet space by adjoining decoupled exterior half-lines with diagonal 2j. The exact difference on each input is

    (j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2),                  (21)

and on each output it is j Adj(ell,ell+1). These operators are identity on targets. They retain every diagonal, including the source's 2j diagonal and the output cap. The combined norm of (21) on its three boundary levels is at most sqrt(2)j. The output contact has norm j. Direct sum across the four rays is harmless. Applying (17), then Duhamel from t0 to t, bounds the error by

    Ecut <= 100[Bin/u0+Bout/ell],  t<=7ell/(8j).                 (22)

For detail, the norm of the three sampled levels is at most sqrt(3) times the sum of the incoming and outgoing vector ceilings in section 5. Multiplication by sqrt(2)j and dt=du/j gives coefficient sqrt(6)/sqrt(2pi)<1 on Bin/u0 and less than 14 on Bout/ell. The factor 100 safely covers these estimates and the smaller output contact. This is a time-integrated boundary proof, not a finite-speed assertion beyond its regime.

Assume ell>=100D. Throughout (3), e'>=1.9 on the support. The incoming positive-ray derivative is negative with gap at least .425ell. Its norm is at most

    dlate=2(G1+6G0)/sqrt(ell).                                  (23)

The internal phase ell k-u e has the same gap. Direct one-IBP gives

    Tlate=(3J1+11J0)/ell.                                      (24)

Now define a full-integer scalar sequence

    B_n(t)=(2pi)^-1/2 integral exp[i(n+ell+D)k-itE(k)] g(k) dk.   (25)

It has norm one by Parseval. The target packet beta_ell(t) is its restriction to 1<=n<=ell on F1, divided by its POSITIVE norm. The n<=0 tail in (25) has negative phase derivative with gap at least .425ell-D>=.4ell. The n>=ell+1 tail has positive gap at least ell/4. Applying (16) separately proves the conservative combined bound

    dF=5(G1+8G0)/sqrt(ell).                                    (26)

The omitted norm is at most dF. In particular dF<1 under section 8, so normalization is well-defined and costs at most a further dF: full-integer B differs from its normalized finite restriction by at most 2dF. This normalization does not physically postselect or discard a head.

Using (8) on the outgoing full-integer Fourier field costs at most d_s by Parseval. Its ideal output for the seed target 0000 is exactly (25) on F1 with cat+. Combining all fields gives

    Efinal <= Einit+100(Bin/u0+Bout/ell)
                    +dlate+Tlate+d_s+2dF.                     (27)

Every output head, target, emitter, cable, and module component is represented in this inequality. Multiplying both vectors by exp(-ict) restores the physical phase. For density operators and arbitrary passive references the unhalved channel/state error is at most 2Efinal; the fixed product preparation can be regarded as an isometry on the passive reference. No arbitrary unknown logical target is being reset.

## 8. Simultaneous explicit sufficient prescription

All constants in (7), (10)--(14), and (18) are evaluated first from (5). Choose

    A=1+rho^-2+G1+2G0+Bin,
    u0=(10^6 A/epsilon)^2,
    Kbig=1+G1+8G0+H1+H0+J0+J1+Bout,
    ell=ceil max{100u0,100D,(10^6 Kbig/epsilon)^2}.               (28)

Then t0 precedes (3), and all gaps, inverses, cutoff normalizations, and factorial conditions used above hold. Here is an explicit conservative allocation, collecting terms with the same denominator rather than hiding large constants:

* Spectral replacement: 4sqrt(P)=4sqrt(3)epsilon/10^4 < epsilon/1024.
* Stationary operation: d_s<epsilon/512.
* Source survival plus incoming/reference tails: rho^-2/u0+2(G1+2G0)/sqrt(u0) <= epsilon/10^12+2epsilon/10^6.
* All square-root-ell terms in (20), (23), and 2(26) together are at most 16epsilon/10^6. This uses G1+G0+H1+H0<=Kbig and G1+6G0,G1+8G0<=Kbig.
* All internal inverse-ell terms are at most 13Kbig/ell <=13epsilon/10^12, because epsilon<=1 and Kbig>=1.
* Boundary integrals are at most 100epsilon/10^12 from each of Bin/u0 and Bout/ell.
* The contact term exp(-ell/2) is less than epsilon/10^6. For example ell>=100(10^6/epsilon)^2 and exp(-x)<=1/x suffice with a much stronger margin.

The sum is below epsilon/8. These inequalities intentionally overpay terms of order epsilon^2; no asymptotic symbol is needed for existence. They also imply dF<1 and prove (1)--(4). The interval width is ell/(8j)>0. The very large fixed cable counts and derivative constants are part of this sufficient family. No useful engineering scale, optimum, or sharper epsilon exponent is claimed.

## 9. Boundaries of the result and failed shortcuts

This is standalone autonomous cat generation from an endpoint head and four ordinary zero targets, with all other heads initially blank. There are no pre-supplied entangled gadget ancillas. The displayed local blocks, exact coefficients, absence of unlisted couplings, product inputs, and common energy convention remain physical supplies.

The construction does not initialize a receiving gadget whose permanent ancilla ZZ penalties are already installed: those data energies change the channel problem. It does not supply autonomous attachment/release, storage, copying a cat, cooling, an input loader, an old literal processor, native coefficient derivation, or permanent halt. Observing a finite output window is not a timed control within the Hamiltonian, but capturing its output is a separate unresolved interface.

Two tempting shortcuts are specifically avoided. First, A1 is NOT a globally conserved program and a fixed-program packet theorem cannot be inserted here; (9)--(15) are full 16-channel operator statements with ordered feedback. Second, the actual seeded network need not have the standalone spectral measure or no point spectrum. Equation (20), followed by exact evolution and (22), is the substitute, and pays all localized seed weight without identifying it spectrally. The spectral cutoff never prepares a packet physically. Scalar repairs and finite terminal diagonals are retained explicitly.

## 10. Sources, status, and work record

N is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact dependencies, read in full in this coherent sequence and reused only at unchanged identities:

* common_product_autonomous_cat_preparer/PROPOSAL.md: d4e708583626102d5f09d6f98c56e25fadb36895fdb437d07b69c0e345ef96af. Distinct stationary review common_product_autonomous_cat_preparer_check/REVIEW.md: 1f606fc5146becf42420d36411011d2a376b121d0c44bd8a7e1dad2c5f6fd59f. Adopt actual local blocks, scalar, ordered stationary word and feedback error, not a finite theorem.
* common_product_autonomous_cat_preparer_geometry/PROPOSAL.md: 0bc68860f2cc55b7895f6f184fe464f810b3a02d4ca7c49bab153864c092125b. Scoped ROOT review common_product_autonomous_cat_preparer_geometry_check/REVIEW.md: cac4a38481c064dec912f6c1dafc1b446dbebfc39bfa7a4754c4b76d0f87fe3f. Its independent interval-intersection check covers the frozen compressed coordinates, paired lengths, entire external rays, module isometries and counts. No unchanged geometry executable was rerun here.
* common_product_writer_resolvent_sharpening/PROPOSAL.md: 22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0. Review common_product_writer_resolvent_sharpening_check/REVIEW.md: d96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5. Adopt only its actual local inverse and derivative argument; new network constants are (10)--(14).
* common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Review common_product_endpoint_launch_check/REVIEW.md: 51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1. Adopt exact scalar decomposition and measure only for the decoupled reference; its cutoff normalization is repeated here.
* common_product_narrow_cutoff_derivative/PROPOSAL.md: 550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3. Review common_product_narrow_cutoff_derivative_check/REVIEW.md: 6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4. Adopt the specified quintic G1,G2 bounds under the checked p and rho/h conditions.
* common_product_single_control_router/PROPOSAL.md: 76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, review 549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0; common_product_stage_separated_router/PROPOSAL.md: 60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182, review 8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d. Actual core matrices and the local Schur formula, already read for the stationary parent, are reused; no finite fixed-program theorem is imported.

ROOT proposed the cat-generation architecture and requested the finite interface; earlier source/cut strategies were also exposed. This is source-exposed same-model author work, not a blind or independent check. The new all-channel jets, normalization, reference contact, finite propagation, counts and simultaneous allocations need their own distinct review. Only this source file was created. Shell reads and hashing are bookkeeping; no scientific dynamics program, eigensolver, numerical fit, sweep, W/Git/canonical/checkpoint/editable-prompt/model change, publication, or delegation occurred. No retained status is assigned.
