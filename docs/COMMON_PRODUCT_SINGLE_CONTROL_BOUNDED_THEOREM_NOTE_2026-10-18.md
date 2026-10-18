# One physical program qubit with finite seeded output and record guarantees

Claim status: bounded_theorem. Conditional result with separate source-exposed analytical checks of the exact replacement and the logarithmic source policy. No retained audit or native realization is asserted.

The [parent staged record theorem](COMMON_PRODUCT_STAGE_RECORD_BOUNDED_THEOREM_NOTE_2026-10-18.md) assumes a coherent legal encoding across twelve program qubits. A single qubit at the center of the router can replace that register exactly. The new device starts directly with the ordinary program qubit; no physical encoder or fanout stage is performed. This is a reduction in a preparation premise, not just a smaller error estimate. The logical path input and blank apparatus remain supplied.

## Positive local replacement and exact identity

Keep the four endpoints I0=(0,0,0), O0=(2,0,0), I1=(2,2,0), O1=(0,2,0), the four edge-midpoint mediator heads, and every head bond and vacancy term. Straight edges join corresponding I/O labels, cross edges join opposite labels. Remove the twelve control qubits and put one program qubit P at (1,1,0). Its four nearest neighbors are precisely the mediators.

For D1>D0>2b>0 and j=b²/D0, write P_p=|p><p| on P and use the full positive two-head block Q_b(x,y)=b(n_x+n_y-a_x†a_y-a_y†a_x). Its norm is2b, including its double-occupation column. Supply the following core:

    H_new,core = sum_(e={u,v}) [Q_b(u,m_e)+Q_b(m_e,v)
                           +b(I-n_u)+b(I-n_v)+M_e]
                          +2j sum_(endpoints v)n_v,

    M_cross=[(D0-2b)P0+(D1-2b)P1]n_m,
    M_straight=[(D1-2b)P0+(D0-2b)P1]n_m.

Every listed block is positive on its full support. The four M_e blocks have norm D1-2b and share the same P. Keep the eight vacancy terms separately in the inventory. There are nine core qubits and24 listed blocks. No program free Hamiltonian is added, and P is conserved.

On either old legal program string s_p, each endpoint has one enabled and one disabled incident edge. The sum of its two old programmed occupations is therefore exactly2j n_v. Both old vacancies and all bonds remain unchanged. The mediator coefficient is D0 on the enabled matching and D1 on the other matching, exactly as in the new M_e. Expansion on every head occupation gives the same common scalar8b and the same physical Hamiltonian in each program sector. This is an occupation-operator identity, not a one-head approximation.

For the full finite head/record space K, define the mathematical isometry

    W(|p>_P tensor psi)=|s_p>_(old twelve controls) tensor psi.

The old two-string subspace is reducing, and H_old W=W H_new. Hence exp(-itH_old)W=W exp(-itH_new) for every real time, also after tensoring with any passive reference. This preserves relative program phases and arbitrary program/path/reference entanglement. W is only a comparison between two devices; it is not implemented or prepared. No identity is asserted on inconsistent old program strings. Although the algebra covers all finite head occupations and record states, the performance guarantees imported below retain their one-head and blank-record input premises.

## Geometry, counts and the shared-qubit load

Translate the core by(20,0,0) in the parent's complete record layout. The new P is at(21,1,0), adjacent to the four translated mediators and disjoint from all heads, cables, writers and rays. Its two z neighbors are unused. Retain the parent's two34-edge cables, two24-head writers coupled to one R at the origin, I rays bending into +z at x=19 and23, and F rays in +x at y=±8,z=1. All interactions are onsite or nearest neighbor. The absence of unlisted interactions is still supplied.

The complete scalar remains c=8b+2c_R, c_R=4(sqrt(2)-1)j. The finite device retains I emitters at M=ell+1 with compensated source blocks and F rays capped at ell with j n_ell. Every source/cap diagonal and all head coordinates are unchanged. The final comparator uses only F sites1,...,ell and makes every other head vacant.

Full-support incident norm sums at a core endpoint, mediator and P are respectively6b+4j, D1+2b and4(D1-2b). In particular all four blocks must be counted at P. Other loads are unchanged, with largest8j at the shared record. The conservative choice

    D1=Lambda/8, D0=zeta D1, b=eta D0,
    0<eta<=1/8, 0<zeta<1/2

puts these sums below Lambda: P<Lambda/2, mediator<9Lambda/64, endpoint<13Lambda/256, and every other sum<Lambda/128. This pays the increased load at the shared program rather than using a state-dependent expectation.

There are124 qubits and160 blocks before external-ray extensions. With the declared separate-vacancy and combined-source-block conventions, the finite totals are126+4ell qubits and164+4ell blocks. At the same ell this removes eleven qubits and four blocks from the parent; it does not change the head count.

The parent used D1=Lambda/2. At the same dimensionless ratios, the conservative new choice scales every energy coefficient by1/4, including j, gamma, all writer/source/cap terms and c. A certified old time s therefore becomes t=4s. Then tE(k)=s E_old(k), ct=c_old s and jt=j_old s. Lengths, cutoff normalization and all dimensionless packet constants remain identical. The seed and complete target both commute through W in the appropriate input/output sense; the record projector acts on the unchanged factor. Thus any separately valid parent tuple transfers exactly, with zero added error and the explicitly paid fourfold physical time. The equality is not a transfer to the historically different literal processor.

## Source policy and complete finite-horizon contract

Use0<epsilon<=1, h=eta²=zeta=epsilon/10^5 and the new D1=Lambda/8, so j=Lambda epsilon²/(8*10^10). First compute q1,q2,T0,T1 by the parent's explicit packet prescription with the separately checked local inverse B=10 and conservative constants20,800,56000. These coefficients are unchanged under the uniform energy rescaling and do not depend on rho or ell. Then set

    alpha=[4096(1+T0)]^-2,
    rho=alpha epsilon sqrt(h), gamma=rho j.

The supplied source is smaller than the parent's final-output-only choice; the stronger contract is not free of coefficient or prefactor cost. Alpha can vary with epsilon through T0; the argument below does not replace it by a constant.

Use the parent's real quintic cutoff chi, plateau h/2 and zero beyond3h/4, and the actual positive normalization

    F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho²)cot k-i rho²],
    p_chi=||chi F||², g=chi F/sqrt(p_chi).

Since alpha<=4096^-2<1/1024, rho<=epsilon sqrt(h)/1024 and omitted mass is at most3rho²/h, proving p_chi>1/2. The actual normalized logarithmic bound is

    G0=||g||_1<=4rho[1+log(2h/rho²)].

It follows from integrating the exact amplitude bound sqrt(2/pi)min{1/rho,rho/[(2-rho²)|k-pi/2|]} across its crossover and paying sqrt(p_chi). The crossover lies within h for this policy. Using sqrt(x)log(1/x)<=2/e and alpha log(1/alpha)<=2sqrt(alpha)/e for0<x,alpha<=1 gives

    G0/epsilon <=(4/sqrt(10^5))alpha sqrt(epsilon)
                        [1+log2+2log(1/alpha)+2log(1/epsilon)]
                  <20sqrt(alpha)/sqrt(10^5)
                  <1/[256(1+T0)].

This pointwise estimate remains valid with epsilon-dependent alpha. It pays the absolute internal flag and F-origin amplitude uniformly throughout transit. It improves the earlier sufficient square-root bound without discarding source phase or spectral mass.

Retain the checked localized derivative ceiling g2=600/rho³, g1=80/rho, bminus=82/rho, and recompute

    H1=g1+q1, H2=g2+2q1g1+q2,
    J0=T0, J1=T0g1+T1,
    v_min=2j cos h,
    A_i=g2+(12j/v_min)g1+4j/v_min+48j²/v_min²,
    A_o=H2+21H1+154,
    L=max{1,bminus,g1+1,H1+1,g1+7},
    Q_budget=max{1,eta^-1,rho^-2,J1+J0,A_i+A_o},
    u=10^12 max{1,(L/epsilon)²,Q_budget/epsilon},
    ell=ceil(100u), M=ell+1,
    t0=u/j, t_minus=3ell/(4j), t_plus=7ell/(8j).

All quantities precede the time/length choice. The fully checked source-policy proof repays the parent's twelve allowances with this new rho: contact, survival, launch, spectral loss, early projection, early external/internal match, finite boundary, late incoming/scattering/internal contributions and final F truncation. L/sqrt(u)<=epsilon/10^6 and Q_budget/u<=epsilon/10^12 give each allowance<epsilon/32. The initial full-vector match pays all seed components, including any localized component. The new rho and ell define a new apparatus and its target, not a claim about an unchanged old source.

Let C0=X_path, C1=I_path, and retain the ordinary program P in the controlled operation C. Define the common scalar sequence

    B_n(t)=(-i)/sqrt(2pi) integral exp(i[n+ell+57]k-itE(k))g(k) dk,
    E(k)=2j(1-cos k), B_fin=P_(1<=n<=ell)B.

Its positive normalization beta_F exists on[t_minus,t_plus]. E_seed places the program directly in P and the path head at I0,M or I1,M, with R=|0> and every other head vacant; arbitrary joint program/path/reference inputs are allowed. For this seed isometry and the complete output embedding J_F, the transferred result is

    sup_(t_minus<=t<=t_plus)
      ||exp(-itH_new)E_seed-exp(-ict)J_F[beta_F(t) tensor C tensor|1>_R]||
        <3epsilon/8.

This includes every output, residual emitter, mediator, cable/writer head, program and record, with arbitrary passive references. The actual state is not projected or normalized. The final window has relative width1/6.

On the ENTIRE finite horizon use the SAME unnormalized target V(t)=exp(-ict)J_F[B_fin(t) tensor C tensor|1>_R]. The record projector P_R1 is mathematical branch notation. The second bound is

    sup_(0<=t<=t_plus)||P_R1 exp(-itH_new)E_seed-V(t)||<epsilon/2.

The source-policy proof first establishes it for the old legal apparatus; exact intertwining and uniform energy/time rescaling transfer it to the new one. Incoming exact packet amplitude is recordblank. Complete outgoing error, internal flag amplitude T0G0, uniformly bounded F-origin omission G0, and all finite-match/tail terms are paid. Before t0 the same outgoing target is small rather than redefined to zero. The two contraction maps have unhalved subnormalized diamond discrepancy<epsilon. No division by a small early success probability is allowed. Separately, the final normalized-output result implies joint record1/retained-F probability>1-(3epsilon/8)² on the final window.

## Resource meaning and remaining physical gaps

With fixed B=10, T0 has a finite limit, so alpha has a positive finite limit even though it varies at finite epsilon. Thus rho=Theta(epsilon^(3/2)), gamma=Theta(Lambda epsilon^(7/2)), L=Theta(epsilon^-3/2) and Q_budget=Theta(epsilon^-9/2). The positive g2 term supplies the matching lower bound for this chosen budget. Consequently size and jt_plus are Theta(epsilon^(-11/2)), and physical t_plus is Theta(Lambda^-1 epsilon^(-15/2)). The uniform quarter-energy/fourfold-time conversion changes constants, not these exponents. These are sufficient chosen families, not necessary resources or practical runtimes.

The same stronger horizon-plus-output contract previously had sufficient size/time powers7/9 under the square-root-L1 source policy. The logarithmic policy improves them to11/2 and15/2 with different small coefficients and potentially large prefactors. Equal exponents to a final-output-only recipe do not imply equal actual durations. Coefficient magnitudes are not fabrication tolerances.

The removed premise is preparation of the twelve-control correlated code. A program qubit, the separate dual-rail head/path input and any input entanglement remain supplied. So do blank R and head vacancies, exact positive interactions, coefficient correlations, choice of occupation basis and absent unwanted couplings. The result does not derive a native Hamiltonian, Record/readout mechanism, autonomous blank initialization, coefficient tolerance or physical unit calibration. It supplies no permanent halt, irreversible latch, capture/reset, arbitrary-time readout, normalized rare-success guarantee or guarantee beyond t_plus. The old literal processor remains a different system.

## Evidence

The [portable source manifest](../outputs/common_product_single_control_2026_10_18/SOURCES.json) pins the complete new sources and scoped checks, with all inherited parent evidence and qualifications. The [integration record](../outputs/common_product_single_control_2026_10_18/INTEGRATION_RECORD.md) records exact identities and the transfer interface. Parent PR9710 is pinned at024901e1ae8ea8ceac0310ca3a35537220a547b8. Earlier source policies remain unchanged in its evidence bundle.

The exact replacement and the logarithmic policy are separate new claims with separately pinned sources and distinct source-exposed checks. Their composition uses the checked generic valid-tuple transfer: the source-policy theorem supplies the tuple, and the exact identity supplies its implementation in the one-control device. ROOT integration does not add independent evidence. Authors/checkers reused earlier component work; model and effort were unchanged, exposure is disclosed, and neither report count nor agreement establishes blind or model-diverse replication. New proofs are analytical; the inherited writer inverse additionally has exact finite-matrix evidence at its component scope. No retained audit status is assigned.
