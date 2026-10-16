# Two shared graphs for one sampled Pauli pair

Status: provisional author conditional theorem. The analytic shared-graph response below is proposed with a complete finite-time proof. A paired ordinary-nearest-neighbor graph certificate is an explicit hypothesis. Its existence for every addressed pair in the supplied autonomous-preparation layout is not yet proved. No source acceptance, independent check, retained audit, full-SWAP implementation, or multi-axis composition follows from this note.

## 1. Exact target and geometry premise

Let O be the unchanged finite original qubit inventory, including every data, dirty, work, and clock factor. Clock sites x_j, 0<=j<M, are distinct from data sites c,e. Let P_c,P_e be nonidentity Hermitian Pauli operators on those two distinct sites. Let H=H0+K_X be the supplied full original Hermitian generator, including all its actual scalars, with [H,N_X]=0 and certified ||H||<=h0. In particular H need not commute with P_c, P_e, or n_j. The target is

    H_tar=H+W,       W=sum_j f_j n_j P_c P_e,       f_j real.

The admitted original domain is the full N_X=1 subspace, tensor arbitrary data and passive reference. This includes the supplied chi_k clock input but is stronger than that one prepared state. No old site moves and H is an identical summand at its original strength.

Supply a finite connected simple graph G=(V,E), |V|=m, max degree d<=6, with distinct labelled vertices a,b,a_0,...,a_(M-1). Supply two injective embeddings iota_+,iota_-:V -> Z^3 such that:

1. All 2m images are fresh sites, disjoint from O and from one another.
2. Each edge of G embeds as an ordinary lattice nearest-neighbor edge in both copies.
3. iota_±(a_j) is adjacent to the actual fixed x_j, iota_±(a) to c, and iota_±(b) to e.
4. Each labelled port therefore has graph degree at most five; all actual incidences must be certified, including any accidental adjacency to old sites. Only declared interactions are installed; absence or bounded error of other couplings is supplied.

The two embeddings need not be related by a geometric reflection. Their abstract adjacency matrices and installed coefficients are identical. This is a certificate to check, not an asserted general routing theorem. It replaces M separate cells at each data site by two ports per site. Failure to supply the certificate does not establish impossibility of a different implementation.

Use X_u,Z_u for fresh Pauli matrices, n_u=(I-Z_u)/2, and S_uv=(X_u X_v+Y_u Y_v)/2. Let r=1/12, h_d=1/4, and choose a finite positive q. For clarity units are chosen so these penalty parameters are dimensionless; q and the source amplitudes carry the same square-root-energy units if Delta is dimensional. Set

    L=sum_(epsilon=±)[ sum_(u in V) n_(u,epsilon)
                         -r sum_(uv in E) S_(u,epsilon;v,epsilon)]
          +h_d P_e (n_(b,+)-n_(b,-)),
    V_src=sum_j t_j n_j (X_(a_j,+)+X_(a_j,-))
                +q P_c (X_(a,+)-X_(a,-)).                (1)

All new nonidentity interactions are onsite or two-qubit ordinary NN under the certificate. The displayed P_e onsite fields in expanding its number operators cancel between the two copies. They may not be discarded one copy at a time.

## 2. Full auxiliary gap and one-particle inverse

For a complete two-qubit pair, -n_u-n_v <= S_uv <= n_u+n_v, including the doubly occupied state. Hence, with N_A the total fresh occupation,

    L >= (1-r d-h_d) N_A >= N_A/4.                       (2)

This inequality holds on the complete original and auxiliary Hilbert space. The only zero vectors have the full auxiliary vacuum Omega; every original vector is allowed there. With J0 appending Omega, P0=J0 J0*, Q0=I-P0,

    ker L=ran J0,      R=Q0 (L|Q0)^(-1) Q0,     ||R||<=4. (3)

Both copy occupations commute with L, as do N_X and each n_j. The full R is used throughout. With holes n^h_u=1-n_u, the same inequality applied to the hole expression shows L<=2m I: the two upper scalar contributions m+h_d P_e and m-h_d P_e sum to2m. Full occupation realizes this value. Thus ||L||=2m exactly. This upper bound also does not assume anything about the original state.

Let A_G be the ordinary real adjacency matrix and B=I-r A_G. Since ||r A_G||<=rd<=1/2,

    G0=B^(-1)=sum_(k>=0) (r A_G)^k,
    ||G0||<=2,     G0_uv>0 for all u,v in connected G.    (4)

Positivity of each entry follows from nonnegative walks and at least one finite path; no continuum or thermodynamic limit enters. Put u_v=(G0)_(v b), z=(G0)_(bb), and

    G_+=(B+h_d |b><b|)^(-1),
    G_-=(B-h_d |b><b|)^(-1).

Here h_d z<=1/2, so every denominator below is strictly positive. Direct rank-one multiplication verifies

    G_±=G0 ∓ [h_d/(1±h_d z)] u u^T,
    G_++G_-=2G0 + [2h_d^2 z/(1-h_d^2 z^2)] u u^T,
    G_+-G_-=-[2h_d/(1-h_d^2 z^2)] u u^T.              (5)

No general inverse theorem is imported: multiplying the first line by B±h_d|b><b| gives I using B u=|b> and u_b=z. When P_e has sign s, the one-particle matrix in the plus copy is B+s h_d|b><b| and in the minus copy is B-s h_d|b><b|. The sum of these inverses is independent of P_e; their difference is P_e(G_+-G_-). Resolving P_e here is legitimate because the two one-particle contractions involve only that commuting data involution. It is not a claim that H commutes with P_e.

Define exact finite constants

    alpha_j=(G_++G_-)_(a_j a_j)>0,
    beta=(G_++G_-)_(aa)>0,
    delta_j=(G_+-G_-)_(a_j a)
            =-2h_d (G0)_(a_j b)(G0)_(ba)/(1-h_d^2 z^2)<0,
    t_j=-f_j/(2q delta_j),
    s_j=t_j^2 alpha_j,        s0=q^2 beta,
    C0=s0 I+sum_j s_j n_j.                               (6)

The source coefficients can be arbitrarily large for long graph distances. No polynomial-overhead, finite common cap, or optimality claim is made. For a supplied finite graph, G0 and delta_j are computable; with rational r,h_d they are rational and delta_j is explicitly nonzero. Choosing q rational and computable f_j gives effective t_j without a sign or zero oracle. The case all f_j=0 may instead omit the whole apparatus.

## 3. Complete second-order contraction and its admitted domain

The full vacuum contraction C=J0* V_src R V_src J0 contains no cross-copy vacuum returns: a flip in one copy cannot remove an excitation in the other. Within a shared copy, all clock ports communicate through its actual inverse. Keeping all such contractions gives

    C = s0 I + sum_(j,k) t_j t_k n_j n_k
                    (G_++G_-)_(a_j a_k)
               +2q sum_j t_j delta_j n_j P_c P_e.       (7)

The unwanted term n_j P_c cancels exactly because the Pc source changes sign between copies, while the symmetric inverse is common. Clock-source squares have no Pe term because the inverse sum is independent of Pe. The Pc-source square is s0 I because Pc^2=I. This establishes the full operator identity, not just a selected data sign calculation.

On N_X=1, n_j n_k=0 for j!=k and n_j^2=n_j. Consequently

    C|_(N_X=1) = C0-W,          (H+C0)-C=H_tar.          (8)

On N_X>=2 there are additional generally nonzero clock-clock terms

    sum_(j!=k) t_j t_k n_j n_k (G_++G_-)_(a_j a_k).

They are retained in (7), not hidden in a full-domain theorem. The exact apparatus below preserves N_X, so (8) suffices on the admitted input. An implementation error that leaks N_X requires a full-space error allowance and is not certified by (8).

This is not a truncation of interacting virtual paths to one excitation. (7) only evaluates the second-order vacuum return. The global second corrector and full evolution below retain all higher auxiliary sectors.

## 4. Static generator and full-output same-time estimate

Install the actual static full-space operator

    K_Delta=Delta L+sqrt(Delta)V_src+A,
    A=(H+C0) tensor I_A,      Delta>0.                  (9)

C0 is installed. Its clock onsite terms are not part of the original K_X and are not erased as a phase; they cancel the explicitly calculated virtual shifts. H0+K_X remains unchanged as a summand.

Let J be J0 restricted to the admitted N_X=1 original domain. Set

    X1=R V_src J,        Y2=R V_src X1,
    Z=J-epsilon X1+epsilon^2 Y2,     epsilon=Delta^(-1/2).

L and R preserve auxiliary number, V_src changes it by one, and A acts only on the original factors. X1 has auxiliary number one, Y2 number two, and J*V_src Y2=0 by parity. Y2 includes actual two-particle returns within a shared graph and between the two copies; these are not replaced by products of one-particle inverses. Noncommutation of H with any data Pauli, n_j, or L is allowed.

The identities LX1=V_src J, LY2=Q0 V_src X1, and P0 V_src X1=J(C0-W) imply by direct multiplication

    K_Delta Z-Z H_tar
       =epsilon [X1 H_tar-A X1+V_src Y2]
            +epsilon^2[A Y2-Y2 H_tar].                 (10)

This exact residual keeps the original clock hopping and every H0 commutator. No transformation, cancellation, relocation, or attenuation of H is used.

For full-space bounds take

    v=2(sum_j |t_j|+q),       a=h0+s0+sum_j s_j,
    b=h0+sum_j |f_j|,         x=4v,        y=16v^2,
    F1=2x+T[(a+b)x+v y],
    F2=2y+T(a+b)y.                                         (11)

Then ||V_src||<=v, ||A||<=a, ||H_tar||<=b, ||X1||<=x, ||Y2||<=y. Finite-dimensional unitary Duhamel applied to Z exp(-itH_tar), followed by both bare endpoint differences, gives uniformly 0<=t<=T

    ||exp(-it K_Delta) J-J exp(-itH_tar)||
        <=F1/sqrt(Delta)+F2/Delta=:E_Delta.              (12)

For requested eta>0, Delta>=max(Delta_ref,(2F1/eta)^2,2F2/eta) is sufficient, where Delta_ref is any fixed positive reference choice. T=0 causes no difficulty, although the bound is not sharp there. The lift Z need not be an isometry and is not physically prepared. The physical auxiliaries start in the product vacuum and are retained as vacuum in the comparator. Both sides evolve for the same actual time t.

Tensoring any passive reference preserves (12). For every admitted mixed original/reference input and appended vacuum, the complete output trace norm error is at most min(2,2E_Delta). No original factor, clock, auxiliary, or reference is traced away. In particular the independent chi_k preparation of the autonomous source is admitted. A supplied subsequent CPTP map contracts the trace bound; normalized selected outcomes need a separate estimate.

## 5. Full scalar, positivity and resource ledger

The exact full normalized Pauli scalar is

    scalar(K_Delta)=scalar(H)+m Delta+s0+(1/2)sum_j s_j. (13)

Each of the 2m auxiliary number terms contributes Delta/2. Hopping and sources are traceless. The opposite Pe detunings have zero total scalar and cancel their Pe-only fields. The clock counterterms supply the displayed scalar even though, on N_X=1, their actual mean is sum_j s_j p_j. Scalar coefficients are not the same as prepared means.

A full-space norm bound is

    B_full=h0+s0+sum_j s_j+2m Delta+sqrt(Delta)v.        (14)

An installed reserve R_pos=h0+sqrt(Delta)v makes K_Delta+R_pos I nonnegative on every original/auxiliary sector. It adds R_pos to (13), the actual mean and B_full, not the variance; the comparison in (12) then carries the exact phase exp(-it R_pos). No positivity follows from L alone for a signed total generator. An additional full-space perturbation norm zeta requires an additional reserve zeta for this certificate.

The added graph has 2m fresh qubits, 2|E| auxiliary edges, 2M clock-source edges, two Pc-source edges and two Pe-detuning edges. Each old addressed site uses two distinct fresh nearest neighbors, independent of M. Counts are for declared supports before any vanishing term is omitted. Every auxiliary incidence is its graph degree plus its declared external port, at most six under the certificate. H's existing graph and strengths remain present. Coupling strength is not bounded merely by bounded degree.

Whole-term norm loads, before assigning global scalar reserves, are: 2sqrt(Delta)|t_j|+s_j on old clock x_j; 2sqrt(Delta)q on c; 2Delta h_d on e; and at fresh u in either copy, Delta[1+r deg_G(u)+h_d 1_(u=b)]+sqrt(Delta)[q 1_(u=a)+sum_j |t_j|1_(u=a_j)]. The scalar s0 and any reserve are assigned to one specified fresh site and fully charged there. This whole-term inventory uses n_j X_(a_j), Pc X_a and Pe n_b as the declared two-qubit blocks. Expanding into separate Pauli occurrences redistributes one-body accounting but cannot reduce an asserted cap without an explicit convention.

For any admitted initial original density rho, put A0=H+C0 and p_j=Tr(rho n_j). Orthogonal single-auxiliary flips give

    mean(K_Delta)=Tr(rho A0),
    Var(K_Delta)=Var_rho(A0)+2Delta[q^2+sum_j t_j^2 p_j]. (15)

Every H/C0 and clock/data covariance remains inside Var_rho(A0); no independence of original inputs is assumed. Small auxiliary return error does not refund these actual energy/precision resources. Equation (12) gives nonvacuum probability <=E_Delta^2, but only the coarse penalty expectation bound 2m Delta E_Delta^2, which need not vanish as Delta grows.

A joint preparation trace error eta_p adds once. A full implemented Hamiltonian error E_actual(t) adds 2 integral_0^T||E_actual(t)||dt in trace norm. For phase-sensitive terminal-time uncertainty use (B_full+R_pos)|delta t| in operator norm, or twice this in trace norm, plus the error integral over the actual interval. Sector-only calibration does not control arbitrary leakage. Appending this one-Pauli-pair simulator to a compatible existing prepared-map comparison costs at most 2E_Delta in complete output trace norm. This statement alone does not implement the whole noncommuting SWAP or compression program.

## 6. What remains to be proved for the fixed campaign geometry

The open geometric lemma is: for the literal fixed original chain, C apparatus, memory rays, and square clock of the autonomous source, and a specified addressed pair c,e, construct the two disjoint matched graphs with all labelled neighbor ports and the same finite abstract adjacency, without moving or replacing any original factor. A finite coordinate/edge list with collision, unit-distance, degree, and graph-isomorphism certificates would discharge this for a finite instance; a uniform routing proof is needed for the full symbolic family.

The analytic theorem is strictly weaker than the full local-interface target because it accepts that certificate and only one fixed Pauli pair. The missing geometry lemma concerns a combinatorial placement, not the global quantum simulation theorem restated in different words. Its remaining role and any narrower explicit placements investigated below must be distinguished from a proof for all scheduled pairs.

The paired graphs are allowed to have length and strengths growing rapidly. Existing four-auxiliary unit-cube cells do not supply this certificate. Conversely, their incidence obstruction does not rule it out. The full-SWAP/multi-axis problem additionally requires compatible simultaneous networks and a new incidence analysis; independent one-pair layouts cannot simply be superimposed at saturated old sites.

## 7. Explicit matched NN graphs for the v0 reset-pair pilot

There is a constructive positive case on the literal original layout. Choose the fixed pair

    c=v0=(0,1,1),       e=e(v0)=(0,2,1),

with arbitrary chosen nonidentity Pauli P_c,P_e. Let L_b>=8, Q=3^r>=3, n_old>=2, x_max=max(n_old-1,Q), X_*=x_max+2 and Y_*=1-L_b. Keep every original C site, memory ray, old chain, and clock site exactly as in the autonomous source. Let M be its supplied positive multiple of four, and put q_c=M/4. The clock is the square perimeter at height z=3 with lower-left corner (X_*,Y_*,3).

Take one copy of the same square perimeter at z=4 and one at z=2. Their vertices directly above/below every original x_j are the respective a_(j,+),a_(j,-), and their edges are the same cycle in the same order. Let a_(j*,±) be the lower-left corner in each cycle. Define

    a_+=(0,1,2),      b_+=(0,2,2),
    a_-=(-1,1,1),     b_-=(-1,2,1).

Thus a_± is a fresh neighbor of c, b_± a fresh neighbor of e, and a_±--b_± is an ordinary NN edge. Add a path from b_+ to the upper-cycle root with the successive integer line segments

    (0,2,2) -> (0,2,4) -> (0,Y_*-6,4)
              -> (X_*,Y_*-6,4) -> (X_*,Y_*,4),          (16)

and a path from b_- to the lower-cycle root with segments

    (-1,2,1) -> (-2,2,1) -> (-2,2,-2)
              -> (-2,Y_*-2,-2) -> (X_*,Y_*-2,-2)
              -> (X_*,Y_*-2,2) -> (X_*,Y_*,2).          (17)

Every segment is filled with its unit lattice steps, with shared endpoints counted once. Both path lengths are exactly

    ell_path=X_*+16-Y_*.

For (16), the lengths are 2, 8-Y_*, X_*, and 6. For (17), they are 1,3,4-Y_*,X_*+2,4,2. The paths have no repeated vertex, meet their own square only at the declared root, and avoid the added a leaf except at the b endpoint's edge. They therefore define identical abstract graphs: the M-cycle, one length-ell_path path attached at j*, and a single a leaf attached to b. Matching graph vertices is by cycle label and by distance along the path, not by geometric reflection.

The paths/copies avoid one another. The upper path away from b_+ has z=4, with its horizontal bridge strictly at y<Y_* and x between0 andX_*. Its initial z=2..4 segment has x=0,y=2. The lower path uses x=-2,y=2 for its initial downward leg, then z=-2, and its final upward leg has x=X_*,y=Y_*-2 and stops at z=2. Its final y approach stays below the clock square until the root. None of these intersections is an upper-copy vertex. The lower cycle has x>=X_*,y>=Y_*,z=2, so it misses the upper path's x=0 initial leg and y<Y_* bridges. The two extra leaves and b vertices are distinct from these segments and from each other.

All original nonclock sites lie in z=-1,0,1. Their full literal positions, beyond that box bound, matter for the four new data-neighbor sites and the initial lower-path vertices. The old memory with y=2,z=1 is the v0 ray at x>=0. Therefore a_-=(-1,1,1), b_-=(-1,2,1) and the downward segment x=-2,y=2 avoid it and every other ray. The original C list has only a0'=(-1,0,1), b0'=(0,0,1), and v0=(0,1,1) at z=1; these do not collide. The old chain has y=z=0. The remaining lower path is at z=-2 or at y<Y_*, and the upper path at z>=2, so they avoid all nonclock originals. The original clock is z=3 and x>=X_*,y>=Y_*; the upper initial vertical segment is at x=0 and the lower final vertical segment is at y=Y_*-2. Both avoid it. No unchanged old site is used as transit or assumed clean.

This proves the certificate of section1 for every displayed finite L_b,Q,n_old,M in the source family, for this one specified pair. There are

    m=M+ell_path+1 vertices per copy,       |E|=m,
    2m fresh auxiliaries in total.

The abstract maximum graph degree is3, attained only at the chosen cycle root. Including its original clock-source edge gives degree4. Other cycle ports have total degree3; b has degree3 including its data detuning; a has degree2 including its data source; nonport path sites have degree2. At the original x_j,c,e exactly two extra NN edges are used. The coarse general r=1/12,h_d=1/4 constants above apply unchanged; the actual degree gives a stronger gap but is not needed for the claimed estimate.

Thus sections1–5 plus this construction give a complete proposed ordinary-NN two-qubit prepared-map theorem for any real sampled program sum_j f_j n_j P_(v0)P_(e(v0)), while preserving all fixed original sites and H0+K_X. It is a single-pair pilot within the original layout, not the entire autonomous preparation program.

## 8. Preserved failure for another literal reset pair

The same construction does not extend automatically to every original data site. In the literal layout,

    v1=(-1,0,0)

has the six occupied neighbors

    q0=(0,0,0),    e(v1)=(-2,0,0),
    a0=(-1,1,0),  a1=(-1,-1,0),
    a0'=(-1,0,1), a1'=(-1,0,-1).

All are original factors whose arbitrary inputs must be retained. Hence v1 has zero fresh nearest neighbors, while the certificate in section1 needs two at each data role. Reversing Pc/Pe does not repair this incidence failure. This is an exact failure of this certificate on that pair; it does not rule out other encodings, use of occupied transit with a new proof, different global networks, or a revised admissible preparation/layout contract. In particular, it is not a general no-go for ordinary-NN autonomous implementation. The open general-layout lemma in section6 must be restricted to sites with adequate accessible vacancies, or replaced by a different mechanism.

The full multi-axis SWAP program also cannot be certified by applying the single-pair result independently three times: that spends six fresh ports per old data site, before existing neighbors, and needs a new global compatibility analysis. The two-copy pilot resolves the M-dependent incidence issue for the stated pair but leaves the axis and saturated-site issues explicit.
