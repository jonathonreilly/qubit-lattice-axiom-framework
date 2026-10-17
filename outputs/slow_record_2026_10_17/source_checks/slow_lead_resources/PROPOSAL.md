# Slow output: exact physical inventory and conditional finite compression

Status: authored resource/compression application requiring a distinct selective check. For M>=1 NEW slow sites beyond the retained gate output port, the proposed finite apparatus has M+236 head qubits, M+241 total physical qubits, M+237 head edges, and 2M+277 positive blocks in the explicit unmerged decomposition below. No modified-device mass, capture onset, runtime, or output-error theorem is inferred.

## Sources and exposure

Fully read root's `../same_carrier_slow_lead/PROPOSAL.md`, SHA256 a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4, and its distinct check `../same_carrier_slow_lead_check/REVIEW.md`, ecec86951cdb2f36011e196fe8266bffec29f55a6d0ec8f67e4bfe5684a578fb. The candidate g=1e-6 and illustrative T/M were exposed; this is not independent origin. My preceding triage is `../passive_capture_next_move/PROPOSAL.md`, 595538459b174aa793eb71b07eb57d8476464d4aeed8f72f7663d8798aca0f97.

Refreshed complete attachment `../record_attached_kernel/PROPOSAL.md`, fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457 (distinct check 7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005), and original inventory `../bandcenter_resources/PROPOSAL.md`, 96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7 (check 01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd). Read the complete weighted proof `../output_lead_weight/PROPOSAL.md`, previously pinned 58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf, with distinct check 1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd. The proof is reproduced below for this changed edge strength and indexing, not accepted from a status label.

Unchanged local instructions/workflow are reused. I authored the attachment and triage and reviewed some dependencies; this application is not an independent review of my own construction. No scientific execution, numerical sweep, dynamics simulation, delegation, W/Git/publication, model, or prompt edit occurred. Only source reads, bookkeeping and this deliverable were performed.

## 1. Geometry, exact cap, and M=1

Retain the 194 original nonoutput heads, eighteen cable heads v_n=(82+n,1,1), 0<=n<=17, and all 24 gate heads including p=(100,1,1) and o=(100,2,2). The shared record remains R=(108,1,1). Add M NEW receiver sites

    r_m=(100,3+m,2), m=0,...,M-1.

Thus o and r_0 are distinct adjacent sites; neither is counted twice. The ray is disjoint from the rest of the checked geometry. Retain its selective installed-pair premise, including uninstalled incidental geometric neighbors.

Let 0<g<j, tau_s=sqrt(jg). This tau_s is the NEW slow connector, not the old converter tau_c=sqrt(j J S0). Use Q(-tau_s) between o and r_0, M-1 Q(-g) receiver bonds, and occupations

    (j-tau_s)n_o,
    (2j-tau_s-g)n_r0,
    2(j-g)n_rm for 1<=m<=M-1,
    g n_r(M-1)  [finite cap].

These coefficients are all positive. Q(-a)=a(n_x+n_y)-a(exchange) is fullspace PSD with norm2a. The occupations are one-qubit PSD blocks. The gate output diagonal remains its previous 2j because its removed j bond diagonal is replaced by tau_s+(j-tau_s). For M>=2 the first receiver diagonal is tau_s+g+(2j-tau_s-g)=2j; each interior diagonal is 2g+2(j-g)=2j; the final diagonal is g+g+2(j-g)=2j.

For M=1 there is NO internal slow edge and NO later-site occupation. The unique receiver diagonal is tau_s+(2j-tau_s-g)+g=2j. The first-site occupation and cap remain two separate installed blocks at this same site, each counted once. This special case is not obtained by adding a second interior occupation.

The infinite version has the same local terms and an infinite g ray without a cap. Compress its one-head operator to the retained sites, leaving every internal coordinate intact. The omitted Q(-g) bond compresses to g n_last, exactly the stated cap. Therefore H_M=P H_infinity P. The unique off-diagonal cut is -g times the full internal identity, including for M=1. This is exact compression, not an absorbing end.

## 2. Complete counts in the chosen decomposition

Head sites: 90 original arm +82 old-port +21 new-input +1 emitter +18 retained output cable +24 gate +M slow = M+236. Add four original old/source qubits and one shared record: M+241 physical qubits. Passive references are not apparatus qubits and the shared B is not replicated at each head site.

Head-bond blocks, one per head edge:

| Installed family | Number |
|---|---:|
| Ordinary old-J bonds (87 nonfilter arm, 80 old-port) | 167 |
| Original filter bond | 1 |
| Original junction square bonds | 4 |
| Original converter bonds, hopping tau_c | 2 |
| New-j input-stub bonds | 20 |
| Structured emitter bond j(n_e+n_end)-kappa(exchange) | 1 |
| Retained cable internal bonds | 17 |
| Cable-to-gate-input bond | 1 |
| Record-gate internal bonds, including its phase cells and square | 24 |
| Gate-output-to-first-slow bond, hopping tau_s | 1 |
| Slow internal bonds | M-1 |
| **Head-bond total** | **M+237** |

The source A--B edge is in B, not a head edge. The head graph is connected and E-V+1=2, agreeing with the original and record-gate cycles.

All other positive blocks:

| Installed family | Number |
|---|---:|
| Shared B: K, Delta_A n_A, Delta_B n_B, Q_AB(-h), u_AB n_A n_B, g_A n_A(I+X_1), g_B n_B(I+X_2) | 7 |
| Original source/head contacts and their onsite/vacancy partners, four per arm | 8 |
| Original entrance J occupations | 2 |
| Original filter beta vacancies | 2 |
| Original junction gamma_J vacancies | 4 |
| Original converter gamma_c vacancies | 4 |
| Emitter j n_e | 1 |
| Record-gate phase-cell occupations | 4 |
| Record-gate junction vacancies | 4 |
| Record terminal contacts j n_T(I+X_R) | 2 |
| New gate-output compensation (j-tau_s)n_o | 1 |
| First slow-site occupation | 1 |
| Later slow-site occupations | M-1 |
| Terminal slow cap | 1 |
| **Non-head-bond total** | **M+40** |

Total positive blocks are therefore (M+237)+(M+40)=2M+277. For M=1 these specialize to237 heads,242 physical qubits,238 head edges and279 blocks. Merging occupations at a site would change the block count but not the Hamiltonian; no such merging is used here. Compared to the attached j-output inventory with its output-count parameter set to M+1, there are M+1 additional occupations (old port plus every new slow site); the cap is replaced, not duplicated.

## 3. Scalar, loads, and supplied coefficients

There are no new vacancy terms. The physical scalar remains exactly

    c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)-1)j.

Here gamma_c=tau_c-j belongs to the two ORIGINAL converters. The new tau_s introduces no gamma_c or extra scalar. The same shared B contains literal K; the target must retain exp(-it c_att), exp(-itK) and literal W. No time-dependent switch or drive is installed.

Slow hopping is not a small full Hamiltonian. Receiver one-head diagonal remains2j, and the full internal B and upstream contacts remain present. In the given decomposition, incident physical-block norm sums on new sites are

    first slow site, M>=2: 2j+tau_s+g;
    first/only slow site, M=1: 2j+tau_s;
    later interior: 2j+2g;
    later final: 2j+g.

At o, its two gate-square edges contribute2sqrt(2)j, its existing junction vacancy contributes(sqrt(2)-1)j, and the new connector plus compensation contribute2tau_s+j-tau_s. Total:3sqrt(2)j+tau_s. No phase-cell or record contact occurs at o. All other gate and source loads are unchanged; in particular the inherited shared-source incident sums27.936224853155858 and22.228906875353305 remain. A global local-load bound by g,2g, or2j would be false.

At the proposed exact nominal g=1e-6, tau_s=sqrt(j*1e-6) is correlated with the already supplied j. The compensation occupations must implement the displayed same-carrier values, including their correlations. This proposal provides no manufacturing tolerance, bit-precision budget, native coefficient generator, physical-unit assignment, or robustness theorem. A changed coefficient perturbs the matching and may accumulate phase over a long hold; exact nominal supply is not eliminated by slower transport. The seed is still supplied emitter occupied, every other head blank, shared source vacuum, record0, with arbitrary old input and passive reference. Native seed preparation, native Record identification, autonomous reset/reuse, and an irreversible latch remain outside this application.

## 4. Weighted finite/infinite comparison on the actual modified graph

On the retained one-head Hilbert space define f=0 on every upstream/gate site and r_0, and f(r_m)=m. Let W_a=exp(a f) tensor I_internal, a>0. For the seed embedding V, W_a V=V. The tau_s edge has ZERO weight difference; all upstream/contact terms also commute with this weight. Only internal receiver edges of strength g have nonzero difference, equal to +/-1.

For H_a=W_a H_M W_a^-1, every onsite block stays self-adjoint, and the block row/column bound gives

    ||Im H_a|| <=2g sinh(a).

This statement concerns the imaginary part after weighting, not ||H_a|| or a norm bound on the infinite many-head Hamiltonian. It preserves every internal coordinate, both record sectors and arbitrary old/reference input. Gronwall gives

    ||P_last exp(-is H_M)V||
       <=exp[-a(M-1)+2g sinh(a)|s|].

On the common infinite one-head space, decouple the cut into H_M direct-sum the omitted compression. Duhamel involves only one cut orientation on the decoupled evolved seed, with norm g times its last-site amplitude. Thus for all real t,

    ||exp(-it H_infinity)V-embed exp(-it H_M)V||
      <=min{2, exp[-a(M-1)]
             [exp(2g sinh(a)|t|)-1]/[2 sinh(a)]}.       (1)

The factor g cancels on integration; there is no extra factor2 for the reverse edge. Full infinite unitarity in the Duhamel identity includes return paths and all spectral types. At M=1 the actual weighted imaginary part is zero, giving the sharper min{2,g|t|}; (1) remains valid. At t=0 the integral expression vanishes.

For a=1, any supplied T>=0 and 0<=t<=2T, e/(2sinh1)<1.2 yields

    error <=min{2,1.2 exp[-M+4g T sinh1]}.             (2)

A sufficient integer count for tolerance epsilon_tr is

    M>=max{1,4g T sinh1+log(1.2/epsilon_tr)}

with the right side rounded upward. These are exact conditional resource inequalities for this Hamiltonian. If a separately proved slow-infinite complete-map error is epsilon_infinity(t), its same comparator bounds the finite embedded map by epsilon_infinity(t)+(1). The identical addition works after a fixed record projection by contractivity. One must not replace the complete comparator by a truncated normalized finite packet without paying that change separately. All target scalar phases and old aging remain unchanged. Passive-reference tensoring preserves these operator bounds.

## 5. Conditional illustration, not a runtime result

For g=1e-6, illustrative T=1e15 and M=5e9, sinh1<1.2 gives

    -M+4gT sinh1 < -5e9+4.8e9=-2e8,
    finite transfer <1.2 exp(-2e8)<1e-6

through the absolute horizon2e15 from seed preparation. This does NOT establish capture by T, an actual slow-device infinite error, or any finite holding interval with high success. The whole capture-plus-hold period must fit inside this absolute horizon if one is subsequently proved. At this illustrative count the apparatus has5,000,000,236 head qubits,5,000,000,241 physical qubits,5,000,000,237 head edges and10,000,000,277 positive blocks in the stated decomposition.

The leading propagation coefficient is4g rather than4j, but this alone establishes no equal-error/equal-onset resource ratio between devices. Storage length remains proportional to the certified horizon at fixed g; finite recurrence and reciprocal returns remain possible beyond it. The unresolved science is the modified gate/source load, actual seed measure, correct slow-momentum output phase/Jacobian and numerical capture/complete-output window. None of the previous j-output runtime, .0045 all-time bound or asymptotic error is imported here.
