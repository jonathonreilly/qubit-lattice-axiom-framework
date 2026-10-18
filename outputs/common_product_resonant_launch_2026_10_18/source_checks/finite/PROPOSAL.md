# Finite standalone resonant launch with a fixed-diagonal cut

New author proposal. The finite-cut estimate below is proved directly. Its complete launch conclusion is conditional on frozen launch-window source c5acbc and that source's pending distinct check. The underlying geometric comparison now has distinct support cfd880, read in full here; this does not by itself check the complete launch corollary or this finite extension. No finite router or record result is asserted.

## 1. Actual finite positive device

Let j>0 and 0<gamma<j. There are M+2 head qubits: emitter s and lead sites 0,...,M, with M>=1. Place these in that order on a nearest-neighbor line. Write n_v=|1><1|_v and use the inherited positive number-conserving bond Q_a with one-head matrix a[[1,-1],[-1,1]] and full norm 2a. Install exactly

    H_F = B + sum_(n=0)^(M-1) Q_j(n,n+1) + j n_M,
    B = Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0.       (1)

The combined B is one listed positive block, with full norm 3j under the inherited Q convention. All other blocks are positive and annihilate the head vacuum. The finite all-head Hamiltonian is well defined, preserves head number, and is zero on the all-vacuum state. The actual supplied seed is |s>, every other head vacant. No incoming packet is prepared.

In the one-head sector every diagonal of (1) is exactly 2j, including M. Its hoppings are -gamma from s to 0 and -j on the lead. The added j n_M is essential: deleting a Laplacian bond without it would change the boundary diagonal and would not implement this comparison.

There are M+2 qubits and M+2 listed positive blocks: B, M uniform bonds, and one cap. The incident full-support loads are 3j at s, 5j at 0, 4j at interior lead sites, and 3j at M. For M=1 the same endpoint formulas apply, with no interior site. Thus j<=Lambda/5 meets a supplied incident cap Lambda. Counting B by its norm, rather than separately counting its summands, is the explicitly inherited listed-block convention. Exact coefficients, their within-block relations, the seed and absence of other couplings remain supplied premises.

## 2. Complete finite/infinite comparison without a propagation assumption

Use the bounded one-head half-line operator H_infinity of the source, with coordinates s,0,1,... and diagonal 2j. This is an analytical comparison space, not an infinite many-head apparatus. Its centered operator K=H_infinity-2jI is a weighted adjacency operator with absolute row sums at most 2j, so ||K||<=2j.

Embed the finite one-head space in this half-line and define

    H_cut = H_F direct-sum H_ext,

where H_ext has sites M+1,M+2,..., all diagonals 2j and hoppings -j. Equivalently the exterior is a positive half-line Laplacian with its additional endpoint onsite j n_(M+1). In this comparison space

    H_cut-H_infinity
      =j(|M><M+1|+|M+1><M|)=V.                         (2)

Only the hopping is removed. All diagonal and common phase terms match exactly. Starting at s, H_cut evolution stays in the finite summand and equals the actual finite device's evolution.

Put d=M+1, the graph distance from s to M. Let P_far project onto lead sites n>=M. For every integer p<d, locality gives P_far K^p|s>=0. The norm-convergent exponential series therefore proves, for t>=0,

    ||P_far exp(-itH_infinity)|s>||
       <= R_d(2jt),
    R_d(x)=sum_(p=d)^infinity x^p/p!.                  (3)

This is a norm of the whole far projection, not an estimate for only one boundary coordinate. In particular both M and M+1 are included. Equation (2) gives exactly

    ||V exp(-itH_infinity)|s>||
       =j sqrt(|psi_M(t)|^2+|psi_(M+1)(t)|^2)
       <=j R_d(2jt).                                  (4)

No factor proportional to the number of lead sites is present. Duhamel with the actual cut propagator on the left, which is unitary, now yields for all 0<=t<=T,

    ||exp(-itH_F)|s>-exp(-itH_infinity)|s>||
       <=j integral_0^t R_d(2js) ds
       <=jT R_d(2jT).                                 (5)

The finite vector in (5) is embedded with zero exterior coordinates. Thus the comparison pays both the missing infinite exterior amplitude and the change of all finite amplitudes. It does not discard an exterior remainder or assume finite and infinite evolutions coincide up to a light cone.

For integer d>=1 and x>=0,

    R_d(x)<=exp(x) x^d/d!<=exp(x)(e x/d)^d.             (6)

The first inequality follows from (d+l)!>=d! l!, and the second from d!>=(d/e)^d. If d>=8e jT, then x=2jT<=d/(4e), and hence

    R_d(2jT)<=exp[d/(4e)]4^(-d)<=exp(-d).              (7)

The last inequality uses log 4-1/(4e)>1. This explicit exponential bound, rather than a crude inverse-distance bound, handles the long resonant launch time.

For a requested cut allowance 0<epsilon<=1 choose

    d=ceil(max{2, 8e jT, log(8jT/epsilon)}),
    M=d-1.                                             (8)

The logarithm is well defined for T>0 and may be negative; the maximum includes 2. Equations (5)--(8) imply uniformly on the ENTIRE horizon [0,T]

    ||exp(-itH_F)|s>-exp(-itH_infinity)|s>||
                                      <=epsilon/8.     (9)

For general small T one can summarize d=O(1+jT+log_+(jT/epsilon)); on the launch family below jT>1, so the advertised O(jT+log(jT/epsilon)) bound applies directly.

## 3. Explicit complete finite launch window

Adopt the exact complete seed decomposition, geometric target and simultaneous estimates of frozen c5acbc. For 0<epsilon<=1 set

    L=log(32/epsilon),
    rho=(epsilon/64)^(3/2) L^(-1/4), gamma=rho j,
    u0=rho^-2 L=(64/epsilon)^3 L^(3/2),
    t_minus=u0/j, T=2u0/j,                             (10)

and choose M using (8) with this T. The adopted infinite result controls the ACTUAL emitter-plus-outgoing-plus-incoming state, with all three pieces retained, by the positively normalized target below with vector error strictly less than epsilon/4 throughout [t_minus,T].

Put a=sqrt(1-rho^2), m(t)=floor(2jt+1/2), and define the finite one-head target by zero emitter amplitude and

    beta_n(t)=exp(-i2jt)exp(i m(t)pi/2)
                 i rho(-ia)^(m(t)-n)
                   /sqrt(1-a^(2(m(t)+1))),  0<=n<=m(t),
    beta_n(t)=0,                            m(t)<n<=M.   (11)

The denominator is positive and its displayed value makes the norm exactly one. The target includes the exact common diagonal phase, rounding phase and source factor i. No fitted phase or complex normalization is introduced. On this family u0>1, while M>=8e jT-1>2jT+1/2. Consequently m(t)<=M on the whole window, so (11) is exactly the infinite comparison target embedded in the physical finite device. No target truncation or second normalization error is needed.

Combining (9) with the complete infinite result gives

    sup_(t_minus<=t<=T)
      ||exp(-itH_F)|s>-beta(t)||<3epsilon/8.             (12)

Here beta means the entire physical state: emitter empty, one head distributed on 0,...,m(t), and all other head sites vacant. This is not an outgoing-only marginal and not conditional on successful observation. The probability that the head lies in this target support with the emitter empty is greater than 1-9epsilon^2/64, by projecting the difference in (12) onto its orthogonal complement. The stronger coherent vector bound remains the primary statement.

The target comparison jumps when its integer center changes, with its prescribed accompanying phase. No device control is switched at these times. An additional supplied common scalar cI would require the same exp(-ict) factor multiplying the whole target.

## 4. Logical coherence, passive references and complete outputs

For two disjoint identical finite devices (1), a path bit may be encoded by putting the single head at either emitter. Every other head is initially vacant. The two-copy Hamiltonian is the sum of the two devices; the unused copy stays exactly in its vacuum, of energy zero. Counts double to 2(M+2) head qubits and 2(M+2) listed blocks; the incident cap is unchanged. Passive program and reference degrees of freedom are retained with identity evolution and are not counted as newly constructed hardware.

Identical coefficients and lengths give the same complex normalized beta(t) for both orthogonal path branches. Hence (12) is an operator-norm bound between the actual seeded isometry and the ideal logical identity transported to the common radial profile. Tensoring with arbitrary passive references does not change it. The input may be any coherent or entangled path/program/reference state; that initial logical coherence is supplied.

The corresponding unhalved complete output-channel (diamond) discrepancy is strictly less than 3epsilon/4 throughout the window. Both emitters and every other physical head remain in the target's declared state; nothing is traced out to obtain the bound. Mixed inputs follow by the same isometry estimate, not by an assumption of incoherent paths. This is transport through two separate sources, not a controlled gate or a record-writing device.

## 5. Sufficient costs and precise limits

The exact time remains the source-only time (10), with a window of relative width one. Since jT=2(64/epsilon)^3 L^(3/2), the first distance term in (8) grows as epsilon^-3 L^(3/2), while its logarithmic term grows only as log(1/epsilon). Thus for this explicit prescription

    M+2 = Theta(epsilon^-3 [log(1/epsilon)]^(3/2)),
    T   = Theta(j^-1 epsilon^-3 [log(1/epsilon)]^(3/2))  (13)

as epsilon tends to zero. These are sufficient family costs, not lower bounds or optimality claims. Choosing j=Lambda/5 fixes the cap and gives the corresponding Lambda^-1 time factor. Exact gamma=rho j still must be supplied; its magnitude is not an accuracy tolerance or manufacturing result. The large numerical constants have not been optimized.

The cut proof (3)--(9) is independent of the geometric approximation and applies to the actual source trajectory from time zero. The sharper geometric result is used only for the complete target on the stated window. A later compact-band requirement must still pay the launch source's explicit spectral cutoff and positive-normalization costs. Unlike (11), a cutoff outgoing target generally has infinite spatial support, so its finite target restriction would also need a new tail estimate. This proposal does not silently transfer its compact-support argument to that different target.

The finite chain can reflect and recur outside the proved horizon. No permanent halt, capture, reset, readout, record flag, router composition, old literal processor transfer, thermal preparation or native Hamiltonian derivation follows. Exact seed vacancy and supplied logical coherence remain assumptions. This proof closes only a finite standalone source interface, without physically inserting an outgoing packet.

## 6. Source identities, exposure and open check

All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- common_product_resonant_launch_window/PROPOSAL.md: c5acbc2c71cf352563e196bfb24225590f2f02718a86d39cc611461fadff5e5a. Fully reread and hash verified here. Its full launch conclusion remains a provisional dependency pending its assigned distinct check.
- common_product_geometric_source_profile/PROPOSAL.md: be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e. Authored and fully read in the immediately preceding chain of tasks. Its distinct common_product_geometric_source_profile_check/REVIEW.md, cfd880ac1dcd866fe47fd51c7b8f29764270fc028e67e540c1cb1a6b1f86dfed, was fully read and hash verified here. Support covers its free-profile and incoming-term estimates, not this finite construction.
- common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Complete source block, normalization and decomposition premises were fully read in the immediately preceding geometric task and reused unchanged through c5acbc.
- common_product_resonance_tail/PROPOSAL.md: 306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002; distinct check common_product_resonance_tail_check/REVIEW.md: de9dbd20bf873f194d969ec6570e77224a2dfb192ba3ac4035b0933fc3d610bd. Full source read in that preceding task and full check read in the launch-window task; accepted scalar-survival scope only.

ROOT proposed the centered hopping-series route, the fixed-diagonal cut and the distance scale. This author reconstructed its projection, factorial, integrated boundary, target-support and finite-device bookkeeping above, with full design/source exposure. This is a new same-model author derivation, not an independent check of its ancestors or a retained theorem. A distinct check must inspect both the cut construction and the pending complete launch dependency before promoting their composition.

Only this file was created. No scientific executable, simulation, sweep, delegation, source revision, W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. Exact frozen sources remain unchanged.
