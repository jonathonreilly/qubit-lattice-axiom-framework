# Exact finite receiver interface for the mediated source graph

Status: conditional author extension requiring a distinct check. The existing complete single-ray cut estimate applies unchanged, with slow hopping g, to each fixed finite mediated source. This provides a sufficient finite read-window transfer and conditional graph inventory. It selects no onset, receiver length, complete error or physical lattice realization.

## 1. Supplied graph and exact compression

Use the corrected installation d2b7b435/recheck2cea5e9a and mass-tuned family d01ed6b6. There are source endpoints s0,s1,s2 and the EXISTING background port p=(40,63,1). Three disjoint mediator paths connect s0--s1--s2--p, with 2n_l internal heads, n1=n2=2m−1,n3=m, integer m>=1. Every new source/mediator diagonal is 2j. Shared B and c_att are extended once, and no additional contacts act on these heads. The original positive j n_p cap is omitted before installing the path; the new path compression restores it exactly.

Keep the unchanged emitter-free processor, converters, input cap, cable, record gate and same-carrier slow output. Its first slow head is r0=(100,3,2), distinct from gate port o=(100,2,2). The connector o--r0 has hopping −sqrt(jg); slow bonds r_n--r_(n+1) have hopping −g, with 0<g<j. The physical compensated diagonal is 2j on every slow site. There are no installed edges from r_n, n>=1, back into the finite core. Geometric adjacency alone is not an installed coupling.

Let H_infinity be the bounded self-adjoint ONE-head operator, retaining the whole internal old/source/record fiber and any passive reference. For a finite receiver retain r0,...,r_(M−1), integer M>=1, and replace the deleted Q_g bond by the positive cap g n_(r_(M−1)). Keep all the same occupation compensation coefficients, including the first-site coefficient 2j−sqrt(jg)−g. Thus even at M=1 the missing bond's diagonal g is restored, rather than silently changing the first site's carrier.

With P_M the retained-head projection and J_M its isometric inclusion,

    H_M=P_M H_infinity P_M on ran(P_M).              (1)

The only retained-to-omitted head hopping is −g I_internal at r_(M−1)--r_M. All source-dependent self-energies are irrelevant to this exact physical identity: they are analytical eliminations, not additional installed edges or diagonal terms.

The delivered seed V occupies s0 with the supplied blank/source-vacuum and record0 registers, and arbitrary old/reference input. It lies entirely in the retained region for every m and M. The finite and infinite physical apparatus use the SAME supplied coefficients, source length and seed; only the output ray is truncated.

## 2. Weighted cut with no source-distance assumption

The checked output-only weight source58f99248/review1c72e347 is located by the inherited mapping in factored_recovery_publication/SOURCES.json at

    outputs/attached_record_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md
    outputs/attached_record_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md.

Its entire argument was refreshed. Define f=0 on every finite upstream head, including ALL mediator/source heads, the record gate, connector and r0, and f(r_n)=n on retained slow sites. The finite weight exp(a f), a>0, commutes with every fixed-head internal block. All new gamma_l,J_m,q bonds have zero weight difference regardless of length; so do the connector and every original core edge. Only slow g bonds contribute to the imaginary part of the weighted generator. Their degree is at most two, hence

    ||Im(exp(a f) H_M exp(-a f))||<=2g sinh(a).

The seed has weight one and the last head has weight exp(a(M−1)). The checked Gronwall and one-orientation Duhamel proof therefore gives the FULL evolution bound

    ||exp(-itH_infinity)V−J_M exp(-itH_M)V||
       <=D_M(t):=min{2,
           exp[-a(M−1)] [exp(2g sinh(a)|t|)−1]/[2sinh(a)]}. (2)

The cut g cancels against the integral rate 2g sinh(a). No extra factor two is needed for the adjoint cut orientation: it annihilates the decoupled retained seed. Returns from the omitted lead are retained by the full propagator in Duhamel. No selected-window, spectral-regularity, inverse, pulse or absence-of-bound-state assumption is needed for (2). In particular the loaded-interface gates are needed only for separate spectral work, not for this physical transfer lemma.

For M=1 the weight is identically one and its actual imaginary part vanishes. Formula (2) remains conservative; min{2,g|t|} is an elementary sharper bound. At t=0 the difference is exactly zero. Noncommuting B, K and all contacts remain in H; no exp(-itK) factorization of actual evolution occurs. These are whole-input operator bounds and extend with arbitrary passive references without a column aggregation factor.

For any independently supplied finite horizon t_max>=0, a=1 gives

    D_M(t)<=min{2,1.2 exp[-M+2g t_max sinh(1)]},
                                      |t|<=t_max.     (3)

Thus for any epsilon_cut>0 the integer condition

    M>=max{1, ceil(2g t_max sinh(1)+log(1.2/epsilon_cut))} (4)

is sufficient. For a read window [T,2T], replace t_max by 2T, recovering the coefficient 4gT sinh(1). This is a sufficient horizon relation, not an optimized receiver count.

## 3. Conditional read-window transfer and comparator choice

Suppose a separately checked result for THIS mediated infinite apparatus supplies, throughout some finite [T0,T1], a common normalized full-output isometry T_infinity(t) with the specified old aging, literal W, record1, all prescribed blank registers and an explicitly fixed physical packet, and

    ||exp(-itH_infinity)V−T_infinity(t)||<=epsilon_inf(t).

Then, with finite evolution embedded as in (1),

    ||J_M exp(-itH_M)V−T_infinity(t)||
                           <=epsilon_inf(t)+D_M(t). (5)

The comparator is the SAME normalized infinite physical packet; it is not truncated or renormalized to hide its tail. This also implies its outside-retained amplitude is at most the total bound, since finite actual evolution is retained. If one instead requests a normalized finite packet, its truncation and normalization need an additional explicit argument; (5) does not silently make that substitution.

The checked raw-traveling source26392923/review111aae supplies only a conditional coefficient interface. Its reference is the restricted critical packet multiplied by (-1)^m/sqrt(Z0), not a unit physical seed or the exact scalar mediated packet of a different proposal. Its full Fourier norm is sqrt(p_rho/Z0), and its incoming reference has W-star at the same physical time. Any use of that interface in the premise of (5) must still include both raw errors, source/mediator/background recovery, actual spectral identification, one global outside vector, and the physical-halfline normalization. The sign (-1)^m, original c_att and 2j carrier, fixed connector/reference-plane phase and old aging cannot be fitted away. This note neither supplies nor combines those missing time estimates.

If the separately obtained total error at a chosen read is e<1, the standard complete-isometry consequences are failure effect<=e² I, success>=1−e², and normalized successful-vector error<=e+1−sqrt(1−e²). Linear complete and subnormalized successful channels have diamond error<=2e. No such numerical consequence is asserted until epsilon_inf is supplied. A statement uniform over a finite time window concerns a chosen single read after unmeasured evolution, not repeated polling safety or finite permanent halt.

## 4. Distances and reference planes

The new local chain has 10m−1 edges between s0 and p: each mediator contributes 2n_l+1, giving 2(5m−2)+3=10m−1. This is a graph distance if the paths have no extra installed contacts. It replaces the old nominal three-edge source prefix, not merely its endpoint coupling.

For the unchanged attached background, the original source port p is new-input index20. Its distance to old input origin is20+1+40=61. The original junction gives two edges to old output origin; the old output buffer and converter give40+1 edges to v0. Thus p to v0 is104. The retained cable gives18 edges to the gate input; the gate junction gives two edges to its output port; the slow connector adds one edge to r0. Consequently

    dist(p,r0)=104+18+2+1=125,
    dist(s0,r_(M−1))=10m+M+123,
    dist(s0,r_M)=10m+M+124.                         (6)

These distances are conditional on the exact inherited installed graph and absence of new shortcuts. Internal/source-register interactions do not move the head. The gate's longer arms do not shorten its two-edge junction route. The source embedding may change Euclidean placement without changing these graph distances.

The output-only weight deliberately uses f(last)=M−1, NOT either distance in (6). No new distance offset is inserted into (2), and no old M+105 distance from the un-gated converted device is reused. A distance-based alternative would need its own appropriate full-generator bound. Here the growth of the source prefix changes resources but not the g-only cut rate.

## 5. Positive local blocks and conditional inventory

The physical new path uses Q_b=b(n_u+n_v−X_uv) on every local edge, with b in {J_m,q,gamma_l}. Each is full-space PSD with norm2b. Add occupations

    (2j−gamma1)n_s0,
    (2j−gamma1−gamma2)n_s1,
    (2j−gamma2−gamma3)n_s2,
    (j−gamma3)n_p,

and (2j−sum incident b)n_v on each internal mediator head. The sufficient inequalities J_m+q<=2j, J_m+gamma_l<=2j, gamma3<=j, gamma1+gamma2<=2j and gamma2+gamma3<=2j make every coefficient nonnegative. The small mass-tuned supplier can satisfy these; length alone does not establish them. All blocks vanish on the vacuum, so no new common scalar is added. On each new nonport head the incident block-norm sum is 2j+sum incident b<=4j. At p, the new local contribution is j+gamma3<=2j; adding its unchanged input Q_j gives head-bond/occupation sum<=4j, with any unchanged internal terms kept separately.

There are 10m−4 internal mediator heads and three source heads in addition to the EXISTING port p. The often-used phrase “10m local heads” INCLUDES p. Thus the new added set has 10m−1 heads, not10m. It replaces the old nominal three-source set. The local path has10m−1 edges and at most20m−1 listed blocks: one Q per edge and one occupation per local head including p. Zero occupations may be omitted; the listed count is an upper inventory, not a minimum.

Start from the checked nominal M-slow-site inventory: M+238 heads, M+243 total qubits, M+239 head edges and2M+281 blocks. Remove its three source heads, three local edges and SIX source blocks. Add the new local set, edges and occupations above, keeping p once. This gives

| Quantity | Mediated finite graph inventory |
|---|---:|
| Head qubits | M+10m+234 |
| Total physical qubits | M+10m+239 |
| Head-hopping edges | M+10m+235 |
| Listed positive blocks | at most 2M+20m+274 |

The five nonhead qubits are the unchanged two old, two shared-source and one record qubit; passive references are not apparatus resources. Equivalently the emitter-free inventory has M+235 heads and2M+276 blocks INCLUDING its cap j n_p. Removing that cap and adding20m−1 path blocks gives the same block formula. This cross-check prevents a double cap or duplicate port count. No original source-register hopping is relabeled a head edge. The head graph still has two independent cycles, so edges minus heads remains one. These counts include the unchanged slow terminal cap, connector compensations and all M slow-site occupations; the receiver cut adds no second cap.

## 6. Graph locality versus an actual lattice implementation

The inherited downstream apparatus has an explicit checked lattice geometry. The new mediated source currently supplies an abstract path with disjoint internal vertices and no unwanted contacts. The present inventory assumes an injective nearest-neighbor embedding of exactly that path attached at p, with no auxiliary routing heads, collisions with the old apparatus/internal qubits, or extra installed interactions. No such full new coordinate list is produced here.

One cannot retain the three old source coordinates and insert arbitrary numbers of nearest-neighbor vertices between them without checking the embedding. If an implementation requires additional routing heads, its couplings, mediator identities, path lengths, counts and possibly source family must be rederived. The formulas above are therefore conditional exact graph counts, not a certified complete physical-lattice layout. Selective installation of only prescribed edges, shared B on all added heads and the supplied coefficient correlations remain physical premises. No resource optimum or native construction follows.

A finite source length and finite receiver give a finite graph; this is not all-future storage. The transfer bound grows with horizon and does not control a fixed finite receiver for t tending to infinity. This note chooses neither m nor M nor a useful time and imports no old nominal complete-error certificate for the changed source.

## 7. Sources and author exposure

Exact loaded, corrected installation and mass-family arguments were read in full in the preceding coherent tasks and their hypotheses are retained. The new raw-traveling source and check, original output-only cut source/check, nominal source inventory and necessary gate/input geometry were refreshed for this task. The cut packet was located through the existing source manifest, not guessed from a theorem label.

- Corrected installation: d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3; recheck2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8.
- Mass tuning: d01ed6b60f3bacf2b7557687995902f8c3e172eafecd7a1547cb3bc458451883; checked family6a7a9f0dcb6ea04e5bde943e99a9ab7e04755ab0cfb26a07e6d1a4fd4e174b2e.
- Loaded inverse:5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; own checkf6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.
- Raw traveling:263929233b06c4466535452e95f3a05ecfd6ab1a1046938bbac57322c2870f97; its distinct check is pinned by exact hash in the final provenance line below.
- Output-only cut:58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf; check1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd.
- Nominal source inventory:4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006; checkede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d.
- Original converted geometry:96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7; attached gate geometryfbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457 with check7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005.

I authored the output-only weight ancestor and several recovery/scalar sources, and checked loaded and traveling ancestors. The checked weight is reused at its exact hypotheses; this new mediated specialization, distance and resource subtraction are author derivations needing a distinct check. Shared exposure is not independent ancestral recertification. Root requested this bounded transfer interface, not a new operating point. Only this proposal was written; no W/Git/PR/checkpoint/prompt/model change, numerical evolution, scientific runner, parameter sweep or delegation occurred.

Exact refreshed raw-traveling review SHA256: 111aaeff2a9839c028d2cf203c4cb5d324cca3ffcec2b0d7f127be9bc8732186.
