# Fixed occupations and positive exchange blocks for mediator precision

Status: new conditional exact operator interface, requiring distinct checking. The earlier positive hopping identity extends to every bond of the finite mediator graph. It removes hopping-dependent occupation tracking in that implementation, while introducing a finite, actual-coefficient-dependent global scalar. It does not remove independent diagonal accuracy, effective-ratio precision, loaded-source or preparation obligations, nor supply a native Hamiltonian or full-time robustness theorem.

## Exposure and exact sources

I read the complete earlier positive hopping proposal and its check, and refreshed the corrected stationary installation and the precision proposal at these exact identities:

| Source | SHA256 |
|---|---|
| three_site_positive_hopping_reexpression/PROPOSAL.md | 9fa50cd2da480d59765aa5fbd7c556728a08ac4c385234dc055c26220b93a5d4 |
| three_site_positive_hopping_reexpression_check/REVIEW.md | 1e9630995e29cea591048983768658b0421b6b5658d3ac7bbbe0fa6dd034b956 |
| mediated_critical_source_interface/PROPOSAL.md | d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3 |
| mediated_critical_source_interface_check/CORRECTION_RECHECK.md | 2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8 |
| mediator_coefficient_precision/PROPOSAL.md | ec94570c294d760dadda17370fb8e65634880aa346709bc2d28fc6f3245f0084 |

ROOT authored the earlier positive identity and requested this extension. I checked that identity and authored the stationary and precision ancestors. The new proof below reconstructs the graph identity and its precision consequences; it is not an independent check of my ancestors. The coefficient-precision source's distinct-review status is not assumed here. Its needed nonuniform Schur formulas are explicitly rederived below. The earlier seven-block three-source inventory is not copied to the larger graph.

## Pair identity and arbitrary finite graph

Let n_v be a head-qubit occupation and X_uv=(X_u X_v+Y_u Y_v)/2. Here the capital single-qubit X,Y are Pauli matrices: X_uv exchanges |10> and |01> and annihilates |00>,|11>. For a positive real bond w, define

    Q_w=w(n_u+n_v-X_uv),
    P_w=w(I_uv-X_uv).

P_w has value w on |00> and |11>. On span{|10>,|01>} it is [[w,-w],[-w,w]], with eigenvalues 0 and 2w. Hence its full spectrum is {0,w,w,2w}, its norm is 2w, and it preserves total head number. The pair identity extended by identity on all other degrees of freedom is the FULL apparatus identity. Consequently

    P_w-Q_w=w I-w n_u-w n_v.                       (1)

This is an equality in all head-number sectors, not only the one-head sector.

For any finite graph of new bonds E, let d_v(w)=sum_{e incident v}w_e and C(w)=sum_{e in E}w_e. For any prescribed number coefficients b_v,

    sum_e Q_we + sum_v [b_v-d_v(w)] n_v
      =sum_v b_v n_v-sum_e w_e X_e,

    sum_e P_we + sum_v b_v n_v
      =sum_v b_v n_v-sum_e w_e X_e+C(w)I.           (2)

The old decomposition is positive when its occupations are nonnegative. The new decomposition only needs w_e>0 and b_v>=0 for its own positivity. If some old compensated occupation becomes negative, the algebraic equality still holds, but no positive implementation or previously restricted theorem for that old decomposition has thereby been proved. The graph is finite for every member of the length family; no divergent infinite sum of identity blocks is introduced.

## Attachment at the existing port: keep the original cap

Let N be all new source and mediator vertices and p the old port. E consists of the three mediator paths connecting s0 to s1 to s2 to p. The background H_bg already contains the positive cap j n_p and has total one-head port diagonal 2j. Extend its shared internal operator B and original scalar c_att to the added coordinates exactly once, using the same supplied convention as the corrected stationary installation. Denote these common, unchanged terms collectively by H_base; their presence is identical in each formula below. In particular H_base contains the capped background, not its uncapped version.

The corrected Q implementation can be collected as the following full operator:

    H_Q(w)=H_base+sum_{v in N}2j n_v-sum_{e in E}w_e X_e.          (3)

To implement (3) by Q blocks, one omits the old j n_p cap, supplies the compensated occupations 2j-d_v(w) on N and j-d_p(w) at p, and supplies all Q bonds. The port then recovers exactly its original cap contribution. This is the corrected installation, not literal addition to an already capped background.

The alternative implementation is simpler:

    H_P(w)=H_base+sum_{v in N}2j n_v+sum_{e in E}P_we.             (4)

KEEP the original cap j n_p. Add NO occupation at p. The new P bond ending at p adds no port-specific diagonal after subtraction of the global scalar. Thus

    H_P(w)=H_Q(w)+C(w)I                                           (5)

on the full qubit/internal Hilbert space. Equivalently one may omit the cap and explicitly restore the same j n_p once; adding it a second time would be wrong. No implemented negative occupation or negative identity block is needed. Subtraction of C(w)I is analytical bookkeeping, not a proposed negative Hamiltonian term.

In the one-head sector, H_P-C(w)I has exactly the original 2j diagonal at every new vertex and p, and negative hoppings -w_e. All old interactions, shared B, literal K/W and c_att remain as in (3). The graph identity does not require these internal operators to commute with the physical processor. The added P blocks act as identity on them.

Compress to every new head blank, retaining the old apparatus. All exchange terms through a new vertex vanish under compression, and the new occupations vanish. Each P contributes w_e times the retained identity. Thus the compressed new operator is H_bg+C(w)I (with the same inherited internal convention). After accounting for C, the emitter-free background is unchanged. In the full head vacuum the new P blocks similarly contribute C; they are not vacuum-annihilating Q blocks. Equation (5) handles vacuum, multiple heads, old/internal states and passive references simultaneously.

## Nonuniform hopping errors no longer force occupation tracking

Supply the new occupations independently at exactly 2j and keep the original background fixed. Allow arbitrary positive actual strong bonds J_i, weak bonds q_i and endpoint bonds gamma_L,gamma_R in each cell. Equations (4)–(5) hold for each actual tuple with its own C(actual). Hopping changes do NOT alter a centered onsite coefficient: the formerly required changes in 2j-d_v(w) and j-d_p(w) are absent from the implemented list.

For one cell, measure z relative to the actual global scalar plus the physical carrier and selected B energy. Its internal pencil is zI+A, where A is the positive bipartite adjacency. If

    a_*=min J_i-max q_i>0,

then its smallest singular magnitude is at least a_*, by the diagonal-minus-weighted-shift singular-value bound. The endpoint self-energy is exactly

    Sigma(z)=Gamma C_end^T(zI+A)^(-1)C_end Gamma,
    Gamma=diag(gamma_L,gamma_R).

Chiral symmetry implies zero diagonal at z=0 and even off-diagonal entries. Bidiagonal substitution gives

    t(0)=(-1)^(n-1)gamma_L gamma_R
                         (product q_i)/(product J_i).             (6)

The derivative of the inverse is -A^(-2), giving

    Sigma'(0)=-diag(c_L,c_R),
    c_L=gamma_L^2 sum_{k=0}^{n-1}
           (product_{i=1}^{k}q_i)^2/(product_{i=1}^{k+1}J_i)^2,
    c_R=gamma_R^2 sum_{k=0}^{n-1}
           (product_{i=n-k}^{n-1}q_i)^2/(product_{i=n-k}^{n}J_i)^2. (7)

Empty products are one. Positivity of all actual bonds retains the endpoint sign gauges and seed-to-port (-1)^m. Unequal errors generally give c_L unequal to c_R; P blocks do not restore reflection symmetry. The same finite-energy resolvent envelopes follow from the actual gap, including ||Sigma(z)-Sigma(0)||<=gamma_max^2 |z|/[a_*(a_*-|z|)] for |z|<a_*.

Consequently the precision interface now applies without its conditional requirement to retune occupations to actual incident sums. The requirement is replaced by supply of the P blocks and fixed diagonal occupations. In particular, exactly

    log|t(actual)/t(nominal)|
      =log(gamma_L/gamma_L0)+log(gamma_R/gamma_R0)
         +sum log(q_i/q_i0)-sum log(J_i/J_i0).                     (8)

Worst-case independently variable relative errors still accumulate with length. For uniform relative error ceiling epsilon<1 on all 2n+1 bonds, |log|t/t0||<=(2n+1)[-log(1-epsilon)]. The unequal slope sums (7), their fixed-gap geometric sensitivity, and the full source mass coefficients Z0=1+c1L, Z1=1+c1R+c2L, Z2=1+c2R+c3L remain. There is still a separate port derivative c3R. None can be discarded merely because compensation controls have been removed.

For common uniform J,q errors with n1=n2=2m-1,n3=m, the exponent cancellation in t3^2/t1 still holds, while the linewidth and mass tuning can change. This construction does not turn exact algebraic mass tuning into a robust identity under independent errors. It changes the positive implementation of the same centered operator family.

Independent diagonal-supplier errors are separate. If occupations on N become 2j+d_v (remaining nonnegative), those d_v enter the centered diagonal directly; they are not absorbed into C(w). Nonuniform internal diagonal errors break the chiral identity and require a separate resolvent estimate. Even a common offset only on the added vertices is not a global identity of the old apparatus. Thus this removes hopping-correlated compensation, not the need to match the mediator onsite to its external physical carrier. Additional errors inside the supplied P block beyond an overall scalar coefficient also require their own analysis: a perturbation that changes its diagonal and exchange pieces independently is not the relative w error model of (8).

## Global phase and actual versus nominal calibration

For each actual tuple the exact unitary identity is

    exp(-itH_P(w))=exp(-itC(w)) exp(-itH_Q(w)).                    (9)

There is no time rescaling, rotating-wave approximation or dropped phase. The physical scalar becomes c_att+C(w); all spectral windows must shift accordingly. Conditional stationary formulas in centered energy use that actual scalar and the unchanged carrier 2j. The finite and infinite receiver versions have the same C for the same finite source graph, so a separately justified cut comparison is multiplied by a common phase; this supplies no new cut bound by itself.

For an uncertain tuple, a complete phase-sensitive vector comparator needs the actual C, or a separately budgeted error from using C0. The exact phase discrepancy is

    |exp(-it[C-C0])-1|=2|sin(t[C-C0]/2)|
                          <=min(2,|t| |C-C0|),
    |C-C0|<=sum_e |w_e-w_e0|.                                    (10)

With a common relative ceiling epsilon this last sum is at most epsilon C0. These are sufficient upper bounds, not lower bounds or universal precision requirements. Channel metrics ignore the global scalar, but the campaign's fixed-phase vector metric does not. Even with actual C calibrated, the centered waveform and linewidth may differ because (6)–(8) changed. A device-specific target/clock and a single predeclared nominal target/runtime therefore remain different claims. No latter robustness theorem is asserted.

## Counts, locality and incident norms

For n1=n2=2m-1,n3=m there are 10m-4 mediator vertices, three new source vertices, and the retained port: 10m local heads in all. There are 10m-1 edges. The new installation adds

    10m-1 P blocks,
    10m-1 fixed 2j occupations on NEW vertices,

for 20m-2 blocks beyond the already capped background. Including that retained cap in the local inventory gives 20m-1 blocks. The corrected Q construction removed one cap and installed at most 20m-1 blocks, hence also at most 20m-2 net added blocks. Unlike the earlier six-to-seven source re-expression, this fully compensated path does not automatically add a block: that earlier count used a different structured bond decomposition. No minimality is claimed; zero occupations or block merging can change a chosen list.

For identical uniform internal J,q and equal endpoints within each cell,

    C_m=(5m-2)J+(5m-5)q+2(gamma1+gamma2+gamma3).                   (11)

For arbitrary errors use the exact edge sum instead. It grows with finite path length; it is not the exponentially small induced coupling. This matters for the nominal phase obligation (10).

The new contribution to the incident block-norm sum at a new vertex v is 2j+2sum_{e incident v}w_e. At p it is 2gamma3R beyond the already capped background's incident load; if the retained cap is listed locally its additional norm is j, counted once. Other background incident terms remain. The identity part of a two-site block does not justify dropping its declared norm 2w from conservative local resource bookkeeping. The earlier Q occupation constraints are unnecessary for positivity of (4), but old stationary/performance hypotheses may still impose smallness and gap conditions and must not be relaxed automatically.

The geometry remains a finite path of nearest-neighbor two-qubit exchange blocks and one-site occupations, with disjoint mediator paths and the old port fixed. Realizing longer paths can move the source coordinates and requires available lattice sites and suppressed unintended contacts, as before. Although the scalar part is mathematically a global identity, each supplied block is supported on its two incident qubits in the usual local-operator sense. This supplies no native microscopic realization of that block or exact selection mechanism. The product seed itself is unchanged.

## Scope of the constructive result

Equations (1)–(5) are exact full-space algebra. Equations (6)–(8) show why independent scalar hopping-coefficient errors retain the chiral zero-energy cancellation when the new occupations are independently fixed. This is a genuine removal of the old occupation-tracking correlation in the stated error model. It is not the removal of all small scales or precision obligations.

The mediator loaded inverse, possible hidden poles, full prepared spectral mass, dressing/population, energy-dependent source response, physical packet and runtime still require their own hypotheses and checks. Existing exact-tuple stationary results can be related by the scalar identity only within their existing coefficient and geometry domains. No old constant-bond source tolerance theorem is imported for energy-dependent mediator Schur functions. The original native Hamiltonian, coefficient and diagonal supplier, initialization and output/Record identifications remain supplied premises.

This is new authored bridge work requiring a distinct check of the port bookkeeping, all-sector scalar identity, tuple-dependent phase, and resource/precision qualifications. No scientific simulation, numerical sweep, operating point, source edits, W/Git/PR/checkpoint/prompt/model changes or delegation occurred. Only this proposal was created.
