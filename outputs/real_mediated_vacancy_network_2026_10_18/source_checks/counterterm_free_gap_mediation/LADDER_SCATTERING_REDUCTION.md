# Exact positive two-plaquette stationary phase gate

Status: new author calculation, pending distinct check. This note gives an explicit feasible stationary solution, not a finite launched/released gate. ROOT proposed investigating the ladder; the Schur reduction and coefficients below were derived algebraically without a coefficient scan. NEXT_RELEASE_DECISION.md SHA `d1e9fc151e85d3d525b06b066402dc0d4b0822aa3d7479a6e8171c260887a417` remains frozen. The physical controlled-link interface is NETWORK_VACANCY_INTERFACE.md SHA `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e`, reported checked by ROOT at its exact scope.

## Geometry, actual positive clock inventory and conventions

Use the six clocks of the decision note. Ports are L=a_-=(0,1,−1), R=b_+=(1,1,1). Other vertices are v=b_-=(1,1,−1), A=a=(0,1,0), B=b=(1,1,0), w=a_+=(0,1,1). The controlled edge A-B has one-head hopping −p, p=old X1X2=±1, with no ordinary parallel A-B hopping. Six ordinary positive exchange blocks have weights

    q1: L-v; q2: L-A; q3: v-B;
    q4: A-w; q5: B-R; q6: w-R.

An edge of weight q contributes q(n_i+n_j−sigma_i^+sigma_j^−−sigma_i^−sigma_j^+) and has full-support norm 2q. Each clock also may have a positive onsite eta_i n_i. Attach unit-weight semi-infinite leads at L and R along the disjoint rays stated in the decision note. The lead contribution to each port diagonal is 1. Lead interiors have diagonal 2 and hopping −1. All this is the compensated effective one-head comparison: its physical realization retains the separately paid repulsion, mediator and compensation blocks.

At E=2−2cos k, 0<k<pi, number the lead coordinate n=0 at its port, increasing outward. Left incidence has amplitude e^{-ikn}+r_p e^{ikn}; the right outgoing wave is t_p e^{ikn}. This convention fixes the common phase, without adding an unmentioned edge-length phase.

## General rational Schur reduction

Let d_i be the actual diagonal of H−E at vertex i:

    dL=q1+q2+1+eta_L−E, dR=q5+q6+1+eta_R−E,
    dv=q1+q3+eta_v−E, dw=q4+q6+eta_w−E,
    dA=q2+q4+eta_A−E, dB=q3+q5+eta_B−E.

Assume dv,dw are nonzero and define

    f=q1 q3/dv, h=q4 q6/dw,
    alpha=dA−q4²/dw, beta=dB−q3²/dv,
    D=alpha beta−1,
    l0=dL−q1²/dv, r0=dR−q6²/dw.

Assume D!=0. Eliminate v,w first, leaving A,B with matrix [[alpha,−p],[−p,beta]]. Their inverse is D^{-1}[[beta,p],[p,alpha]]. The final two-port H−E Schur matrix is [[ell_p,−h_p],[−h_p,rho_p]], where

    ell_p=l0−[beta q2²+2p q2 f+alpha f²]/D,
    rho_p=r0−[beta h²+2p h q5+alpha q5²]/D,
    h_p=[beta q2 h+alpha f q5+p(q2 q5+f h)]/D.    (1)

These formulas include all onsite sums from positive blocks; no diagonal has been silently flattened. The internal determinant is dv dw D, so the stated exclusions precisely justify this elimination.

Outgoing lead matching gives

    ell_p(1+r_p)−h_p t_p−(e^{-ik}+r_p e^{ik})=0,
    −h_p(1+r_p)+(rho_p−e^{ik})t_p=0.             (2)

In particular zero reflection requires

    h_p²=(ell_p−e^{-ik})(rho_p−e^{ik}).           (3)

All quantities in (1) are real at real nonsingular E. Since sin k>0, (3) implies ell_p=rho_p. Then with A_p=ell_p−cos k and y=sin k,

    h_p²=A_p²+y², t_p=h_p/(A_p−iy).             (4)

Both sector equations and their transmission ratio must be checked; equal probabilities alone do not implement a coherent old-sector gate.

## Symmetric reduction and constructive solution

Impose the explicitly allowed inversion symmetry

    q1=q6=a, q2=q5=b, q3=q4=c,
    eta_L=eta_R, eta_v=eta_w, eta_A=eta_B.

Then dv=dw=d, f=h=ac/d, alpha=beta=z, D=z²−1, l0=r0. Consequently ell_p=rho_p and

    ell_p=l0−[z(b²+f²)+2pbf]/D,
    h_p=[2zbf+p(b²+f²)]/D.                       (5)

One constructive branch sets k=pi/2, z=0, l0=0. Then D=−1, ell_p=2pbf and h_p=−p(b²+f²). Transparency (4) reduces to (b²−f²)²=1. The desired relative phase is obtained by choosing b=3f and f²=1/8, since

    (b²−f²)/(2bf)=4/3=tan theta.

Here is a complete positive realization of those constraints:

    f=1/sqrt(8), a=c=f/2, b=3f,
    eta_L=eta_R=1−5f/2,
    eta_A=eta_B=2−5f/2,
    eta_v=eta_w=2−3f/4.                            (6)

All weights and onsite coefficients are strictly positive. For example 5f/2=5/(4sqrt2)<1 since 25<32. At E=2 their actual shifted diagonals are dL=dR=f, dv=dw=f/4, dA=dB=f. Thus ac/d=f, z=f−c²/d=0, l0=f−a²/d=0. The internal determinant is −f²/16, nonzero. Every use of (1) is therefore legitimate at this energy.

Equations (5)-(6) give

    ell_p=rho_p=3p/4, h_p=−5p/4,
    r_+=r_-=0,
    t_+=−(3+4i)/5, t_-=−(3−4i)/5.                (7)

Indeed |h_p|²=25/16=(3/4)²+1. Therefore

    t_+/t_-=exp(2i theta),
    t_p=−exp(−i theta) w_p.                      (8)

The real inversion-symmetric core has the same matched transmission for incidence from the other lead. Its two-port scattering matrix is S_p=t_p X_ports at k=pi/2. The complete on-shell logical operation is consequently the literal W times the common scalar −exp(−i theta), along with swapping input/output port labels. For arbitrary coherent old inputs and passive references this statement follows from the orthogonal old-X sector decomposition; it is not a classical choice of p.

## Positive inventory and unresolved packet obligations

The core clock background uses six ordinary exchange blocks and six positive onsite blocks, q_core=12. Their actual coefficients are (6). Its sum-of-full-norm bound is

    2 sum_edges q_e +sum_vertices eta_i
       =16f+(10−23f/2)=10+9f/2.

This is a conservative full-space bound, not the one-head spectral norm. Additional finite lead bonds and endpoint/source repairs must be listed and paid. With M_I,M_O additional finite lead vertices and no such repairs yet, L=6+M_I+M_O clocks and q=12+M_I+M_O ordinary background blocks. The compensated physical inventory formula is L+3 qubits and L+4+q blocks. These counts alone do not specify a launched finite device: the finite boundary diagonal and source preparation still need a design.

The literal old K, actual mediator phase and effective mediator aging remain those of the pinned interface; (8) adds the common stationary phase −exp(−i theta). This source derives no time-independent common clock output, no normalizable stationary state, and no ready-to-use finite runtime. It has two infinite leads only as an on-shell scattering calculation; the positive physical approximation theorem applies after specifying a finite network and its norm/horizon budget.

The next decisive proof is now concrete rather than a coefficient search: derive a pole-free momentum interval about pi/2 from (1), bound the derivatives of both full scattering columns and all internal maps, and show the relative phase/profile error is small for an explicitly normalized narrow packet. At the center energy the flux velocities match because the two lead dispersions are identical; away from it, sector-dependent group delay and reflected amplitudes must be paid. Then construct an actual product endpoint-seed launch, finite cuts and an output window before return, preserving all mediator/clock/reference outputs. Existing unrelated launch or release theorems are not imported by analogy.

The compensated-network physical error remains additional to those packet errors. In the original bound it pays ||B||+r(L−2) on the complete finite network; any sharper locality estimate needs its own proof. No permanent halt, capture, reset or native supplier is established by perfect transmission at one energy.

This new exact solution was obtained by symbolic hand reduction of the symmetric equations, without a coefficient scan or scientific executable. ROOT supplied the ladder task; the source is shared-lineage author work pending distinct check. Only this note was written; frozen sources, Git, canonical/checkpoint/editable-prompt/model settings remain unchanged.
