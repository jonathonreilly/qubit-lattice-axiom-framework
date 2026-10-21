# A finite autonomous cat preparer from product endpoint inputs

Claim type: bounded_theorem.
Primary runner: `scripts/common_product_device_controls_2026_10_18.py`.

Claim status: bounded_theorem. Conditional analytical result with distinct source-exposed stationary and finite-composition checks, and a separately checked cubic geometry. No retained audit, native realization or physical preparation of an operating mediator gadget is asserted.

A static network of supplied positive nearest-neighbor qubit blocks can turn one occupied endpoint and four zero target qubits into a four-qubit cat state with one common outgoing head packet. Every other head, including the source, is vacant in the complete comparison state. The guarantee holds throughout a specified positive-width finite window, with no supplied entangled ancilla and no timed Hamiltonian change.

The nearest canonical primitive is the [single-control router theorem](COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md), together with its staged writer ancestry. The present construction uses those local scattering primitives in a new network and proves its finite input/output comparison separately. It does not depend mathematically on the later pair-cat selector theorem. In particular, no selector ground state, cooling operation or pre-existing cat is a premise.

## Device, product input and complete output

The network has six stages: a real Hadamard splitter, four pairs of writer modules, and a single-control router. In writer stage a, path 1 flips target A_a; path 0 uses the scalar + specialization of the same writer. That specialization replaces the target contact j n_T(I+X_A) by 2j n_T and requires no dummy qubit in a supplied |+> state. The final router is controlled by A1, the target flipped at the first writer. Its ideal action is C_0=X_path and C_1=I_path.

With W_a=|0><0|_path tensor I+|1><1|_path tensor X_Aa, the ordered ideal word is

    U_f=C_A1 W4 W3 W2 W1 H_path,
    U_f |0,0000> = |1> tensor (|0000>+|1111>)/sqrt(2).             (1)

A1 is not conserved by the complete network. The proof therefore uses operator-valued scattering on all sixteen target channels; it never treats A1 as a classical fixed program. All targets have zero free Hamiltonian when the head is absent. Adding receiving-gadget target energies would change this problem.

The splitter is a four-head square with signed exchange magnitudes j/sqrt(2). Positive vacancy repairs of strength (sqrt(2)-1)j give its exact Hadamard scattering and contribute a scalar. The eight writers have 24 heads each. The router has eight heads and uses A1 as its sole physical control. All listed blocks are positive on their full qubit supports, including double occupation. The scalar + writer and signed hopping blocks remain within the explicitly supplied primitive class.

The frozen cubic layout makes the shared A1 adjacent to its two writer terminals and four router mediators on six distinct nearest neighbors. Its five paired cable lengths are

    (20935, 40122, 60222, 80222, 100648).                          (2)

Module heads total 204 and cable-interior heads total 604288. The four external rays have disjoint infinite +z continuations, with n=0 origins already counted among module heads. The geometry check covers module isometries, all 82 compressed cable segments, equal paired lengths, the shared-target contacts and entire external rays. Unlisted interactions, including geometrically adjacent but unconnected sites, are absent by premise.

Truncate each input at M=ell+1. Both inputs, including the initially unused I1, have the identical positive weak-source block

    B_gamma=Q_gamma(ell,M)+(2j-gamma)n_M+(j-gamma)n_ell,
    Q_a(x,y)=a(n_x+n_y-a_x†a_y-a_y†a_x).                         (3)

Use ordinary Q_j bonds from the input origin through ell. Truncate both output rays at ell and add j n_ell at each end. These repairs keep every external one-head diagonal at 2j. The combined block (3) has full norm 3j; it is counted once. The finite device has exactly

    604498+4ell qubits,       604606+4ell positive blocks.         (4)

Initially the head at I0,M is occupied, every other head is zero, and A1...A4=0000. This is a product over physical qubits. Any passive reference or spectator state is retained identically; the theorem does not reset arbitrary unknown target states. The supplied exact coefficients, interaction supports, absent extra couplings, occupation basis and product inputs remain assumptions.

For every 0<epsilon<=1 and Lambda>0, the prescription below defines a static device satisfying the incident full-support norm cap Lambda. Throughout

    t_minus=3ell/(4j) <= t <= t_plus=7ell/(8j),                   (5)

its complete state differs in vector norm by less than epsilon/8 from

    exp(-ict) |beta_ell(t)>_F1 tensor |cat+>_A,
    c=8b+36(sqrt(2)-1)j.                                        (6)

Here all heads outside the single-head packet on F1 are vacant, including both emitters and every internal head. Thus the unhalved complete-output trace error is less than epsilon/4, also after adjoining arbitrary passive references. The joint probability of cat+, a head on the retained F1 ray and all other heads vacant exceeds 1-epsilon^2/64. These claims concern the actual unprojected state; no successful outcome is normalized operationally.

## Actual parameters and common packet

Set

    h=epsilon/10^6, eta^2=zeta=epsilon/10^6,
    D1=Lambda/16, D0=zeta D1, b=eta D0, j=eta^2 D0,
    rho=epsilon sqrt(h)/10^4, gamma=rho j.                       (7)

Thus j=Lambda epsilon^2/(16*10^12). Shared A1 carries all four router controls and both writer terminals, with load 4(D1-2b)+4j; it is not charged in only one program sector. Other core endpoint and mediator loads are at most 6b+4j and D1+2b. Writer heads have load at most 12j, splitter heads less than 6j, ordinary cables 4j, source-adjacent sites 5j and output ends 3j. These all lie below Lambda under (7), independently of the number of sites.

Let E(k)=2j(1-cos k), z=exp(ik), and D=90+sum L=302239. The exact standalone source amplitude is

    F(k)=-i sqrt(2/pi) rho sin(k)exp(ik)
                    /[(2-rho^2)cos(k)-i rho^2 sin(k)].            (8)

It has L2(0,pi) norm one. Use a real quintic cutoff chi equal to one for |k-pi/2|<=h/2 and zero for |k-pi/2|>=3h/4. In each transition its value is 1-10s^3+15s^4-6s^5 with s=4(|k-pi/2|-h/2)/h. Define

    p=||chi F||_2^2, g=chi F/sqrt(p),
    P=3rho^2/h, G0=2, G1=80/rho, G2=600/rho^3.                  (9)

The checked source measure and localized derivative estimates give p>=1-P>1/2, ||F-g||_2<=2sqrt(P), and ||g^(a)||_1<=Ga for a=0,1,2. The cutoff specifies a comparison function, not a physically prepared pulse.

The scalar sequence determining the complete target is

    B_n(t)=(2pi)^(-1/2) integral_0^pi
                exp(i[n+ell+D]k-itE(k))g(k) dk.                 (10)

Its full-integer norm is one. Restrict it to 1<=n<=ell on F1 and divide by that restriction's positive norm to obtain beta_ell(t). This norm is proved nonzero throughout (5). Both the exp(ik) in F and the full exponent D are retained. The four constant writer factors (-i) multiply to one; no additional fitted phase or relative branch correction occurs in (10). The scalar exp(-ict) in (6) is part of the physical comparison.

## A constructive sufficient length and time

The following constants make the large resource allowance explicit. They are evaluated before choosing ell and are not physical controls. Put C=604288, Lmax=100648, B=11 and

    delta=33epsilon/10^6,
    s1=6B^2+2B, s2=36B^3+18B^2+2B,
    a1=Lmax+s1, a2=Lmax^2+2Lmax*s1+s2,
    r0=6/(1-6delta), r1=r0^2 a1,
    r2=2r0^3 a1^2+r0^2 a2,
    v0=1+r0, v1=r1+r0 a1,
    S1=s1+s1 r0+r1+r0 a1,
    S2=s2+s2 r0+2s1 r1+2s1 r0 a1+r2+2r1 a1+r0 a2,
    Q1=S1+D, Q2=S2+2D S1+D^2,
    H0=G0, H1=G1+Q1G0, H2=G2+2Q1G1+Q2G0,
    T0=2Bv0+2sqrt(C)v0,
    T1=s1v0+2Bv1+2sqrt(C)[(Lmax+s1)v0+v1],
    J0=T0G0, J1=T1G0+T0G1,
    Bin=G2+6G1+14G0, Bout=H2+24H1+200H0.                       (11)

Choose

    A=1+rho^-2+G1+2G0+Bin,
    u0=(10^6 A/epsilon)^2,
    Kbig=1+G1+8G0+H1+H0+J0+J1+Bout,
    ell=ceil max{100u0,100D,(10^6 Kbig/epsilon)^2}.              (12)

This is a noncircular, deliberately conservative prescription. The internal geometry and its scattering derivatives do not grow when ell is increased. The physical time is t_plus=7ell/(8j); the interval width is ell/(8j). The fixed internal geometry already contains over six hundred thousand heads, before the very large external-ray allowance (12). No practical duration, optimized exponent or fabrication tolerance is claimed. Coefficient magnitude is not coefficient precision.

## Why stationary scattering transfers to this product seed

Let H_v be a module's relative one-head matrix, including the attached-lead diagonal, and E_ports the inclusion of its port coordinates. Each module has the exact boundary matrix

    M_v=H_v/j-2(1-cos k)I-z Pi_ports,
    L_v=-2i sin(k)M_v^-1 E_ports,
    S_v=E_ports* L_v-I.                                        (13)

The actual writer inverse is less than 10 on the band by its checked two-chain calculation. The splitter inverse is at most 2. The core Schur complement gives an inverse below 4, including its mediator components. Thus B=11 safely bounds every local inverse on every target fiber. Since ||M_v'|| and ||M_v''|| are at most 3, inverse differentiation yields s1,s2 in (11).

Let P_c connect the twenty internal port ends with phases z^L. The full ordered feedback is

    S=S_ee+S_ei(I-P_c S_ii)^(-1)P_c S_ie.                       (14)

The ideal internal transition is nilpotent of order six. Local error delta therefore gives inverse norm at most r0 and

    ||S-z^D [[0,U_f*],[U_f,0]]||
                  <=d_s=49delta/(1-6delta)<epsilon/512.         (15)

This uses full target operators, not a global A1 decomposition. Flux cancellation on the paired cables proves unitarity of the complete scattering matrix. Differentiating (14) in its actual multiplication order gives S1,S2. Demodulation by z^-D gives Q1,Q2. Reconstructing both traveling waves on each cable and every module head gives T0,T1; all 604492 internal heads, including port origins, are represented once.

An exact infinite packet is obtained with incident envelope exp(iell k)g(k): on external n>=1 its integrand is

    exp(-itE)[exp(-ink)I_in+exp(ink)S I_in]exp(iell k)g,

and on internal heads it is the corresponding complete map T. These stationary columns solve the actual one-head Schrödinger equation. In the remote past the incoming full-line Fourier field has norm one, while the outgoing and internal fields vanish in norm by integration by parts. Conservation of norm therefore proves that the complete packet has norm one at every time. No asymptotic completeness theorem or absence of bound states is assumed.

For the early source comparison, disconnect the splitter input contacts and continue both input rays through their origins into artificial negative-index chains. Keep every origin diagonal 2j. The reference consists of two exact standalone launchers and a head-vacant rest. Relative to c, the rest annihilates head vacuum for every target fiber, so large mediator energies do not enter the reference trajectory. The actual/reference contact difference is bounded by 4j and lies M=ell+1 steps from the source. At t0=u0/j its complete-vector Duhamel bound is

    4u0 sum_(m>=M)(4u0)^m/m! <= exp(-ell/2).                    (16)

Artificial coordinates are comparison space, not extra physical apparatus. The exact reference state is the occupied-source amplitude plus O_t F+I_t conjugate(F). Its source residual is at most 1/(rho^2u0). Reversal x=ell-n produces exactly the incident exp(iell k) factor. Cutoff loss, unwanted incoming tails and the early internal packet are all charged. This compares full vectors before contact; it does not assign the reference's scalar spectral measure to the actual network. Any localized seed component is already paid by that comparison.

The remaining finite/infinite difference preserves every diagonal. On each input it is

    (j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2),

and on each output it is j Adj(ell,ell+1). Two integrations by parts give the time-integrated error 100(Bin/u0+Bout/ell) through t_plus. This pays source reabsorption, unused-input reflections and output returns in the stated interval. A Laplacian edge deletion would not be this operator.

For transparency, the complete error bound used before (12) is

    Einit=exp(-ell/2)+rho^-2/u0+2(G1+2G0)/sqrt(u0)+4sqrt(P)
         +2(G1+G0+H1+H0)/sqrt(ell)+2(J0+J1)/ell,
    Efinal<=Einit+100(Bin/u0+Bout/ell)+d_s
         +2(G1+6G0)/sqrt(ell)+(3J1+11J0)/ell
         +10(G1+8G0)/sqrt(ell).                                (17)

The final line includes the entire late incoming/internal field and both omitted tails of (10), with its positive normalization cost. The phase gaps are at least .425ell for late incoming/internal fields, .4ell for the nonpositive output tail, and ell/4 at the far output boundary. Equation (12) satisfies all required gaps.

The spectral term is less than epsilon/1024 and stationary scattering less than epsilon/512. Source survival and source tails contribute at most epsilon/10^12+2epsilon/10^6; all inverse-square-root-length terms at most 16epsilon/10^6; internal inverse-length terms at most 13epsilon/10^12; the two boundary terms at most 100epsilon/10^12 each; and contact less than epsilon/10^6. Their sum is below epsilon/8. This proves the complete guarantee rather than merely a final target marginal.

## Scope and evidence

The result removes the supplied-cat premise for this standalone generator. It does not prepare the cats of a continuously coupled operating gadget. A permanent receiving H0, data coupler or target bias changes the scattering channels; autonomous attachment and release have not been constructed. Capture, storage, reset, cooling, an unknown-input loader, native interaction identification and indefinite halt also remain outside the result. The ordinary product inputs and exact positive Hamiltonian are supplied. The optional signed-splitter cat-minus extension is not used in this finite theorem.

## Current source bindings and bounded validation

The complete mathematical sources remain live at the paths below. Their embedded historical author, pending-review and acceptance language records provenance and supplies no present verdict. Current claims require the stated premises and full proofs; finite checks neither establish general estimates by sampling nor promote native interactions or audit status. The original manuscript and all original packet versions are recoverable from `archive/common_product_devices_review_2026_10_18/MANIFEST.json`.

- `outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_finite_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_geometry_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_signs_PROPOSAL.md`

The shared primary computes finite ordered algebra, selector spectra, complete logical words, local physical blocks, exact scalar propagation, source normalization, literal geometry and sufficient-policy allocations. It does not construct the enormous prescribed apparatus or replace the analytical packet, derivative and tail estimates. Complete literal source closure and inherited version pins are in `outputs/common_product_devices_review_2026_10_18/INPUT_CLOSURE.json`.
