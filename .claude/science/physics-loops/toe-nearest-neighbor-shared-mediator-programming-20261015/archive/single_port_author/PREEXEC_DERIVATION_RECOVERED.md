# One physical port per axis from a designed inverse and two source quadratures

Status: proposed conditional bounded theorem, source-exposed author discovery. No independent review or audit is claimed. The target is a sampled one-pair program on the admitted one-excitation clock sector, retaining every original, auxiliary and passive-reference factor over the same physical time. The construction below also supplies three disjoint NN components for the X/Y/Z sum on the actual fixed v0,e(v0) pair. It does not implement all pairs of the autonomous preparation word or resolve the saturated v1 site.

## 1. Domain, imports and the failed real-source version

Keep the literal original chain, C apparatus, all E/F memory rays and the fixed clock square of the autonomous derivation b726766403bf6f4b0080172d046cf773facad028eed538d7473417683b931bb7. Their exact source snapshots are in SOURCE_MANIFEST.json. Let H=H0+K_X, with its full scalar and certified ||H||<=h0, and [H,N_X]=0. No commutation with a data Pauli or n_j is assumed. All original inputs and passive references are arbitrary on N_X=1. Supply only fresh auxiliary product vacuum, isolation of unlisted interactions, finite coefficient access and the stated precision. No old site, state or term of H is moved, replaced, attenuated or assumed clean.

For one nonidentity Pauli P_c at c and P_e at a distinct e, the target is

    H_tar=H+sum_(j=0)^(M-1) f_j n_j P_c P_e,     f_j real.

Root exposed the unchecked matrix suggestion below. Its numerical values, and the earlier two-copy candidate, are not accepted premises: the needed identities and full-sector argument are proved here. Generic inverse-response, Schur-complement and global-residual methods are attributed to the supplied earlier mediator family. No complete novelty claim is made.

On abstract core terminals (r,a,b), put

    G=[[1,-1/960,1/8],[-1/960,1,1/8],[1/8,1/8,1]],
    D=G^(-1),       h_d=1/4,       c0=961/960.

The off-diagonal absolute row sums of G are at most1/4, so 3I/4<=G<=5I/4 and 4I/5<=D<=4I/3. Direct cofactors give

    det G=892769/921600,
    D_rr=D_aa=907200/892769,
    D_bb=921599/892769,
    D_ra=15360/892769,
    D_rb=D_ab=-115320/892769.                         (1)

For s=±1, D_s=D+s h_d|b><b|>=11I/20. Multiplying the rank-one identity verifies

    D_s^(-1)=G-[s h_d/(1+s h_d)] G|b><b|G,
    (D_s^(-1))_ra=-s/240,
    (D_s^(-1))_rr=(D_s^(-1))_aa=c0-s/240.             (2)

In particular the root cross-entry suggestion is correct, but both diagonal entries retain an odd part. A real clock source with transported amplitude x_j and a real q Pc source at a would give the desired cross term when x_j=120 f_j/q, while leaving -(x_j^2/240)n_j Pe. With general unequal f_j^2, this is not removable by an onsite clock scalar and a single onsite Pe field. This is a failure of that real-source ansatz, not a no-go for one-port mediators.

## 2. The NN one-particle matrix and full-sector positivity

We give an explicit way to implement D through a subdivided cycle, then attach a clock network only at r. Let a physical auxiliary cycle contain three distinct terminals r,a,b. Its three arcs between consecutive terminals have disjoint internal vertices. A direct length-one arc ij receives hopping coefficient D_ij. If an arc ij has k>=1 internal vertices, place the positive path matrix T_arc=I-A_path/12 on its internal vertices. Let g_arc=(T_arc^(-1))_(1k)>0. Connect i to its first vertex with coefficient1 and j to its last vertex with coefficient -D_ij/g_arc. All these couplings are real, possibly signed. Eliminating this internal path gives cross response D_ij because minus the endpoint product times g_arc is D_ij. Its diagonal shifts are retained below. For k=1, both endpoint couplings meet the same internal vertex; they remain different physical edges.

Let a connected clock transport graph have maximum degree3, matrix T_clk=I-A_clk/12, distinct clock-source vertices u_j, and a vertex u_* adjacent to the physical core r. Its physical edges and clock-source edges must all be NN. Install coupling -w between u_* and r, with w=1/12. Define

    tau=T_clk^(-1),       beta_j=w tau_(u_j,u_*)>0,
    gamma_j=tau_(u_j,u_j)>0.                           (3)

The Neumann walk expansion proves strict positivity because the graph is connected and ||A_clk/12||<=1/4. No inverse zero-test is used.

Collect every arc-internal vertex and every transport vertex into a space E, disjoint from the three core terminals. Let T be the direct sum of all their path/transport matrices, and Q the real E-by3 matrix of endpoint couplings just specified. It includes the entry -w from u_* to r. Then T>=3I/4 and the installed full one-particle matrix is

    B=[[T,Q],[Q^T,D+Q^T T^(-1)Q]].                    (4)

The lower block is an actual installation, including every diagonal compensation. On a subdivided arc ij, its off-diagonal is D_ij-D_ij=0; on a direct arc it is D_ij. Thus all remaining off-diagonal entries have declared NN edges. The apparent dense formula in (4) introduces no additional core chord. Clock elimination changes only the r diagonal. The complete finite rational matrix is fixed before Delta is chosen.

For s=±1, let B_s=B+s h_d|b><b|. Completing the block square factors B_s as

    B_s=F^* diag(T,D_s) F,
    F=[[I,T^(-1)Q],[0,I]].                            (5)

Let Qabs=sum_(u,i)|Q_ui|, and take the conservative rational certificate

    g=(11/20)/[1+(4/3)Qabs]^2 >0.                     (6)

Since ||F^(-1)||<=1+||T^(-1)Q||<=1+(4/3)Qabs, (5) gives B_s>=g I. It is not necessary that the physical matrix be diagonally dominant; signed cycle hoppings are essential to the response.

For every fresh auxiliary site v write sigma_v^+=|1><0|, n_v=sigma_v^+sigma_v^-, and S_uv=sigma_u^+sigma_v^-+sigma_v^+sigma_u^-. Install on the complete qubit Hilbert space

    L=sum_v B_vv n_v+sum_(u<v) B_uv S_uv+h_d Pe n_b.   (7)

This has the exact one-particle matrix B_s at Pe sign s. More importantly, a positive matrix inequality implies the full-qubit inequality: if B_s-gI=R^*R, then

    L_s-g sum_v n_v
      =sum_alpha (sum_v R_(alpha v) sigma_v^-)^*
                  (sum_v R_(alpha v) sigma_v^-) >=0.   (8)

This identity uses no bosonic/fermionic commutation convention, excitation truncation or free-particle approximation. It proves L>=g N_A on every auxiliary sector. L annihilates exactly all original vectors tensored with auxiliary vacuum. A sufficient complete norm is

    ell_L=sum_v B_vv+sum_(u<v)|B_uv|+h_d.             (9)

All B_vv are positive by (5), and every n_v and S_uv has norm1. Pe commutes with all auxiliaries, so resolving Pe for (8) proves a joint operator inequality even if H does not commute with Pe.

The Pe n_b term expands as (Pe-Pe Z_b)/2. Its Pe-only field is physically present; unlike the mirror construction it does not cancel against another copy. The full operator (7), its onsite compensation and the counterterm below must be installed together.

## 3. Exact response and the quadrature repair

The block inverse of (4), verified by multiplication, has core block D_s^(-1). Because the transport component connects only at r with negative coupling -w,

    (B_s^(-1))_(u_j a)=beta_j(D_s^(-1))_ra=-s beta_j/240,
    (B_s^(-1))_(u_j u_j)=gamma_j+beta_j^2(c0-s/240),
    (B_s^(-1))_aa=c0-s/240.                           (10)

Arc subdivisions affect the core diagonal compensation and full gap, but not these blocks. Off-diagonal transport entries are tau_(u_j,u_k)+beta_j beta_k(c0-s/240).

Choose a positive real q and a finite supplied Lambda with Lambda>max_j|120 f_j/q|. For effective inputs a certified strictly larger bound suffices; no maximum equality decision is needed. Set

    x_j=120 f_j/q,
    z_j=[x_j+i sqrt(Lambda^2-x_j^2)]/beta_j,
    V=q Pc X_a+sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)]. (11)

Here Y|0>=i|1>, so the created amplitude at u_j is exactly z_j. There is one fresh qubit and one physical clock edge per j. Its two Hermitian quadratures are two coefficients on that same edge, not two sites or two fresh neighbors. The combined bracket has norm |z_j|. Splitting into Pauli occurrences must charge both real coefficients when pricing separate calibration errors.

Let J0 append the auxiliary vacuum, P0=J0J0*, Q0=I-P0 and R=Q0(L|Q0)^(-1)Q0. R is the full reduced inverse, ||R||<=1/g. At second order only one auxiliary excitation is present, so (10) applies. Define

    s0=c0 q^2,
    s_j=|z_j|^2[gamma_j+c0 beta_j^2]
        =Lambda^2[gamma_j/beta_j^2+c0],
    d=(q^2+Lambda^2)/240,
    C0=s0 I+sum_j s_j n_j-d Pe.                       (12)

The full clock-space contraction is obtained by retaining every n_j n_k in the transport quadratic form, with coefficients z_j^* z_k(B_(Pe)^(-1))_(u_j,u_k), plus q^2(c0-Pe/240) and the clock/data cross term. It is Hermitian; off-diagonal clock pairs combine to twice their real parts. No cross-clock term is deleted on general clock inputs.

On the admitted N_X=1 subspace, n_j n_k=0 for j!=k. The Pc cross term is

    -[q beta_j Re(z_j)/120] n_j Pc Pe=-f_j n_j Pc Pe.

The two odd diagonal contributions are

    -q^2 Pe/240,
    -(1/240)sum_j |z_j|^2 beta_j^2 n_j Pe
        =-Lambda^2 Pe/240.                            (13)

The second equality uses both the constant transported modulus and sum_j n_j=1. Therefore, as an exact operator identity on that entire domain,

    C:=J0* V R V J0=C0-W,
    W=sum_j f_j n_j Pc Pe.                            (14)

There is no n_j Pc term, since the actual cross entry in (10) has zero even part. Both Pe shifts, including the Pc-source square, are canceled by installing the negative onsite field -d Pe in C0. It is not discarded, counted as a scalar, or presented as modification of the original H. On clock vacuum the installed field overcompensates by -Lambda^2 Pe/240, and multiple clock excitations have extra cross terms. Thus (14) is not a full-clock-domain theorem. The exact dynamics below preserve N_X; full-space error allowances handle imperfect leakage.

## 4. Complete bare-output dynamics and scalar/energy costs

Install the static full-space generator

    K_Delta=Delta L+sqrt(Delta)V+A,
    A=(H+C0) tensor I_A,      Delta>0.                (15)

Let J be J0 restricted to N_X=1 and define X1=RVJ, Y2=RVX1 and Z=J-epsilon X1+epsilon^2Y2, epsilon=Delta^(-1/2). L,R preserve total auxiliary number; V changes it by one. Hence X1 has number1, Y2 number2, and J*VY2=0 by parity. Neither Y2 nor the full interacting evolution is restricted to one particle. The identities LX1=VJ, LY2=Q0VX1 and P0VX1=J(C0-W) give by direct expansion

    K_Delta Z-Z H_tar
      =epsilon[X1 H_tar-A X1+VY2]
         +epsilon^2[A Y2-Y2 H_tar].                  (16)

Every noncommuting H0/K_X term remains in this identity. Z need not be an isometry and is not a supplied dressed preparation.

For a horizon T_fin>=0, use full-space bounds

    v=q+sum_j |z_j|,
    a=h0+s0+sum_j s_j+d,       b=h0+sum_j |f_j|,
    x=v/g,                    y=v^2/g^2,
    F1=2x+T_fin[(a+b)x+v y],
    F2=2y+T_fin(a+b)y.

Two bare endpoint differences and unitary Duhamel applied to (16) give, uniformly 0<=t<=T_fin,

    ||exp(-it K_Delta)J-J exp(-it H_tar)||
       <=F1/sqrt(Delta)+F2/Delta=:E_Delta.             (17)

Choosing Delta>=max(Delta_ref,(2F1/eta)^2,2F2/eta) suffices for any eta>0, with any fixed positive Delta_ref. The full auxiliary vacuum is retained in the comparator, and every original/passive-reference input is allowed on the admitted domain. Tensoring references preserves operator norm; complete mixed-output trace error is at most min(2,2E_Delta). No tracing, postselection, changed elapsed time or altered H is used.

The exact normalized full Pauli scalar and a complete norm bound are

    scalar(K_Delta)=scalar(H)+(Delta/2)Tr B+s0+(1/2)sum_j s_j,
    B_full=h0+s0+sum_j s_j+d+Delta ell_L+sqrt(Delta)v. (18)

The Pe counterterm is traceless, while auxiliary onsite compensation contributes through Tr B. Neither is dropped. The actual reserve

    R_pos=h0+d+sqrt(Delta)v                            (19)

makes K_Delta+R_pos I nonnegative on every original and auxiliary sector. It adds to the scalar, actual mean, full norm and comparator phase exp(-it R_pos). It does not change variance. This reserve is a sufficient price, not an optimized one.

For arbitrary admitted initial density rho, A0=H+C0 and p_j=Tr(rho n_j), orthogonal flips give

    mean(K_Delta)=Tr(rho A0),
    Var(K_Delta)=Var_rho(A0)+Delta[q^2+sum_j |z_j|^2 p_j]. (20)

All covariances remain inside Var(A0). Small auxiliary nonvacuum probability <=E_Delta^2 gives only the penalty-energy bound Delta ell_L E_Delta^2, not energetic return or reuse. The amplitudes and compensations can grow very rapidly with graph distance. There is no common-cap or efficiency theorem.

For a physical edge the clock-source load is sqrt(Delta)|z_j| in the combined-block convention, or sqrt(Delta)(|Re z_j|+|Im z_j|) when the two quadratures are charged separately. The Pc source adds sqrt(Delta)q at c, and Pe detuning plus counterterm add Delta h_d+d at e. Each fresh vertex v has load Delta[B_vv+sum_u|B_uv|+h_d 1_(v=b)], plus its source load if any. Clock onsite s_j is charged at x_j; global s0 and R_pos are assigned to a specified fresh site and charged there. H's original loads remain.

All displayed coefficients are computable from finite rational graph inverses and supplied computable f_j, with strictly positive certified denominators and the chosen positive radicand margin. If scalar/hopping/Pe/source-quadrature/counterterm coefficients have errors, sum their full operator norms; a bound zeta on the complete Hamiltonian error costs at most2 T_fin zeta in trace norm. The number of declared added coefficients per component is m+|E_B|+3M+4, counting the two clock quadratures separately, the Pc source, Pe detuning, M clock counterterms, global s0 and the Pe counterterm, before a reserve. A joint preparation trace error adds once. Terminal timing error costs at most2(B_full+R_pos)|delta t| in trace norm, together with calibration integration over the actual interval. Full-space perturbations of norm zeta require an additional reserve zeta for this positivity certificate.

## 5. Actual disjoint three-component geometry at v0,e(v0)

Set c=(0,1,1), e=(0,2,1), L_b>=8, Q_mem=3^(r_mem)>=3, n_old>=2, X_*=max(n_old-1,Q_mem)+2>=5 and Y_*=1-L_b<=-7. The original M=4q_c clock is the square perimeter at z=3 from (X_*,Y_*,3) to (X_*+q_c,Y_*+q_c,3). No additional occupied sites beyond the literal source inventory are assumed. All line segments below contain their integer unit steps. No original factor is used as transit.

Component1 uses core terminals and internal vertex

    a1=(-1,1,1), b1=(-1,2,1), r1=(-2,1,1), d1=(-2,2,1)

in the square a1--b1--d1--r1--a1. Its transport graph is the original clock square shifted to z=2, with one attached tail from u1=(-3,1,1) through

    (-3,3,1), (-3,3,-2), (-3,Y_*-4,-2),
    (X_*,Y_*-4,-2), (X_*,Y_*-4,2), (X_*,Y_*,2).

The last point is the transport-cycle root; the first is adjacent to r1. The tail has length X_*+23-Y_*. Each original clock site couples to its shifted neighbor at z=2. The four core sites use the compiler of section2; only the b1--r1 arc is subdivided.

Component2 uses

    a2=(0,1,2), b2=(0,2,2), r2=(-1,1,2), d2=(-1,2,2)

in the square a2--b2--d2--r2--a2. Its transport graph is the clock square at z=4, with tail from u2=(-1,1,3) through

    (-1,3,3), (-1,3,5), (-1,Y_*-3,5),
    (X_*,Y_*-3,5), (X_*,Y_*,5), (X_*,Y_*,4).

This tail has length X_*+15-Y_*. Its start is adjacent to r2 and its end is the transport-cycle root. Clock source ports are the shifted sites at z=4.

Component3 uses a3=(1,1,1), b3=(0,3,1). Its core cycle is the union of two internally disjoint paths from a3 to b3:

    P: (1,1,1)->(1,1,2)->(1,3,2)->(0,3,2)->(0,3,1),
    Q: (1,1,1)->(2,1,1)->(2,1,3)->(2,4,3)
                    ->(0,4,3)->(0,4,1)->(0,3,1).

Their lengths are5 and11, so this is a16-vertex cycle. Choose r3=(2,4,3). Its three terminal arcs are compiled by section2; the core vertices other than r3,a3,b3 are auxiliary subdivision sites, with their full onsite compensation charged.

The third transport cycle is the outer square perimeter at z=3 with corners

    (X_*-1,Y_*-1,3), (X_*+q_c+1,Y_*-1,3),
    (X_*+q_c+1,Y_*+q_c+1,3), (X_*-1,Y_*+q_c+1,3).

It has M+8 vertices. Clock ports are the outward NN site along each clock edge, with each original corner assigned to its outgoing edge in the traversal bottom/right/top/left. Thus bottom uses y=Y_*-1, right uses x=X_*+q_c+1, top uses y=Y_*+q_c+1, left uses x=X_*-1. These M source ports are distinct and none is an outer-cycle corner. Attach a tail from u3=(3,4,3), adjacent to r3, through

    (3,Y_*-2,3), (X_*-1,Y_*-2,3), (X_*-1,Y_*-1,3).

Its length is X_*+3-Y_* and its end is the outer-cycle lower-left corner, which is not a clock-source port.

These three geometries are disjoint and fresh for all stated parameters. The core1 sites have z=1,x=-1 or-2,y=1 or2; negative-x old memory rays at x<=-2 have transverse (y,z) in {(0,0),(1,0),(0,1),(-1,0),(0,-1)}, so none meets them. No old memory occupies x=-1. The only old C sites at z=1 are (-1,0,1),(0,0,1),(0,1,1), so core1 is also disjoint from C. Core2 is at z=2. Core3's z=1 vertices lie at y=1 with x=1 or2, or y=3 or4 with x=0; the source's only positive-x memory at z=1 has y=0 or2, and no original nonclock site has y>=3. Its remaining sites have z=2 or3 and x<=2, outside both clock and other cores. Core3's listed z=2 points have x=1,2 or y>=3, while core2 has x=-1,0,y=1,2.

The component1 tail leaves through x=-3,y>=1,z=1, then descends at y=3 to z=-2, below all original sites; its final ascent is at y=Y_*-4, below both original box and every transport cycle, and stops at z=2. The component2 tail leaves at x=-1,z=3 to y=3, then uses z=5 until its final descent to z=4. These differ from the finite core3 coordinates and from each other. The component3 tail has x=3,z=3 until y=Y_*-2, then stays below its outer cycle until the root. Its transport cycle has x>=X_*-1>=4 and y>=Y_*-1; the other transport cycles lie at z=2 and4. The first two tails' portions near those x ranges are at z=-2 or5 or outside their cycles' lower y bounds. Thus no tail meets another graph. Each tail meets its own cycle exactly once. Original clock sites have z=3, x>=X_*, y>=Y_*; the new outer cycle is exterior and every new z=3 tail/core portion is either at x<=3 or y<Y_*. This excludes original-clock collisions. Unlisted nearest-neighbor interactions remain excluded or charged by the isolation premise, including adjacency between different components.

Each transport graph has maximum degree3. Its root is either a clock-source vertex (components1,2) or not a source (component3); fresh total degree is at most4. Each core terminal has two core-cycle edges and at most one external edge: r to transport, a to c, or b to e. At c the three used fresh neighbors are (-1,1,1),(0,1,2),(1,1,1), exactly its three available neighbors in the literal inventory. At e the used neighbors are (-1,2,1),(0,2,2),(0,3,1). At every clock site the used fresh neighbors are below, above and outward; together with its two old clock bonds this gives degree5. One component per axis therefore fits without sharing an auxiliary or spending a second port for a quadrature.

The fresh qubit counts are

    m1=M+X_*+27-Y_*,
    m2=M+X_*+19-Y_*,
    m3=M+X_*+27-Y_*,
    m_total=3M+3X_*+73-3Y_*.

Each component is a core cycle and a transport cycle joined by one edge; tails are part of the transport graph. Therefore |E_B,i|=m_i+1. Counts exclude the clock/data source and detuning edges, which are priced separately above.

## 6. Simultaneous X/Y/Z response with one global inverse

Take three components of section5, with Pc_i=X_c,Y_c,Z_c and Pe_i=X_e,Y_e,Z_e, supplied real f_(ij), positive q_i and Lambda_i>max_j|120 f_(ij)/q_i|. Each has its own computed B_i, beta_(ij), gamma_(ij), z_(ij), L_i,V_i,s0_i,s_(ij),d_i. Put

    L=sum_i L_i, V=sum_i V_i,
    S0=sum_i s0_i, S_j=sum_i s_(ij), Dsum=sum_i d_i,
    C0=S0 I+sum_j S_j n_j-sum_i d_i Pe_i,
    H_tar=H+sum_(i,j) f_(ij)n_j Pc_i Pe_i.             (21)

The L_i generally do not commute, since their Pe_i act on the same e. Nevertheless L_i>=g_i N_i is an operator inequality; summing gives L>=g_min N_total, with the entire original-space vacuum kernel and full reduced inverse norm at most1/g_min. Every individual auxiliary component number N_i commutes with every L_k. On a sector with only component i excited, every other L_k vanishes on the original space because its auxiliaries are vacuum. Hence the restriction of the global inverse is exactly that component's inverse. A source in another component cannot remove its excitation, so cross-component second-order vacuum contractions vanish. Adding (14) therefore gives C=C0-(H_tar-H) on N_X=1 without diagonalizing the three Pe_i simultaneously.

The second corrector Y2=RVRVJ retains actual sectors with two distinct components excited; their inverse is the inverse of the sum, not the sum/product of separate inverses. The global residual (16) is proved with this R exactly as before. Use

    g=g_min, ell_L=sum_i ell_L,i,
    v=sum_i[q_i+sum_j|z_(ij)|],
    a=h0+S0+sum_j S_j+Dsum,
    b=h0+sum_(i,j)|f_(ij)|

in (17). The full scalar is scalar(H)+(Delta/2)sum_i Tr B_i+S0+(1/2)sum_j S_j. The reserve h0+Dsum+sqrt(Delta)v makes the complete operator nonnegative. The initial variance is Var_rho(H+C0)+Delta sum_i[q_i^2+sum_j|z_(ij)|^2 p_j]. All original/auxiliary/reference outputs and the entire physical interval are retained. Noncommutation of the Pe-only counterterms with H or with each other is already included in A and the residual.

Consequently this proposed theorem covers the X/Y/Z sampled sum on the one fixed accessible pair. A scalar sampled identity coefficient can be included directly as an original-clock onsite term in the supplied target and installed generator, with its norm, scalar, mean and timing cost added. This gives a conditional local implementation of a sampled SWAP logarithm for this pair when its three Pauli and scalar coefficients are supplied. It does not synthesize the whole preparation waveform, apply three axes to every scheduled pair, or make the v1 neighbor obstruction disappear.

## 7. Preserved limits and next check

Real one-quadrature sources fail for arbitrary f_j through the explicit n_j Pe shift. Omitting the Pe counterterm fails even after fixing the transported modulus: both -q^2 Pe/240 and -Lambda^2 Pe/240 are present. Replacing the signed designed core by a generic positive-hopping graph does not preserve the zero even cross entry. Deleting charged root/subdivision diagonal shifts changes the core inverse. Applying the one-excitation contraction on all clock sectors fails. Independent per-axis one-particle inverses do not replace the mixed full-sector inverse in the dynamics.

All six neighbors of v1=(-1,0,0) remain original occupied factors q0,e(v1),a0,a1,a0',a1'. The present construction uses fresh ports and offers no implementation there. This is an explicit limitation of this construction, not a no-go for other mechanisms. Additional occupied sites, common strength caps, efficient resource scaling, physical initialization and control manufacture remain outside the result. The axis theorem is conditional finite-Hamiltonian mathematics, not derived native physics or retained status.

The planned single exact fixture will check literal three-component placement, independent direct one-particle inversions, source-square/cross response and mutations. It will not form the full many-qubit matrix, check arbitrary-H dynamics numerically, establish a symbolic-family theorem from a sample, or confer independent scientific acceptance. Complete source/plan/execution identities and actual failures will be preserved separately.
