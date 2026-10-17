# Three-site product source: complete output with two finite receivers

Claim type: bounded_theorem. Status: conditional mathematical publication candidate prepared for review. Both receiver points have completed distinct composition checks. This combined note also requires final integration review; no retained audit status is conferred.

The [spectral parent note](CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md) supplies a positive three-site product source, its exact installed seed moment and full-channel stationary matching. The present temporal extension adds all-three-source recovery, full outgoing/incoming synthesis, prepared-background recovery and scalar halfline concentration. These are the missing components needed for a complete state comparison, rather than concentration alone.

Under the unchanged original source/calibration, matching and physical-identification premises, the two certificates are:

| Point | Slow hopping g | Analysis halfwidth h | New receiver sites M | Chosen read interval | Complete normalized-target ceiling | Composition status |
|---|---:|---:|---:|---|---:|---|
| Larger receiver | 5×10^-8 | 4×10^-6 | 50,000,000 | [2×10^14,4×10^14] | <.0006 | Distinctly checked |
| Compact receiver | 10^-9 | 8×10^-8 | 1,000,000 | [2×10^14,4×10^14] | <.001722 | Distinctly checked |

Both use lambda=10^-13, a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda and the ORIGINAL calibrated j, enclosed by .0027<j<.003. The common time scale is T=2×10^14. These are different slow-output Hamiltonians: changing g changes its connector and compensating occupations, and M changes the cap position. The three-site source couplings are the same. The halfwidth h and proof cutoffs below select analytical windows; they are not additional Hamiltonian controls.

The metric is the full unconditioned vector map, retaining every head, shared source, record and arbitrary passive reference. Actual output is not postselected or renormalized. Every t in the stated interval is an allowed single chosen read time; intermediate measurements, permanent storage and reset/reuse are not asserted.

## Physical apparatus and exact common target

Keep the inherited calibrated contact/filter source, shared B, two converters, capped input, eighteen-edge cable and 24-head record gate. At p=(40,63,1) use s2=(40,64,1), s1=(40,65,1), s0=(40,66,1), with the head initially at s0 and all other heads blank. Shared sources begin in their supplied vacuum and the record in computational 0. The six source blocks are

    j(n_s2+n_p)−kappa exchange_(s2,p),
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j−a2)n_s2, (2j−a1−a2)n_s1, (2j−a1)n_s0,
    Q_a(x,y)=a(n_x+n_y−exchange_xy).

They are positive on the full qubit space, give source diagonals 2j and add no vacancy scalar. Compression off the three source heads leaves exactly j n_p, preserving the full emitter-free background. The shared B is included once, with B iota=iota K; no separate internal source is replicated at each head.

The slow receiver starts at r_m=(100,3+m,2), m>=0, beyond distinct gate port o=(100,2,2). Its connector is Q_sqrt(jg), internal bonds Q_g, and occupations are (j−sqrt(jg))n_o, (2j−sqrt(jg)−g)n_r0 and 2(j−g)n_rm for m>=1. Retain M sites and add cap g n_r(M−1). This is exact seeded-sector compression of the infinite apparatus, not an absorbing boundary. Original selective installed-pair and native interaction premises remain essential.

Retain literally

    K=2I+Z1Z2,
    W=[(9+12i)I+(−16+12i)X1X2]/25,
    c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)−1)j.

Actual H need not commute with K. For d=2j sin h the physical windows are I_b=c_att+b+2j+[−d,d], b=1,3. Write delta=−2j cos q=−2g cos k and k_old(q)=2asin(sqrt(j/J)sin(q/2)), with the original J=.030021107107032 and j/J calibration. The exact scalar coefficient is

    q3(delta)=(delta²−lambda²/3)(delta−kappa²m_j(delta+i0))
                                                −(8lambda²/3)delta,
    F3(q)=kappa a1a2(2j sin q) zeta exp[i61q+i172k_old(q)]
                                            /[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)).

The physical j-chain Weyl root m_j, fixed zeta, complex denominator phase and slow Jacobian are retained. The total phase is 61.5q+.5k+172k_old together with arg(1/q3); it is not 61 slow-site translations or a fitted input-dependent phase. Let p=int|F_s|² and

    beta_t(m)=1/sqrt(2pi) int F_s(k)
                    exp[ikm−it(2j−2g cos k)]dk, m>=0,
    r(t)=||beta_t||,
    Tnorm(t)=exp(−it c_att) Jout[(beta_t/r(t)) tensor exp(−itK)W].

Jout supplies source vacuum, record1 and blank nonoutput heads. Each point has its own exact common packet. Its r(t)>0 is established by the scalar estimates. The finite actual state is embedded into the same infinite comparison space; the target tail is not silently cut off.

## Actual spectral and local interfaces

The full ordered source denominator is Q=(D²−a1²)(D−kappa²G)−a2²D, with D=E−c_att−2j−B. The unchanged background gives ||G−m_j(D)||<a0+b0|delta|, a0=8×10^-18, b0=46000/.0053+290/g. Selected and complementary channels are both retained. With

    s=sqrt(1−3lambda/j),
    Theta=(j a0+kappa²b0)/s+6kappa²(a0+b0d), c3=(1−Theta)s,

complete matching gives ||Q^-1||<=1/[c3(delta²+lambda²)^(3/2)] on both lips. The actual noncommuting order is retained; lower Q is not assumed to be upper Q-adjoint. Strict margins and root continuation give in-window seed absolute continuity, including endpoints. Outside atoms and singular spectrum are paid by the actual omitted-state bound.

The installed moment is mu6=3lambda^6+(8/3)jlambda^5. Its second term comes from first arrival at p on the third application of H−E_b. The full-input bound is epsilon_sp<=sqrt(2mu6)/d³ on the common two-window union. It assumes neither [H,K]=0 nor orthogonal omitted output ranges and includes all passive references. This actual omitted vector is charged once globally.

The [local-source proof](../outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape__PROPOSAL.md) subtracts the entire three-source resolvent column. Its reference last-source column has squared numerator (delta²+lambda²)², allowing explicit selected and complementary Stone integrals. The resulting represented bound retains all three source amplitudes, scalar finite-band errors, reference truncation and wrong-window forcing. Reference truncation is distinct from epsilon_sp.

The [prepared-core recovery](../outputs/three_site_temporal_2026_10_17/proofs/prepared_core_recovery__PROPOSAL.md) uses an exact discrete dwell identity at the original physical port planes:

    Psi*Psi+Psi_closed*Psi_closed
       =−i S_B* dS_B/dk+I+Re S_B+cot(k)Im S_B.

The actual scattering derivative, including all 170 propagation-phase derivatives, yields old-core open-incidence norm <30. After converter/cap propagation and explicit complementary forcing, the disjoint old/input/cable/gate-plus-tail bounds give the FULL forcing norm L0<14000. This is a value-recovery theorem, not a wavefunction-derivative or latency inference. Its [dwell review](../outputs/three_site_temporal_2026_10_17/proofs/prepared_core_dwell_check__REVIEW.md) and [composition review](../outputs/three_site_temporal_2026_10_17/proofs/prepared_core_composition_check__REVIEW.md) have separate scopes.

For the actual background column −kappa L a1a2 Q^-1, absolute integration pays both windows and both lips:

    B_I(t)<=8sqrt(2)kappa L0/(3pi c3).

It contains all remaining finite heads and every closed slow tail, excludes the three source heads and propagating ray, and requires no background derivative or cancellation. It is a sufficient nondecaying allowance, not a physical residual or lower bound.

## Traveling synthesis and scalar concentration

The [actual outgoing proof](../outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing__PROPOSAL.md) compares the complete loaded row with F_s, including wrong-window columns. Its raw allowance is E=sqrt(2)Esel+Ewrong, with exact scalar second moment lambda²/3 and full ordered inverse error. In the [traveling interface](../outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface__PROPOSAL.md), real physical coordinate conjugation identifies the incoming coefficient with the conjugate of the outgoing coefficient. Its time phase remains exp(−itE_b), and its ideal old multiplier is W*, not W. Both traveling discrepancies cost 2E because they share a physical ray.

For the exact conjugate scalar packet let J_raw bound its norm on m>=0. Let C_out bound the outgoing negative-halfline fraction of F_s/sqrt(p). Parseval gives r>=sqrt(p)sqrt(1−C_out²). The complete infinite comparison is

    ||exp(−itH)V−Tnorm(t)||
      <=epsilon_sp+S_I(t)+B_I(t)+2E+J_raw(t)+1−r(t).

No actual state is normalized, and raw E avoids paying spectral normalization twice. The scalar comparison's own normalization error is proof error in deriving J_raw and C_out, not a second actual omitted vector.

The larger-receiver point uses the [fixed scalar-time proof](../outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_time__PROPOSAL.md) and [exact tail refinement](../outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_tail__PROPOSAL.md), with auxiliary D=100lambda. Its cubic residue, both hard-cutoff tails, nonlinear dispersion, physical phase and integer-lattice aliases are all charged.

The compact point uses the [weighted scalar refinement](../outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time__PROPOSAL.md) at D=g/4. In x=2g(k−pi/2), the cubic reference density has exact second and fourth moments lambda²/3 and lambda^4. A physical phase Lipschitz constant P=1/(4g)+102.78/(2j cos h) therefore costs P lambda/sqrt(3), rather than P D. The independent denominator margin sqrt(1−3eta)sinc(D/(2g))³ replaces a cutoff-displacement smallness requirement. A TRUNCATED sixth-moment integral bounds dispersion by |t|sqrt(16lambda^5D/(3pi))/(24g²); no divergent full sixth moment is used. Both tails, aliases and normalization remain paid. Its [distinct check](../outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time_check__REVIEW.md) supports this scalar refinement only.

Both scalar routes preserve the exact F_s and its conjugate, include m=0, and bound a stronger outgoing excluded set m<=0. They do not analytically continue the interacting apparatus. Their dispersion errors grow with the horizon, so they are evaluated through 2T, not asserted for all later times.

## Complete budgets and exact finite cut

The two point sources give the following strict ceilings uniformly on their common interval. Both compositions have distinct analytical checks at the exact source revisions below.

| Contribution | Larger receiver | Compact receiver |
|---|---:|---:|
| One actual omitted state | 4.1×10^-11 | .0000051 |
| Represented three-source amplitude | .000003 | .000119 |
| Remaining finite/closed background | .000505 | .000506 |
| Raw outgoing plus incoming coefficient errors | .0000216 | .001074 |
| Raw scalar incoming packet | .0000691 | .000016 |
| Physical target normalization | 2.46×10^-9 | 4×10^-9 |
| Finite/infinite transfer | 10^-8 | 10^-9 |
| Sum of displayed ceilings | .000598712501 | .001720105 |
| Stated certificate | .0006 | .001722 |

The larger point has Theta<5.24×10^-6 and c3>.9999947; the compact point recomputes Theta<.0002611 and c3>.9997388 for its different g. The latter does not inherit the former's errors or mass. Its smaller h increases the actual moment tail, while the weighted scalar argument permits the much slower receiver without the older cutoff-supremum loss.

For the finite cut give weight zero to every upstream/source/gate site and r0, and weight m to r_m. Only g receiver edges change weight; all shared internal terms commute with this position weight. The connector has zero increment. Exact compression and single-cut Duhamel give

    finite transfer <=min{2,1.2 exp[−M+4gT sinh(1)]},
                                     0<=t<=2T.

Adding two source heads in the zero-weight region does not change this estimate. At the larger point the exponent is <−2,000,000 using sinh1<1.2. At the compact point it is <−59200 using sinh1<1.176. Returns and all internal channels are included. The cap is not absorbing, and the proof does not rule out later recurrence.

## Counts, comparisons and interpretation

The exact finite inventory is M+238 heads, M+243 physical qubits, M+239 head edges and 2M+281 unmerged positive blocks. Shared old/source and record qubits are counted once; passive references are excluded.

| Inventory | Larger receiver | Compact receiver |
|---|---:|---:|
| Head qubits | 50,000,238 | 1,000,238 |
| All physical qubits | 50,000,243 | 1,000,243 |
| Head edges | 50,000,239 | 1,000,239 |
| Positive blocks | 100,000,281 | 2,000,281 |

Source incident block norms remain 3j+a2, 2j+a1+a2 and 2j+a1; old source/contact loads are not bounded by the slow hopping g. Exact compensation and coupling correlations are supplied data.

The [previous wide-output certificate](WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md) gives the same complete metric with ceiling .00191 on [10^15,2×10^15] and M=250,000,000 for its one-site source and g=5×10^-8. The larger three-site certificate uses five times fewer new receiver sites and a five-times-earlier interval scale, with the smaller sufficient ceiling .0006. The compact point uses 250 times fewer new sites at that same earlier interval scale and ceiling .001722. Total-qubit ratios include the different finite offsets. Between the two three-site points, the compact receiver has 50 times fewer new sites and a weaker error ceiling.

These compare sufficient certificates for changed hardware and common waveforms, not measured errors, equal hardware, optimality or proof that the prior device cannot work earlier. Neither h nor the auxiliary proof cutoff is a hardware control. No physical-seconds conversion is supplied.

For any supported complete ceiling epsilon, record1 success at one chosen read exceeds 1−epsilon², and complete-channel and successful SUBNORMALIZED CP-map diamond errors are at most 2epsilon, including passive references and subsequent apparatus trace-out. Normalized successful vectors are within epsilon+1−sqrt(1−epsilon²). Normalized conditioning is nonlinear and has no asserted diamond-channel bound. Thus the larger checked point gives success >.99999964 and diamond ceiling .0012; the compact point gives success >.999997 and diamond ceiling .003444. These are consequences of the complete metric, not assumptions or repeated-monitoring claims.

## Evidence, exposure and remaining gates

The larger point is [source b64b5a07](../outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate__PROPOSAL.md), full SHA256 `b64b5a073aeedf47c8d1f3b604763af43edd0ac0d61ac572638a6bfac2ab0e5a`, with [distinct check](../outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate_check__REVIEW.md) `b660546cf354778d99dc08c7277e386069aa62ab9ef9efba5fb44596a19cc821`. The compact [source a170bcff](../outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver__PROPOSAL.md) is `a170bcffaa3defccb50fdae85527f36e90832a2b89e980683e7af8227a94911d`; its [distinct check](../outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver_check__REVIEW.md) is `8e89c1e6a90aef5abf9c484988beb3997e3ea5be92d890e827ea4ab2468ef7d0`. The [source manifest](../outputs/three_site_temporal_2026_10_17/SOURCES.json) pins exact new copies and inherited repository evidence. Root owns final copy/graph validation and publication; source identity is not proof.

I authored the traveling and weighted-reference interfaces, reviewed several source/inverse/scalar and larger-point arguments, and read the compact source completely for this synthesis. The compact author authored scalar and recovery ancestors and checked other interfaces. The new dwell and downstream recovery have separately scoped checks. This is source-exposed same-model synthesis, not independent checking of my own work or blind/model-diverse verification. Original source/filter/calibration and matching premises remain conditional, as do exact correlated coefficients, product preparation, selective local installation and native Hamiltonian/Record identification.

The scalar or perturbed-source robustness results are not imported into these complete certificates. No native supplier, coefficient-tolerance theorem, irreversible capture, permanent halt, reset/reuse, practical physical-time conversion or retained audit status follows. No new scientific runner, numerical inverse, spectrum, quadrature, dynamics, sweep or parameter point was introduced in this publication drafting. The drafter wrote only this research note. Root subsequently integrated the completed compact check and prepared the exact source packet. Final distinct integration review remains required before publication; its record accompanies this note. No editable prompt, physical axiom or model was changed.
